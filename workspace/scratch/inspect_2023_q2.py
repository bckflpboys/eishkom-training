import json

with open('workspace/items/dbe-english_fal-g12-p1-2023-nov.jsonl', encoding='utf-8') as f:
    for line in f:
        d = json.loads(line)
        if d['question_ref'] == '2':
            print("=== 2023 QUESTION 2 MEMO ===")
            print(d['memo'])
            print("=== 2023 QUESTION 2 FINAL ANSWER ===")
            print(d['final_answer'])
