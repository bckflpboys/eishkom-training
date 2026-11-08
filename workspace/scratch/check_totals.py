import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("workspace/scratch/qp_dump.txt", "r", encoding="utf-8") as f:
    qp = f.read()

# Let's inspect the questions
# In DBE Physical Sciences P1:
# Total is 150 marks.
# Let's see the total marks per question from the QP totals:
# Usually at the end of each question: [16], [15], etc.
totals = re.findall(r"\[(\d+)\]", qp)
print("Totals in QP [marks]:", totals)

# Let's find question headers and their totals
for q_num in range(1, 11):
    m = re.search(rf"QUESTION\s+{q_num}[\s\S]*?(?=QUESTION\s+{q_num+1}|TOTAL:|$)", qp)
    if m:
        text = m.group(0)
        tot = re.findall(r"\[(\d+)\]", text)
        print(f"Question {q_num}: marks = {tot[-1] if tot else 'None'}")
