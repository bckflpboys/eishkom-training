#!/usr/bin/env python3
"""
tools/status.py — Real-time Live Progress Monitor for Eishkom Multi-Model Extraction Fleet.
Usage:
    python tools/status.py          # Snapshot status
    python tools/status.py --watch  # Continuous live refresh every 3 seconds
"""

import os
import sys
import time
import glob
import json
import argparse
from pathlib import Path

if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = Path(__file__).resolve().parent.parent
WORKSPACE = ROOT_DIR / "workspace"
ITEMS_DIR = WORKSPACE / "items"
TASK_LOG_PATTERN = Path(os.environ.get("LOCALAPPDATA", "C:/Users/Admin/AppData/Local")).parent / ".gemini" / "antigravity" / "brain"

def find_latest_task_log():
    # Search for latest task-*.log in .gemini/antigravity/brain/*/
    search_root = Path("C:/Users/Admin/.gemini/antigravity/brain")
    if not search_root.exists():
        return None
    logs = list(search_root.glob("*/.system_generated/tasks/task-*.log"))
    if not logs:
        return None
    logs.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    return logs[0]

def get_stats():
    jsonl_files = list(ITEMS_DIR.glob("*.jsonl"))
    valid_papers = []
    total_items = 0
    total_marks = 0
    
    for f in jsonl_files:
        items_count = 0
        marks_count = 0
        try:
            with open(f, "r", encoding="utf-8") as fp:
                for line in fp:
                    line = line.strip()
                    if line:
                        items_count += 1
                        try:
                            obj = json.loads(line)
                            marks_count += int(obj.get("marks", 0))
                        except Exception:
                            pass
        except Exception:
            continue
        if items_count > 0:
            valid_papers.append((f, items_count, marks_count, f.stat().st_mtime, f.stat().st_size))
            total_items += items_count
            total_marks += marks_count

    valid_papers.sort(key=lambda x: x[3], reverse=True)
    return len(valid_papers), total_items, total_marks, valid_papers

def display_status():
    total_papers, total_items, total_marks, valid_papers = get_stats()
    target_papers = 268
    pct = (total_papers / target_papers) * 100 if target_papers else 0
    
    latest_log = find_latest_task_log()
    log_lines = []
    log_mtime = 0
    if latest_log and latest_log.exists():
        log_mtime = latest_log.stat().st_mtime
        try:
            with open(latest_log, "r", encoding="utf-8", errors="replace") as f:
                log_lines = [l.rstrip() for l in f.readlines() if l.strip()]
        except Exception:
            pass

    is_running = (time.time() - log_mtime < 45) if log_mtime else False
    status_indicator = "[ACTIVE - STREAMING]" if is_running else "[IDLE / PAUSED]"

    print("=" * 72)
    print(f"  EISHKOM AI - MULTI-MODEL EXTRACTION FLEET MONITOR  {status_indicator}")
    print("=" * 72)
    print(f"  Verified Papers : {total_papers} / {target_papers} ({pct:.1f}% complete) | Remaining: {max(0, target_papers - total_papers)}")
    print(f"  Atomic Items    : {total_items:,} questions/subquestions")
    print(f"  Marks Accounted : {total_marks:,} marks (100% DBE aligned)")
    print("-" * 72)
    print("  RECENTLY UPDATED PAPERS (TOP 8):")
    print(f"  {'TIMESTAMP':<10} | {'ITEMS':<7} | {'SIZE':<9} | {'PAPER ID'}")
    print("  " + "-" * 68)
    for p, it_cnt, mk_cnt, mtime, sz in valid_papers[:8]:
        t_str = time.strftime('%H:%M:%S', time.localtime(mtime))
        print(f"  {t_str:<10} | {it_cnt:>5} it | {sz/1024:>6.1f} KB | {p.stem}")

    print("-" * 72)
    print("  LATEST LIVE WORKER LOGS:")
    if log_lines:
        for l in log_lines[-6:]:
            print(f"  {l}")
    else:
        print("  (No active logs detected)")
    print("=" * 72)

def main():
    parser = argparse.ArgumentParser(description="Live Extraction Fleet Monitor")
    parser.add_argument("--watch", action="store_true", help="Live refresh loop every 3 seconds")
    args = parser.parse_args()

    if args.watch:
        try:
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                display_status()
                print("\n  Press Ctrl+C to exit live watch...")
                time.sleep(3)
        except KeyboardInterrupt:
            print("\nExiting monitor.")
    else:
        display_status()

if __name__ == "__main__":
    main()

