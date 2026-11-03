#!/usr/bin/env python3
"""
retrieval.py - a small search engine over your own text (BM25, pure Python, no dependencies).

WHY THIS EXISTS
  The model's weights should hold SKILLS (how to teach, which language to use, how to call tools).
  CONTENT (what CAPS says, what a textbook explains) lives in a library the model looks things up in.
  This file builds that library from workspace/text/*.txt and searches it. It is used in two places:
    1. while making training data: the `search_curriculum` tool result is a REAL search result, not
       something the teacher model made up;
    2. in your app: do the same search (BM25 here, or embeddings later) and return the same text format.

USAGE
  python retrieval.py build  --text workspace/text --out workspace/index/bm25.json
  python retrieval.py search "quadratic formula" --index workspace/index/bm25.json [-k 3] [--subject maths]
"""
from __future__ import annotations

import argparse
import json
import math
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

STOP = set("""a an the and or of to in on for with is are was were be as at by it this that from not
die en of van in op vir met is was wat as by dit nie 'n""".split())
PAGE_RE = re.compile(r"^=== page (\d+) ===\s*$", re.M)
K1, B = 1.5, 0.75


def tokenize(text):
    return [t for t in re.findall(r"\w+", text.lower()) if len(t) > 1 and t not in STOP]


def chunk_pages(text, max_chars=900, overlap=120):
    """Split text into chunks, remembering the page number from the '=== page N ===' markers."""
    pieces = PAGE_RE.split(text)          # [before, page1, text1, page2, text2 ...]
    pages = []
    if len(pieces) == 1:
        pages.append((None, pieces[0]))
    else:
        for i in range(1, len(pieces), 2):
            pages.append((int(pieces[i]), pieces[i + 1]))
    for page, body in pages:
        body = re.sub(r"[ \t]+", " ", body).strip()
        start = 0
        while start < len(body):
            end = min(len(body), start + max_chars)
            if end < len(body):                       # break on a sentence/line end if possible
                cut = max(body.rfind("\n", start, end), body.rfind(". ", start, end))
                if cut > start + max_chars // 2:
                    end = cut + 1
            piece = body[start:end].strip()
            if len(piece) > 40:
                yield page, piece
            if end >= len(body):
                break
            start = max(start + 1, end - overlap)


def build_index(text_dir, meta_by_source=None):
    docs, postings, doc_len = [], defaultdict(list), []
    for path in sorted(Path(text_dir).glob("*.txt")):
        source_id = path.stem
        if source_id.startswith("_"):
            continue
        info = (meta_by_source or {}).get(source_id, {})
        for page, piece in chunk_pages(path.read_text(encoding="utf-8", errors="ignore")):
            toks = tokenize(piece)
            if not toks:
                continue
            idx = len(docs)
            docs.append({"s": source_id, "p": page, "t": piece, "subject": info.get("subject", ""),
                         "grade": info.get("grade", ""), "language": info.get("language", "")})
            doc_len.append(len(toks))
            for term, tf in Counter(toks).items():
                postings[term].append([idx, tf])
    n = len(docs)
    return {"N": n, "avgdl": (sum(doc_len) / n) if n else 0, "doc_len": doc_len, "docs": docs, "postings": postings}


def search(index, query, k=3, subject=None, grade=None, language=None):
    """Return the top-k chunks: [{'source_id','page','score','text'}]."""
    scores = defaultdict(float)
    N, avgdl = index["N"], index["avgdl"] or 1
    for term in set(tokenize(query)):
        plist = index["postings"].get(term)
        if not plist:
            continue
        idf = math.log(1 + (N - len(plist) + 0.5) / (len(plist) + 0.5))
        for doc_idx, tf in plist:
            dl = index["doc_len"][doc_idx]
            scores[doc_idx] += idf * tf * (K1 + 1) / (tf + K1 * (1 - B + B * dl / avgdl))
    out = []
    for doc_idx, sc in sorted(scores.items(), key=lambda kv: -kv[1]):
        d = index["docs"][doc_idx]
        if subject and subject.lower() not in str(d["subject"]).lower():
            continue
        if grade and str(grade) != str(d["grade"]):
            continue
        if language and language != d["language"]:
            continue
        out.append({"source_id": d["s"], "page": d["p"], "score": round(sc, 3), "text": d["t"]})
        if len(out) >= k:
            break
    return out


def format_results(results, max_chars=350):
    """The exact text a `search_curriculum` tool call returns to the model (your app must match this)."""
    if not results:
        return "No results."
    lines = []
    for i, r in enumerate(results, 1):
        where = f"{r['source_id']}" + (f" p.{r['page']}" if r["page"] else "")
        text = re.sub(r"\s+", " ", r["text"]).strip()
        text = text[:max_chars] + ("..." if len(text) > max_chars else "")
        lines.append(f"[{i}] {where}: {text}")
    return "\n".join(lines)


def save_index(index, path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(index, ensure_ascii=False), encoding="utf-8")


def load_index(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _sources_meta(csv_path):
    import csv
    meta = {}
    if csv_path and Path(csv_path).exists():
        with open(csv_path, encoding="utf-8-sig", newline="") as f:
            for row in csv.DictReader(f):
                meta[row.get("source_id", "")] = row
    return meta


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("build")
    b.add_argument("--text", default="workspace/text")
    b.add_argument("--out", default="workspace/index/bm25.json")
    b.add_argument("--sources", default="workspace/sources/sources.csv", help="optional, adds subject/grade/language")
    s = sub.add_parser("search")
    s.add_argument("query")
    s.add_argument("--index", default="workspace/index/bm25.json")
    s.add_argument("-k", type=int, default=3)
    s.add_argument("--subject")
    s.add_argument("--grade")
    s.add_argument("--language")
    a = ap.parse_args(argv)
    if a.cmd == "build":
        idx = build_index(a.text, _sources_meta(a.sources))
        save_index(idx, a.out)
        print(f"indexed {idx['N']} chunks from {a.text} -> {a.out}")
        return 0
    idx = load_index(a.index)
    print(format_results(search(idx, a.query, a.k, a.subject, a.grade, a.language)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
