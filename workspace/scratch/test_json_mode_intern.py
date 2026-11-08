import urllib.request
import json
import ssl

ctx = ssl.create_default_context()
intern_key = "sk-7394079193455baf4de2616444aa1523f92883ca8e3720815d7022d3bb4abe90"
url = "https://discovery-api.intern-ai.org.cn/v1/chat/completions"
headers = {"Authorization": f"Bearer {intern_key}", "Content-Type": "application/json"}

for m in ["glm-5.3", "deepseek-v4.1-flash-1017", "Atria-Dawn"]:
    payload = {
        "model": m,
        "messages": [
            {"role": "system", "content": "You are a JSON generator. Do NOT write chain-of-thought in your response text. Output the raw JSON directly starting with { and ending with }."},
            {"role": "user", "content": "Output a tutoring record JSON for solving 2x = 6. Output format: {\"messages\": [{\"role\": \"user\", \"content\": \"...\"}, {\"role\": \"assistant\", \"reasoning\": \"...\", \"content\": \"...\"}], \"meta\": {\"final_answer\": \"x = 3\"}}"}
        ],
        "response_format": {"type": "json_object"},
        "max_tokens": 3000
    }
    req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
            res = json.loads(resp.read().decode("utf-8"))
            msg = res["choices"][0]["message"]
            c = msg.get("content") or ""
            print(f"[{m}] SUCCESS! Content len: {len(c)}")
            print(f"[{m}] Output: {c[:150]}...")
    except Exception as e:
        print(f"[{m}] Error: {e}")

