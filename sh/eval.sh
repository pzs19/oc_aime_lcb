#!/bin/bash
# set -x

cd $(dirname $(dirname $0))
echo "Current directory: $(pwd)"
MODE=$1
if [ -z "$MODE" ]; then
    MODE="all"
fi
export CUDA_VISIBLE_DEVICES=6,7
# export CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7
echo "CUDA_VISIBLE_DEVICES: $CUDA_VISIBLE_DEVICES"
N_GPU=$(echo $CUDA_VISIBLE_DEVICES | tr ',' '\n' | wc -l)
echo "N_GPU: $N_GPU"

source ~/.bashrc
source activate opencompass

export N_REPEAT=2

opencompass -r \
    -w outputs/reasoning \
    --datasets aime2024_gen_wwpp aime2025_gen_wwpp lcb_gen_wwpp \
    --models aime_lcb_models_debug \
    --summarizer aime_lcb \
    --max-num-worker $N_GPU \
    --dump-eval-details True \
    --mode $MODE

export MODEL_NAME="deepseek-ai/DeepSeek-R1-0528"
export OPENAI_API_KEY=""
export OPENAI_API_BASE=""
export TEMPERATURE=0.6
export MAX_SEQ_LEN=32768
export MAX_OUT_LEN=32768

opencompass -r \
    -w outputs/reasoning \
    --datasets aime2024_gen_wwpp aime2025_gen_wwpp lcb_gen_wwpp \
    --models aime_lcb_models_api \
    --summarizer aime_lcb \
    --max-num-worker $N_GPU \
    --dump-eval-details True \
    --mode $MODE