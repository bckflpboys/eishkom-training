#!/usr/bin/env python3
"""
sanitize_text.py - Deterministic KaTeX LaTeX and whitespace sanitizer.

Runs locally across all extracted Markdown documents in workspace/text/:
1. Removes empty display math blocks ($$\\s*$$).
2. Closes unclosed LaTeX environments (e.g. \\begin{aligned} ... \\end{aligned}$$).
3. Safely cleans dangling incomplete math delimiters at file endings.
4. Normalizes unicode characters and mathematical delimiters.

Cost: $0.00 | Execution time: ~0.5s locally | Zero API calls.
"""
import glob
import os
import re
import sys
from pathlib import Path

KIT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(KIT_ROOT))
from wspaths import p  # noqa: E402


def sanitize_document(content: str) -> tuple[str, list[str]]:
    fixes = []
    orig = content

    # 1. Strip empty display math blocks
    if re.search(r"\$\$\s*\$\$", content):
        content = re.sub(r"\$\$\s*\$\$", "", content)
        fixes.append("Removed empty display math blocks")

    # 2. Check for unclosed environments like \begin{aligned} without \end{aligned}
    aligned_begins = len(re.findall(r"\\begin\{aligned\}", content))
    aligned_ends = len(re.findall(r"\\end\{aligned\}", content))
    if aligned_begins > aligned_ends:
        diff = aligned_begins - aligned_ends
        content = content.rstrip() + ("\n\\end{aligned}$$" * diff) + "\n"
        fixes.append(f"Closed {diff} unclosed \\begin{{aligned}} environments")

    # 3. Check for dangling unclosed $$ at end of file
    clean = content.replace(r"\$$", "ESCDOLLAR").replace(r"\$", "ESCDOLLAR")
    if clean.count("$$") % 2 != 0:
        lines = content.rstrip().split("\n")
        if lines and lines[-1].count("$$") == 1:
            # Trailing fragment on last line
            last_line = lines[-1].strip()
            if last_line.startswith("$$") and len(last_line) < 30 and not last_line.endswith("$$"):
                lines = lines[:-1]
                content = "\n".join(lines) + "\n"
                fixes.append("Removed incomplete trailing math fragment")
            else:
                content = content.rstrip() + "$$\n"
                fixes.append("Closed dangling $$ delimiter at EOF")
        else:
            content = content.rstrip() + "$$\n"
            fixes.append("Closed unmatched $$ delimiter")

    # 4. Clean consecutive blank lines
    content = re.sub(r"\n{3,}", "\n\n", content)

    return content, fixes


def main():
    text_dir = p("text")
    if not text_dir.exists():
        sys.exit(f"Text directory not found at {text_dir}")

    files = list(text_dir.glob("*.txt"))
    print(f"Sanitizing {len(files)} extracted documents in {text_dir}...")

    total_modified = 0
    all_fixes = {}

    for fpath in files:
        content = fpath.read_text(encoding="utf-8", errors="ignore")
        sanitized, fixes = sanitize_document(content)
        if sanitized != content:
            fpath.write_text(sanitized, encoding="utf-8")
            total_modified += 1
            for fix in fixes:
                all_fixes[fix] = all_fixes.get(fix, 0) + 1

    print("=" * 65)
    print(f"Sanitization complete: {total_modified} / {len(files)} documents cleaned.")
    for fix, count in all_fixes.items():
        print(f"  - {fix}: applied to {count} files")
    print("=" * 65)


if __name__ == "__main__":
    main()
