"""wspaths.py - where things live. Every script uses p("some", "folder") instead of hard-coded paths.

The workspace folder defaults to ./workspace (next to where you run the script). To put it somewhere
else (for example on Google Drive in Colab), set the environment variable SA_WORKSPACE.
"""
import os
from pathlib import Path

KIT_ROOT = Path(__file__).resolve().parent


def root():
    return Path(os.environ.get("SA_WORKSPACE", "workspace"))


def p(*parts):
    return root().joinpath(*parts)


def ensure_parent(path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    return Path(path)


def read_jsonl(path):
    import json
    with open(path, encoding="utf-8") as f:
        content = f.read()
    lines = [l.strip() for l in content.splitlines() if l.strip()]
    if lines:
        try:
            return [json.loads(l) for l in lines]
        except json.JSONDecodeError:
            pass
    stripped = content.strip()
    if stripped.startswith("[") and stripped.endswith("]"):
        try:
            return json.loads(stripped)
        except json.JSONDecodeError:
            pass
    dec = json.JSONDecoder()
    idx = 0
    out = []
    length = len(content)
    while idx < length:
        while idx < length and content[idx].isspace():
            idx += 1
        if idx >= length:
            break
        if content[idx] == ",":
            idx += 1
            continue
        try:
            obj, end = dec.raw_decode(content[idx:])
            out.append(obj)
            idx += end
        except json.JSONDecodeError:
            break
    return out


def write_jsonl(path, rows):
    import json
    ensure_parent(path)
    with open(path, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    return len(rows)


def append_jsonl(path, row):
    import json
    ensure_parent(path)
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
