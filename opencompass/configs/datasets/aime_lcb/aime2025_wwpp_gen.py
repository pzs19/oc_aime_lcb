from opencompass.openicl.icl_prompt_template import PromptTemplate
from opencompass.openicl.icl_retriever import ZeroRetriever
from opencompass.openicl.icl_inferencer import GenInferencer
from opencompass.openicl.icl_evaluator import MATHEvaluator
from opencompass.datasets import Aime2025Dataset
import os

aime2025_reader_cfg = dict(
    input_columns=['question'],
    output_column='answer'
)


aime2025_infer_cfg = dict(
    prompt_template=dict(
        type=PromptTemplate,
        template=dict(
            round=[
                dict(role='HUMAN', prompt='{question}\nRemember to put your final answer within \\boxed{}.'),
            ],
        )
    ),
    retriever=dict(type=ZeroRetriever),
    inferencer=dict(type=GenInferencer)
)

aime2025_eval_cfg = dict(
    evaluator=dict(type=MATHEvaluator)
)

aime2025_datasets = [
    dict(
        abbr=f'aime2025_run{idx}',
        type=Aime2025Dataset,
        path='opencompass/aime2025',
        reader_cfg=aime2025_reader_cfg,
        infer_cfg=aime2025_infer_cfg,
        eval_cfg=aime2025_eval_cfg,
        mode='singlescore',
    )
    for idx in range(int(os.getenv('N_REPEAT', 1)))
]