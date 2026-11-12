import urllib.request, json, ssl, time
from pathlib import Path
env = dict(l.strip().split('=', 1) for l in Path('.env').read_text().splitlines() if '=' in l and not l.startswith('#'))
k = env.get('INTERN_API_KEY')
base = env.get('INTERN_BASE_URL', 'https://discovery-api.intern-ai.org.cn/v1')
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

req = urllib.request.Request(f'{base}/chat/completions',
    data=json.dumps({'model': 'deepseek-v4.1-flash-1017', 'messages': [{'role': 'user', 'content': 'Respond with {"status": "ok"}'}], 'max_tokens': 50}).encode(),
    headers={'Authorization': f'Bearer {k}', 'Content-Type': 'application/json', 'User-Agent': 'curl/8.4.0'})
try:
    with urllib.request.urlopen(req, context=ctx, timeout=25) as r:
        res = json.loads(r.read().decode())
        choice = res['choices'][0]['message']
        print('Intern-AI DeepSeek SUCCESS!', choice.get('content') or choice.get('reasoning_content'))
except Exception as e:
    print('Intern-AI DeepSeek Error:', e)

