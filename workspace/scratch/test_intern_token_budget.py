import urllib.request
import json
import ssl

ctx = ssl.create_default_context()
intern_key = "sk-7394079193455baf4de2616444aa1523f92883ca8e3720815d7022d3bb4abe90"
url = "https://discovery-api.intern-ai.org.cn/v1/chat/completions"
headers = {"Authorization": f"Bearer {intern_key}", "Content-Type": "application/json"}

for m in ["glm-5.3", "Atria-Dawn", "deepseek-v4.1-flash-1017"]:
    payload = {
        "model": m,
        "messages": [{"role": "user", "content": "Solve for x: x^2 + x - 12 = 0. Output JSON: {\"solution\": \"...\"}"}],
        "max_tokens": 3000
    }
    req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=35) as resp:
            res = json.loads(resp.read().decode("utf-8"))
            msg = res["choices"][0]["message"]
            c = msg.get("content") or ""
            r = msg.get("reasoning_content") or ""
            print(f"[{m}] Content len: {len(c)} | Reasoning len: {len(r)}")
            if c:
                print(f"[{m}] Output: {c[:150]}")
    except Exception as e:
        print(f"[{m}] Failed: {e}")

