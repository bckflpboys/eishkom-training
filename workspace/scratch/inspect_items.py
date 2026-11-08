import urllib.request
import json
import re

api_key = "AQ.Ab8RN6KWottlmFmKypg9atadZdfk9IVDF02wuF0hzsrZ1l6CmQ"
model_name = "models/gemini-flash-lite-latest"
url = f"https://generativelanguage.googleapis.com/v1beta/{model_name}:generateContent?key={api_key}"

with open('workspace/text/dbe-mathematics-g12-p2-2022-may.txt', 'r', encoding='utf-8') as f:
    qp = f.read()
with open('workspace/text/dbe-mathematics-g12-p2-2022-may-memo.txt', 'r', encoding='utf-8') as f:
    memo = f.read()

qp_q1 = qp[1062:2127].strip()
memo_q1 = memo[1579:2866].strip()

prompt = f"""You are an educational data extraction assistant following the Universal Document & Visual Extraction Standard (UDVES).
Extract all atomic subquestions for QUESTION 1 from the Question Paper and Memorandum into a JSON code block.

SOURCE DETAILS:
- source_id: dbe-mathematics-g12-p2-2022-may
- pair_source_id: dbe-mathematics-g12-p2-2022-may-memo
- subject: mathematics
- grade: 12
- language: en
- track: core_maths

INSTRUCTIONS:
1. Extract subquestions 1.1, 1.2, etc. as atomic items in a JSON array.
2. Put the mass frequency table into the "passage" field.
3. Use KaTeX LaTeX ($...$ inline, $$...$$ display) for all mathematical expressions.
4. Decimal convention: inside math mode use $0{{,}}15$, in final_answer use standard decimal point (e.g. 0.15).
5. All method marks and criteria from the memo must be included in "memo", with checkmarks formatted as $\\checkmark$.
6. Output ONLY a valid JSON array wrapped in ```json and ```.

QUESTION PAPER:
{qp_q1}

MEMORANDUM:
{memo_q1}
"""

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

with urllib.request.urlopen(req, timeout=30) as resp:
    data = json.loads(resp.read().decode("utf-8"))
    raw = data["candidates"][0]["content"]["parts"][0]["text"]
    match = re.search(r'(\[[\s\S]*\])', raw)
    items = json.loads(match.group(1) if match else raw)

print(f"Total items: {len(items)}")
print(f"Total marks: {sum(it.get('marks', 0) for it in items)}")
for it in items:
    print("-" * 50)
    print(f"Item: {it.get('item_id')} | Marks: {it.get('marks')}")
    print(f"Question: {it.get('question')}")
    print(f"Memo:\n{it.get('memo')}")
    print(f"Final Answer: {it.get('final_answer')}")

