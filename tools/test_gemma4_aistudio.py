import urllib.request, json
from pathlib import Path
env = dict(l.strip().split('=', 1) for l in Path('.env').read_text().splitlines() if '=' in l and not l.startswith('#'))
k1 = env.get('GEMINI_API_KEY')
k2 = env.get('GEMINI_API_KEY_2')

for k_name, k in [('Key 1', k1), ('Key 2', k2)]:
    for m in ['gemma-4-26b-a4b-it', 'gemma-4-31b-it']:
        url = f'https://generativelanguage.googleapis.com/v1beta/models/{m}:generateContent?key={k}'
        payload = {
            'contents': [{'parts': [{'text': 'Respond with JSON: {"status": "ok"}'}]}]
        }
        try:
            req = urllib.request.Request(url, data=json.dumps(payload).encode(), headers={'Content-Type': 'application/json'})
            with urllib.request.urlopen(req, timeout=15) as r:
                res = json.loads(r.read().decode())
                cand = res.get('candidates', [{}])[0]
                text = cand.get('content', {}).get('parts', [{}])[0].get('text', '')
                print(f'{k_name} | {m}: SUCCESS! Reply: {text.strip()[:60]}')
        except urllib.error.HTTPError as e:
            print(f'{k_name} | {m}: HTTP {e.code} -> {e.read().decode()[:200]}')
        except Exception as e:
            print(f'{k_name} | {m}: Error -> {e}')

