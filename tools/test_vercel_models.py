import urllib.request
import json
import os
from concurrent.futures import ThreadPoolExecutor

env = {}
if os.path.exists('.env'):
    for line in open('.env', encoding='utf-8'):
        line = line.strip()
        if '=' in line and not line.startswith('#'):
            k, v = line.split('=', 1)
            env[k.strip()] = v.strip().strip('"').strip("'")

key = env.get('VERCEL_GATEWAY_API_KEY')
url = 'https://ai-gateway.vercel.sh/v1/chat/completions'
headers = {'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'}

models_to_test = [
    'nvidia/nemotron-3-ultra-550b-a55b',
    'openai/gpt-oss-120b',
    'nvidia/nemotron-3.5-super-vl',
    'nvidia/nemotron-3.5-lightning-free',
    'deepseek/deepseek-v4.1-flash-1017',
    'thinkingmachines/inkling-2-small',
    'meta/muse-ember',
    'minimax/minimax-m3.1-flash',
    'anthropic/claude-haiku-5.5',
    'xiaomi/mimo-v2.6-flash',
    'xiaomi/mimo-v2.6-pro',
    'meta/muse-spark-1.3-contributor'
]

def check_model(m):
    payload = {
        'model': m,
        'messages': [{'role': 'user', 'content': 'hi'}],
        'max_tokens': 10
    }
    req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            print(f'{m:<35s}: OK', flush=True)
    except urllib.error.HTTPError as he:
        print(f'{m:<35s}: HTTP {he.code}: {he.read().decode("utf-8")[:100]}', flush=True)
    except Exception as e:
        print(f'{m:<35s}: {e}', flush=True)

with ThreadPoolExecutor(max_workers=12) as ex:
    ex.map(check_model, models_to_test)

