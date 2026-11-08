import os
import json
import urllib.request
import urllib.error
from pathlib import Path

env_txt = Path('.env').read_text(encoding='utf-8')
api_key = ''
for line in env_txt.splitlines():
    if line.startswith('GEMINI_API_KEY='):
        api_key = line.split('=', 1)[1].strip().strip('"\'')

for model in ['gemini-3.1-flash-lite', 'gemma-4-26b-a4b-it', 'gemma-4-31b-it', 'gemini-2.5-flash']:
    url = f'https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}'
    data = json.dumps({'contents': [{'parts': [{'text': 'Say hello'}]}]}).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            res = json.loads(r.read().decode('utf-8'))
            ans = res['candidates'][0]['content']['parts'][0]['text'].strip()
            print(f'[{model}] SUCCESS: {ans[:30]}')
    except urllib.error.HTTPError as e:
        err = e.read().decode('utf-8')
        try:
            err_j = json.loads(err)
            msg = err_j.get('error', {}).get('message', '')
        except:
            msg = err[:100]
        print(f'[{model}] HTTP {e.code}: {msg}')
    except Exception as e:
        print(f'[{model}] Exception: {e}')

