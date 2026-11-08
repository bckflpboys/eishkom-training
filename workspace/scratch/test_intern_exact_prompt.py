import urllib.request
import json
import ssl

ctx = ssl.create_default_context()
intern_key = "sk-7394079193455baf4de2616444aa1523f92883ca8e3720815d7022d3bb4abe90"
url = "https://discovery-api.intern-ai.org.cn/v1/chat/completions"
headers = {"Authorization": f"Bearer {intern_key}", "Content-Type": "application/json"}

prompt = """CRITICAL: DO NOT WRITE THINKING OR ANALYSIS IN YOUR RESPONSE TEXT. START YOUR RESPONSE WITH { IMMEDIATELY.

You are an expert South African teacher. Output ONE tutoring record JSON:
{
  "messages": [
    {"role": "user", "content": "How do I find the roots of x^2 - 9 = 0?"},
    {"role": "assistant", "reasoning": "Solve by difference of squares: (x-3)(x+3)=0.", "content": "Notice that x^2 - 9 is a difference of two squares. How can you factorise it?"},
    {"role": "user", "content": "(x - 3)(x + 3) = 0 so x = 3 or x = -3"},
    {"role": "assistant", "reasoning": "Learner solved correctly.", "content": "Spot on! x = 3 or x = -3."}
  ],
  "meta": {
    "strategy_used": "socratic_hints",
    "final_answer": "x = 3 or x = -3",
    "verify_code": "import sympy as sp\\nx = sp.Symbol('x')\\nprint(sp.solve(x**2 - 9, x))"
  }
}
"""

payload = {
    "model": "deepseek-v4.1-flash-1017",
    "messages": [
        {"role": "system", "content": "You are a JSON generator. Output RAW JSON ONLY. Never output thinking process outside the JSON."},
        {"role": "user", "content": prompt}
    ],
    "response_format": {"type": "json_object"},
    "max_tokens": 3000
}

req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
try:
    with urllib.request.urlopen(req, context=ctx, timeout=35) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        msg = res["choices"][0]["message"]
        c = msg.get("content") or ""
        print("SUCCESS! Content length:", len(c))
        print("Preview:\n", c[:250])
except Exception as e:
    print("FAILED:", e)

