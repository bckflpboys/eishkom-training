import os

def update_guide(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    
    old_target = """# ==============================================================================
# PHASE 7 & 8: VERTEX AI COLAB ENTERPRISE SFT & GGUF EXPORT
# (Execute inside colab/sa_tutor_colab.ipynb on NVIDIA L4 Spot VM)
# ==============================================================================
# koeberg-stage-1 (27B) -> koeberg-stage-1-UD-Q4_K_XL.gguf
# kendal-stage-1 (4B)   -> kendal-stage-1-Q6_K.gguf & kendal-flash-stage-1-Q4_K_M.gguf
# gariep-stage-1 (2B)   -> gariep-stage-1-Q6_K.gguf"""

    new_target = """# ==============================================================================
# PHASE 7 & 8: VERTEX AI COLAB ENTERPRISE SFT & GGUF EXPORT (VERIFIED NOV 9, 2026)
# Runtime template: eishkom-gpu (g2-standard-4, 1x NVIDIA L4 24GB VRAM, 100GB SSD)
# Spot VM enabled (~$0.32/hr consuming promotional credits, Quota GPUS_ALL_REGIONS = 1 approved)
# ==============================================================================
# 1. Unpack dataset (5,755 samples) and training scripts:
#    !unzip -q eishkom_colab_kit.zip
#    os.environ['SA_WORKSPACE'] = os.path.abspath('workspace')
#
# 2. Train kendal-stage-1 (4B) on unsloth/Qwen3.5-4B (4-bit QLoRA, bfloat16, FlashAttention):
#    !python training/train_sft.py --model unsloth/Qwen3.5-4B --data workspace/build/r1 --out workspace/runs/r1 --load-4bit --epochs 3 --show 0
#
# 3. Export clean branded GGUF models:
#    !python training/export_gguf.py --adapter workspace/runs/r1/adapter --out workspace/exports/kendal-stage-1 --quants q6_k q4_k_m
#
# 4. Train koeberg-stage-1 (27B) on unsloth/Qwen3.8-27B (~5.5 hrs, ~$1.76 credits):
#    !python training/train_sft.py --model unsloth/Qwen3.8-27B --data workspace/build/r1 --out workspace/runs/r1-koeberg --load-4bit --epochs 3"""

    if old_target in text:
        text = text.replace(old_target, new_target, 1)
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Updated {path}")
    else:
        print(f"Target not found in {path}")

update_guide("GUIDE.md")
update_guide("sa-tutor-kit/sa-tutor-kit/GUIDE.md")

