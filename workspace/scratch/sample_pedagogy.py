import json

with open('workspace/verified/train_all_canonical.jsonl', encoding='utf-8') as f:
    lines = [json.loads(l) for l in f]

indices = [10, 50, 100, 200, 300, 400]
for idx in indices:
    if idx < len(lines):
        r = lines[idx]
        c = r.get('control', {})
        m = r.get('meta', {})
        msgs = r.get('messages', [])
        subj = c.get('subject')
        track = c.get('language_track', '')
        grade = c.get('grade')
        print("=" * 80)
        print(f"SAMPLE {idx}: {subj} ({track}) Grade {grade} | Generator: {m.get('generator')}")
        print(f"Topic: {m.get('topic')}")
        print(f"Techniques: {m.get('techniques')}")
        for k, msg in enumerate(msgs):
            role = msg.get('role', '').upper()
            if 'reasoning' in msg and msg['reasoning']:
                print(f"  [{role} REASONING ({k})]: {msg['reasoning']}")
            print(f"  [{role} ({k})]: {msg.get('content')}")
        print()

