#!/bin/bash

llm_agent=gpt-4o-2024-05-13  # You can replace it with other llms. We recommend using gpt-4o series and deepseek-r1 series.

### ed task
ed_models=("cedar tagprime oneie degree queryandextract")
ed_datasets=("ace05 genia2011 casie phee fewevent mee-en m2e2")
for ed_model in ${ed_models}
do
    for ed_dataset in ${ed_datasets}
    do
        python evaluate.py --method ${ed_model} --dataset ${ed_dataset} --task ed --agent ${llm_agent}
    done
done

### eae task
eae_models=("ampere tagprime degree paie bartgen")
eae_datasets=("ace05 genia2011 casie phee wikievents rams geneva")
for eae_model in ${eae_models}
do
    for eae_dataset in ${eae_datasets}
    do 
        python evaluate.py --method ${eae_model} --dataset ${eae_dataset} --task eae --agent ${llm_agent}
    done
done
