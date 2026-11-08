import re
import json

raw_text = '*   Input: Request for a JSON object containing a list of 2 numbers: 1 and 2.\n    *   Constraints: Valid parseable JSON, double-quoted strings (for non-scalars/booleans/nulls), no comments, single JSON array if multiple are requested (not applicable here), no extra text.\n\n    *   Key: "numbers" (or similar)\n    *   Value: [1, 2]\n\n    ```json\n    {\n      "numbers": [1, 2]\n    }\n    ```\n\n    *   Valid JSON? Yes.\n    *   Parseable? Yes.\n    *   No extra text? Yes.\n    *   No comments? Yes.'

def extract_json(text: str):
    # Try finding markdown code block first
    code_match = re.search(r'```(?:json)?\s*([\s\S]*?)\s*```', text)
    if code_match:
        content = code_match.group(1).strip()
        try:
            return json.loads(content)
        except Exception:
            pass
    # Try finding first valid JSON object or array
    for pattern in [r'(\[[\s\S]*\])', r'(\{[\s\S]*\})']:
        m = re.search(pattern, text)
        if m:
            try:
                return json.loads(m.group(1))
            except Exception:
                pass
    return json.loads(text.strip())

parsed = extract_json(raw_text)
print("Extracted successfully:", parsed)

