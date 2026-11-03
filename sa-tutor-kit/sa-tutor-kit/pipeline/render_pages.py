#!/usr/bin/env python3
"""
render_pages.py - turn PDF pages into PNG images (for the vision phase).

    python pipeline/render_pages.py --pdf workspace/raw/dbe/maths_p1.pdf --out workspace/images/maths_p1 --dpi 130 [--pages 1-5]

WHY
  To teach the model to READ a photographed worksheet or exam page you need pictures of questions
  paired with the correct transcription (see GUIDE.md phase 11). Rendering real exam pages gives you
  printed examples for free. Handwriting needs real photos (get consent; no learner names or faces).
  Keep dpi modest (110-150): more pixels = more image tokens = slower and more memory on a phone.
"""
import argparse
import csv
import sys
from pathlib import Path


def parse_pages(spec, n):
    if not spec:
        return list(range(n))
    out = []
    for part in spec.split(","):
        if "-" in part:
            a, b = part.split("-")
            out += list(range(int(a) - 1, min(int(b), n)))
        else:
            out.append(int(part) - 1)
    return [i for i in out if 0 <= i < n]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--pdf", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--dpi", type=int, default=130)
    ap.add_argument("--pages", help="e.g. 1-5,8")
    a = ap.parse_args()
    try:
        import pypdfium2 as pdfium
    except ImportError:
        sys.exit("pip install pypdfium2")
    pdf = pdfium.PdfDocument(a.pdf)
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    rows = []
    for i in parse_pages(a.pages, len(pdf)):
        img = pdf[i].render(scale=a.dpi / 72).to_pil().convert("RGB")
        name = f"{Path(a.pdf).stem}_p{i + 1:03d}.png"
        img.save(out / name)
        rows.append([name, i + 1, img.width, img.height])
    with open(out / "manifest.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["file", "page", "width", "height"])
        w.writerows(rows)
    print(f"wrote {len(rows)} images to {out}")


if __name__ == "__main__":
    main()
