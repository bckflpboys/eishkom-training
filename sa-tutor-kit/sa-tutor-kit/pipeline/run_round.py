#!/usr/bin/env python3
"""
run_round.py - run one whole DATA round in order: plan -> generate -> verify -> (merge -> report -> build).

    python pipeline/run_round.py --round r2 --target 800 --judge --merge r1 r2 --name r2

It only calls the scripts you already know, one after another, and STOPS if one fails or the spending cap is reached.
It does not replace reading: it pauses (unless --yes) after the cost estimate and tells you to review a sample before you train.
Then: python pipeline/review_sample.py export --round r2   (read, mark, apply) and train in Colab.
"""
import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from wspaths import p  # noqa: E402


def run(*args, capture=False):
    cmd = [sys.executable, *map(str, args)]
    print("\n$", " ".join(cmd))
    r = subprocess.run(cmd, cwd=ROOT)
    if r.returncode:
        sys.exit(f"step failed: {' '.join(map(str, args))}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--round", required=True)
    ap.add_argument("--target", type=int, help="number of records to plan")
    ap.add_argument("--workers", type=int, default=3)
    ap.add_argument("--judge", action="store_true")
    ap.add_argument("--merge", nargs="*", help="rounds to merge into one file (e.g. r1 r2) and build")
    ap.add_argument("--name", help="name of the build folder under workspace/build (default: the round name)")
    ap.add_argument("--val", type=float, default=0.1)
    ap.add_argument("--yes", action="store_true", help="do not pause after the cost estimate")
    a = ap.parse_args()

    plan = ["pipeline/plan.py", "--round", a.round] + (["--target", a.target] if a.target else [])
    run(*plan)
    run("pipeline/generate.py", "--round", a.round, "--dry-run")
    if not a.yes and input("\nGo ahead and spend that? [y/N] ").strip().lower() != "y":
        sys.exit("stopped before spending anything.")
    run("pipeline/generate.py", "--round", a.round, "--workers", a.workers)
    run("pipeline/verify.py", "--round", a.round, *(["--judge"] if a.judge else []))
    if a.merge:
        name = a.name or a.round
        merged = p("verified", f"train_{name}.jsonl")
        run("pipeline/merge.py", "--rounds", *a.merge, "--out", merged)
        run("tutor_data.py", "report", merged)
        run("tutor_data.py", "build", merged, "--out", p("build", name), "--val", a.val)
    print(f"\nDONE. NEXT: python pipeline/review_sample.py export --round {a.round}   (READ before you train)")


if __name__ == "__main__":
    main()
