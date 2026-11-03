#!/usr/bin/env python3
"""
make_vision_records.py - make "photo of a problem" training records (and exam items) from records you already verified.

    # training records: needs verified FAITHFUL maths/science records (they carry the question text)
    python pipeline/make_vision_records.py records --records workspace/verified/train_r3.jsonl --out workspace/verified/vision_r3.jsonl --n 300
    # exam items from held-out questions
    python pipeline/make_vision_records.py exam --source dbe-maths-g12-p1-2024-nov --max 20
    then: python tutor_data.py validate workspace/verified/vision_r3.jsonl --images-root workspace/images

WHAT IT BUILDS
  The learner sends a PICTURE of the question. A good tutor first says what it read and waits for a yes,
  because photos and handwriting get misread. So each record is:
     learner: [picture of the question] "Can you help me with this one?"
     tutor  : "I read this as: <the question>. Is that right?"          <- the transcription is the item's own text
     learner: "yes" / "yeah that's right"
     tutor  : ... the original, already verified, tutoring conversation continues
  A share of records (--unreadable) use a heavily BLURRED picture, and the correct reply is to ask for a clearer
  photo instead of guessing. This teaches the model NOT to hallucinate unreadable text.

THE PICTURES
  Printed-style pictures are drawn from the question text itself (matplotlib mathtext, with small random changes
  in size, tilt, noise) so you get unlimited, perfectly-labelled printed examples. They are a start, not the real
  thing: add real rendered exam pages (render_pages.py) and, with written consent and no faces or names, real
  photos of handwriting. Handwriting is the hard part; do not promise it before you have tested it.
"""
import argparse
import copy
import random
import re
import sys
import textwrap
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import tutor_data as td  # noqa: E402
from wspaths import p, read_jsonl, write_jsonl  # noqa: E402

YES = ["yes", "yes thats right", "yeah that's right", "ja", "yes it is", "correct"]
ASK_AGAIN = ("I can't read that clearly. Could you take another photo, a bit closer and in good light, "
             "or type the question for me? I don't want to guess and get it wrong.")
SAY = {"en": "I read this as: {q} Is that right?"}


def clean_question(text):
    return re.sub(r"\s+", " ", str(text)).strip()


