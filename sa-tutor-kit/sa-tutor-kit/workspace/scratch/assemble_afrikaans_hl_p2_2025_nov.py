# -*- coding: utf-8 -*-
"""
assemble_afrikaans_hl_p2_2025_nov.py - Assembles, validates, and writes
all 104 atomic items for DBE Afrikaans Huistaal Graad 12 Vraestel 2 November 2025.
"""

import json
import os
import re
import sys
from pathlib import Path

# Add scratch to path to import builders
SCRATCH_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRATCH_DIR))

from build_poetry import get_poetry_items
from build_novels import get_novel_items
from build_dramas import get_drama_items


def check_latex_syntax(text):
    """Accurately check for broken LaTeX math blocks and syntax."""
    errors = []
    
    # Check for empty display math blocks ($$$$ or $$  $$ on same line)
    if re.search(r"\$\$[ \t]*\$\$", text):
        errors.append("Empty display math block")

    # Match all standard display math blocks ($$...$$)
    display_blocks = re.findall(r"\$\$.*?\$\$", text, flags=re.DOTALL)
    
    # Remove valid display math blocks
    no_display = re.sub(r"\$\$.*?\$\$", " DISPLAYMATH ", text, flags=re.DOTALL)
    
    # Check if there is a leftover unclosed $$
    clean_no_display = no_display.replace(r"\$$", "ESCDOLLAR").replace(r"\$", "ESCDOLLAR")
    if clean_no_display.count("$$") % 2 != 0:
        errors.append("Unclosed display math block ($$)")

    # Match inline math ($...$)
    # Check for unclosed single dollar signs
    # Replace escaped dollars
    single_clean = no_display.replace(r"\$", "ESCDOLLAR")
    if single_clean.count("$") % 2 != 0:
        errors.append(f"Unclosed inline math delimiter ($): count={single_clean.count('$')}")
        
    # Check for unescaped broken fraction commands
    broken_fracs = len(re.findall(r"\\frac(?![{\s\d])", text))
    if broken_fracs > 0:
        errors.append(f"Broken fraction commands: {broken_fracs}")

    return errors


def main():
    poetry_items = get_poetry_items()
    novel_items = get_novel_items()
    drama_items = get_drama_items()

    all_items = poetry_items + novel_items + drama_items
    print(f"Total items assembled: {len(all_items)}")
    total_marks = sum(item["marks"] for item in all_items)
    print(f"Total marks across all literature options: {total_marks}")

    # Validation Checks
    expected_keys = {
        "item_id", "source_id", "pair_source_id", "subject", "grade",
        "language", "track", "kind", "question_ref", "marks", "topic",
        "passage", "question", "memo", "final_answer", "needs_review",
        "licence", "attribution"
    }

    item_ids = set()
    latex_errors_total = 0

    for idx, item in enumerate(all_items, 1):
        # Key check
        missing_keys = expected_keys - set(item.keys())
        if missing_keys:
            raise ValueError(f"Item {idx} missing keys: {missing_keys}")
        
        # ID check
        if item["item_id"] in item_ids:
            raise ValueError(f"Duplicate item_id: {item['item_id']}")
        item_ids.add(item["item_id"])

        # Value types
        assert isinstance(item["marks"], int) and item["marks"] > 0, f"Invalid marks: {item['marks']}"
        assert item["grade"] == 12, f"Invalid grade: {item['grade']}"
        assert item["language"] == "af", f"Invalid language: {item['language']}"
        assert item["track"] == "languages_hl", f"Invalid track: {item['track']}"
        assert item["kind"] == "passage_questions", f"Invalid kind: {item['kind']}"
        assert isinstance(item["needs_review"], bool), f"Invalid needs_review: {item['needs_review']}"
        assert len(item["passage"]) > 0, f"Empty passage in item {item['item_id']}"
        assert len(item["question"]) > 0, f"Empty question in item {item['item_id']}"
        assert len(item["memo"]) > 0, f"Empty memo in item {item['item_id']}"
        assert len(item["final_answer"]) > 0, f"Empty final_answer in item {item['item_id']}"

        # LaTeX syntax checks
        for field in ["passage", "question", "memo", "final_answer"]:
            errs = check_latex_syntax(item[field])
            if errs:
                print(f"LaTeX error in {item['item_id']} field '{field}': {errs}")
                latex_errors_total += len(errs)

    if latex_errors_total > 0:
        raise ValueError(f"LaTeX validation failed with {latex_errors_total} errors!")
    else:
        print("LaTeX syntax validation: PASS (0 errors)")

    # Output paths
    dest1 = Path("sa-tutor-kit/sa-tutor-kit/workspace/items/afrikaans_hl/dbe-afrikaans_hl-g12-p2-2025-nov.jsonl")
    dest2 = Path("sa-tutor-kit/sa-tutor-kit/workspace/items/dbe-afrikaans_hl-g12-p2-2025-nov.jsonl")

    dest1.parent.mkdir(parents=True, exist_ok=True)
    dest2.parent.mkdir(parents=True, exist_ok=True)

    with open(dest1, "w", encoding="utf-8") as f1, open(dest2, "w", encoding="utf-8") as f2:
        for item in all_items:
            line = json.dumps(item, ensure_ascii=False) + "\n"
            f1.write(line)
            f2.write(line)

    print(f"Successfully wrote {len(all_items)} items to:")
    print(f"  1. {dest1} ({dest1.stat().st_size} bytes)")
    print(f"  2. {dest2} ({dest2.stat().st_size} bytes)")

    # Verify written files
    for path in [dest1, dest2]:
        with open(path, "r", encoding="utf-8") as f:
            lines = [json.loads(l) for l in f if l.strip()]
        assert len(lines) == 104, f"File {path} has {len(lines)} lines instead of 104"
        assert sum(x["marks"] for x in lines) == 350, f"File {path} has incorrect total marks"

    print("Post-write verification passed: Both output files exist and match exactly.")


if __name__ == "__main__":
    main()
