#!/usr/bin/env python3
"""
ingest.py - turn the files you downloaded into clean text, and check your sources list.

    python pipeline/ingest.py [--sources workspace/sources/sources.csv] [--only SOURCE_ID]

WHAT IT DOES
  Reads workspace/sources/sources.csv. For each row it finds the file at workspace/raw/<local_path>
  and writes workspace/text/<source_id>.txt with "=== page N ===" markers (so answers can cite pages).
  Supports .pdf (text layer), .html/.htm, .txt/.md, .docx.

WHY THE LICENCE COLUMN IS CHECKED
  What you are allowed to do with a file depends on its licence. This script refuses rows with no
  licence and warns about the risky ones:
    - "NC" (non-commercial) -> do not train a model you sell on it
    - "ND" (no derivatives) -> the branded Siyavula books are CC BY-ND; use the UNBRANDED (CC BY) ones
    - anything saying copyright / all rights reserved / unknown -> get permission or use it only
      for evaluation, or as a seed for ORIGINAL questions (see GUIDE.md phase 5)
  This is not legal advice; it just makes sure you decided on purpose.

SCANNED PDFs
  If a page has almost no text, the PDF is probably a scan or the maths is drawn as pictures. Plain text
  extraction will not work: use an OCR/maths-aware tool (see GUIDE.md phase 2: marker, docling or MinerU),
  save the result as .md or .txt in raw/, and point local_path at it.
"""
import argparse
import csv
import html.parser
import json
import re
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from wspaths import p  # noqa: E402

RISKY = [
    (re.compile(r"\bNC\b|non-?commercial", re.I), "NON-COMMERCIAL licence: do not train a model you sell on this"),
    (re.compile(r"\bND\b|no-?derivative", re.I), "NO-DERIVATIVES licence: adapting/training may not be allowed (Siyavula: use the unbranded CC BY version)"),
    (re.compile(r"copyright|all rights|unknown|check", re.I), "licence unclear: check the terms, or use only for evaluation / as seeds for original questions"),
]
REQUIRED = ["source_id", "licence", "subject", "kind", "local_path"]


class _Text(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts, self.skip = [], 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "nav", "footer", "header"):
            self.skip += 1
        if tag in ("p", "div", "br", "li", "tr", "h1", "h2", "h3", "h4"):
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in ("script", "style", "nav", "footer", "header"):
            self.skip = max(0, self.skip - 1)

    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)


def read_pdf(path):
    from pypdf import PdfReader
    reader = PdfReader(str(path))
    pages = []
    for i, page in enumerate(reader.pages, 1):
        try:
            pages.append(page.extract_text() or "")
        except Exception:                                  # noqa: BLE001
            pages.append("")
    return pages


def read_docx(path):
    with zipfile.ZipFile(path) as z:
        xml = z.read("word/document.xml").decode("utf-8", "ignore")
    xml = re.sub(r"</w:p>", "\n", xml)
    return [re.sub(r"<[^>]+>", "", xml)]


def read_html(path):
    parser = _Text()
    parser.feed(Path(path).read_text(encoding="utf-8", errors="ignore"))
    return ["".join(parser.parts)]


def extract(path):
    suffix = Path(path).suffix.lower()
    if suffix == ".pdf":
        return read_pdf(path)
    if suffix in (".html", ".htm"):
        return read_html(path)
    if suffix == ".docx":
        return read_docx(path)
    return [Path(path).read_text(encoding="utf-8", errors="ignore")]


def clean(text):
    text = text.replace("\x00", "")
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--sources", default=str(p("sources", "sources.csv")))
    ap.add_argument("--only", help="process just this source_id")
    a = ap.parse_args()

    rows = list(csv.DictReader(open(a.sources, encoding="utf-8-sig", newline="")))
    report, problems = {}, 0
    for row in rows:
        sid = (row.get("source_id") or "").strip()
        if not sid or (a.only and sid != a.only):
            continue
        missing = [k for k in REQUIRED if not (row.get(k) or "").strip()]
        if missing:
            print(f"[{sid}] SKIPPED: missing required column(s): {', '.join(missing)}")
            problems += 1
            continue
        for rx, msg in RISKY:
            if rx.search(row["licence"]):
                print(f"[{sid}] LICENCE WARNING ({row['licence']}): {msg}")
        path = p("raw", row["local_path"].strip())
        if not path.exists():
            print(f"[{sid}] SKIPPED: file not found: {path}")
            problems += 1
            continue
        pages = extract(path)
        out_lines, low = [], []
        for i, txt in enumerate(pages, 1):
            txt = clean(txt)
            if len(txt) < 150:
                low.append(i)
            out_lines.append(f"=== page {i} ===\n{txt}\n")
        text = "\n".join(out_lines)
        out = p("text", f"{sid}.txt")
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text, encoding="utf-8")
        report[sid] = {"pages": len(pages), "chars": len(text), "low_text_pages": low[:50]}
        flag = ""
        if pages and len(low) > max(2, len(pages) // 3):
            flag = "  <-- mostly empty: probably a SCAN or maths-as-pictures; needs OCR (GUIDE.md phase 2)"
        print(f"[{sid}] {len(pages)} pages, {len(text):,} characters -> {out}{flag}")
    p("text", "_ingest_report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"\ndone: {len(report)} sources extracted, {problems} problems. Open a .txt and READ a few pages "
          f"before going on: garbled maths now means garbled training data later.")


if __name__ == "__main__":
    main()
