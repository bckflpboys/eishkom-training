import json
import re

raw_payload = r'{"memo": "$\checkmark$ \text{kg} \frac{1}{2}"}'

def robust_json_loads(text: str):
    try:
        return json.loads(text, strict=False)
    except Exception:
        pass
    # Escape any backslash that is part of LaTeX commands (e.g. \text, \frac, \checkmark)
    # or not already double-escaped
    cleaned = re.sub(r'(?<!\\)\\(?=[a-zA-Z])', r'\\\\', text)
    try:
        return json.loads(cleaned, strict=False)
    except Exception:
        cleaned2 = re.sub(r'\\(?![/"\\bfnrtu]|u[0-9a-fA-F]{4})', r'\\\\', text)
        return json.loads(cleaned2, strict=False)

parsed = robust_json_loads(raw_payload)
print("Parsed with clean LaTeX preserved:", parsed)
