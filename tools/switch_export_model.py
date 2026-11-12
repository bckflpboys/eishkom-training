#!/usr/bin/env python3
import json

def update_export(path):
    with open(path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    for cell in nb['cells']:
        if cell.get('cell_type') == 'code':
            src = cell.get('source', [])
            for i, line in enumerate(src):
                if '!python training/export_gguf.py --adapter workspace/runs/{ROUND}/adapter --out workspace/exports/kendal-stage-1' in line:
                    src[i] = '# !python training/export_gguf.py --adapter workspace/runs/{ROUND}/adapter --out workspace/exports/kendal-stage-1 --quants q6_k q4_k q4_k_m\n'
                elif '# !python training/export_gguf.py --adapter workspace/runs/r1-gariep/adapter' in line or '# !python training/export_gguf.py --adapter workspace/runs/{ROUND}/adapter --out workspace/exports/gariep-stage-1' in line:
                    src[i] = '!python training/export_gguf.py --adapter workspace/runs/{ROUND}/adapter --out workspace/exports/gariep-stage-1 --quants q8_0 q6_k q4_k q4_k_m\n'
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)
    print('Updated export in:', path)

update_export('sa_tutor_colab.ipynb')
update_export('sa-tutor-kit/sa-tutor-kit/colab/sa_tutor_colab.ipynb')

