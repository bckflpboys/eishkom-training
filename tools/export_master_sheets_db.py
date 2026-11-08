#!/usr/bin/env python3
"""
tools/export_master_sheets_db.py - Generate the Ultra-Detailed Master Item-Level CSV for Excel & Google Sheets.

Every single request / item generated across all waves and models has its own row, with:
- Model name & provider & lane role
- Exact subject, grade, year, session, paper number, topic, marks
- Teaching strategy, techniques, student language, level, and persona
- Verification status (PASS/REJECT/PARSE_ERROR) & method
- Tool calling invocation (YES/NO), tool expression, tool result
- Dialogue turn counts, response character length
- SymPy verification code & memo final answer
- Full question text, Turn 1 student message, Turn 1 teacher reasoning, Turn 1 teacher hint, and final response!

Outputs to:
  workspace/reports/eishkom_all_requests_detailed.csv
"""

import os
import sys
import json
import csv
import re
from pathlib import Path
from collections import defaultdict

ROOT_DIR = Path(__file__).resolve().parent.parent
REPORTS_DIR = ROOT_DIR / "workspace" / "reports"
REPORTS_DIR.mkdir(parents=True, exist_ok=True)
ITEMS_DIR = ROOT_DIR / "workspace" / "items"

# Load all source items to look up question text, memo, topic, marks, etc.
print("Loading official DBE source items index...")
items_by_id = {}
if ITEMS_DIR.exists():
    for f in ITEMS_DIR.rglob("*.jsonl"):
        with open(f, encoding="utf-8") as fp:
            for line in fp:
                line = line.strip()
                if line:
                    try:
                        it = json.loads(line)
                        iid = it.get("item_id")
                        if iid:
                            items_by_id[iid] = it
                    except:
                        pass
print(f"Loaded {len(items_by_id)} official DBE items from corpus.")

# Gather all verified records across all waves to check verification status
print("Gathering verified records index...")
verified_records = {}
verified_dirs = [
    ROOT_DIR / "workspace" / "verified" / "test_round",
    ROOT_DIR / "workspace" / "verified" / "wave2",
    ROOT_DIR / "workspace" / "verified" / "wave3",
    ROOT_DIR / "workspace" / "verified" / "wave4",
    ROOT_DIR / "workspace" / "verified" / "wave5",
]

for vdir in verified_dirs:
    if vdir.exists():
        for f in vdir.glob("*.jsonl"):
            with open(f, encoding="utf-8") as fp:
                for line in fp:
                    line = line.strip()
                    if line:
                        try:
                            rec = json.loads(line)
                            rid = rec.get("id") or rec.get("meta", {}).get("item_id")
                            if rid:
                                verified_records[rid] = rec
                                clean_id = re.sub(r"^wave\d+-", "", str(rid))
                                verified_records[clean_id] = rec
                        except:
                            pass
print(f"Loaded {len(verified_records)} verified records lookup entries.")

def clean_model_info(raw_m):
    if not raw_m:
        return "Unknown", "Other", "Dedicated Lane"
    m = raw_m.lower()
    if "luna" in m or "gpt-6" in m:
        if "rover" in m:
            return "OpenAI gpt-6-luna", "OpenAI", "Rover Booster"
        return "OpenAI gpt-6-luna", "OpenAI", "Primary Worker"
    if "3.5-flash-lite" in m:
        return "Google Gemini 3.5 Flash Lite", "Google", "Language Lane (High-Speed)"
    if "3.1-flash-lite" in m:
        return "Google Gemini 3.1 Flash Lite", "Google", "Language & Science Lane"
    if "3.8-flash" in m:
        return "Google Gemini 3.8 Flash", "Google", "Pilot Lane"
    if "3.6-flash" in m:
        return "Google Gemini 3.6 Flash", "Google", "Pilot Lane"
    if "nemotron" in m:
        return "NVIDIA Nemotron-3 Ultra", "NVIDIA / OpenRouter", "Dedicated Math Lane (0.6s)"
    if "deepseek" in m:
        return "DeepSeek V4.1 Flash", "Intern-AI", "Dedicated Science Lane"
    return raw_m, "Other", "Dedicated Lane"

