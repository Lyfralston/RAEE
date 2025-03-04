import os
import json
import argparse
from pattern import patterns
from prompt import prompts

def ed(tests, fp, args):
    cnt = 0 
    for test in tests:
        opt_str = prompts['inference'][args.task]
        opt_str += 'Types of events that may occur include: \n'
        for tp in patterns[args.dataset].keys():
            opt_str += f"{tp}. {patterns[args.dataset][tp]['event description']}\n"
            
        opt_str += f"Context: {test['text']}"
        
        item = {
            'input': opt_str,
            'tokens': test['tokens'],
            'text': test['text'],
            'triggers': test['triggers']
        }
        fp.write(json.dumps(item))
        fp.write('\n')
        cnt += 1
    
    return cnt

def eae(tests, fp, args):
    cnt = 0
    for test in tests:
        opt_str = prompts['inference'][args.task]
        trg = test['trigger']
        tp = trg[2]
        opt_str += f"The event of interest is {tp}. {patterns[args.dataset][tp]['event description']} "
        opt_str += 'Roles of interest include: '
        for arg in patterns[args.dataset][tp]['valid roles']:
            opt_str += arg + ', '
        opt_str = opt_str[:-2]
        opt_str += f". There is a template for comprehension: {patterns[args.dataset][tp]['EAE template']}\n"
        
        tokens = test['tokens'][0:trg[0]] + ["[t]"] + test['tokens'][trg[0]:trg[1]] + ["[/t]"] + test['tokens'][trg[1]:]
        
        opt_str += f"Context: {' '.join(tokens)}"
        
        item = {
            'input': opt_str,
            'tokens': test['tokens'],
            'text': test['text'],
            'trigger': test['trigger'],
            'arguments': test['arguments']
        }
        fp.write(json.dumps(item))
        fp.write('\n')
        cnt += 1
    return cnt


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--task', type=str, choices=['ed', 'eae'])
    parser.add_argument('--number', type=int, default=250)
    args = parser.parse_args()
    
    test_path = f"input_reassessment/id2llm.json"
    
    if os.path.exists(test_path):
        with open(test_path) as fp:
            tests = json.load(fp)
    
    fp = open(f"input_inference/gpt4o-{args.dataset}-{args.task}.json", "w")
    
    inference_item_num = None
    if args.task == 'ed':
        inference_item_num = ed(tests, fp, args)
    elif args.task == 'eae':
        inference_item_num = eae(tests, fp, args)
        
    if inference_item_num != None:
        print(f"Successfully generatee {inference_item_num} items for LLM {args.task} task inference on {args.dataset}.")
    else:
        print('Failed Generation!')


if __name__ == '__main__':
    main()