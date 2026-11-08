import pymupdf

doc = pymupdf.open("workspace/raw/dbe/english/physical_sciences/2021/physical_sciences_g12_2021_nov_p1.pdf")

for page_idx in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]:
    page = doc[page_idx]
    pix = page.get_pixmap(dpi=150)
    pix.save(f"workspace/scratch/page_{page_idx+1}.png")
print("Rendered pages 3 to 17")
