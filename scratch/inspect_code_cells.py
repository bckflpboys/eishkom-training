import json

nb = json.load(open('sa_tutor_colab.ipynb', encoding='utf-8'))
for i, c in enumerate(nb['cells']):
    if c['cell_type'] == 'code':
        print(f"=== CELL {i} ===")
        print("".join(c.get('source', [])))

