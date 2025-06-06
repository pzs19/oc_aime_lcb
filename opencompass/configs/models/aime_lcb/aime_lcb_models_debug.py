# For Debug

from opencompass.models import (
    TurboMindModelwithChatTemplate,
)

models = sum([v for k, v in locals().items() if k.endswith('_model')], [])

models += [
    # You can comment out the models you don't want to evaluate
    # All models use sampling mode
    dict(
        type=TurboMindModelwithChatTemplate,
        abbr='deepseek-r1-distill-qwen-7b-turbomind',
        path='deepseek-ai/DeepSeek-R1-Distill-Qwen-7B',
        engine_config=dict(session_len=34768, max_batch_size=128, tp=1),
        gen_config=dict(
                        do_sample=True,
                        temperature=0.6,
                        top_p=0.95,
                        max_new_tokens=32768),
        max_seq_len=34768,
        max_out_len=32768,
        batch_size=128,
        run_cfg=dict(num_gpus=1),
    ),
]
