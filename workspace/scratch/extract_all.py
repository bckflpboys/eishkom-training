import fitz
import os

qp_doc = fitz.open('sa-tutor-kit/sa-tutor-kit/workspace/raw/dbe/english/english_fal/2022/english_fal_g12_2022_nov_p1.pdf')
os.makedirs('workspace/scratch', exist_ok=True)

for pno, page in enumerate(qp_doc):
    images = page.get_images(full=True)
    for idx, img in enumerate(images):
        xref = img[0]
        base_img = qp_doc.extract_image(xref)
        w, h = base_img['width'], base_img['height']
        ext = base_img['ext']
        fname = f'workspace/scratch/page_{pno+1}_img_{idx}.{ext}'
        with open(fname, 'wb') as f:
            f.write(base_img['image'])
        print(f'Page {pno+1} Image {idx}: {fname} ({w}x{h})')
