import re

path = "sa-tutor-kit/sa-tutor-kit/training/train_sft.py"

with open(path, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Update batch and grad-accum defaults / dynamic auto-scaling
old_batch_block = """    ap.add_argument("--batch", type=int, default=2)
    ap.add_argument("--grad-accum", type=int, default=8, help="effective batch = batch x grad-accum")"""

new_batch_block = """    ap.add_argument("--batch", type=int, default=0, help="batch size per device. 0 = auto-scale based on VRAM/model size")
    ap.add_argument("--grad-accum", type=int, default=0, help="effective batch = batch x grad-accum. 0 = auto-scale")"""

if old_batch_block in code:
    code = code.replace(old_batch_block, new_batch_block, 1)

# Add auto-scale logic right after parse_args
old_parse = "    a = ap.parse_args()"
new_parse = """    a = ap.parse_args()

    # Dynamic VRAM optimization: Auto-scale batch size based on model tier
    if a.batch == 0 or a.grad_accum == 0:
        m_lower = a.model.lower()
        if "2b" in m_lower or "1.5b" in m_lower or "1b" in m_lower:
            a.batch = 8 if a.batch == 0 else a.batch
            a.grad_accum = 2 if a.grad_accum == 0 else a.grad_accum
            print(f"[VRAM Optimizer] Small model detected ({a.model}). Scaling batch={a.batch}, grad_accum={a.grad_accum} for maximum throughput.")
        elif "4b" in m_lower:
            a.batch = 4 if a.batch == 0 else a.batch
            a.grad_accum = 4 if a.grad_accum == 0 else a.grad_accum
            print(f"[VRAM Optimizer] Mid-tier model detected ({a.model}). Scaling batch={a.batch}, grad_accum={a.grad_accum} (18GB VRAM target).")
        else: # 27B or larger
            a.batch = 2 if a.batch == 0 else a.batch
            a.grad_accum = 8 if a.grad_accum == 0 else a.grad_accum
            print(f"[VRAM Optimizer] Flagship model detected ({a.model}). Safe batch={a.batch}, grad_accum={a.grad_accum} (21GB VRAM target).")"""

if old_parse in code and "[VRAM Optimizer]" not in code:
    code = code.replace(old_parse, new_parse, 1)

# Add clean callback definition and pass it to Trainer
old_trainer_import = "    from transformers import Trainer, TrainingArguments"
new_trainer_import = """    from transformers import Trainer, TrainingArguments, TrainerCallback

    class CleanProgressCallback(TrainerCallback):
        def __init__(self, total_steps):
            self.total_steps = total_steps
            self.t0 = time.time()
        def on_log(self, args, state, control, logs=None, **kwargs):
            if not logs: return
            step = state.global_step
            loss = logs.get("loss", "N/A")
            lr = logs.get("learning_rate", 0)
            elapsed = (time.time() - self.t0) / 60
            pct = 100 * step / max(1, self.total_steps)
            if isinstance(loss, float):
                loss_str = f"{loss:.4f}"
            else:
                loss_str = str(loss)
            print(f"  -> [Step {step:3d}/{self.total_steps} ({pct:4.1f}%)] Loss: {loss_str} | LR: {lr:.2e} | Elapsed: {elapsed:4.1f}m", flush=True)"""

if old_trainer_import in code and "CleanProgressCallback" not in code:
    code = code.replace(old_trainer_import, new_trainer_import, 1)

old_trainer_call = "    trainer = Trainer(model=model, args=TrainingArguments(**kw), train_dataset=Rows(train_rows),\n                      eval_dataset=Rows(val_rows) if val_rows else None, data_collator=make_collator(pad_id))"
new_trainer_call = "    clean_cb = CleanProgressCallback(total_steps)\n    trainer = Trainer(model=model, args=TrainingArguments(**kw), train_dataset=Rows(train_rows),\n                      eval_dataset=Rows(val_rows) if val_rows else None, data_collator=make_collator(pad_id), callbacks=[clean_cb])"

if old_trainer_call in code:
    code = code.replace(old_trainer_call, new_trainer_call, 1)

with open(path, "w", encoding="utf-8") as f:
    f.write(code)

print("Successfully injected VRAM optimizer & clean progress callback into train_sft.py!")

