import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open("workspace/text/dbe-physical_sciences-g12-p1-2021-nov.txt", "r", encoding="utf-8") as f:
    qp = f.read()

with open("workspace/text/dbe-physical_sciences-g12-p1-2021-nov-memo.txt", "r", encoding="utf-8") as f:
    memo = f.read()

print("QP length:", len(qp))
print("Memo length:", len(memo))

# Find lines matching QUESTION \d+
for line in qp.split("\n"):
    if re.match(r"^\s*QUESTION\s+\d+", line, re.IGNORECASE):
        print("QP:", line.strip())

for line in memo.split("\n"):
    if re.match(r"^\s*QUESTION\s+\d+", line, re.IGNORECASE):
        print("MEMO:", line.strip())
