#!/usr/bin/env python3
"""
vision_prepare.py - get picture-and-text samples ready for vision fine-tuning (GUIDE.md phase 11).

    python training/vision_prepare.py --data workspace/build/r3/train.jsonl --images-root workspace/images --out workspace/build/r3/vision_train.jsonl

WHAT IT DOES
  Takes the samples of a build that contain images (user messages with {"type": "image", "path": ...}) and writes
  them in the layout Unsloth's vision notebooks use:  messages -> content = [{"type":"image",...},{"type":"text",...}].
  Images stay as PATHS in the file; load them when training:

      from PIL import Image
      def load_images(example):
          for m in example["messages"]:
              for part in m["content"]:
                  if part["type"] == "image":
                      part["image"] = Image.open(IMAGES_ROOT / part["path"]).convert("RGB")
          return example

  For thinking-on samples the reasoning is written inline as <think>...</think> before the reply.
  Samples with tool calls are left out (not supported in this version).

WHICH PARTS TO TRAIN (the "freeze layers" question)
  Unsloth's vision API lets you choose: finetune_vision_layers, finetune_language_layers, finetune_attention_modules,
  finetune_mlp_modules. Safe start: language layers ON, vision encoder OFF. A modern vision encoder already reads
  printed text well; unfreeze it only if reading handwriting is still poor after you add enough real examples.
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import tutor_data as td  # noqa: E402
from wspaths import read_jsonl, write_jsonl  # noqa: E402


def parts(content):
    if isinstance(content, str):
        return [{"type": "text", "text": content}]
    out = []
    for p_ in content:
        out.append({"type": "image", "path": p_["path"]} if p_.get("type") == "image" else {"type": "text", "text": p_.get("text", "")})
    return out


def convert(sample):
    msgs = []
    for m in sample["prompt"]:
        if m["role"] == "tool" or m.get("tool_calls"):
            return None
        msgs.append({"role": m["role"], "content": parts(m["content"])})
    c = sample["completion"]
    if c.get("tool_calls"):
        return None
    text = c.get("content", "")
    if sample["thinking"] == "on" and c.get("reasoning_content"):
        text = f"<think>\n{c['reasoning_content']}\n</think>\n\n{text}"
    msgs.append({"role": "assistant", "content": [{"type": "text", "text": text}]})
    return {"id": sample["id"], "thinking": sample["thinking"], "messages": msgs}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data", required=True)
    ap.add_argument("--images-root", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    rows, missing, skipped = [], 0, 0
    for s in read_jsonl(a.data):
        if not any(td.has_image(m.get("content")) for m in s["prompt"]):
            continue
        conv = convert(s)
        if conv is None:
            skipped += 1
            continue
        for m in conv["messages"]:
            for part in m["content"]:
                if part["type"] == "image" and not (Path(a.images_root) / part["path"]).exists():
                    missing += 1
        rows.append(conv)
    write_jsonl(a.out, rows)
    n_img = sum(1 for r in rows for m in r["messages"] for p_ in m["content"] if p_["type"] == "image")
    print(f"{len(rows)} vision samples ({n_img} images) -> {a.out}; skipped {skipped} with tool calls; MISSING image files: {missing}")
    if missing:
        sys.exit("fix the missing images before training")


if __name__ == "__main__":
    main()
