import urllib.request
import json
import os

with open('workspace/text/dbe-mathematics-g12-p2-2022-may.txt', 'r', encoding='utf-8') as f:
    qp = f.read()
with open('workspace/text/dbe-mathematics-g12-p2-2022-may-memo.txt', 'r', encoding='utf-8') as f:
    memo = f.read()

qp_q1 = qp[1062:2127].strip()
memo_q1 = memo[1579:2866].strip()

prompt = f"""Extract all subquestions for QUESTION 1 as a JSON array of items:
QUESTION PAPER:
{qp_q1}

MEMORANDUM:
{memo_q1}
"""

api_key = "AQ.Ab8RN6KWottlmFmKypg9atadZdfk9IVDF02wuF0hzsrZ1l6CmQ"
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemma-4-31b-it:generateContent?key={api_key}"

payload = {
    "contents": [{"parts": [{"text": prompt}]}],
    "generationConfig": {
        "responseMimeType": "application/json"
    }
}

req = urllib.request.Request(
    url,
    data=json.dumps(payload).encode("utf-8"),
    headers={"Content-Type": "application/json"}
)

try:
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        print("Response structure keys:", res.keys())
        cand = res.get("candidates", [{}])[0]
        print("Finish reason:", cand.get("finishReason"))
        parts = cand.get("content", {}).get("parts", [])
        print("Number of parts:", len(parts))
        if parts:
            print("First 500 chars of response text:\n", parts[0].get("text", "")[:500])
except Exception as e:
    print("Error:", e)
    if hasattr(e, "read"):
        print("HTTP error body:", e.read().decode("utf-8"))

