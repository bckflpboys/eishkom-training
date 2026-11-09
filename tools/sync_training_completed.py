import os

def update_file(path):
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    old_target = "Loss dropped from 1.662 down to 0.6597 by Step 104/870 at 8.14s/it."
    new_status = (
        "Loss dropped from 1.662 down to 0.6597 by Step 104/870 at 8.14s/it.\n"
        "- **Kendal Stage 1 (4B) Training COMPLETED (Nov 9, 2026):** Supervised fine-tuning successfully "
        "completed all 870 steps across 3 epochs on 5,755 South African curriculum items. Final adapter "
        "weights saved to `workspace/runs/r1/adapter/` (`adapter_model.safetensors`). Ready for GGUF multi-quant export."
    )

    if old_target in content and "Kendal Stage 1 (4B) Training COMPLETED" not in content:
        content = content.replace(old_target, new_status, 1)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {path}")
    else:
        print(f"Skipped {path}")

update_file("workspace/DECISIONS.md")
update_file("sa-tutor-kit/sa-tutor-kit/workspace/DECISIONS.md")

