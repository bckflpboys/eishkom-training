import os

def update_file(path):
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    old_needle = "60-minute automatic idle shutdown."
    addition = (
        "60-minute automatic idle shutdown.\n"
        "- **L4 GPU Verified Active (Nov 9, 2026):** NVIDIA L4 GPU (23,034 MiB / 24GB VRAM) "
        "successfully booted and verified in Vertex AI Colab Enterprise with CUDA 13.0."
    )
    if old_needle in content and "L4 GPU Verified Active" not in content:
        content = content.replace(old_needle, addition, 1)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {path}")
    else:
        print(f"Skipped {path}")

update_file("workspace/DECISIONS.md")
update_file("sa-tutor-kit/sa-tutor-kit/workspace/DECISIONS.md")

