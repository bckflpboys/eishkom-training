import os

def update_guide(path):
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    addition = """

### Step 8: Multi-Stage Scaling & Evolution Architecture (Stages 2, 3 & 4)

#### 1. Stage 2 (v2 Models) — Cumulative Dataset Scaling & Base Model Adaptability:
- **Cumulative Dataset Rule:** Never train on only the new data! Combine Round 1 + Round 2 into `workspace/build/r2/` (5,755 + 10,000 = 15,755 total samples) to prevent catastrophic forgetting.
- **LoRA Capacity Scaling:** Scale from `--rank 16` (0.47% weights) up to `--rank 32` or `--rank 64` (1%–2% weights) to give the neural network sufficient capacity for the 15,000+ multi-style lessons.
- **Base Model Upgradability:** The dataset is vendor-neutral intellectual property (conforming to `tutor-v1` schema). If Alibaba releases `Qwen3.8-4B` or Google releases `Gemma 3`, simply point `train_sft.py` to the new base model to instantly upgrade Kendal with zero dataset rework.

#### 2. Stage 3 (v3 Models) — Baby Jake (1B) & Cross-Tier Self-Distillation:
- **The Ultra-Budget Challenge:** On legacy dual-core Celeron PCs with 4GB RAM, 2B models run at ~4 tokens/second.
- **The Solution:** Release **`baby-jake-stage-3`** (or `atom-stage-3`):
  - **Parameter Class:** 1B (e.g. `unsloth/Qwen3.5-1.5B` or `LFM-1B`).
  - **Export Size:** `Q4_K_M` (~650–850 MB) requiring only ~1.2 GB RAM.
  - **Speed:** Delivers **10 to 14 tokens/second** on budget Celeron CPUs (2.5x–3x faster!).
- **Self-Distillation Protocol:**
  - In Stage 3, our fine-tuned `kendal-4b` and `koeberg-27b` become the certified local teachers.
  - They generate training lessons locally on PC ($0.00 API cost).
  - The automated SymPy arithmetic engine and DBE marking memorandums verify all calculations before accepting into 1B training sets.

#### 3. Stage 4 — Autonomous Cross-Style Expansion:
- Uses verified Stage 3 local models to generate diverse teaching styles across additional grades and technical subjects with authentic South African classroom pedagogy."""

    needle = "### Step 7: SFT Training in Vertex AI Colab Enterprise"
    if needle in content and "baby-jake-stage-3" not in content:
        # Append after the Colab Enterprise section or at the end
        content += addition
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {path}")
    else:
        print(f"Skipped {path}")

update_guide("GUIDE.md")
update_guide("sa-tutor-kit/sa-tutor-kit/GUIDE.md")

