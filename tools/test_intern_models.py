import os
import sys
import json
import time
import ssl
import urllib.request
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

def load_env():
    keys = {}
    for env_path in [ROOT_DIR / ".env", ROOT_DIR / "sa-tutor-kit" / "sa-tutor-kit" / ".env"]:
        if env_path.exists():
            for line in env_path.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if "=" in line and not line.startswith("#"):
                    k, v = line.split("=", 1)
                    keys[k.strip()] = v.strip().strip("'\"")
    return keys

ENV_KEYS = load_env()
INTERN_KEY = ENV_KEYS.get("INTERN_API_KEY", "")
INTERN_BASE_URL = ENV_KEYS.get("INTERN_BASE_URL", "https://discovery-api.intern-ai.org.cn/v1")

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = f"{INTERN_BASE_URL}/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {INTERN_KEY}",
    "User-Agent": "curl/8.4.0"
}

models_to_test = ["deepseek-v4.1-flash-1017", "deepseek-v4-flash-0731"]

test_prompt = "Return valid JSON only starting with { immediately. Solve: calculate force for mass 10kg, acceleration 2m/s^2."

for m in models_to_test:
    payload = {
        "model": m,
        "messages": [
            {"role": "system", "content": "You are a CAPS physics tutor. Output raw JSON starting with {"},
            {"role": "user", "content": test_prompt}
        ],
        "temperature": 0.2,
        "max_tokens": 1000
    }
    t0 = time.time()
    try:
        req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
            raw = resp.read().decode("utf-8")
            dt = time.time() - t0
            data = json.loads(raw)
            choice = data["choices"][0]["message"]
            content = choice.get("content") or choice.get("reasoning_content") or ""
            print(f"Model {m}: Success in {dt:.2f}s! ({len(content)} chars)")
            print("Preview:", content[:100].replace('\n', ' '))
    except Exception as e:
        dt = time.time() - t0
        print(f"Model {m}: Error in {dt:.2f}s: {e}")
    time.sleep(2)

