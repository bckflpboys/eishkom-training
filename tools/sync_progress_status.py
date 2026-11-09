import os

def update_progress(path):
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    
    old_status = "> **Status:** **Phase 1, Phase 2, Phase 2.5 Completed (100%)** | **Phase 4 & 5 Multi-Model Fleet Waves 1 & 2 Completed (429 Verified Lessons, 1,099 SFT Samples)** | **Total Compute Spend: $0.00 / $60.00**"
    new_status = "> **Status:** **Phase 1 to 7 Completed (100%)** | **Phase 8 SFT Training ACTIVE on Vertex AI Colab Enterprise NVIDIA L4 GPU Spot VM (`kendal-stage-1` 4B, 5,755 samples, Loss: 0.6597)** | **Total Compute Spend: ~$0.32 / $60.00**"
    
    if old_status in text:
        text = text.replace(old_status, new_status, 1)
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Updated {path}")
    else:
        print(f"Old status not found in {path}")

update_progress("PROGRESS.md")
update_progress("sa-tutor-kit/sa-tutor-kit/PROGRESS.md")
update_progress("stage-1/PROGRESS.md")
update_progress("sa-tutor-kit/sa-tutor-kit/stage-1/PROGRESS.md")

