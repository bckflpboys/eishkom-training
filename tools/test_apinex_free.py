import urllib.request
import urllib.error
import json
import time

url = "https://api.apinex.bond/v1/chat/completions"
key = "sk-apxa989180905641e7065d9d54287436797ae6a8cab8b890be"
headers = {
    "Authorization": f"Bearer {key}",
    "Content-Type": "application/json"
}

# The remaining free models on APInex that hit the 15 RPM rate limit earlier:
candidates = [
    "free/gemini-3.8-flash",
    "free/gemini-3.1-pro",
    "free/claude-sonnet-4.6",
    "free/claude-opus-4.6",
    "free/glm-5.3",
    "free/mimo-v2.6-flash",
    "free/kimi-k2.8",
    "free/minimax-m3",
    "free/hy4",
    "free/jev-1.13",
]

for model in candidates:
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": "Hi"}],
        "max_tokens": 10
    }
    t0 = time.time()
    try:
        req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            content = data["choices"][0]["message"]["content"]
            print(f"[PASS] {model} ({time.time()-t0:.2f}s): {content.strip()[:40]}")
    except urllib.error.HTTPError as e:
        err = e.read().decode("utf-8", errors="ignore")
        print(f"[FAIL] {model} ({time.time()-t0:.2f}s): HTTP {e.code}: {err[:150]}")
    except Exception as e:
        print(f"[FAIL] {model} ({time.time()-t0:.2f}s): {e}")
    time.sleep(4.5)  # Stay safely under 15 RPM

