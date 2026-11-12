#!/usr/bin/env python3
import json

def update_nb(path):
    with open(path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    for cell in nb['cells']:
        if cell.get('cell_type') == 'code':
            src = cell.get('source', [])
            for i, line in enumerate(src):
                if 'MODEL = "unsloth/Qwen3.5-4B"' in line and '# Choose the base' in ''.join(src):
                    src[i] = 'MODEL = "empero-ai/Qwen3.8-2B-Distill"                # Gariep Budget Tutor (2B)\n'
                elif '# MODEL = "empero-ai/Qwen3.8-2B-Distill"' in line:
                    src[i] = '# MODEL = "unsloth/Qwen3.5-4B"                           # Kendal Desktop (4B)\n'
                elif "unsloth/Qwen3.5-4B" in line and "globals().get" in line:
                    src[i] = line.replace('unsloth/Qwen3.5-4B', 'empero-ai/Qwen3.8-2B-Distill')
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)
    print('Updated:', path)

update_nb('sa_tutor_colab.ipynb')
update_nb('sa-tutor-kit/sa-tutor-kit/colab/sa_tutor_colab.ipynb')

