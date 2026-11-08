import urllib.request
import json
import ssl

ctx = ssl.create_default_context()
openrouter_key = "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"
url = "https://openrouter.ai/api/v1/chat/completions"
headers = {"Authorization": f"Bearer {openrouter_key}", "Content-Type": "application/json"}

payload = {
    "model": "nvidia/nemotron-3-ultra-550b-a55b:free",
    "messages": [
        {"role": "system", "content": "You are a JSON generator. Do NOT write chain-of-thought in your response text. Output the raw JSON directly starting with { and ending with }."},
        {"role": "user", "content": "Output a tutoring record JSON for solving 2x = 6. Output format: {\"messages\": [{\"role\": \"user\", \"content\": \"...\"}, {\"role\": \"assistant\", \"reasoning\": \"...\", \"content\": \"...\"}], \"meta\": {\"final_answer\": \"x = 3\"}}"}
    ],
    "response_format": {"type": "json_object"},
    "max_tokens": 2500
}
req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
try:
    with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        msg = res["choices"][0]["message"]
        c = msg.get("content") or ""
        print(f"[nemotron-3-ultra-550b] SUCCESS! Content len: {len(c)}")
        print(f"[nemotron-3-ultra-550b] Output: {c[:150]}...")
except Exception as e:
    print(f"[nemotron-3-ultra-550b] Error: {e}")

