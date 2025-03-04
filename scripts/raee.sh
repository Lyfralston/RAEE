#!/bin/bash

MODEL=$1
DATASET=$2
TASK=$3
AGENT=$4

python gen_reassessment.py --method ${MODEL} --dataset ${DATASET} --task ${TASK} --metric precision
python gen_reassessment.py --method ${MODEL} --dataset ${DATASET} --task ${TASK} --metric recall

python llm.py --agent ${AGENT} --save ${AGENT}/reassessment-${MODEL}-${DATASET}-${TASK}-precision/ --prompt input_reassessment/${MODEL}-${DATASET}-${TASK}-precision.json
python llm.py --agent ${AGENT} --save ${AGENT}/reassessment-${MODEL}-${DATASET}-${TASK}-recall/ --prompt input_reassessment/${MODEL}-${DATASET}-${TASK}-recall.json

python evaluate.py --method ${MODEL} --dataset ${DATASET} --task ${TASK} --agent ${AGENT}

max_retries=3
attempt=1

while [ $attempt -le $max_retries ]; do
    echo "Now checking. Attempt $attempt of $max_retries..."
    
    python wrong_files.py
    status=$?

    if [ $status -eq 0 ]; then
        echo "Evaluation done. No more errors."
        break
    else
        echo "It seems that a small amount of cases have errors. Now trying to assess these cases again..."

        python llm.py --agent ${AGENT} --save ${AGENT}/reassessment-${MODEL}-${DATASET}-${TASK}-precision/ --prompt input_reassessment/${MODEL}-${DATASET}-${TASK}-precision.json
        python llm.py --agent ${AGENT} --save ${AGENT}/reassessment-${MODEL}-${DATASET}-${TASK}-recall/ --prompt input_reassessment/${MODEL}-${DATASET}-${TASK}-recall.json

        python evaluate.py --method ${MODEL} --dataset ${DATASET} --task ${TASK} --agent ${AGENT}

        echo "Reassessment and evaluation done. Checking for errors again..."
    fi

    attempt=$((attempt+1))
done