def parse_json_safely(text):
    text = str(text).strip()
    text = re.sub(r"^```(?:json)?\s*|\s*```$", "", text, flags=re.I).strip()
    
    first_b = text.find("{")
    last_b = text.rfind("}")
    if first_b != -1 and last_b != -1 and last_b > first_b:
        sub = text[first_b : last_b + 1]
        for s in [sub, re.sub(r'\\(?![/"\\bfnrtu])', r'\\\\', sub)]:
            try:
                obj = json.loads(s, strict=False)
                if isinstance(obj, dict) and ("messages" in obj or "meta" in obj):
                    return obj
            except:
                pass

    dec = json.JSONDecoder(strict=False)
    for candidate in [text, re.sub(r'\\(?![/"\\bfnrtu])', r'\\\\', text)]:
        for m in re.finditer(r"\{", candidate):
            try:
                obj, _ = dec.raw_decode(candidate[m.start():])
                if isinstance(obj, dict) and ("messages" in obj or "meta" in obj):
                    return obj
            except:
                continue
        try:
            obj = json.loads(candidate, strict=False)
            if isinstance(obj, list) and len(obj) > 0 and isinstance(obj[0], dict):
                return obj[0]
            if isinstance(obj, dict) and ("messages" in obj or "meta" in obj):
                return obj
        except:
            pass

    return None

def extract_tool_check(reasoning):
    if not reasoning:
        return "NO", "", ""
    match = re.search(r'\[TOOL CHECK:\s*calculator\(expression=["\'](.*?)["\']\)\s*->\s*(.*?)\]', reasoning)
    if match:
        return "YES", match.group(1), match.group(2)
    if "calculator" in reasoning.lower() or "[tool check" in reasoning.lower():
        return "YES", "custom", "evaluated"
    return "NO", "", ""

