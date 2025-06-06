# Support for AIME24, AIME25, LiveCodeBench
import os

summary_groups = sum(
    [v for k, v in locals().items() if k.endswith('_summary_groups')], []
)

summary_groups += [
    {
        'name': 'AIME2024_Aveage',
        'subsets':[[f'aime2024_run{idx}', 'accuracy'] for idx in range(int(os.getenv('N_REPEAT', 1)))]
    },
    {
        'name': 'AIME2025_Aveage',
        'subsets':[[f'aime2025_run{idx}', 'accuracy'] for idx in range(int(os.getenv('N_REPEAT', 1)))]
    },
    {
        'name': 'LCB_Aveage',
        'subsets':[[f'lcb_code_generation_run{idx}', 'accuracy'] for idx in range(int(os.getenv('N_REPEAT', 1)))]
    }
]

summarizer = dict(
    dataset_abbrs=[
        ['AIME2024_Aveage', 'accuracy'],
        ['AIME2025_Aveage', 'accuracy'],
        ['LCB_Aveage', 'accuracy'],
    ],
    summary_groups=summary_groups
)
