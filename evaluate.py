import re
import os
import json
import numpy as np
import argparse
from scorer import compute_scores, print_scores, print_scores_new, safe_div

def add_wrong_files(fn):
    if not os.path.exists('wrong_files.json'):
        with open('wrong_files.json', 'w') as fp:
            fp.write(str(list()))
    wrong_fp = open('wrong_files.json', 'r')
    wrong_files = json.load(wrong_fp)
    if fn not in wrong_files:
        wrong_files.append(fn)
    wrong_fp = open('wrong_files.json', 'w')
    json.dump(wrong_files, wrong_fp)
    

def llm_outputs_to_list(dir_name):
    items = []
    temp = [f for f in os.listdir(dir_name) if f.endswith('.txt')]
    file_num = len(temp)
    files = [f"{idx}.txt" for idx in range(file_num)]
    for file in files:
        file_path = os.path.join(dir_name, file)
        
        with open(file_path) as fp:
            try:
                content = fp.read()
                pattern = re.compile(r'```python(.*?)```', re.DOTALL)
                code_blocks = pattern.findall(content)
                data = eval(code_blocks[0].strip())
                items.append(data)
            except Exception as e:
                print(f"File {file_path} decoding error: {e}")
                add_wrong_files(file_path)
                return []
    return items


def get_span_idx(pieces, token_start_idxs, span, tokenizer, trigger_span=None):
    """
    P.S. Follow TextEE
    This function is how we map the generated prediction back to span prediction.
    Detailed Explanation:
        We will first split our prediction and use tokenizer to tokenize our predicted "span" into pieces. Then, we will find whether we can find a continuous span in the original "pieces" can match tokenized "span". 
    If it is an argument/relation extraction task, we will return the one which is closest to the trigger_span.
    """
    words = []
    for s in span.split(' '):
        words.extend(tokenizer.encode(s, add_special_tokens=False))
    
    candidates = []
    for i in range(len(pieces)):
        j = 0
        k = 0
        while j < len(words) and i+k < len(pieces):
            if pieces[i+k] == words[j]:
                j += 1
                k += 1
            elif tokenizer.decode(words[j]) == "":
                j += 1
            elif tokenizer.decode(pieces[i+k]) == "":
                k += 1
            else:
                break
        if j == len(words):
            candidates.append((i, i+k))
            
    candidates = [(token_start_idxs.index(c1), token_start_idxs.index(c2)) for c1, c2 in candidates if c1 in token_start_idxs and c2 in token_start_idxs]
    if len(candidates) < 1:
        return -1, -1
    else:
        if trigger_span is None:
            return candidates[0]
        else:
            return sorted(candidates, key=lambda x: np.abs(trigger_span[0]-x[0]))[0]


