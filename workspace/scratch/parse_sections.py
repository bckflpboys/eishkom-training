import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open("workspace/text/dbe-physical_sciences-g12-p1-2021-nov.txt", "r", encoding="utf-8") as f:
    qp = f.read()

with open("workspace/text/dbe-physical_sciences-g12-p1-2021-nov-memo.txt", "r", encoding="utf-8") as f:
    memo = f.read()

# Let's inspect subquestions in QP
print("--- SUBQUESTIONS IN QP ---")
lines = qp.split("\n")
for i, line in enumerate(lines):
    # Match patterns like 1.1, 2.1, 2.2.1, etc. at the start of a line
    m = re.match(r"^(\d+\.\d+(\.\d+)?)\s*(.*)", line.strip())
    if m:
        # Check if the line or next lines have marks [X] or (X)
        print(f"Line {i+1}: {line.strip()[:80]}")

# Let's inspect subquestions in MEMO
print("\n--- SUBQUESTIONS IN MEMO ---")
lines_m = memo.split("\n")
for i, line in enumerate(lines_m):
    m = re.match(r"^(\d+\.\d+(\.\d+)?)\s*(.*)", line.strip())
    if m:
        print(f"Line {i+1}: {line.strip()[:80]}")
