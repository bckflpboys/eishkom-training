import re

path1 = "sa-tutor-kit/sa-tutor-kit/training/train_sft.py"

with open(path1, "r", encoding="utf-8") as f:
    code = f.read()

# Replace logging_steps and add disable_tqdm
old_kw = 'logging_steps=5, save_strategy="epoch", save_total_limit=2, seed=a.seed, report_to="none",'
new_kw = 'logging_steps=25, disable_tqdm=True, save_strategy="epoch", save_total_limit=2, seed=a.seed, report_to="none",'

if old_kw in code:
    code = code.replace(old_kw, new_kw, 1)
    with open(path1, "w", encoding="utf-8") as f:
        f.write(code)
    print("Updated train_sft.py with disable_tqdm=True and logging_steps=25")
else:
    print("Pattern not found in train_sft.py")

