#!/bin/bash

# ed task
ed_models=("cedar tagprime oneie degree queryandextract")
ed_datasets=("ace05 genia2011 casie phee fewevent mee-en m2e2")
for ed_model in ${ed_models}
do
    for ed_dataset in ${ed_datasets}
    do
        python gen_reassessment.py --method ${ed_model} --dataset ${ed_dataset} --task ed --metric precision
        python gen_reassessment.py --method ${ed_model} --dataset ${ed_dataset} --task ed --metric recall
    done
done

# eae task
eae_models=("ampere tagprime degree paie bartgen")
eae_datasets=("ace05 genia2011 casie phee wikievents rams geneva")
for eae_model in ${eae_models}
do
    for eae_dataset in ${eae_datasets}
    do 
        python gen_reassessment.py --method ${eae_model} --dataset ${eae_dataset} --task eae --metric precision
        python gen_reassessment.py --method ${eae_model} --dataset ${eae_dataset} --task eae --metric recall
    done
done

