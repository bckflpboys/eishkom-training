import json
import urllib.request
import time
from pathlib import Path

env_file = Path('.env')
keys = {}
for line in env_file.read_text(encoding='utf-8').splitlines():
    if '=' in line and not line.startswith('#'):
        k, v = line.split('=', 1)
        keys[k.strip()] = v.strip().strip("'\"")

intern_key = keys.get('INTERN_API_KEY', '')
base_url = keys.get('INTERN_BASE_URL', 'https://discovery-api.intern-ai.org.cn/v1')

print(f"Testing Intern-AI at {base_url} with deepseek-v4.1-flash-1017...")
url = f"{base_url.rstrip('/')}/chat/completions"
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    "Authorization": f"Bearer {intern_key}",
    "Content-Type": "application/json",
    "User-Agent": "curl/8.4.0"
}
payload = {
    "model": "deepseek-v4.1-flash-1017",
    "messages": [
        {"role": "user", "content": "Hello, please answer in 1 sentence: What is 2 + 2?"}
    ],
    "max_tokens": 100
}

t0 = time.time()
try:
    req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers)
    with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
        elapsed = time.time() - t0
        data = json.loads(resp.read().decode('utf-8'))
        print(f"SUCCESS in {elapsed:.2f}s:")
        print(data['choices'][0]['message'].get('content'))
except Exception as e:
    print(f"FAILED ({e})")
