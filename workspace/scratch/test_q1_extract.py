import urllib.request
import json
import re

api_key = "AQ.Ab8RN6KWottlmFmKypg9atadZdfk9IVDF02wuF0hzsrZ1l6CmQ"
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemma-4-31b-it:generateContent?key={api_key}"

with open('workspace/text/dbe-mathematics-g12-p2-2022-may.txt', 'r', encoding='utf-8') as f:
    qp = f.read()
with open('workspace/text/dbe-mathematics-g12-p2-2022-may-memo.txt', 'r', encoding='utf-8') as f:
    memo = f.read()

qp_q1 = qp[1062:2127].strip()
memo_q1 = memo[1579:2866].strip()

prompt = f"""You are an expert South African CAPS curriculum educational data extraction assistant following the Universal Document & Visual Extraction Standard (UDVES).

Your task is to extract all atomic subquestions for QUESTION 1 from the provided Question Paper text and Marking Guideline (Memorandum) text.

SOURCE DETAILS:
- source_id: dbe-mathematics-g12-p2-2022-may
- pair_source_id: dbe-mathematics-g12-p2-2022-may-memo
- subject: mathematics
- grade: 12
- language: en
- track: core_maths

RULES:
1. Extract every subquestion (e.g. 1.1, 1.2, etc.) as an atomic JSON item.
2. If there is a table or context in the preamble, include it in the "passage" field of each subquestion.
3. Use KaTeX LaTeX ($...$ inline, $$...$$ display) for all mathematical expressions.
4. Decimal convention: inside math mode use $0{{,}}15$, in final_answer use decimal point (e.g. 0.15).
5. All method marks and criteria from the memo must be included in "memo", with checkmarks formatted as $\\checkmark$.
6. Ensure all '$' delimiters are strictly balanced.

OUTPUT FORMAT:
Return a JSON array of objects with keys:
[
  {{
    "item_id": "dbe-mathematics-g12-p2-2022-may-1.1",
    "source_id": "dbe-mathematics-g12-p2-2022-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2022-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "1.1",
    "marks": 1,
    "topic": "Statistics - Modal Class",
    "passage": "<table or context>",
    "question": "<verbatim question>",
    "memo": "<step-by-step marking criteria $\\checkmark$>",
    "final_answer": "<concise answer>",
    "needs_review": false,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
  }}
]

QUESTION PAPER TEXT:
{qp_q1}

MEMORANDUM TEXT:
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

print("Sending Question 1 extraction request to Gemma 4 31B...")

def extract_json(text: str):
    code_match = re.search(r'```(?:json)?\s*([\s\S]*?)\s*```', text)
    if code_match:
        content = code_match.group(1).strip()
        try:
            return json.loads(content)
        except Exception:
            pass
    for pattern in [r'(\[[\s\S]*\])', r'(\{[\s\S]*\})']:
        m = re.search(pattern, text)
        if m:
            try:
                return json.loads(m.group(1))
            except Exception:
                pass
    return json.loads(text.strip())

try:
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        raw = res["candidates"][0]["content"]["parts"][0]["text"]
        items = extract_json(raw)
        print(f"Extracted {len(items)} items for Question 1!")
        total_marks = sum(it.get("marks", 0) for it in items)
        print(f"Total marks for Q1: {total_marks}")
        for it in items:
            print(f"  {it.get('question_ref')} ({it.get('marks')}m): {it.get('question')[:50]}...")
            print(f"     final_answer: {it.get('final_answer')}")
except Exception as e:
    print("Error:", e)
    if hasattr(e, "read"):
        print("Details:", e.read().decode("utf-8"))

