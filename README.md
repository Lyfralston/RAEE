### Reproduction of Reassessment Experiments in the Paper

1. Get predicted results of evaluated models and corresponding golden annotations. 

You can follow a unified event extraction training and testing framework [TextEE](https://github.com/ej0cl6/TextEE), applying its default settings to get these results and annotations. We provide these results and annotations in `test_data.tar` of [this huggingface repository](https://huggingface.co/datasets/Ralston/RAEE_reproduction_data/tree/main).

2. Generate reassessment data:

```
. scripts/gen_all_reassessment.sh
```

3. Let LLM to reassess. You need to provide your agent LLM's `BASE_URL` and `API_KEY` in `llm.py`, and then run:

```
. scripts/llm.sh
```

We provide the reassessing results in `gpt-4o-2024-05-13.tar` of [this huggingface repository](https://huggingface.co/datasets/Ralston/RAEE_reproduction_data/tree/main).

4. Reassess according to the evaluation results from LLMs:

```
. evaluate.sh
```

In this step, you may find that some results (~<1%) have formatting irregularities or cannot be parsed. This is caused by LLMs not always following the python format to generate outputs or other unexpected errors. To solve this problem, you can run `wrong_file.py`  to delete these results and reassess again.

### Apply RAEE to Evaluate

RAEE can be easily applied to semantically evaluate other models in other datasets. You can follow several steps to do evaluation:

1. Format model's predictions and golden annotations. 

We follow the data format of [TextEE](https://github.com/ej0cl6/TextEE). You can find this format in [TextEE](https://github.com/ej0cl6/TextEE) or in `test_data.tar` file of [this huggingface repository](https://huggingface.co/datasets/Ralston/RAEE_reproduction_data/tree/main). The ideal file tree would be:

```
test_data/
--<model_name>/
----<dataset_1_name>/
------golds.json
------preds.json
```

2. Provide agent LLM's `BASE_URL` and `API_KEY` in `llm.py`. gpt-4o and deepseek-r1 series LLMs are recommended to do evaluation.
3. Run following command:

```
. scripts/raee.sh <model_name> <dataset_name> <task_name: ed/eae> <llm_agent>
```

For example:

```
. scripts/raee.sh oneie ace05 ed gpt-4o-2024-05-13
```

After that, you can get evaluation results in `reassessment_results.json` file.