def reassess_non_llm(items, preds, golds, args, metric):
    total_num = 0
    total_reassess_true_num = 0
    total_reassess_false_num = 0
    with open('input_reassessment/reassess_index_record.json') as fp:
        records = json.load(fp)
    record = records[f"{args.method}-{args.dataset}-{args.task}-{metric}"]
    for i, (pred, gold) in enumerate(zip(preds, golds)):
        if 'tokens' not in pred:
            pred['tokens'] = gold['tokens']
        reference, reassess = (gold, pred) if metric == 'precision' else (pred, gold)
        mention = 'triggers' if args.task == 'ed' else 'arguments'
        if i in record:
            ref_nugs = []
            non_reassess_num = 0
            total_num += len(reassess[mention])
            duple_check = []
            for idx, nug in enumerate(reference[mention]):
                nug_presentation = f"{' '.join(reference['tokens'][nug[0]:nug[1]])} # type: {nug[2]}"
                nug_item = {'presentation': nug_presentation,
                            'offset': nug[0:2] if args.task == 'ed' else ''}
                if metric == 'recall':  # reference is pred, then add duplicate check.
                    if nug_item not in duple_check:
                        duple_check.append(nug_item)
                    else:
                        continue
                ref_nugs.append(nug_item)
            for idx, nug in enumerate(reassess[mention]):
                nug_presentation = f"{' '.join(reassess['tokens'][nug[0]:nug[1]])} # type: {nug[2]}"
                nug_item = {'presentation': nug_presentation,
                            'offset': nug[0:2] if args.task == 'ed' else ''}
                if metric == 'precision':  # reassess is pred, then add duplicate check.
                    if nug_item not in duple_check:
                        duple_check.append(nug_item)
                    else:  # The duplicate one is eliminated.
                        non_reassess_num += 1
                        total_num -= 1
                        continue
                if nug_item in ref_nugs:
                    total_reassess_true_num += 1
                    non_reassess_num += 1
                else:
                    pass # The instance we have reassessed.
            
            item = items[record.index(i)]
            try:
                assert len(reassess[mention]) == non_reassess_num + len(item['Final Reassessment Results'])
            except:
                print(f"--- {args.method}.{args.dataset}.{args.task}.{metric} ---")
                print(f"record_index: {record.index(i)}")
                print('Unmatched reassessing mention number.')
                add_wrong_files(f'{args.agent}/reassessment-{args.method}-{args.dataset}-{args.task}-{metric}/{record.index(i)}.txt')
                # raise Exception('Unmatched reassessing mention number.')
            for reass in item['Final Reassessment Results']:
                if reass == 1:
                    total_reassess_true_num += 1
                elif reass == 0:
                    total_reassess_false_num += 1
                else:
                    print(f"--- {args.method}.{args.dataset}.{args.task}.{metric} ---")
                    print(f"record_index: {record.index(i)}")
                    print("Unexpected 'Final Reassessment' Results value when reassessing.")
                    add_wrong_files(f'{args.agent}/reassessment-{args.method}-{args.dataset}-{args.task}-{metric}/{record.index(i)}.txt')
                    # raise ValueError("Unexpected 'Final Reassessment' Results value when reassessing.")
        else:
            ref_nugs = []
            total_num += len(reassess[mention])
            for idx, nug in enumerate(reference[mention]):
                nug_presentation = f"{' '.join(reference['tokens'][nug[0]:nug[1]])} # type: {nug[2]}"
                ref_nugs.append(nug_presentation)
            for idx, nug in enumerate(reassess[mention]):
                nug_presentation = f"{' '.join(reassess['tokens'][nug[0]:nug[1]])} # type: {nug[2]}"
                if nug_presentation in ref_nugs:
                    total_reassess_true_num += 1
                else:
                    total_reassess_false_num += 1
        
    return 100 * safe_div(total_reassess_true_num, total_num), total_reassess_true_num, total_num


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--method', type=str)
    parser.add_argument('--dataset', type=str, choices=['ace05', 'genia2011', 'casie', 'phee', 'wikievents', 'rams', 'geneva', 'fewevent', 'mee-en', 'm2e2'])
    parser.add_argument('--task', type=str, choices=['ed', 'eae'], default='eae')
    parser.add_argument('--agent', type=str, default='gpt-4o-2024-05-13')
    parser.add_argument('--raee_only', action='store_true', help="do not output exact match evaluation results")
    
    args = parser.parse_args()
    
    if not os.path.exists('reassessment_results.json'):
        with open('reassessment_results.json', 'w') as fp:
            json.dump({'ed': {}, 'eae': {}}, fp)
            
    with open('reassessment_results.json', 'r') as fp:
        reassessment_results = json.load(fp)
    if args.method not in reassessment_results[args.task].keys():
        reassessment_results[args.task][args.method] = {}
    if args.dataset not in reassessment_results[args.task][args.method].keys():
        reassessment_results[args.task][args.method][args.dataset] = {}
        
    print("-"*30)
    print(f"Reassessed Model: {args.method} \nDataset: {args.dataset} \nTask: {args.task}")
    
    ### do old evaluation (Exact Match)
    
    gold_path = f"test_data/{args.method}/{args.dataset}/{args.task}/golds.json"
    pred_path = f"test_data/{args.method}/{args.dataset}/{args.task}/preds.json"
    if os.path.exists(gold_path) and os.path.exists(pred_path):
        with open(gold_path) as fp:
            golds = json.load(fp)
        with open(pred_path) as fp:
            preds = json.load(fp)
    else:
        raise Exception("There is no file as given pred path or gold path.")
    
    if not args.raee_only:
        old_scores = compute_scores(preds, golds, args.task.upper())
        if args.task == 'eae':
            print("Exact Match evaluation\t(p & r & f1): {:.2f} & {:.2f} & {:.2f}".format(old_scores['argument_attached_cls']['precision'], old_scores['argument_attached_cls']['recall'], old_scores['argument_attached_cls']['f1']))
            reassessment_results[args.task][args.method][args.dataset]['old'] = {
                'p': old_scores['argument_attached_cls']['precision'],
                'r': old_scores['argument_attached_cls']['recall'],
                'f1': old_scores['argument_attached_cls']['f1']
            }
        else:
            print("Exact Match evaluation\t(p & r & f1): {:.2f} & {:.2f} & {:.2f}".format(old_scores['trigger_cls']['precision'], old_scores['trigger_cls']['recall'], old_scores['trigger_cls']['f1']))
            reassessment_results[args.task][args.method][args.dataset]['old'] = {
                'p': old_scores['trigger_cls']['precision'],
                'r': old_scores['trigger_cls']['recall'],
                'f1': old_scores['trigger_cls']['f1']
            }
        
    
    ### do new evaluation (RAEE)
    raee_p_dir = f"{args.agent}/reassessment-{args.method}-{args.dataset}-{args.task}-precision"
    raee_r_dir = f"{args.agent}/reassessment-{args.method}-{args.dataset}-{args.task}-recall"
    raee_p_items = llm_outputs_to_list(raee_p_dir)
    raee_r_items = llm_outputs_to_list(raee_r_dir)
    precision, p_match_num, pred_num = reassess_non_llm(raee_p_items, preds, golds, args, 'precision')
    recall, r_match_num, gold_num = reassess_non_llm(raee_r_items, preds, golds, args, 'recall')
    f1 = safe_div(2 * precision * recall, precision + recall)
    
    if args.task == 'ed':
        new_scores = {
            'trigger_cls': {'precision': precision,
                            'recall': recall,
                            'f1': f1,
                            'pred_num': pred_num,
                            'gold_num': gold_num,
                            'p_match_num': p_match_num,
                            'r_match_num': r_match_num}
        }
    elif args.task == 'eae':
        new_scores = {
            'argument_attached_cls': {'precision': precision,
                            'recall': recall,
                            'f1': f1,
                            'pred_num': pred_num,
                            'gold_num': gold_num,
                            'p_match_num': p_match_num,
                            'r_match_num': r_match_num}
        }
    else:
        raise ValueError("Unexpected 'args.task' value.")

    if args.task == 'eae':
        print("RAEE evaluation\t\t(p & r & f1): {:.2f} & {:.2f} & {:.2f}".format(new_scores['argument_attached_cls']['precision'], new_scores['argument_attached_cls']['recall'], new_scores['argument_attached_cls']['f1']))
        reassessment_results[args.task][args.method][args.dataset]['new'] = {
            'p': new_scores['argument_attached_cls']['precision'],
            'r': new_scores['argument_attached_cls']['recall'],
            'f1': new_scores['argument_attached_cls']['f1']
        }
    else:
        print("RAEE evaluation\t\t(p & r & f1): {:.2f} & {:.2f} & {:.2f}".format(new_scores['trigger_cls']['precision'], new_scores['trigger_cls']['recall'], new_scores['trigger_cls']['f1']))
        reassessment_results[args.task][args.method][args.dataset]['new'] = {
            'p': new_scores['trigger_cls']['precision'],
            'r': new_scores['trigger_cls']['recall'],
            'f1': new_scores['trigger_cls']['f1']
        }
    
    with open('reassessment_results.json', 'w') as fp:
        json.dump(reassessment_results, fp)
    
    return


if __name__ == '__main__':
    main()