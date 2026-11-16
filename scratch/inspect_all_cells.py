import json

nb = json.load(open('sa_tutor_colab.ipynb', encoding='utf-8'))
for i, c in enumerate(nb['cells']):
    print(f"=== CELL {i} ({c['cell_type']}) ===")
    print("".join(c.get('source', [])))

