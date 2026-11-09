import os

def update_last_session(path):
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    old_target = "5. **`gariep-flash-stage-1`**: Budget Vision/OCR Tutor (LiquidAI/LFM3-VL-2B, `Q6_K`, ~1.55 GB) — Specialized for geometry diagrams, handwritten work, and document OCR."
    new_addition = (
        "5. **`gariep-flash-stage-1`**: Budget Vision/OCR Tutor (LiquidAI/LFM3-VL-2B, `Q6_K`, ~1.55 GB) — Specialized for geometry diagrams, handwritten work, and document OCR.\n"
        "6. **`baby-jake-stage-3`** *(or `atom-stage-3`)*: Ultra-Budget Celeron & Entry Phone Tutor (1B, Q4_K_M ~650–850 MB) — Scheduled for Stage 3. Specially engineered for extreme budget Celeron PCs (4GB RAM) achieving 10–14 tokens/sec, and entry Android phones (2GB–3GB RAM). Trained via Stage 3 Kendal-4B self-distillation with SymPy automated checks."
    )

    if old_target in content and "baby-jake" not in content:
        content = content.replace(old_target, new_addition, 1)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {path}")
    else:
        print(f"Skipped {path}")

update_last_session("LAST_SESSION.md")
update_last_session("sa-tutor-kit/sa-tutor-kit/workspace/LAST_SESSION.md")

