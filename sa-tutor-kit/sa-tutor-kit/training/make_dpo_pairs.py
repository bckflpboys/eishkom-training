#!/usr/bin/env python3
"""
make_dpo_pairs.py - turn your model's OWN good and bad answers into "reward this, not that" training pairs (DPO).

    # 1. choose prompts your SFT run never trained on (the VALIDATION split of the build), with checks attached
    python training/make_dpo_pairs.py prompts --build workspace/build/r2 --out workspace/eval/dpo_prompts.jsonl --n 300
    # 2. let the trained model answer each prompt several times (this is where good and bad answers come from)
    python eval/run_eval.py --name r2-dpo-samples --items workspace/eval/dpo_prompts.jsonl --backend hf --model unsloth/Qwen3.5-4B \
           --adapter workspace/runs/r2/adapter --n 6 --temperature 0.8
    # 3. mark them with the SAME automatic checks as the exam and pair a passing answer with a failing one
    python training/make_dpo_pairs.py pairs --name r2-dpo-samples --items workspace/eval/dpo_prompts.jsonl --out workspace/build/dpo_r2.jsonl

WHY THIS WORKS (plain words)
  SFT shows the model examples of good answers. It never tells the model "THIS kind of answer is worse".
  Your model still sometimes leaks the answer, slips into the wrong language, or rambles. Preference training
  fixes exactly those habits: for the same question we show a GOOD answer (it passed every check) and a BAD
  one (it failed), both written by the model itself, and nudge it toward the good one.
  Own answers matter: bad answers invented by a person are too obviously bad to teach anything.

LIMITS
  * only prompts where thinking is off (the pairs compare final replies; reasoning is handled by SFT)
  * prompts that involve tool calls are skipped in this version
  * if the model never passes a prompt, --teacher-chosen asks the teacher for a good answer (costs a little)
OUTPUT  the pairs file is in the standard "prompt / chosen / rejected" chat format that TRL and Unsloth's DPO notebook read;
        a sidecar <out>.meta.jsonl says why each pair was made.
"""
import argparse
import json
import random
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "eval"))
import tutor_data as td  # noqa: E402
from score_eval import run_checks  # noqa: E402
from wspaths import p, read_jsonl, write_jsonl  # noqa: E402

SEVERITY = ["no_leak", "final_answer", "language", "tool_call", "asks_question", "auto:length", "auto:no_think_leak", "auto:non_empty"]


def cmd_prompts(a):
    build = Path(a.build)
    manifest = {m["id"]: m for m in read_jsonl(build / "manifest.jsonl")}
    samples = read_jsonl(build / f"{a.split}.jsonl")
    items = []
    for s in samples:
        if not s["id"].endswith("#1") or s["thinking"] != "off":
            continue
        m = manifest[s["record_id"]]
        c, meta = m["control"], m["meta"]
        if any(x["role"] == "assistant" for x in s["prompt"]):
            continue
        checks = []
        reply = c["response_language"] if c["response_language"] != "mirror" else meta.get("student_language")
        if reply in ("en", "af") and c["subject"] not in td.LANGUAGE_SUBJECTS:
            checks.append({"type": "language", "expected": reply})
        fa = meta.get("final_answer")
        if fa and c["answer_policy"] in ("hint_only", "guided"):
            checks += [{"type": "no_leak", "answers": [fa]}, {"type": "asks_question"}]
        elif fa and c["answer_policy"] == "full_solution" and c["subject"] in td.CHECKABLE:
            checks.append({"type": "final_answer", "expected": fa})
        if not checks:
            continue
        items.append({"id": f"dpo-{s['record_id']}", "tags": ["dpo"], "task_type": meta.get("task_type", "solve_problem"), "control": c,
                      "thinking": "off", "messages": [x for x in s["prompt"] if x["role"] != "system"], "checks": checks})
    random.Random(1).shuffle(items)
    items = items[: a.n]
    write_jsonl(a.out, items)
    print(f"wrote {len(items)} prompts with checks to {a.out}")
    if len(items) < 50:
        print("That is few. Build with a bigger validation share (tutor_data.py build ... --val 0.15) or add --split train.")


