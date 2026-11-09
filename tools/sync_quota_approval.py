import os

def update_file(path):
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    old_needle = "- **GPU Quota:** NVIDIA L4 GPU quota increased to 1 in `IAM & Admin > Quotas`."
    addition = (
        "- **GPU Quota (APPROVED Nov 9, 2026):** Global GPU Quota `GPUS_ALL_REGIONS` limit officially "
        "approved and increased from 0 to 1 by Google Cloud Support for project `eishkom`."
    )
    if old_needle in content and "APPROVED Nov 9, 2026" not in content:
        content = content.replace(old_needle, addition, 1)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {path}")
    else:
        print(f"Skipped {path}")

update_file("workspace/DECISIONS.md")
update_file("sa-tutor-kit/sa-tutor-kit/workspace/DECISIONS.md")

