#!/usr/bin/env python3
"""
init_workspace.py - create the folders and starter files for the project (run this ONCE).

    python pipeline/init_workspace.py

WHY A FIXED FOLDER LAYOUT
  Every later script reads from one folder and writes to the next, so you can see exactly where each
  piece of data came from. If something looks wrong in the training data, you can walk back:
  build/ <- verified/ <- gen/ <- plans/ <- items/ <- text/ <- raw/.  Nothing is ever overwritten silently.
"""
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from wspaths import KIT_ROOT, p, root  # noqa: E402

FOLDERS = {
    "config": "settings you edit: plan_config.json, misconceptions.jsonl",
    "sources": "sources.csv - one row per file you download (licence is mandatory)",
    "raw": "the files exactly as downloaded (PDFs, HTML). Never edit these.",
    "text": "text extracted from raw/ (one .txt per source, with page markers)",
    "items": "questions + memos cut out of the text (one .jsonl per source)",
    "index": "the search index over text/ (used by the search_curriculum tool)",
    "plans": "generation plans: which control settings to write for which item",
    "gen": "teacher output, per round: raw replies, candidate records, failures",
    "verified": "records that passed every check, per round (this is your training data)",
    "review": "samples exported for a human (you / a teacher / an Afrikaans speaker) to read",
    "build": "final train/val/test files, per round",
    "eval": "your exam: eval_items.jsonl (never train on these)",
    "eval_runs": "model answers and scores, one folder per model/run",
    "runs": "training runs: LoRA adapters, logs, run.json (put this on Google Drive in Colab)",
    "reports": "charts and notes",
    "logs": "llm_usage.jsonl (every API call and its cost)",
    "images": "pictures for the vision phase",
}


def main():
    ws = root()
    for name, why in FOLDERS.items():
        (ws / name).mkdir(parents=True, exist_ok=True)
    copies = [
        (KIT_ROOT / "templates" / "sources_template.csv", p("sources", "sources.csv")),
        (KIT_ROOT / "templates" / "plan_config.default.json", p("config", "plan_config.json")),
        (KIT_ROOT / "templates" / "misconceptions.starter.jsonl", p("config", "misconceptions.jsonl")),
        (KIT_ROOT / "eval" / "eval_seed.jsonl", p("eval", "eval_items.jsonl")),
        (KIT_ROOT / ".env.example", KIT_ROOT / ".env"),
    ]
    for src, dst in copies:
        if not src.exists():
            print(f"  (skipped, template missing: {src.name})")
        elif dst.exists():
            print(f"  kept existing {dst}")
        else:
            shutil.copy(src, dst)
            print(f"  created {dst}")
    (ws / "README.txt").write_text(
        "Folders in this workspace (see GUIDE.md):\n\n" + "\n".join(f"  {k:<10} {v}" for k, v in FOLDERS.items()) + "\n",
        encoding="utf-8")
    print(f"\nWorkspace ready at: {ws.resolve()}")
    print("Next:")
    print("  1. open .env in the kit folder and paste your teacher API key")
    print("  2. put downloaded PDFs in workspace/raw/ and list them in workspace/sources/sources.csv")
    print("  3. python pipeline/ingest.py")


if __name__ == "__main__":
    main()
