import json

nb = json.load(open('sa_tutor_colab.ipynb', encoding='utf-8'))
for i, c in enumerate(nb['cells']):
    s = c.get('source', [])
    first = s[0].strip() if s else 'EMPTY'
    print(f"Cell {i:2d} ({c.get('cell_type')}): {first[:75]}")

