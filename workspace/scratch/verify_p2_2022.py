import json

path = 'workspace/items/mathematics/dbe-mathematics-g12-p2-2022-may.jsonl'
with open(path, 'r', encoding='utf-8') as f:
    items = [json.loads(line) for line in f if line.strip()]

print(f"Total items: {len(items)}")
total_marks = sum(it.get('marks', 0) for it in items)
print(f"Total marks: {total_marks}")

unbalanced = 0
for it in items:
    for field in ['question', 'memo', 'passage', 'final_answer']:
        val = it.get(field) or ''
        if val.count('$') % 2 != 0:
            unbalanced += 1
print(f"Unbalanced dollar instances: {unbalanced}")

print("\n--- SAMPLE ITEMS ---")
for it in [items[0], items[5], items[20], items[-1]]:
    print(f"[{it['item_id']}] ({it['marks']}m): {it['question'][:60]}")
    print(f"  Final Answer: {it.get('final_answer')}")
    print(f"  Memo preview: {it.get('memo')[:60]}...")

