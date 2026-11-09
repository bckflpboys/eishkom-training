import os

def update_file(path):
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    old_needle = "- **GPU Quota:** NVIDIA L4 GPU quota increased to 1 in `IAM & Admin > Quotas`."
    addition = (
        "- **GPU Quota:** NVIDIA L4 GPU quota increased to 1 in `IAM & Admin > Quotas`.\n"
        "- **Runtime Template Provisioned (Verified Nov 9, 2026):** Template `eishkom-gpu` "
        "(ID `5096703687183564800`) successfully configured and provisioned in `us-central1 (Iowa)` "
        "with `g2-standard-4` (4 vCPUs, 16GB RAM), 1x NVIDIA L4 GPU (24GB VRAM), 100GB SSD persistent "
        "disk (`pd-ssd`), and 60-minute automatic idle shutdown."
    )
    if old_needle in content and "eishkom-gpu" not in content:
        content = content.replace(old_needle, addition, 1)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {path}")
    else:
        print(f"Skipped {path} (already present or needle missing)")

update_file("workspace/DECISIONS.md")
update_file("sa-tutor-kit/sa-tutor-kit/workspace/DECISIONS.md")

