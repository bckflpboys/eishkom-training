import os

def update_file(path):
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    old_row = "| **`gariep-flash-stage-1`** | Budget Vision/OCR (2B LiquidAI) | `LiquidAI/LFM3-VL-2B` | `Q6_K` (`LiquidAI/LFM3-VL-2B-GGUF`) | ~1.55 GB | **Local:** Budget phones for high-speed document, diagram, and OCR reading |"
    new_rows = (
        "| **`gariep-flash-stage-1`** | Budget Vision/OCR (2B LiquidAI) | `LiquidAI/LFM3-VL-2B` | `Q6_K` (`LiquidAI/LFM3-VL-2B-GGUF`) | ~1.55 GB | **Local:** Budget phones for high-speed document, diagram, and OCR reading |\n"
        "| **`baby-jake-stage-3`** *(or `atom-stage-3`)* | Ultra-Budget Celeron & Entry Phone Tutor (1B) | `unsloth/Qwen3.5-1.5B` *(or LFM-1B)* | `Q4_K_M` / `Q6_K` | ~650–850 MB | **Local:** Extreme budget Celeron PCs (4GB RAM) & entry Android smartphones (2GB–3GB RAM). Targets 10–14 tokens/sec on legacy dual-core CPUs. Scheduled for Stage 3 via Stage 3 Kendal-4B self-distillation. |"
    )

    if old_row in content and "baby-jake" not in content:
        content = content.replace(old_row, new_rows, 1)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {path}")
    else:
        print(f"Skipped {path}")

update_file("workspace/DECISIONS.md")
update_file("sa-tutor-kit/sa-tutor-kit/workspace/DECISIONS.md")

