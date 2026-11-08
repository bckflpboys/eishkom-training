import os
from pathlib import Path

vdir = Path("workspace/verified/wave2")
gdir = Path("workspace/gen/wave2")
items_dir = Path("workspace/items")

papers = [
    ("LANE-1", "Afrikaans FAL (gemini-3.1-flash-lite)", "dbe-afrikaans_fal-g12-p1-2023-nov"),
    ("LANE-2", "Afrikaans HL (gemini-3.1-flash-lite)", "dbe-afrikaans_hl-g12-p1-2022-nov"),
    ("LANE-3", "English HL (gemini-3.5-flash-lite)", "dbe-english_hl-g12-p1-2022-nov"),
    ("LANE-4", "English FAL (gemini-3.5-flash-lite)", "dbe-english_fal-g12-p1-2023-nov"),
    ("LANE-5", "Maths EN (nemotron-3-ultra-550b)", "dbe-mathematics-g12-p1-2022-nov"),
    ("LANE-6", "Wiskunde AF (gpt-6-luna)", "dbe-wiskunde-g12-v1-2023-nov"),
    ("LANE-7", "Physics EN (gemini-3.8->3.6)", "dbe-physical_sciences-g12-p1-2022-nov"),
    ("LANE-8", "Physics AF (gemini-3.8->3.6)", "dbe-fisiese_wetenskappe-g12-v1-2023-nov")
]

print(f"{'LANE':<8} | {'DESCRIPTION':<38} | {'TOTAL':<5} | {'GEN':<5} | {'VERIFIED':<8} | {'PASS RATE':<9} | {'STATUS'}")
print("-" * 105)

total_items = 0
total_gen = 0
total_ver = 0

for lid, desc, p in papers:
    item_file = items_dir / f"{p}.jsonl"
    item_cnt = sum(1 for _ in open(item_file, encoding="utf-8")) if item_file.exists() else 0
    gen_file = gdir / f"{p}.jsonl"
    gen_cnt = sum(1 for _ in open(gen_file, encoding="utf-8")) if gen_file.exists() else 0
    ver_file = vdir / f"{p}.jsonl"
    ver_cnt = sum(1 for _ in open(ver_file, encoding="utf-8")) if ver_file.exists() else 0
    
    total_items += item_cnt
    total_gen += gen_cnt
    total_ver += ver_cnt
    
    rate = f"{(ver_cnt / gen_cnt * 100):.1f}%" if gen_cnt > 0 else "0.0%"
    status = "COMPLETE" if gen_cnt >= item_cnt else f"RUNNING ({gen_cnt}/{item_cnt})"
    print(f"{lid:<8} | {desc:<38} | {item_cnt:<5} | {gen_cnt:<5} | {ver_cnt:<8} | {rate:<9} | {status}")

print("-" * 105)
cum_rate = f"{(total_ver / total_gen * 100):.1f}%" if total_gen > 0 else "0.0%"
print(f"{'TOTAL':<8} | {'ALL 8 LANES':<38} | {total_items:<5} | {total_gen:<5} | {total_ver:<8} | {cum_rate:<9} |")

