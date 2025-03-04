import os
import json
import argparse
from copy import deepcopy
from pattern import patterns
from prompt import prompts


def generate(preds, golds, args):
    cnt = 0
    record = []
    references, reassesses = (golds, preds) if args.metric == 'precision' else (preds, golds)
    reference_name, reassess_name = ('Gold', 'Pred') if args.metric == 'precision' else ('Pred', 'Gold')
    nug_name, nug_type_name = ('trigger', 'event type') if args.task == 'ed' else ('argument', 'role type')
    for i, (reference, reassess) in enumerate(zip(references, reassesses)):
        reference_nugs = []
        reassess_nugs = []
        nug_types = []
        duple_check = []
        
        inference_reference_nugs = []
        inference_reassess_nugs = []
        
        if 'tokens' not in reference:
            reference['tokens'] = reassess['tokens']
        if 'tokens' not in reassess:
            reassess['tokens'] = reference['tokens']
        for nug in reference[nug_name + 's']:
            nug_presentation = f"{' '.join(reference['tokens'][nug[0]:nug[1]])} # {nug_type_name}: {nug[2]}"
            nug_item = {'presentation': nug_presentation, 
                        'offset': nug[0:2] if args.task == 'ed' else ''}
            inference_reference_nugs.append(str(nug_item))
            if args.metric == 'recall':  # reference is pred, then add duplicate check.
                if nug_item not in duple_check:
                    duple_check.append(nug_item)
                else:
                    continue
            reference_nugs.append(nug_item)
            if nug[2] not in nug_types:
                nug_types.append(nug[2])
        for nug in reassess[nug_name + 's']:
            nug_presentation = f"{' '.join(reassess['tokens'][nug[0]:nug[1]])} # {nug_type_name}: {nug[2]}"
            nug_item = {'presentation': nug_presentation,
                        'offset': nug[0:2] if args.task == 'ed' else ''}
            inference_reassess_nugs.append(str(nug_item))
            if args.metric == 'precision':  # reassess is pred, then add duplicate check.
                if nug_item not in duple_check:
                    duple_check.append(nug_item)
                else:
                    continue
            if nug_item not in reference_nugs:  # There is no need to reassess the exactly matched one.
                reassess_nugs.append(nug_item)
            if nug[2] not in nug_types:
                nug_types.append(nug[2])

            
        if args.metric == 'precision':
            if len(reassess_nugs) == 0:  # In precision reassessment, it's ok with no reference (golden annotation).
                continue
        else:
            if len(reassess_nugs) == 0 or len(reference_nugs) == 0:
                continue
        
        opt_str = prompts[args.task][args.metric]
        if args.task == 'ed':
            opt_str += '\nEvents of interest include: \n'
            for tp in nug_types:
                opt_str += f"{tp}. {patterns[args.dataset][tp]['event description']}\n"
            
            tokens = reference['tokens']
            for nugs, name in [[reference_nugs, reference_name], [reassess_nugs, reassess_name]]:
                for idx, nug in enumerate(nugs):  # add a pair of [t] and [/t] in the context for each trigger
                    tokens[nug['offset'][0]] = f"[t.{name}.{idx}] " + tokens[nug['offset'][0]]
                    
                    tokens[nug['offset'][1]-1] = tokens[nug['offset'][1]-1] + f" [/t.{name}.{idx}]"
            
            opt_str += f"Context: {' '.join(tokens)}\n"
        else:
            trg = reference['trigger']
            tp = trg[2]

            opt_str += f"\nThe event of interest is {tp}. {patterns[args.dataset][tp]['event description']}\n"
            opt_str += f"Argument roles of interest: {patterns[args.dataset][tp]['valid roles']}\n"
            
            tokens = reference['tokens'][0:trg[0]] + ["[t]"] + reference['tokens'][trg[0]:trg[1]] + ["[/t]"] + reference['tokens'][trg[1]:]
            opt_str += f"Context: {' '.join(tokens)}\n"
        
        if args.task == 'ed':
            opt_str += f"The position of each following trigger is labeled in the context between a pair of [t] and [/t].\n"
        
        if len(reference_nugs) == 0:
            opt_str += f"None of gold {nug_name}s.\n"
        for nugs, name in [[reference_nugs, reference_name], [reassess_nugs, reassess_name]]:
            for idx, nug in enumerate(nugs):
                if args.task == 'ed':
                    opt_str += f"Trigger {name}.{idx}: {nug['presentation']}\n"
                else:
                    opt_str += f"{name} argument {idx}: {nug['presentation']}\n"
        
        opt_str.strip()     
        item = {
            'input': opt_str
        }
        args.fp.write(json.dumps(item))
        args.fp.write('\n')
        cnt += 1
        record.append(i)
        
    return cnt, record


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--method', type=str)
    parser.add_argument('--dataset', type=str, choices=['ace05', 'genia2011', 'casie', 'phee', 'wikievents', 'rams', 'geneva', 'fewevent', 'mee-en', 'm2e2'])
    parser.add_argument('--task', type=str, choices=['ed', 'eae'])
    parser.add_argument('--metric', type=str, choices=['precision', 'recall'])
    args = parser.parse_args()
    
    pred_path = f"test_data/{args.method}/{args.dataset}/{args.task}/preds.json"
    gold_path = f"test_data/{args.method}/{args.dataset}/{args.task}/golds.json"
    
    if os.path.exists(pred_path) and os.path.exists(gold_path):
        with open(pred_path) as fp:
            preds = json.load(fp)
        with open(gold_path) as fp:
            golds = json.load(fp)
    else:
        raise Exception("There is no file as given pred path or gold path.")

    if not os.path.exists("input_reassessment"):
        os.mkdir("input_reassessment")
        ### The following file is used to record data to be reassessed. The data can be easily evaluated by exact match is excluded.
        with open("input_reassessment/reassess_index_record.json", "w") as temp_fp:
            temp_fp.write(str(dict()))
    fp = open(f"input_reassessment/{args.method}-{args.dataset}-{args.task}-{args.metric}.json", 'w')
    args.fp = fp
    fp2 = open("input_reassessment/reassess_index_record.json", "r")
    records = json.load(fp2)
    reassess_item_num = None
    reassess_item_num, record = generate(preds, golds, args)
    
    if reassess_item_num != None:
        print(f"Discard {len(golds)-reassess_item_num}/{len(golds)} items with no need for reassessing.")
        print(f"Successfully generate {reassess_item_num} items for reassessing {args.method} on {args.dataset} dataset, {args.task} task and {args.metric} metric.")
        records[f"{args.method}-{args.dataset}-{args.task}-{args.metric}"] = record
        fp2 = open("input_reassessment/reassess_index_record.json", "w")
        json.dump(records, fp2)
    else:
        print('Failed Generation!')

if __name__ == '__main__':
    main()