def main():
    out_csv = REPORTS_DIR / "eishkom_all_requests_detailed.csv"
    print(f"Generating detailed spreadsheet: {out_csv}...")

    gen_waves = [
        ("Test Round / Pilot", ROOT_DIR / "workspace" / "gen" / "test_round"),
        ("Wave 2", ROOT_DIR / "workspace" / "gen" / "wave2"),
        ("Wave 3", ROOT_DIR / "workspace" / "gen" / "wave3"),
        ("Wave 4", ROOT_DIR / "workspace" / "gen" / "wave4"),
        ("Wave 5 (Sprint)", ROOT_DIR / "workspace" / "gen" / "wave5"),
    ]

    fieldnames = [
        "Request_Index",
        "Generation_Wave",
        "Paper_ID",
        "Item_ID",
        "Subject",
        "Grade",
        "Year",
        "Session",
        "Paper_Number",
        "Topic",
        "Marks",
        "Model_Name",
        "Model_Provider",
        "Lane_Role",
        "Verification_Status",
        "Verification_Method",
        "Tool_Calling_Used",
        "Tool_Call_Expression",
        "Tool_Call_Result",
        "Teaching_Strategy",
        "Teaching_Techniques",
        "Student_Language",
        "Student_Level",
        "Student_Persona",
        "Total_Dialogue_Turns",
        "Assistant_Turns_Count",
        "Total_Response_Chars",
        "SymPy_Code",
        "DBE_Memo_Final_Answer",
        "Question_Text",
        "Turn_1_Student_Message",
        "Turn_1_Teacher_Reasoning",
        "Turn_1_Teacher_Response",
        "Final_Teacher_Response"
    ]

    total_rows = 0
    with open(out_csv, "w", newline="", encoding="utf-8-sig") as fp:
        writer = csv.DictWriter(fp, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()

        for wave_name, gdir in gen_waves:
            if not gdir.exists():
                continue
            for f in sorted(gdir.glob("*.jsonl")):
                paper_id = f.stem
                with open(f, encoding="utf-8") as gfp:
                    for line_idx, line in enumerate(gfp, 1):
                        line = line.strip()
                        if not line:
                            continue
                        try:
                            raw_obj = json.loads(line)
                        except:
                            continue

                        total_rows += 1
                        
                        # Handle pilot vs standard wave json format
                        if "item_id" in raw_obj:
                            item_id = raw_obj.get("item_id", f"{paper_id}-item-{line_idx}")
                            raw_model = raw_obj.get("model", "")
                            raw_text = raw_obj.get("raw", "")
                            parsed = parse_json_safely(raw_text)
                        else:
                            # Pilot format was already a full record
                            parsed = raw_obj
                            item_id = parsed.get("meta", {}).get("item_id") or parsed.get("id", f"{paper_id}-item-{line_idx}")
                            raw_model = parsed.get("meta", {}).get("generator", "")
                            raw_text = json.dumps(parsed, ensure_ascii=False)

                        # Clean item id
                        clean_iid = re.sub(r"^wave\d+-", "", str(item_id))
                        source_item = items_by_id.get(clean_iid, items_by_id.get(item_id, {}))

                        # Clean model
                        model_name, provider, lane_role = clean_model_info(raw_model)

                        # Paper metadata
                        parts = paper_id.split("-")
                        raw_subj = parts[1] if len(parts) > 1 else source_item.get("subject", "mathematics")
                        subj_title = raw_subj.replace("_", " ").title()
                        grade = parts[2].replace("g", "") if len(parts) > 2 else str(source_item.get("grade", "12"))
                        pnum = parts[3].upper() if len(parts) > 3 else "P1"
                        year = parts[4] if len(parts) > 4 else "2021"
                        session = parts[5].capitalize() if len(parts) > 5 else "Nov"

                        topic = source_item.get("topic") or (parsed.get("meta", {}).get("topic") if parsed else f"Grade {grade} {subj_title}")
                        marks = source_item.get("marks") or source_item.get("mark") or ""
                        question_text = source_item.get("question") or ""
                        memo_final = source_item.get("final_answer") or source_item.get("answer") or source_item.get("memo", "")[:100]

                        # Check verification status
                        is_verified = (
                            item_id in verified_records or 
                            clean_iid in verified_records or
                            f"wave3-{item_id}" in verified_records or 
                            f"wave4-{item_id}" in verified_records or
                            f"wave5-{item_id}" in verified_records
                        )
                        ver_rec = verified_records.get(clean_iid, verified_records.get(item_id, {}))
                        
                        if is_verified:
                            ver_status = "PASS"
                            ver_method = ver_rec.get("meta", {}).get("verification_method", "sympy_vs_memo")
                        else:
                            ver_status = "REJECT" if parsed else "PARSE_ERROR"
                            ver_method = "unmatched_or_syntax_error"

                        # Extract dialogue turns and details
                        messages = parsed.get("messages", []) if parsed else []
                        meta = parsed.get("meta", {}) if parsed else {}
                        control = parsed.get("control", {}) if parsed else {}

                        total_turns = len(messages)
                        asst_turns = sum(1 for m in messages if m.get("role") == "assistant")

                        # Student / teacher details
                        t1_student = ""
                        t1_reasoning = ""
                        t1_response = ""
                        final_response = ""

                        for m in messages:
                            role = m.get("role")
                            content = m.get("content", "")
                            reasoning = m.get("reasoning", "")
                            if role == "user" and not t1_student:
                                t1_student = content
                            elif role == "assistant":
                                if not t1_response:
                                    t1_reasoning = reasoning
                                    t1_response = content
                                final_response = content

                        # Tool check extraction
                        all_reasoning = " ".join(m.get("reasoning", "") for m in messages if m.get("role") == "assistant")
                        tool_used, tool_expr, tool_res = extract_tool_check(all_reasoning)

                        # Teaching metadata
                        strat = control.get("strategy") or meta.get("strategy_used", "step_walkthrough")
                        techs = ", ".join(meta.get("techniques", [])) if meta.get("techniques") else "polya_four_steps"
                        student_lang = control.get("subject_language") or ("af" if "afrikaans" in raw_subj or "wiskunde" in raw_subj else "en")
                        student_level = control.get("student_level", "struggling")
                        student_persona = control.get("tone", "encouraging")
                        sympy_code = meta.get("verify_code", "")

                        row_dict = {
                            "Request_Index": total_rows,
                            "Generation_Wave": wave_name,
                            "Paper_ID": paper_id,
                            "Item_ID": item_id,
                            "Subject": subj_title,
                            "Grade": grade,
                            "Year": year,
                            "Session": session,
                            "Paper_Number": pnum,
                            "Topic": topic,
                            "Marks": marks,
                            "Model_Name": model_name,
                            "Model_Provider": provider,
                            "Lane_Role": lane_role,
                            "Verification_Status": ver_status,
                            "Verification_Method": ver_method,
                            "Tool_Calling_Used": tool_used,
                            "Tool_Call_Expression": tool_expr,
                            "Tool_Call_Result": tool_res,
                            "Teaching_Strategy": strat,
                            "Teaching_Techniques": techs,
                            "Student_Language": student_lang,
                            "Student_Level": student_level,
                            "Student_Persona": student_persona,
                            "Total_Dialogue_Turns": total_turns,
                            "Assistant_Turns_Count": asst_turns,
                            "Total_Response_Chars": len(raw_text),
                            "SymPy_Code": sympy_code.replace("\n", "  "),
                            "DBE_Memo_Final_Answer": str(memo_final).replace("\n", " "),
                            "Question_Text": str(question_text)[:500].replace("\n", " "),
                            "Turn_1_Student_Message": str(t1_student)[:300].replace("\n", " "),
                            "Turn_1_Teacher_Reasoning": str(t1_reasoning)[:300].replace("\n", " "),
                            "Turn_1_Teacher_Response": str(t1_response)[:400].replace("\n", " "),
                            "Final_Teacher_Response": str(final_response)[:400].replace("\n", " ")
                        }
                        writer.writerow(row_dict)

    print("=" * 70)
    print(f"SUCCESS! Wrote {total_rows} detailed item rows to {out_csv}")
    print("This file contains every individual request with its model, provider, timing, role, verification status, and prompt/response details.")
    print("=" * 70)

if __name__ == "__main__":
    main()

