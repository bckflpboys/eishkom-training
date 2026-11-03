#!/usr/bin/env python3
"""
train_sft.py - teach the base model your tutor behaviour (supervised fine-tuning with LoRA). Run in Colab on a GPU.

    # 1. free check on any computer (no GPU): render, count tokens, look at what the model will see
    python training/train_sft.py --model unsloth/Qwen3.5-4B --data workspace/build/r1 --dry-run
    # 2. the "can it memorise?" test (GUIDE.md phase 7): 20 samples, many passes. Loss should fall close to 0.
    python training/train_sft.py --model unsloth/Qwen3.5-4B --data workspace/build/r1 --out workspace/runs/overfit --limit 20 --epochs 15
    # 3. the real run
    python training/train_sft.py --model unsloth/Qwen3.5-4B --data workspace/build/r1 --out workspace/runs/r1

WHAT "LoRA" MEANS HERE (plain words)
  The base model has billions of numbers ("weights"). We lock all of them and clip on a small extra set (the
  "adapter", about 1-2% of the size, rank --rank). Training only changes the adapter. That is why it fits on a
  free/cheap GPU, why the result is a small folder (~100-300 MB) instead of 9 GB, and why the base model's
  general skills are mostly preserved. Everything is saved to <out>/adapter.

NOTES
  * Qwen3.5: Unsloth recommends 16-bit LoRA (the default here), NOT 4-bit QLoRA. --load-4bit exists for models where 4-bit is fine.
  * Every round starts again from the BASE model on ALL data so far (GUIDE.md): never continue round 2 from round 1's adapter.
  * This script could not be run on a GPU by the person who wrote it. If model loading fails, open Unsloth's official notebook for
    your model and copy ITS loading cell into load_model() below. Rendering, masking and saving stay the same.
  * --resume continues an interrupted run from the last checkpoint (Colab disconnects: keep --out on Google Drive).
"""
import argparse
import hashlib
import inspect
import json
import math
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

USE_UNSLOTH = False
if "--no-unsloth" not in sys.argv and "--dry-run" not in sys.argv:
    try:
        import unsloth  # noqa: F401  (Unsloth must be imported BEFORE transformers/peft so it can patch them)
        USE_UNSLOTH = True
    except Exception as e:                                                    # noqa: BLE001
        print(f"(Unsloth not available: {type(e).__name__}; using plain transformers + peft, slower and hungrier)")

import tutor_data as td  # noqa: E402
from render import load_tokenizer, render_file, show  # noqa: E402
from wspaths import read_jsonl  # noqa: E402

DEFAULT_TARGETS = ["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"]


class Rows:
    def __init__(self, rows):
        self.rows = rows

    def __len__(self):
        return len(self.rows)

    def __getitem__(self, i):
        return self.rows[i]


def make_collator(pad_id):
    import torch

    def collate(batch):
        m = max(len(b["input_ids"]) for b in batch)
        ids = torch.full((len(batch), m), pad_id, dtype=torch.long)
        lab = torch.full((len(batch), m), -100, dtype=torch.long)
        att = torch.zeros((len(batch), m), dtype=torch.long)
        for i, b in enumerate(batch):
            n = len(b["input_ids"])
            ids[i, :n] = torch.tensor(b["input_ids"])
            lab[i, :n] = torch.tensor(b["labels"])
            att[i, :n] = 1
        return {"input_ids": ids, "attention_mask": att, "labels": lab}
    return collate


def load_model(a):
    targets = a.target_modules.split(",") if a.target_modules else DEFAULT_TARGETS
    if USE_UNSLOTH:
        from unsloth import FastLanguageModel
        kw = dict(model_name=a.model, max_seq_length=a.max_len, load_in_4bit=a.load_4bit)
        try:
            model, tok = FastLanguageModel.from_pretrained(**kw, load_in_16bit=not a.load_4bit)
        except TypeError:
            model, tok = FastLanguageModel.from_pretrained(**kw)
        model = FastLanguageModel.get_peft_model(model, r=a.rank, lora_alpha=a.alpha, lora_dropout=0.0, bias="none",
                                                 target_modules=targets, use_gradient_checkpointing="unsloth", random_state=a.seed)
    else:
        import torch
        from peft import LoraConfig, get_peft_model
        from transformers import AutoModelForCausalLM
        dtype = torch.bfloat16 if torch.cuda.is_available() and torch.cuda.is_bf16_supported() else torch.float16
        model = AutoModelForCausalLM.from_pretrained(a.model, torch_dtype=dtype, device_map="auto")
        model.gradient_checkpointing_enable()
        model.enable_input_require_grads()
        model = get_peft_model(model, LoraConfig(r=a.rank, lora_alpha=a.alpha, lora_dropout=0.0, bias="none",
                                                 target_modules=targets, task_type="CAUSAL_LM"))
        tok = None
    tok = getattr(tok, "tokenizer", tok)
    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    total = sum(p.numel() for p in model.parameters())
    print(f"trainable parameters: {trainable:,} of {total:,} ({100 * trainable / total:.2f}%)")
    if trainable / total < 0.001:
        print("WARNING: very few trainable parameters. The target module names probably do not match this architecture. "
              "Copy target_modules from Unsloth's notebook for your model and pass them with --target-modules a,b,c")
    return model, tok


