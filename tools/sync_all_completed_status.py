import os

def update_file(path, old, new):
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    if old in content:
        content = content.replace(old, new, 1)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {path}")
    else:
        print(f"Pattern not found in {path}")

# Update PROGRESS.md
p_old = "Phase 8 SFT Training ACTIVE on Vertex AI Colab Enterprise NVIDIA L4 GPU Spot VM (`kendal-stage-1` 4B, 5,755 samples, Loss: 0.6597)"
p_new = "Phase 8 SFT Training COMPLETED on Vertex AI Colab Enterprise NVIDIA L4 GPU Spot VM (`kendal-stage-1` 4B, 5,755 samples, 870 steps complete)"

for p in ["PROGRESS.md", "sa-tutor-kit/sa-tutor-kit/PROGRESS.md", "stage-1/PROGRESS.md", "sa-tutor-kit/sa-tutor-kit/stage-1/PROGRESS.md"]:
    update_file(p, p_old, p_new)

# Update LAST_SESSION.md
ls_old = "### Phase 8: Active Supervised Fine-Tuning Run (`kendal-stage-1` 4B)"
ls_new = "### Phase 8: COMPLETED Supervised Fine-Tuning Run (`kendal-stage-1` 4B) (Verified Nov 9, 2026)"

update_file("LAST_SESSION.md", ls_old, ls_new)
update_file("sa-tutor-kit/sa-tutor-kit/workspace/LAST_SESSION.md", ls_old, ls_new)

