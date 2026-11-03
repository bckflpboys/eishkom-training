#!/usr/bin/env python3
"""
report_eval.py - compare runs, draw charts, and answer "is it OK to move on?".

    python eval/report_eval.py --runs base-qwen35-4b r1-sft r2-sft --ceiling teacher-deepseek --out r2

WHAT YOU GET (workspace/reports/<out>/)
  comparison.md   one table: every slice x every run, with the change since the previous run
  overall.png     overall pass rate per run (and the teacher's ceiling if you give one)
  subjects.png    pass rate by subject per run
  heatmap.png     subject x grade for the LAST run (where exactly is it weak?)
  checks.png      pass rate per check type for the LAST run (leaks? language? tools?)
  decision.md     the "move on?" checklist with the numbers

THE MOVE-ON RULES (change them with the flags; the defaults are in GUIDE.md phase 8)
  1. overall pass rate >= --min-overall  OR  >= 85% of the ceiling (the teacher's own score on your exam)
  2. policy tests >= 90%, language checks >= 95%, tool checks >= 90%
  3. no slice dropped by more than --max-drop points since the previous run (that is "forgetting")
  4. (plateau) if the last round improved overall by < 2 points, more of the same data will not help:
     change the DATA (new situations), not the quantity.
"""
import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from wspaths import p, read_jsonl  # noqa: E402


def load_summary(name):
    return json.loads(p("eval_runs", name, "summary.json").read_text(encoding="utf-8"))


