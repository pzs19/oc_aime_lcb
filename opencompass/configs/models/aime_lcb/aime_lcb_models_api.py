from opencompass.models import OpenAISDK
import os
models = sum([v for k, v in locals().items() if k.endswith('_model')], [])

models += [
    # You can comment out the models you don't want to evaluate
    # All models use sampling mode
    dict(
        type=OpenAISDK,
        abbr=os.getenv("MODEL_NAME"),
        path=os.getenv("MODEL_NAME"),
        key=os.getenv('OPENAI_API_KEY', "EMPTY"), # You need to set your own API key
        openai_api_base=[
            os.getenv('OPENAI_API_BASE')
        ],
        meta_template=dict(
            round=[
                dict(role='HUMAN', api_role='HUMAN'),
                dict(role='BOT', api_role='BOT', generate=True),
            ], 
        ),
        query_per_second=1,
        batch_size=128,
        temperature=os.getenv("TEMPERATURE", 0.6),
        max_seq_len=os.getenv("MAX_SEQ_LEN", 32768),
        max_out_len=os.getenv("MAX_OUT_LEN", 32768),
        verbose=True,
        retry=10,
    ),
]
