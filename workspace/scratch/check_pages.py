import pymupdf
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

qp_pdf = "workspace/raw/dbe/english/physical_sciences/2021/physical_sciences_g12_2021_nov_p1.pdf"
memo_pdf = "workspace/raw/dbe/english/physical_sciences/2021/physical_sciences_g12_2021_nov_p1_memo.pdf"

doc_qp = pymupdf.open(qp_pdf)
print(f"QP PDF has {len(doc_qp)} pages")

doc_memo = pymupdf.open(memo_pdf)
print(f"Memo PDF has {len(doc_memo)} pages")

# Let's inspect pages of QP
for page_num in range(len(doc_qp)):
    text = doc_qp[page_num].get_text()
    for line in text.split('\n'):
        if line.strip().startswith("QUESTION"):
            print(f"Page {page_num + 1}: {line.strip()}")
