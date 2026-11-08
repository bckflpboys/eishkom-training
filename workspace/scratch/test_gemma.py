import urllib.request
import json

api_key = "AQ.Ab8RN6KWottlmFmKypg9atadZdfk9IVDF02wuF0hzsrZ1l6CmQ"
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemma-4-31b-it:generateContent?key={api_key}"

payload = {
    "contents": [{
        "parts": [{"text": "Output JSON object: {\"status\": \"ok\"}"}]
    }],
    "generationConfig": {
        "responseMimeType": "application/json",
        "thinkingConfig": {
            "thinkingBudget": 0
        }
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
        print("Success with thinkingBudget: 0!")
        print(res["candidates"][0]["content"]["parts"][0]["text"])
except Exception as e:
    print("Error:", e)
    if hasattr(e, "read"):
        print("Details:", e.read().decode("utf-8"))
