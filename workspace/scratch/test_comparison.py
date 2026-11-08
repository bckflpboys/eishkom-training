import urllib.request
import json
import re

api_key = "AQ.Ab8RN6KWottlmFmKypg9atadZdfk9IVDF02wuF0hzsrZ1l6CmQ"

with open('workspace/text/dbe-mathematics-g12-p2-2022-may.txt', 'r', encoding='utf-8') as f:
    qp = f.read()
with open('workspace/text/dbe-mathematics-g12-p2-2022-may-memo.txt', 'r', encoding='utf-8') as f:
    memo = f.read()

qp_q1 = qp[1062:2127].strip()
memo_q1 = memo[1579:2866].strip()

prompt = f"""You are an expert South African CAPS curriculum educational data extraction assistant following UDVES.
Extract all atomic subquestions for QUESTION 1 from the provided Question Paper and Memorandum text.

SOURCE DETAILS:
- source_id: dbe-mathematics-g12-p2-2022-may
- pair_source_id: dbe-mathematics-g12-p2-2022-may-memo
- subject: mathematics
- grade: 12
- language: en
- track: core_maths

RULES:
1. Extract every subquestion (1.1, 1.2, etc.) as an atomic item.
2. In the "passage" field, include the mass frequency table.
3. Use KaTeX LaTeX ($...$ inline, $$...$$ display) for all mathematical expressions.
4. Decimal convention: in math mode use $0{{,}}15$, in final_answer use standard decimal point (e.g. 0.15).
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
    "memo": "<marking criteria $\\checkmark$>",
    "final_answer": "<concise answer>",
    "needs_review": false,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
  }}
]

QUESTION PAPER:
{qp_q1}

MEMORANDUM:
{memo_q1}
"""

for model_name in ["gemini-flash-latest", "gemma-4-26b-a4b-it"]:
    print(f"\n--- Testing {model_name} ---")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={api_key}"
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
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            raw = data["candidates"][0]["content"]["parts"][0]["text"]
            
            # extract json
            match = re.search(r'(\[[\s\S]*\])', raw)
            items = json.loads(match.group(1) if match else raw)
            print(f"SUCCESS with {model_name}! Extracted {len(items)} items.")
            marks = sum(it.get("marks", 0) for it in items)
            print(f"Total marks: {marks}")
            for it in items:
                print(f"  {it.get('question_ref')} ({it.get('marks')}m): {it.get('question')[:40]}... -> {it.get('final_answer')}")
            break
    except Exception as e:
        status = getattr(e, 'code', 'error')
        print(f"Failed {model_name}: HTTP {status} - {e}")

