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

key = env.get('DASHSCOPE_API_KEY')
url = 'https://ws-kvneg1w4j01n4v80.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1/chat/completions'
headers = {'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'}

models_to_test = [
    'qwen3.8-flash',
    'qwen3.7-flash',
    'qwen3.8-27b',
    'qwen3-vl-plus',
    'glm-5.3',
    'deepseek-v4.1-flash-1017',
    'deepseek-v4.1-flash',
    'qwen3.8-max-0902',
    'qwen3.7-plus',
    'kimi-k3',
    'qwen3.7-max',
    'deepseek-v4-pro',
    'qwen3.8-2.4t-a95b',
    'deepseek-v4-pro-0813'
]

def check_model(m):
    payload = {
        'model': m,
        'messages': [{'role': 'user', 'content': 'hi'}],
        'max_tokens': 10
    }
    req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            print(f'{m:<28s}: OK', flush=True)
    except urllib.error.HTTPError as he:
        print(f'{m:<28s}: HTTP {he.code}: {he.read().decode("utf-8")[:100]}', flush=True)
    except Exception as e:
        print(f'{m:<28s}: {e}', flush=True)

with ThreadPoolExecutor(max_workers=14) as ex:
    ex.map(check_model, models_to_test)
