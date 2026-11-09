import os

def update_file(path):
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    old_needle = "verified in Vertex AI Colab Enterprise with CUDA 13.0."
    addition = (
        "verified in Vertex AI Colab Enterprise with CUDA 13.0.\n"
        "- **Kendal Stage 1 (4B) Training Run Active (Nov 9, 2026):** Supervised fine-tuning running on "
        "L4 Spot VM. Loss dropped from 1.662 down to 0.6597 by Step 104/870 at 8.14s/it."
    )
    if old_needle in content and "Kendal Stage 1 (4B) Training Run Active" not in content:
        content = content.replace(old_needle, addition, 1)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {path}")
    else:
        print(f"Skipped {path}")

update_file("workspace/DECISIONS.md")
update_file("sa-tutor-kit/sa-tutor-kit/workspace/DECISIONS.md")

