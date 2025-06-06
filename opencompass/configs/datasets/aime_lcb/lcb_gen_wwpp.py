from opencompass.openicl.icl_prompt_template import PromptTemplate
from opencompass.openicl.icl_retriever import ZeroRetriever
from opencompass.openicl.icl_inferencer import GenInferencer
from opencompass.datasets import (
    LCBCodeGenerationDataset,
    LCBCodeGenerationEvaluator,
)
import os

lcb_code_generation_reader_cfg = dict(
    input_columns=[
        'question_content',
        'format_prompt',
    ],
    # output_column='evaluation_sample',
    output_column='question_id',
)

SYSTEM_MESSAGE_GENERIC = f'You are an expert Python programmer. You will be given a question (problem specification) and will generate a correct Python program that matches the specification and passes all tests. You will NOT return anything except for the program.'

prompt_template = '### Question:\n{question_content}\n\n{format_prompt}' + \
                    '### Answer: (use the provided format with backticks)\n\n'


# Code Generation Tasks
lcb_code_generation_infer_cfg = dict(
    prompt_template=dict(
        type=PromptTemplate,
        template=dict(
            round=[
                dict(
                    role='HUMAN',
                    prompt=prompt_template
                )
            ]
        )
    ),
    retriever=dict(type=ZeroRetriever),
    inferencer=dict(type=GenInferencer)
)

lcb_code_generation_eval_cfg = dict(
    evaluator=dict(
        type=LCBCodeGenerationEvaluator,
        num_process_evaluate=32,
        timeout=6,
    ),
    pred_role='BOT',
)

LCB_datasets = [
    dict(
        type=LCBCodeGenerationDataset,
        abbr=f'lcb_code_generation_run{idx}',
        path='./data/code_generation_lite',
        reader_cfg=lcb_code_generation_reader_cfg,
        infer_cfg=lcb_code_generation_infer_cfg,
        eval_cfg=lcb_code_generation_eval_cfg,
        release_version='release_v5',
        start_date='2024-08-01',
        end_date='2025-02-01'
    )
    for idx in range(int(os.getenv('N_REPEAT', 1)))
]