def draw_question(text, path, rng, blur=False):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from PIL import Image, ImageFilter
    import numpy as np
    wrapped = "\n".join(textwrap.wrap(text, width=rng.choice([46, 54, 62]), break_long_words=False, break_on_hyphens=False)) or text
    size = rng.choice([15, 17, 19])
    lines = wrapped.count("\n") + 1
    fig = plt.figure(figsize=(7, 0.55 + 0.5 * lines), dpi=110)
    try:
        fig.text(0.03, 0.5, wrapped, fontsize=size, va="center", ha="left")
        fig.savefig(path, facecolor="white")
    except Exception:                                                     # noqa: BLE001  (mathtext cannot parse some LaTeX)
        plt.close(fig)
        return False
    plt.close(fig)
    img = Image.open(path).convert("RGB")
    img = img.rotate(rng.uniform(-2.0, 2.0), expand=True, fillcolor=(255, 255, 255))
    arr = np.asarray(img).astype("float32")
    arr += np.random.default_rng(rng.randint(0, 10**6)).normal(0, 6, arr.shape)
    img = Image.fromarray(np.clip(arr, 0, 255).astype("uint8"))
    if blur:
        img = img.filter(ImageFilter.GaussianBlur(radius=9)).resize((img.width // 3, img.height // 3))
    img.save(path)
    return True


def question_of(rec):
    first = next(m for m in rec["messages"] if m["role"] == "user")
    return clean_question(td.text_of(first["content"]))


def cmd_records(a):
    rng = random.Random(a.seed)
    recs = [r for r in read_jsonl(a.records) if r["meta"].get("mode") == "faithful" and r["control"]["subject"] in td.CHECKABLE
            and r["messages"] and isinstance(r["messages"][0]["content"], str) and not r["control"].get("learner_context")]
    rng.shuffle(recs)
    out, img_dir = [], p("images", "synth")
    img_dir.mkdir(parents=True, exist_ok=True)
    for r in recs[: a.n]:
        rec = copy.deepcopy(r)
        q = question_of(rec)
        blurry = rng.random() < a.unreadable
        rel = f"synth/{rec['id']}{'_blur' if blurry else ''}.png"
        if not draw_question(q, str(p("images") / rel), rng, blur=blurry):
            continue
        rec["id"] = rec["id"] + ("-vb" if blurry else "-v")
        rec["group_id"] = rec["group_id"] + "-vision"
        msgs = rec["messages"]
        user_part = [{"type": "image", "path": rel}, {"type": "text", "text": rng.choice(["Can you help me with this one?", "pls help with this question", "How do I do this?"])}]
        reason = "The picture shows a question. I should say what I read and wait for the learner to confirm before I solve anything, because photos can be misread."
        if blurry:
            new = [{"role": "user", "content": user_part}, {"role": "assistant", "content": ASK_AGAIN}]
            if rec["thinking"] == "on":
                new[1]["reasoning"] = "The picture is too blurry to read the numbers reliably. Guessing could teach the wrong maths, so I ask for a clearer photo."
            rec["messages"] = new
            rec["meta"]["notes"] = "unreadable image: correct behaviour is to ask for a clearer photo"
            rec["meta"].pop("final_answer", None)
        else:
            confirm = {"role": "assistant", "content": SAY["en"].format(q=q)}
            if rec["thinking"] == "on":
                confirm["reasoning"] = f"The image shows: {q} " + reason
            rec["messages"] = [{"role": "user", "content": user_part}, confirm,
                               {"role": "user", "content": rng.choice(YES)}] + msgs[1:]
        rec["meta"].update(task_type="photo_problem", image_kind="printed", split="auto" if rec["meta"].get("answer_verified") else "exclude")
        out.append(rec)
    write_jsonl(a.out, out)
    n_blur = sum(1 for r in out if r["id"].endswith("-vb"))
    print(f"wrote {len(out)} vision records ({n_blur} unreadable-image cases) -> {a.out}")
    print(f"images in {p('images', 'synth')}. NEXT: python tutor_data.py validate {a.out} --images-root {p('images')}")


def cmd_exam(a):
    rng = random.Random(a.seed)
    items = [i for i in read_jsonl(p("items", f"{a.source}.jsonl")) if not i.get("needs_review") and i.get("final_answer") and i["subject"] in td.CHECKABLE]
    rng.shuffle(items)
    out_path = p("eval", "eval_items_vision.jsonl")
    out = []
    (p("images") / "exam").mkdir(parents=True, exist_ok=True)
    for it in items[: a.max]:
        q = clean_question(it["question"])
        rel = f"exam/{it['item_id']}.png"
        if not draw_question(q, str(p("images") / rel), rng):
            continue
        nums = re.findall(r"\d+(?:[.,]\d+)?", q)[:3]
        checks = [{"type": "asks_question"}, {"type": "no_leak", "answers": [it["final_answer"]]}]
        if nums:
            checks.append({"type": "contains_all", "words": nums})
        out.append({"id": f"vis-{it['item_id']}", "tags": ["vision"], "task_type": "photo_problem",
                    "control": {"subject": it["subject"], "grade": int(it["grade"]), "subject_language": it.get("language") or "en", "response_language": "mirror",
                                "strategy": "auto", "answer_policy": "guided", "student_level": "on_track", "tone": "encouraging",
                                "response_length": "short", "math_format": "latex", "tools": ["calculator"]},
                    "thinking": "off",
                    "messages": [{"role": "user", "content": [{"type": "image", "path": rel}, {"type": "text", "text": "Can you help me with this one?"}]}],
                    "checks": checks})
    write_jsonl(out_path, out)
    print(f"wrote {len(out)} vision exam items to {out_path} (images in workspace/images/exam).")
    print("They test: says what it read (numbers copied correctly), asks a question, does not solve it yet.")
    print("Run with: python eval/run_eval.py --items", out_path, "--backend openai --base-url http://localhost:8080/v1 ... (llama-server started with --mmproj)")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("records")
    r.add_argument("--records", required=True)
    r.add_argument("--out", required=True)
    r.add_argument("--n", type=int, default=300)
    r.add_argument("--unreadable", type=float, default=0.1, help="share of blurred, unreadable pictures")
    r.add_argument("--seed", type=int, default=1)
    r.set_defaults(fn=cmd_records)
    e = sub.add_parser("exam")
    e.add_argument("--source", required=True)
    e.add_argument("--max", type=int, default=20)
    e.add_argument("--seed", type=int, default=1)
    e.set_defaults(fn=cmd_exam)
    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
