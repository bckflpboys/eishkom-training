#!/usr/bin/env python3
"""
evaluate.py - one command that does a whole evaluation: answer, mark, compare, analyse.

    python eval/evaluate.py --name r2 --backend hf --model unsloth/Qwen3.5-4B --adapter workspace/runs/r2/adapter \
           --compare base r1 --ceiling teacher --n 1 --analyze
    python eval/evaluate.py --name r2-q6 --backend openai --base-url http://localhost:8080/v1 --model local --compare r2

It just runs, in order: run_eval.py -> score_eval.py -> report_eval.py -> (analyze_failures.py). Anything it does not
know is passed on to run_eval.py (for example --tags core, --temperature 0.7, --thinking off).
READ the decision.md it prints at the end, then failures.md.
"""
import argparse
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def run(script, *args):
    cmd = [sys.executable, str(HERE / script), *map(str, args)]
    print("\n$", " ".join(cmd))
    r = subprocess.run(cmd)
    if r.returncode:
        sys.exit(f"{script} failed (exit {r.returncode})")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--name", required=True)
    ap.add_argument("--compare", nargs="*", default=[], help="earlier run names, oldest first")
    ap.add_argument("--ceiling", help="run name of the teacher on the same exam")
    ap.add_argument("--judge", action="store_true", help="also mark rubric checks with the judge model")
    ap.add_argument("--analyze", action="store_true", help="also ask the teacher to analyse the failures")
    a, rest = ap.parse_known_args()
    run("run_eval.py", "--name", a.name, *rest)
    run("score_eval.py", "--name", a.name, *(["--judge"] if a.judge else []))
    run("report_eval.py", "--runs", *a.compare, a.name, "--out", a.name, *(["--ceiling", a.ceiling] if a.ceiling else []))
    if a.analyze:
        run("analyze_failures.py", "--name", a.name)


if __name__ == "__main__":
    main()