def cmd_pairs(a):
    items = {i["id"]: i for i in read_jsonl(a.items)}
    outs = defaultdict(list)
    for o in read_jsonl(p("eval_runs", a.name, "outputs.jsonl")):
        outs[o["id"]].append(o)
    fields = set(td.OPTIONAL_RENDER)
    client = None
    pairs, metas, stats = [], [], defaultdict(int)
    for iid, samples in outs.items():
        item = items.get(iid)
        if not item or any(s.get("tool_calls") for s in samples):
            stats["skipped (tools)"] += 1
            continue
        scored = []
        for s in samples:
            checks = run_checks(item, s, None)
            graded = [c for c in checks if c["passed"] is not None]
            scored.append((all(c["passed"] for c in graded), checks, s))
        good = [x for x in scored if x[0] and x[2]["text"].strip()]
        bad = [x for x in scored if not x[0]]
        if not bad:
            stats["skipped (always right)"] += 1
            continue
        if not good and a.teacher_client:
            from llm import Client
            client = client or Client("TEACHER")
            sysmsg = {"role": "system", "content": td.render_system(item["control"], fields)}
            try:
                r = client.chat([sysmsg] + item["messages"], temperature=0.3, max_tokens=900, tag="dpo:teacher-chosen")
                fake = {"text": r["text"], "tool_calls": []}
                chk = run_checks(item, fake, None)
                if all(c["passed"] for c in chk if c["passed"] is not None):
                    good = [(True, chk, fake)]
                    stats["teacher-written chosen"] += 1
            except Exception:                                                  # noqa: BLE001
                pass
        if not good:
            stats["skipped (never right)"] += 1
            continue
        words = sorted(td.words(x[2]["text"]) for x in good)
        median = words[len(words) // 2]
        chosen = min(good, key=lambda x: abs(td.words(x[2]["text"]) - median))      # avoid rewarding the longest answer
        def severity(x):
            failed = [c["type"] for c in x[1] if c["passed"] is False]
            return min((SEVERITY.index(t) if t in SEVERITY else 99) for t in failed) if failed else 99
        rejected = min(bad, key=severity)
        prompt = [{"role": "system", "content": td.render_system(item["control"], fields)}] + item["messages"]
        pairs.append({"prompt": prompt, "chosen": [{"role": "assistant", "content": chosen[2]["text"]}],
                      "rejected": [{"role": "assistant", "content": rejected[2]["text"]}]})
        metas.append({"item": iid, "failed": [c["type"] for c in rejected[1] if c["passed"] is False]})
        stats["pairs"] += 1
    write_jsonl(a.out, pairs)
    write_jsonl(str(a.out) + ".meta.jsonl", metas)
    print(json.dumps(dict(stats), indent=1))
    kinds = defaultdict(int)
    for m in metas:
        for f in m["failed"]:
            kinds[f] += 1
    print("what the BAD answers got wrong:", dict(kinds))
    print(f"wrote {len(pairs)} pairs to {a.out}.  READ 10 of them. Then train with Unsloth's DPO notebook (GUIDE.md phase 9).")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    pr = sub.add_parser("prompts")
    pr.add_argument("--build", required=True)
    pr.add_argument("--split", default="val")
    pr.add_argument("--out", default=str(p("eval", "dpo_prompts.jsonl")))
    pr.add_argument("--n", type=int, default=300)
    pr.set_defaults(fn=cmd_prompts)
    pa = sub.add_parser("pairs")
    pa.add_argument("--name", required=True)
    pa.add_argument("--items", default=str(p("eval", "dpo_prompts.jsonl")))
    pa.add_argument("--out", required=True)
    pa.add_argument("--teacher-chosen", dest="teacher_client", action="store_true")
    pa.set_defaults(fn=cmd_pairs)
    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