def sanity_generate(model, tok_render, a):
    """After training: one quick answer, so you SEE whether the format came out right (not a test, a smoke check)."""
    import torch
    if USE_UNSLOTH:
        from unsloth import FastLanguageModel
        FastLanguageModel.for_inference(model)
    control = {"subject": "mathematics", "grade": 9, "subject_language": "en", "response_language": "en", "strategy": "step_walkthrough",
               "answer_policy": "guided", "student_level": "on_track", "tone": "friendly_playful", "response_length": "short",
               "math_format": "latex", "tools": []}
    msgs = [{"role": "system", "content": td.render_system(control, set(td.OPTIONAL_RENDER))},
            {"role": "user", "content": "Solve for x: 5x + 7 = 32"}]
    kw = {"enable_thinking": False} if a.think_style == "qwen" else {}
    text = tok_render.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True, **kw)
    inputs = tok_render(text, return_tensors="pt", add_special_tokens=False).to(model.device)
    with torch.no_grad():
        out = model.generate(**inputs, max_new_tokens=200, do_sample=False)
    print("\n--- sanity answer (thinking off) ---\n" + tok_render.decode(out[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--model", required=True, help="e.g. unsloth/Qwen3.5-4B (the SAME model you will export and serve)")
    ap.add_argument("--tokenizer", help="default: same as --model")
    ap.add_argument("--data", required=True, help="a build/<name> folder with train.jsonl (and val.jsonl)")
    ap.add_argument("--out", help="run folder (put it on Google Drive in Colab)")
    ap.add_argument("--think-style", choices=["qwen", "gemma", "none"], default="qwen")
    ap.add_argument("--max-len", type=int, default=4096)
    ap.add_argument("--epochs", type=float, default=2.0, help="passes over the data. 2-3 is usual; more memorises")
    ap.add_argument("--lr", type=float, default=2e-4, help="learning rate for LoRA (1e-4 to 3e-4 is normal)")
    ap.add_argument("--rank", type=int, default=16, help="LoRA size: 16 is a good start, 32-64 if you add many skills")
    ap.add_argument("--alpha", type=int, default=16)
    ap.add_argument("--batch", type=int, default=2)
    ap.add_argument("--grad-accum", type=int, default=8, help="effective batch = batch x grad-accum")
    ap.add_argument("--seed", type=int, default=3407)
    ap.add_argument("--limit", type=int, default=0, help="use only the first N samples (overfit test)")
    ap.add_argument("--target-modules", help="comma list; default q,k,v,o,gate,up,down projections")
    ap.add_argument("--load-4bit", action="store_true")
    ap.add_argument("--no-unsloth", action="store_true")
    ap.add_argument("--dry-run", action="store_true", help="render + statistics only; needs no GPU")
    ap.add_argument("--resume", action="store_true")
    ap.add_argument("--show", type=int, default=1, help="print N rendered samples")
    a = ap.parse_args()

    data = Path(a.data)
    tok_r = load_tokenizer(a.tokenizer or a.model)
    train_rows, st = render_file(data / "train.jsonl", tok_r, a.think_style, a.max_len, a.limit)
    val_rows, vst = (render_file(data / "val.jsonl", tok_r, a.think_style, a.max_len)
                     if (data / "val.jsonl").exists() and (data / "val.jsonl").stat().st_size else ([], {}))
    for s in read_jsonl(data / "train.jsonl")[: a.show]:
        show(s, tok_r, a.think_style)
    print("\ntrain:", json.dumps(st))
    print("val  :", json.dumps(vst))
    if st["mismatch"]:
        sys.exit("TEMPLATE PROBLEM (see first_error above). Fix before training.")
    if not train_rows:
        sys.exit("no training samples after rendering.")
    steps_per_epoch = math.ceil(len(train_rows) / (a.batch * a.grad_accum))
    total_steps = max(1, int(steps_per_epoch * a.epochs))
    print(f"\n{len(train_rows)} samples, {steps_per_epoch} optimizer steps per epoch, {total_steps} steps in total, "
          f"{st['trainable_tokens']:,} tokens to learn from per epoch")
    if a.dry_run:
        print("dry run finished: nothing was trained.")
        return
    if not a.out:
        sys.exit("--out is required for a real run")

    import torch
    from transformers import Trainer, TrainingArguments
    model, tok_model = load_model(a)
    pad_id = (tok_model or tok_r).pad_token_id if (tok_model or tok_r).pad_token_id is not None else tok_r.eos_token_id
    bf16 = torch.cuda.is_available() and torch.cuda.is_bf16_supported()
    try:
        import bitsandbytes  # noqa: F401
        optim = "adamw_8bit"
    except ImportError:
        optim = "adamw_torch"
    sig = inspect.signature(TrainingArguments.__init__).parameters
    out = Path(a.out)
    kw = dict(output_dir=str(out / "checkpoints"), per_device_train_batch_size=a.batch, gradient_accumulation_steps=a.grad_accum,
              num_train_epochs=a.epochs, learning_rate=a.lr, lr_scheduler_type="cosine", warmup_steps=max(1, int(0.03 * total_steps)),
              weight_decay=0.01, logging_steps=5, save_strategy="epoch", save_total_limit=2, seed=a.seed, report_to="none",
              remove_unused_columns=False, optim=optim, bf16=bf16, fp16=not bf16, dataloader_num_workers=0)
    if val_rows:
        kw["eval_strategy" if "eval_strategy" in sig else "evaluation_strategy"] = "epoch"
        kw["per_device_eval_batch_size"] = a.batch
    trainer = Trainer(model=model, args=TrainingArguments(**kw), train_dataset=Rows(train_rows),
                      eval_dataset=Rows(val_rows) if val_rows else None, data_collator=make_collator(pad_id))
    t0 = time.time()
    result = trainer.train(resume_from_checkpoint=True if a.resume else None)
    minutes = (time.time() - t0) / 60

    adapter = out / "adapter"
    model.save_pretrained(str(adapter))
    (tok_model or tok_r).save_pretrained(str(adapter))
    (out / "log_history.json").write_text(json.dumps(trainer.state.log_history, indent=1), encoding="utf-8")
    sha = hashlib.sha1((data / "train.jsonl").read_bytes()).hexdigest()
    (out / "run.json").write_text(json.dumps({
        "model": a.model, "data": str(data), "train_jsonl_sha1": sha, "args": vars(a), "train_stats": st, "val_stats": vst,
        "final_train_loss": result.training_loss, "minutes": round(minutes, 1), "unsloth": USE_UNSLOTH,
        "when": time.strftime("%Y-%m-%d %H:%M"), "kit_render_version": td.RENDER_VERSION}, indent=2, default=str), encoding="utf-8")
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        logs = [x for x in trainer.state.log_history if "loss" in x]
        evals = [x for x in trainer.state.log_history if "eval_loss" in x]
        plt.figure(figsize=(6, 3.5))
        plt.plot([x["step"] for x in logs], [x["loss"] for x in logs], label="train loss")
        if evals:
            plt.plot([x["step"] for x in evals], [x["eval_loss"] for x in evals], "o-", label="val loss")
        plt.xlabel("step"); plt.ylabel("loss"); plt.legend(); plt.tight_layout(); plt.savefig(out / "loss.png", dpi=120)
    except Exception:                                                         # noqa: BLE001
        pass
    print(f"\nsaved adapter to {adapter}  ({minutes:.1f} minutes, final train loss {result.training_loss:.3f})")
    print("READ loss.png: train loss should fall and flatten; val loss falling then RISING means over-fitting (use fewer epochs).")
    try:
        sanity_generate(model, tok_r, a)
    except Exception as e:                                                    # noqa: BLE001
        print(f"(sanity generation skipped: {type(e).__name__}: {e})")
    print("NEXT: python eval/run_eval.py --backend hf --model", a.model, "--adapter", adapter, "--name", out.name)


if __name__ == "__main__":
    main()