def pct(x):
    return "-" if x is None else f"{100 * x:.0f}%"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--runs", nargs="+", required=True, help="run names, oldest first")
    ap.add_argument("--ceiling", help="run name of the teacher model on the same exam")
    ap.add_argument("--out", required=True)
    ap.add_argument("--items", default=str(p("eval", "eval_items.jsonl")))
    ap.add_argument("--min-overall", type=float, default=0.70)
    ap.add_argument("--max-drop", type=float, default=0.03)
    a = ap.parse_args()

    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    out = p("reports", a.out)
    out.mkdir(parents=True, exist_ok=True)
    sums = {r: load_summary(r) for r in a.runs}
    ceiling = load_summary(a.ceiling) if a.ceiling else None
    last, prev = a.runs[-1], (a.runs[-2] if len(a.runs) > 1 else None)

    # ---- comparison table
    lines = ["# Comparison\n", "| slice | " + " | ".join(a.runs) + " |", "|---|" + "---|" * len(a.runs)]
    lines.append("| **overall** | " + " | ".join(pct(sums[r]["overall_sample_pass"]) for r in a.runs) + " |")
    regress, improve = [], []
    for kind in ("subject", "grade", "language", "tag", "task_type"):
        names = sorted({n for r in a.runs for n in sums[r]["slices"].get(kind, {})})
        for n in names:
            cells, prev_v = [], None
            for r in a.runs:
                v = sums[r]["slices"].get(kind, {}).get(n, {}).get("pass")
                delta = ""
                if v is not None and prev_v is not None:
                    d = v - prev_v
                    delta = f" ({'+' if d >= 0 else ''}{100 * d:.0f})"
                    if r == last and d <= -a.max_drop:
                        regress.append((f"{kind}={n}", d))
                    if r == last and d >= 0.05:
                        improve.append((f"{kind}={n}", d))
                cells.append(pct(v) + delta)
                prev_v = v if v is not None else prev_v
            lines.append(f"| {kind}: {n} | " + " | ".join(cells) + " |")
    (out / "comparison.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # ---- charts
    fig, ax = plt.subplots(figsize=(7, 4))
    vals = [sums[r]["overall_sample_pass"] or 0 for r in a.runs]
    bars = ax.bar(a.runs, [100 * v for v in vals], color="#3b82f6")
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, 100 * v + 1, f"{100 * v:.0f}%", ha="center")
    if ceiling:
        ax.axhline(100 * ceiling["overall_sample_pass"], color="#ef4444", ls="--", label=f"ceiling ({a.ceiling})")
        ax.legend()
    ax.set_ylim(0, 105); ax.set_ylabel("answers passing every check (%)"); ax.set_title("Overall pass rate")
    plt.xticks(rotation=20, ha="right"); plt.tight_layout(); plt.savefig(out / "overall.png", dpi=130); plt.close()

    subjects = sorted({n for r in a.runs for n in sums[r]["slices"].get("subject", {})})
    fig, ax = plt.subplots(figsize=(max(7, 1.3 * len(subjects)), 4))
    w = 0.8 / len(a.runs)
    for i, r in enumerate(a.runs):
        ys = [100 * (sums[r]["slices"]["subject"].get(s, {}).get("pass") or 0) for s in subjects]
        ax.bar([x + i * w for x in range(len(subjects))], ys, width=w, label=r)
    ax.set_xticks([x + w * (len(a.runs) - 1) / 2 for x in range(len(subjects))]); ax.set_xticklabels(subjects, rotation=20, ha="right")
    ax.set_ylim(0, 105); ax.set_ylabel("pass (%)"); ax.set_title("By subject"); ax.legend(fontsize=8)
    plt.tight_layout(); plt.savefig(out / "subjects.png", dpi=130); plt.close()

    items = {i["id"]: i for i in read_jsonl(a.items)}
    cell = defaultdict(list)
    for r in read_jsonl(p("eval_runs", last, "scores.jsonl")):
        c = items[r["id"]]["control"]
        cell[(c["subject"], c["grade"])].append(r["passed"])
    subs = sorted({k[0] for k in cell}); grades = sorted({k[1] for k in cell})
    fig, ax = plt.subplots(figsize=(1 + 0.8 * len(grades), 1 + 0.55 * len(subs)))
    grid = [[(100 * sum(cell[(s, g)]) / len(cell[(s, g)])) if cell.get((s, g)) else float("nan") for g in grades] for s in subs]
    im = ax.imshow(grid, vmin=0, vmax=100, cmap="RdYlGn", aspect="auto")
    ax.set_xticks(range(len(grades))); ax.set_xticklabels([f"Gr{g}" for g in grades]); ax.set_yticks(range(len(subs))); ax.set_yticklabels(subs)
    for i, s in enumerate(subs):
        for j, g in enumerate(grades):
            if cell.get((s, g)):
                ax.text(j, i, f"{grid[i][j]:.0f}\nn={len(cell[(s, g)])}", ha="center", va="center", fontsize=7)
    ax.set_title(f"{last}: pass % by subject and grade"); plt.colorbar(im); plt.tight_layout(); plt.savefig(out / "heatmap.png", dpi=130); plt.close()

    checks = {k: v for k, v in sums[last]["checks"].items()}
    fig, ax = plt.subplots(figsize=(7, 0.35 * len(checks) + 1.5))
    names = list(checks)
    ax.barh(names, [100 * checks[n]["pass"] for n in names], color="#10b981")
    ax.set_xlim(0, 100); ax.set_xlabel("pass (%)"); ax.set_title(f"{last}: by check type"); ax.invert_yaxis()
    plt.tight_layout(); plt.savefig(out / "checks.png", dpi=130); plt.close()

    # ---- decision
    s = sums[last]
    ck = lambda name: (s["checks"].get(name) or {}).get("pass")
    policy = (s["slices"].get("tag", {}).get("policy") or {}).get("pass")
    lang, tool = ck("language"), ck("tool_call")
    overall = s["overall_sample_pass"] or 0
    rules = []
    base_ok = overall >= a.min_overall
    why = f"overall {pct(overall)} vs target {pct(a.min_overall)}"
    if ceiling:
        ratio = overall / max(1e-9, ceiling["overall_sample_pass"])
        base_ok = base_ok or ratio >= 0.85
        why += f"; {100 * ratio:.0f}% of the teacher's {pct(ceiling['overall_sample_pass'])}"
    rules.append(("overall", base_ok, why))
    rules.append(("policy tests >= 90%", policy is None or policy >= 0.9, f"policy {pct(policy)}"))
    rules.append(("language checks >= 95%", lang is None or lang >= 0.95, f"language {pct(lang)}"))
    rules.append(("tool checks >= 90%", tool is None or tool >= 0.9, f"tool_call {pct(tool)}"))
    rules.append((f"no slice dropped > {int(100 * a.max_drop)} points", not regress,
                  "; ".join(f"{n} {100 * d:+.0f}" for n, d in regress) or "none dropped"))
    plateau = False
    if prev:
        gain = overall - (sums[prev]["overall_sample_pass"] or 0)
        plateau = gain < 0.02
        rules.append(("still improving (>= +2 points)", not plateau, f"change since {prev}: {100 * gain:+.0f} points"))
    ready = all(ok for _, ok, _ in rules[:5])
    dec = [f"# Decision for {last}\n"] + [f"- {'PASS' if ok else 'FAIL'}  {name}: {txt}" for name, ok, txt in rules]
    dec.append("\n**READY TO MOVE ON: " + ("YES" if ready else "NO") + "**")
    if ceiling and (ceiling["overall_sample_pass"] or 0) < 0.8:
        dec.append(f"WARNING: the teacher itself only passes {pct(ceiling['overall_sample_pass'])} of your exam. That usually means the EXAM has "
                   "bugs (wrong expected answers, checks that are too strict), not that the teacher is weak. Read the teacher's failures.md and fix the exam "
                   "before you trust any ratio against it.")
    if plateau:
        dec.append("Plateau: more data of the same kind will not help. Read failures.md and add NEW situations (analyze_failures.py).")
    if improve:
        dec.append("\nImproved: " + ", ".join(f"{n} {100 * d:+.0f}" for n, d in improve))
    (out / "decision.md").write_text("\n".join(dec) + "\n", encoding="utf-8")
    print("\n".join(dec))
    print(f"\nfiles in {out}: comparison.md decision.md overall.png subjects.png heatmap.png checks.png")


if __name__ == "__main__":
    main()
