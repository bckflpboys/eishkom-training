import urllib.request
import json
import time

url = "https://api.apmix.ai/v1/chat/completions"
headers = {
    "Authorization": "Bearer apx_live_FXywyzcZdig3imjqxQIJT5QJgeTCz1Y0YUK3uZSJ",
    "Content-Type": "application/json"
}

models = ["deepseek-v4.1-flash-1017-free", "nemotron-3.5-super-vl-free"]

for model in models:
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": "Hi"}],
        "max_tokens": 10
    }
    t0 = time.time()
    try:
        req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
        with urllib.request.urlopen(req, timeout=45) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            content = data["choices"][0]["message"]["content"]
            print(f"PASS {model} ({time.time()-t0:.2f}s): {content}")
    except Exception as e:
        print(f"FAIL {model} ({time.time()-t0:.2f}s): {e}")

