import json

with open('workspace/items/dbe-english_fal-g12-p1-2023-nov.jsonl', encoding='utf-8') as f:
    for line in f:
        d = json.loads(line)
        print(f"{d['question_ref']:<10} {d['marks']:<3} {d['kind']:<18} {d['topic']}")
