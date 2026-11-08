# -*- coding: utf-8 -*-
import json
import os
import re

def check_file(path):
    print("Checking:", path)
    assert os.path.exists(path), f"File does not exist: {path}"
    with open(path, "r", encoding="utf-8") as f:
        lines = [json.loads(line) for line in f]
    
    print(f"  Line count: {len(lines)}")
    marks = sum(x["marks"] for x in lines)
    print(f"  Total marks: {marks}")
    assert marks == 150, f"Marks mismatch: {marks}"
    
    needs_review_count = sum(1 for x in lines if x["needs_review"])
    print(f"  needs_review count: {needs_review_count}")
    
    req_fields = [
        "item_id", "source_id", "pair_source_id", "subject", "grade",
        "language", "track", "kind", "question_ref", "marks", "topic",
        "passage", "question", "memo", "final_answer", "needs_review",
        "licence", "attribution"
    ]
    
    errors = []
    warnings = []
    
    for idx, item in enumerate(lines):
        item_id = item.get("item_id", f"index-{idx}")
        for rf in req_fields:
            if rf not in item:
                errors.append(f"Missing field {rf} in {item_id}")
        if item.get("subject") != "mathematics":
            errors.append(f"Invalid subject in {item_id}: {item.get('subject')}")
        if item.get("grade") != 12:
            errors.append(f"Invalid grade in {item_id}: {item.get('grade')}")
        if item.get("language") != "en":
            errors.append(f"Invalid language in {item_id}: {item.get('language')}")
        if item.get("track") != "core_maths":
            errors.append(f"Invalid track in {item_id}: {item.get('track')}")
        if item.get("source_id") != "dbe-mathematics-g12-p1-2023-may":
            errors.append(f"Invalid source_id in {item_id}")
        if item.get("pair_source_id") != "dbe-mathematics-g12-p1-2023-may-memo":
            errors.append(f"Invalid pair_source_id in {item_id}")
            
        # Check KaTeX balance in question, memo, passage
        for field in ["question", "memo", "passage"]:
            val = item.get(field, "")
            parts = val.split("$$")
            if len(parts) % 2 == 0:
                errors.append(f"Unbalanced $$ in {item_id} field {field}")
            # check single dollars
            outside_display = "".join(parts[::2])
            single_count = outside_display.count("$")
            if single_count % 2 != 0:
                errors.append(f"Unbalanced $ in {item_id} field {field}")
                
            # check bare decimal commas in math mode
            # Find math spans: $...$ or $$...$$
            all_math_spans = re.findall(r"\$\$[\s\S]*?\$\$|\$[^$\n]+\$", val)
            for span in all_math_spans:
                # search for bare digit,digit
                bare = re.findall(r"\d+,\d+", span)
                if bare:
                    warnings.append(f"Bare comma in math span in {item_id} ({field}): {bare} in '{span[:40]}'")
                    
    if errors:
        print(f"  ERRORS FOUND ({len(errors)}):")
        for e in errors:
            print("    ", e)
    else:
        print("  0 Errors found!")
        
    if warnings:
        print(f"  WARNINGS FOUND ({len(warnings)}):")
        for w in warnings:
            print("    ", w)
    else:
        print("  0 Warnings found!")
        
    print("  File validation finished.\n")
    return len(errors) == 0

res1 = check_file("sa-tutor-kit/sa-tutor-kit/workspace/items/mathematics/dbe-mathematics-g12-p1-2023-may.jsonl")
res2 = check_file("sa-tutor-kit/sa-tutor-kit/workspace/items/dbe-mathematics-g12-p1-2023-may.jsonl")

if res1 and res2:
    print("ALL VALIDATION CHECKS PASSED PERFECTLY!")
else:
    print("VALIDATION FAILED!")
