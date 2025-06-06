from opencompass.models import OpenAISDK
import os
models = sum([v for k, v in locals().items() if k.endswith('_model')], [])

models += [
    # You can comment out the models you don't want to evaluate
    # All models use sampling mode
    dict(
        type=OpenAISDK,
        abbr='deepseek-r1',
        path='deepseek-reasoner',
        key=os.getenv('DEEPSEEK_API_KEY', None), # You need to set your own API key
        openai_api_base=[
            os.getenv('DEEPSEEK_API_BASE', None)
        ],
        meta_template=dict(
            round=[
                dict(role='HUMAN', api_role='HUMAN'),
                dict(role='BOT', api_role='BOT', generate=True),
            ], 
        ),

        query_per_second=1,
        batch_size=128,
        temperature=0.6,
        max_seq_len=34768,
        max_out_len=8192,
        verbose=True,
        retry=20,
    ),

    dict(
        type=OpenAISDK,
        abbr='o3-mini',
        path='o3-mini',
        key=os.getenv('OPENAI_API_KEY', None), # You need to set your own API key
        openai_api_base=[
            os.getenv('OPENAI_API_BASE', None)
        ],
        meta_template=dict(
            round=[
                dict(role='HUMAN', api_role='HUMAN'),
                dict(role='BOT', api_role='BOT', generate=True),
            ], 
        ),

        query_per_second=1,
        batch_size=128,
        temperature=0.6,
        max_seq_len=34768,
        max_out_len=32768,
        verbose=True,
        retry=20,
    ),
]
