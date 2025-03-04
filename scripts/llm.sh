#!/bin/bash

llm_agent=gpt-4o-2024-05-13  # You can replace it with other llms. We recommend using gpt-4o series and deepseek-r1 series.

### ed task
ed_models=("cedar tagprime oneie degree queryandextract")
ed_datasets=("ace05 genia2011 casie phee fewevent mee-en m2e2")
for ed_model in ${ed_models}
do
    for ed_dataset in ${ed_datasets}
    do
        python llm.py --agent ${llm_agent} --save ${llm_agent}/reassessment-${ed_model}-${ed_dataset}-ed-precision/ --prompt input_reassessment/${ed_model}-${ed_dataset}-ed-precision.json
        python llm.py --agent ${llm_agent} --save ${llm_agent}/reassessment-${ed_model}-${ed_dataset}-ed-recall/ --prompt input_reassessment/${ed_model}-${ed_dataset}-ed-recall.json
    done
done

### eae task
eae_models=("ampere tagprime degree paie bartgen")
eae_datasets=("ace05 genia2011 casie phee wikievents rams geneva")
for eae_model in ${eae_models}
do
    for eae_dataset in ${eae_datasets}
    do 
        python llm.py --agent ${llm_agent} --save ${llm_agent}/reassessment-${eae_model}-${eae_dataset}-eae-precision/ --prompt input_reassessment/${eae_model}-${eae_dataset}-eae-precision.json
        python llm.py --agent ${llm_agent} --save ${llm_agent}/reassessment-${eae_model}-${eae_dataset}-eae-recall/ --prompt input_reassessment/${eae_model}-${eae_dataset}-eae-recall.json
    done
done