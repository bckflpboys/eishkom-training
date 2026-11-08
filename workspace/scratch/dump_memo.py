import pymupdf
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

memo_pdf = "workspace/raw/dbe/english/physical_sciences/2021/physical_sciences_g12_2021_nov_p1_memo.pdf"
doc = pymupdf.open(memo_pdf)

full_memo = ""
for page in doc:
    full_memo += page.get_text() + "\n---PAGE---\n"

# Let's inspect the sections in memo
with open("workspace/scratch/memo_dump.txt", "w", encoding="utf-8") as f:
    f.write(full_memo)

print("Dumped memo to workspace/scratch/memo_dump.txt")
