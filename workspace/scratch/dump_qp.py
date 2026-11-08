import pymupdf
import sys

sys.stdout.reconfigure(encoding='utf-8')

qp_pdf = "workspace/raw/dbe/english/physical_sciences/2021/physical_sciences_g12_2021_nov_p1.pdf"
doc = pymupdf.open(qp_pdf)

full_qp = ""
for i, page in enumerate(doc):
    full_qp += f"\n=== PAGE {i+1} ===\n" + page.get_text()

with open("workspace/scratch/qp_dump.txt", "w", encoding="utf-8") as f:
    f.write(full_qp)

print("Dumped qp to workspace/scratch/qp_dump.txt")
