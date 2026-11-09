import os

def update_readme(path):
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    old_row = "| **`gariep-flash-stage-1`** | Budget Vision/OCR | `LiquidAI/LFM3-VL-2B` | `Q6_K` | ~1.55 GB | Budget phones for reading geometry diagrams, handwritten work, and OCR |"
    new_rows = (
        "| **`gariep-flash-stage-1`** | Budget Vision/OCR | `LiquidAI/LFM3-VL-2B` | `Q6_K` | ~1.55 GB | Budget phones for reading geometry diagrams, handwritten work, and OCR |\n"
        "| **`baby-jake-stage-3`** *(or `atom-stage-3`)* | Ultra-Budget Celeron & Entry Phone | `unsloth/Qwen3.5-1.5B` *(or LFM-1B)* | `Q4_K_M` | ~650–850 MB | Extreme budget Celeron PCs (4GB RAM, 10–14 tokens/sec) & 2GB–3GB phones (100% offline). Stage 3 release via Stage 3 Kendal-4B self-distillation. |"
    )

    if old_row in content and "baby-jake" not in content:
        content = content.replace(old_row, new_rows, 1)

    old_roadmap = """- **Pedagogical Strategy & Stage 2 (v2) Roadmap:**
  - **Stage 1 (Current):** Employs **subject-adaptive teaching styles** (Polya 4-step & substitution check for Maths; concept mapping & SI units for Physics; context clues & visual literacy for Languages; frustrated learner de-escalation & mnemonics across all subjects) balanced in a **1:2 Multi-Task Curriculum Ratio** (1 full solution demonstration per 2 Socratic hint dialogues).
  - **Stage 2 (v2 Models):** Will execute the **Strategy Permutation Architecture**: retraining on the **exact same 265 question papers** across systematically rotated teaching styles (`worked_example`, `mnemonic_memory_hook`, `faded_example`, `frustrated_learner_recovery`, `rapid_short_prompt`). This scales the corpus 4x–5x (10,000+ samples) completely organically from verified DBE past papers."""

    new_roadmap = """- **Pedagogical Strategy & Architectural Roadmap (Stages 1–4):**
  - **Stage 1 (Current):** Employs **subject-adaptive teaching styles** (Polya 4-step for Maths; concept mapping & SI units for Physics; context clues & visual literacy for Languages; frustrated learner de-escalation across all subjects) balanced in a **1:2 Multi-Task Curriculum Ratio** (1 full solution demonstration per 2 Socratic hint dialogues across 5,755 SFT samples).
  - **Stage 2 (v2 Models) — Strategy Permutations & Cumulative SFT Scaling:**
    - **Cumulative Dataset Rule:** Retrain on combined datasets (`r1` + `r2` = 15,000+ samples) to prevent catastrophic forgetting.
    - **Base Model Adaptability:** If newer models release (e.g. `Qwen3.8-4B`), the compiled dataset plugs in directly with zero data rework.
    - **LoRA Capacity Scaling:** Scale from Rank 16 (0.5% weights) up to Rank 32/64 (1%–2% weights) as data expands to 15k–30k+ samples.
  - **Stage 3 (v3 Models) — Baby Jake (1B) & Cross-Tier Self-Distillation:**
    - Release **`baby-jake-stage-3`** (or `atom-stage-3`), an ultra-lightweight 1B model (~650–850 MB) achieving 10–14 tokens/sec on 4GB Celeron laptops.
    - Train 1B via **self-distillation** using Stage 3 `kendal-4b` and `koeberg-27b` as certified local teachers.
    - The automated SymPy and DBE marking memorandum pipeline validates all math steps ($0.00 API cost).
  - **Stage 4 — Autonomous Cross-Style Expansion:**
    - Use verified Stage 3 local models to generate diverse teaching styles and subject expansions with authentic South African classroom pedagogy."""

    if old_roadmap in content:
        content = content.replace(old_roadmap, new_roadmap, 1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {path}")

for p in ["README.md", "stage-1/README.md", "sa-tutor-kit/sa-tutor-kit/README.md", "sa-tutor-kit/sa-tutor-kit/stage-1/README.md"]:
    update_readme(p)

