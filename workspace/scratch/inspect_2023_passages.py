import json

with open('workspace/items/dbe-english_fal-g12-p1-2023-nov.jsonl', encoding='utf-8') as f:
    items = [json.loads(line) for line in f]

for ref in ['1.1.1', '2', '3.1', '4.1', '5.1.1a', '5.2.1']:
    for it in items:
        if it['question_ref'] == ref:
            print(f"=== {ref} PASSAGE PREVIEW ===")
            print(it['passage'][:300])
            print("...\n" + it['passage'][-200:])
            print("="*50)
