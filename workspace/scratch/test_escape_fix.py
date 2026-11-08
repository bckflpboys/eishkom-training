import json
import re

raw = open('workspace/scratch/deepseek_raw.txt', 'r', encoding='utf-8').read()

try:
    obj = json.loads(raw)
    print("Plain loads succeeded!")
except Exception as e:
    print("Plain loads failed as expected:", e)

# Fix unescaped backslashes in JSON
sanitized = re.sub(r'\\(?![/"\\bfnrtu])', r'\\\\', raw)
try:
    obj = json.loads(sanitized)
    print("\nSANITIZED LOADS SUCCEEDED!")
    print("Keys:", list(obj.keys()))
    print("Messages count:", len(obj["messages"]))
    print("Final answer:", obj["meta"]["final_answer"])
except Exception as e:
    print("Sanitized loads failed:", e)

