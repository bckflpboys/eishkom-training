import os

def update_progress(path):
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    old_row = "| **`gariep-flash-stage-1`** | Budget Vision/OCR (2B LiquidAI) | `LiquidAI/LFM3-VL-2B` | `Q6_K` | ~1.55 GB | **Local:** Budget phones for high-speed document, diagram, and OCR reading |"
    new_rows = (
        "| **`gariep-flash-stage-1`** | Budget Vision/OCR (2B LiquidAI) | `LiquidAI/LFM3-VL-2B` | `Q6_K` | ~1.55 GB | **Local:** Budget phones for high-speed document, diagram, and OCR reading |\n"
        "| **`baby-jake-stage-3`** *(or `atom-stage-3`)* | Ultra-Budget Celeron & Entry Phone Tutor (1B) | `unsloth/Qwen3.5-1.5B` *(or LFM-1B)* | `Q4_K_M` | ~650–850 MB | **Local:** Extreme budget Celeron PCs (4GB RAM, 10–14 tokens/sec) & 2GB–3GB phones (100% offline). Stage 3 release via Stage 3 Kendal-4B self-distillation. |"
    )

    if old_row in content and "baby-jake" not in content:
        content = content.replace(old_row, new_rows, 1)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {path}")
    else:
        print(f"Skipped {path}")

for p in ["PROGRESS.md", "sa-tutor-kit/sa-tutor-kit/PROGRESS.md", "stage-1/PROGRESS.md", "sa-tutor-kit/sa-tutor-kit/stage-1/PROGRESS.md"]:
    update_progress(p)

