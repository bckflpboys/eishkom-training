import urllib.request
import json

api_key = "AQ.Ab8RN6KWottlmFmKypg9atadZdfk9IVDF02wuF0hzsrZ1l6CmQ"
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemma-4-31b-it:generateContent?key={api_key}"

payload = {
    "contents": [{"parts": [{"text": "Hello, return: {\"message\": \"hi\"}"}]}]
}

req = urllib.request.Request(
    url,
    data=json.dumps(payload).encode("utf-8"),
    headers={"Content-Type": "application/json"}
)

try:
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        print("Success without responseMimeType!")
        print(res["candidates"][0]["content"]["parts"][0]["text"])
except Exception as e:
    print("Error:", e)
    if hasattr(e, "read"):
        print("HTTP error body:", e.read().decode("utf-8"))

