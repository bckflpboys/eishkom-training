import json
import os
import urllib.request
import ssl
from pathlib import Path

ctx = ssl.create_default_context()

# Load 1 real DBE question
item_file = Path("workspace/items/dbe-mathematics-g12-p1-2023-nov.jsonl")
with open(item_file, "r", encoding="utf-8") as f:
    item = json.loads(f.readline())

prompt = f"""You are an expert South African teacher and a careful data writer. You write ONE training record for a school tutor AI following CAPS curriculum. Reply with a single JSON object and nothing else.

SOURCE ITEM:
Question: {item.get('question')}
Memo: {item.get('memo')}
Final answer: {item.get('final_answer')}

OUTPUT FORMAT:
{{
  "messages": [
    {{"role": "user", "content": "..."}},
    {{"role": "assistant", "reasoning": "...", "content": "..."}},
    {{"role": "user", "content": "..."}},
    {{"role": "assistant", "reasoning": "...", "content": "..."}}
  ],
  "meta": {{
    "strategy_used": "socratic_hints",
    "final_answer": "{item.get('final_answer')}",
    "verify_code": "import sympy as sp\\n# solve and print final answer"
  }}
}}

RULES:
1. Socratic hint ladder: ask 1 small question at a time and guide the learner.
2. In assistant messages, include "reasoning" (private thought diagnosing student) and "content" (the response).
3. In meta.verify_code, write a short Python snippet with sympy that prints the final answer.
4. Output valid JSON only.
"""

def test_provider(name, url, headers, payload, is_openai_luna=False):
    print(f"\n--- Testing {name} ---")
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=45) as resp:
            res = json.loads(resp.read().decode("utf-8"))
            msg = res["choices"][0]["message"]
            content = msg.get("content") or ""
            reasoning = msg.get("reasoning_content") or msg.get("reasoning") or ""
            print(f"[{name}] SUCCESS! Content length: {len(content)} chars. Reasoning length: {len(reasoning)} chars.")
            # Preview first 150 chars of content
            print(f"[{name}] Preview:\n{content[:200]}...")
            return True
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "ignore")[:300]
        print(f"[{name}] HTTP {e.code}: {body}")
        return False
    except Exception as e:
        print(f"[{name}] Error: {e}")
        return False

# 1. OpenAI (gpt-6-luna)
openai_key = "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"
test_provider(
    "OpenAI (gpt-6-luna)",
    "https://api.openai.com/v1/chat/completions",
    {"Authorization": f"Bearer {openai_key}", "Content-Type": "application/json"},
    {
        "model": "gpt-6-luna",
        "messages": [{"role": "user", "content": prompt}],
        "max_completion_tokens": 1500
    }
)

# 2. OpenRouter (nemotron-3-ultra-550b)
or_key = "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"
test_provider(
    "OpenRouter (nemotron-3-ultra-550b)",
    "https://openrouter.ai/api/v1/chat/completions",
    {"Authorization": f"Bearer {or_key}", "Content-Type": "application/json"},
    {
        "model": "nvidia/nemotron-3-ultra-550b-a55b:free",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 1500
    }
)

# 3. Intern-AI (glm-5.3)
intern_key = "sk-7394079193455baf4de2616444aa1523f92883ca8e3720815d7022d3bb4abe90"
test_provider(
    "Intern-AI (glm-5.3)",
    "https://discovery-api.intern-ai.org.cn/v1/chat/completions",
    {"Authorization": f"Bearer {intern_key}", "Content-Type": "application/json"},
    {
        "model": "glm-5.3",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 1500
    }
)

# 4. Intern-AI (deepseek-v4.1-flash-1017)
test_provider(
    "Intern-AI (deepseek-v4.1-flash-1017)",
    "https://discovery-api.intern-ai.org.cn/v1/chat/completions",
    {"Authorization": f"Bearer {intern_key}", "Content-Type": "application/json"},
    {
        "model": "deepseek-v4.1-flash-1017",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 1500
    }
)

