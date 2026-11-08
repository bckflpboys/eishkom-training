import pymupdf
import sys

sys.stdout.reconfigure(encoding='utf-8')

qp_pdf = "workspace/raw/dbe/english/physical_sciences/2021/physical_sciences_g12_2021_nov_p1.pdf"
doc = pymupdf.open(qp_pdf)
print(doc[16].get_text()) # page 17 is index 16
