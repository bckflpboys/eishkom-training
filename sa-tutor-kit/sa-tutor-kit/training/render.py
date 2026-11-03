#!/usr/bin/env python3
"""
render.py - turn build/*.jsonl samples into token ids with the BASE MODEL's chat template, plus the loss mask.

    python training/render.py --data workspace/build/r1/train.jsonl --tokenizer unsloth/Qwen3.5-4B --show 2 --stats

WHY THIS IS ITS OWN STEP (and why it is the #1 place training silently goes wrong)
  Every model family expects its conversations written in its own format ("chat template"): special tokens
  like <|im_start|>, how tools are listed, where <think> goes. If your training text uses a different format
  from what the app sends at run time, the model learns a format it will never see again.
  So we never hand-write that format. We ask the tokenizer's own template to do it.

HOW THE LOSS MASK WORKS (labels)
  1. render the PROMPT (system + history) with add_generation_prompt=True   -> text A
  2. render the PROMPT + the tutor's answer                                 -> text B
  3. B must START WITH A (we check); the answer is B minus A
  4. tokenize B with character offsets; tokens that lie inside A get label -100 ("ignore"), so the model is
     graded ONLY on the answer it should have written (including its private <think> part and tool calls)
  Why not train on the whole conversation? The model would also be "taught" to write the LEARNER's messages
  and the system prompt: wasted effort that can make it chatty in the wrong role.

THINKING
  thinking "on"  samples: answer = <think>reasoning</think> reply     (prompt rendered with thinking enabled)
  thinking "off" samples: answer = reply only                         (prompt rendered with thinking DISABLED,
                                                                      exactly what your app does when it wants a fast reply)
  --think-style qwen  : the template flag enable_thinking (Qwen3 / Qwen3.5)
  --think-style gemma : a thinking token at the start of the system prompt (check Gemma's model card)
  --think-style none  : the model has no thinking switch
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from wspaths import read_jsonl  # noqa: E402

THINK_TOKEN_GEMMA = "<|think|>"


class TemplateMismatch(Exception):
    pass


def load_tokenizer(name_or_path):
    from transformers import AutoTokenizer
    tok = AutoTokenizer.from_pretrained(name_or_path)
    if not getattr(tok, "is_fast", False):
        raise SystemExit("this tokenizer is not a 'fast' one; the loss mask needs character offsets. Use the model's official tokenizer.")
    return tok


def _hf_msgs(msgs, gemma_think=False):
    """Our stored messages -> what HF chat templates expect (tool-call arguments as dicts)."""
    out = []
    for m in msgs:
        m = dict(m)
        if m.get("tool_calls"):
            fixed = []
            for tc in m["tool_calls"]:
                fn = dict(tc["function"])
                if isinstance(fn.get("arguments"), str):
                    try:
                        fn["arguments"] = json.loads(fn["arguments"])
                    except json.JSONDecodeError:
                        pass
                fixed.append({**{k: v for k, v in tc.items() if k != "function"}, "function": fn})
            m["tool_calls"] = fixed
        out.append(m)
    if gemma_think and out and out[0]["role"] == "system":
        out[0]["content"] = THINK_TOKEN_GEMMA + "\n" + out[0]["content"]
    return out


def render_sample(sample, tok, think_style="qwen"):
    """Returns (prompt_text, completion_text)."""
    thinking_on = sample["thinking"] == "on"
    kw = {"enable_thinking": thinking_on} if think_style == "qwen" else {}
    prompt = _hf_msgs(sample["prompt"], gemma_think=(think_style == "gemma" and thinking_on))
    tools = sample.get("tools") or None
    done = _hf_msgs([sample["completion"]])[0]
    if think_style != "qwen" and "reasoning_content" in done and not thinking_on:
        done.pop("reasoning_content")
    prompt_text = tok.apply_chat_template(prompt, tools=tools, tokenize=False, add_generation_prompt=True, **kw)
    full_text = tok.apply_chat_template(prompt + [done], tools=tools, tokenize=False, add_generation_prompt=False, **kw)
    if not full_text.startswith(prompt_text):
        raise TemplateMismatch(
            "the template does not render prompt+answer as 'prompt then answer'.\n"
            f"  prompt ends : ...{prompt_text[-80:]!r}\n  full text at that point: ...{full_text[max(0, len(prompt_text) - 80):len(prompt_text) + 40]!r}")
    return prompt_text, full_text[len(prompt_text):]


def tokenize_with_mask(prompt_text, completion_text, tok, max_len):
    """Returns (input_ids, labels) or None if longer than max_len. Labels are -100 inside the prompt."""
    full = prompt_text + completion_text
    enc = tok(full, add_special_tokens=False, return_offsets_mapping=True)
    ids, offs = enc["input_ids"], enc["offset_mapping"]
    if len(ids) > max_len:
        return None
    cut = len(prompt_text)
    labels = [-100 if end <= cut else tid for tid, (start, end) in zip(ids, offs)]
    return ids, labels


def render_file(path, tok, think_style="qwen", max_len=4096, limit=0):
    rows = read_jsonl(path)
    if limit:
        rows = rows[:limit]
    out, stats = [], {"samples": len(rows), "kept": 0, "too_long": 0, "mismatch": 0, "no_answer_tokens": 0}
    first_error = None
    for s in rows:
        try:
            pt, ct = render_sample(s, tok, think_style)
        except TemplateMismatch as e:
            stats["mismatch"] += 1
            first_error = first_error or str(e)
            continue
        res = tokenize_with_mask(pt, ct, tok, max_len)
        if res is None:
            stats["too_long"] += 1
            continue
        ids, labels = res
        if sum(1 for x in labels if x != -100) < 2:
            stats["no_answer_tokens"] += 1
            continue
        out.append({"id": s["id"], "thinking": s["thinking"], "input_ids": ids, "labels": labels})
        stats["kept"] += 1
    if out:
        lens = [len(r["input_ids"]) for r in out]
        train_tok = [sum(1 for x in r["labels"] if x != -100) for r in out]
        stats.update(total_tokens=sum(lens), trainable_tokens=sum(train_tok), longest=max(lens),
                     mean_len=round(sum(lens) / len(lens), 1), trainable_share=round(sum(train_tok) / sum(lens), 3))
    stats["first_error"] = first_error
    return out, stats


def show(sample, tok, think_style):
    pt, ct = render_sample(sample, tok, think_style)
    print("=" * 90)
    print(f"sample {sample['id']}  thinking={sample['thinking']}")
    print(pt, end="")
    print("\n<<<<<<<<<<<<<<<<<<<< the model is trained from HERE on (loss starts) >>>>>>>>>>>>>>>>>>>>")
    print(ct)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data", required=True, help="a build/<name>/train.jsonl file")
    ap.add_argument("--tokenizer", required=True, help="Hugging Face model name or a local folder")
    ap.add_argument("--think-style", choices=["qwen", "gemma", "none"], default="qwen")
    ap.add_argument("--max-len", type=int, default=4096)
    ap.add_argument("--show", type=int, default=0, help="print N rendered samples so you can READ what the model will be trained on")
    ap.add_argument("--stats", action="store_true")
    a = ap.parse_args()
    tok = load_tokenizer(a.tokenizer)
    rows = read_jsonl(a.data)
    for s in rows[: a.show]:
        show(s, tok, a.think_style)
    if a.stats or not a.show:
        _, st = render_file(a.data, tok, a.think_style, a.max_len)
        print(json.dumps(st, indent=2))
        if st["mismatch"]:
            print("\nTEMPLATE PROBLEM: some samples cannot be split into prompt + answer. See first_error above. Do NOT train yet.")
        if st["too_long"]:
            print(f"\n{st['too_long']} samples are longer than --max-len {a.max_len} and were dropped. Raise --max-len or shorten the data.")


if __name__ == "__main__":
    main()
