# Eishkom AI — Stage 1 Release Cycle

> **Stage 1 Release Documentation & Architecture Map**  
> South African Curriculum (CAPS) Multilingual AI Tutor Models  
> Release Cycle: **Stage 1** (`koeberg-stage-1`, `kendal-stage-1`, `kendal-flash-stage-1`, `gariep-stage-1`, `gariep-flash-stage-1`)

---

## Overview

The `stage-1/` directory is the master coordination center for **Eishkom AI's Stage 1 release cycle**. It tracks all progress, documentation, architectural specifications, and data artifacts for our initial release of five specialized models.

```
stage-1/
├── PROGRESS.md           # Master progress tracker, phase checklists, and execution logs
├── README.md             # This overview of the Stage 1 release cycle
├── GUIDE.md              # Step-by-step developer manual for Stage 1 execution
├── MODELS.md             # Detailed architectural specifications for all 5 models
├── CORPUS.md             # Inventory and statistics for the 600 Phase 1 downloaded PDFs
└── EXTRACTION_TRACKER.md # Live checklist of item extraction progress across all 301 pairs
```

---

## Stage 1 Model Lineup

All models in this release adhere to our **Clean Branding Rule**: public model names never display parameter numbers (`27B`, `4B`, `2B`) or quantization suffixes (`Q4`, `Q6`).

| Public Release Name | Tier | Base Repo (Hugging Face) | GGUF Quantization | Size | Primary Target |
|---|---|---|---|---|---|
| **`koeberg-stage-1`** | Flagship Cloud | `unsloth/Qwen3.8-27B` | `UD-Q4_K_XL` | ~17.6 GB | Google Cloud Run (Scale-to-zero serverless NVIDIA L4 GPU) & High-RAM PCs |
| **`kendal-stage-1`** | Budget PC & Laptop | `unsloth/Qwen3.5-4B` | `Q6_K` / `UD-Q6_K_XL` | ~3.53–4.15 GB | GTX 1650 (4GB VRAM) desktops & 16GB RAM laptops (100% offline) |
| **`kendal-flash-stage-1`** | Mobile & Phone | `empero-ai/Qwen3.8-4B-Distill` | `Q4_K_M` | ~2.78–2.91 GB | Midrange smartphones (6GB–8GB RAM) & 4GB PCs (100% offline) |
| **`gariep-stage-1`** | Budget Phone Tutor | `empero-ai/Qwen3.8-2B-Distill` | `Q6_K` / `Q8_0` | ~1.75–2.15 GB | Budget smartphones (4GB RAM) & entry laptops (100% offline) |
| **`gariep-flash-stage-1`** | Budget Vision/OCR | `LiquidAI/LFM3-VL-2B` | `Q6_K` | ~1.55 GB | Budget phones for reading geometry diagrams, handwritten work, and OCR |
| **`baby-jake-stage-3`** *(or `atom-stage-3`)* | Ultra-Budget Celeron & Entry Phone | `unsloth/Qwen3.5-1.5B` *(or LFM-1B)* | `Q4_K_M` | ~650–850 MB | Extreme budget Celeron PCs (4GB RAM, 10–14 tokens/sec) & 2GB–3GB phones (100% offline). Stage 3 release via Stage 3 Kendal-4B self-distillation. |

---

## Master Milestones at a Glance

- **Phase 0 (Environment Setup):** `100% Complete` — Python 3.12 verified, Colab Enterprise notebook ready, Spot VM configuration loaded, multi-model rotation active.
- **Phase 1 (Data Collection):** `100% Complete` — **600 PDFs downloaded (378.15 MB, 0 errors)** from DBE across Grades 10–12 for Mathematics, Physical Sciences, English, and Afrikaans. All 16 November 2024 Grade 12 papers are locked as held-out evaluation benchmarks in [`sources.csv`](../sa-tutor-kit/sa-tutor-kit/workspace/sources/sources.csv).
- **Phase 2 (Vision Ingestion & Quality Audit):** `100% Complete & Verified` — All 4 curriculum stages vision-extracted into **11,310,442 characters of clean KaTeX LaTeX and Markdown**. Two-pass verification audited all 301 exam pairs (**287 / 301 clean structural passes, 95.3%**; 47,299 equations; 1,005 diagrams; 137 documents sanitized via `pipeline/sanitize_text.py`).
- **Phase 2.5 (Item Extraction):** `100% Complete & Audited` — **265 / 265 exam papers extracted** (100% of real DBE papers in corpus, 3 zero-byte stubs skipped). **13,168 atomic items**, **31,278 marks accounted for** (100% agreement with DBE memorandums), **0 KaTeX delimiter errors** across all items. Quad-mirrored across `workspace/items/<subject>/`, `workspace/items/`, and `sa-tutor-kit/sa-tutor-kit/workspace/items/`.
- **Phase 3 (Benchmark Lock & Quarantine):** `100% Locked` — 33 held-out 2024 Grade 12 benchmark papers strictly quarantined in `workspace/eval/` (0% training contamination).
- **Phase 4 & 5 (Multi-Model Fleet & Verification):** `100% Active & Scaling` — Wave 1 (176 lessons), Wave 2 (253 lessons), and Wave 3 turbo fleet operating across 10 parallel lanes. Pass rate sustained above 80% with forensic South African decimal comma normalization.
- **Phase 7 (SFT Dataset Packaging):** `100% Complete` — **5,755 Production SFT Samples Compiled** in `workspace/build/r1/` (`tutor-v1` schema) with multi-task 1:2 curriculum ratio and embedded calculator checks.
- **Phase 8 (Kendal Stage 1 4B SFT & Multi-Quant Export):** `100% Verified` — Trained `unsloth/Qwen3.5-4B` for 3 epochs (870 steps, loss down to 0.34). Exported `kendal-stage-1-Q6_K.gguf` (3.4 GB), `kendal-flash-stage-1-Q4_K_M.gguf` (2.65 GB), and pure `kendal-stage-1-Q4_K.gguf`. Synced to Google Cloud Storage.
- **Phase 9 (Gariep Stage 1 2B SFT & Multi-Quant Export):** `100% Complete & Verified` — Trained `empero-ai/Qwen3.8-2B-Distill` for 3 epochs across 5,755 SFT samples. Successfully exported all 4 mandated formats (`Q8_0`, `Q6_K`, pure `Q4_K`, and mobile `Q4_K_M`). Packaged into cloud-ready `.zip` archives.
- **Phase 10 (Application Pipeline & Page-Worker Architecture):** `Architecture Finalized` — Codified the Transient Chunked Page-Worker Pattern (Map-Reduce) decoupling high-res page image digitization from text-based Socratic tutoring.
- **Phase 11 (Vision Model Fine-Tuning Pipeline):** `Ready to Run` — Synthetic ground-truth transcription pipeline using Gemini Flash Multimodal Vision and DBE marking memorandums with Unsloth `FastVisionModel`.
- **Phase 12 (Stage 2 Master SFT Dataset Build):** `100% Complete & Verified` — All 224 exam papers in the Stage 2 dedicated pool completed. **23,503 canonical records** (10,591 multi-turn Socratic lessons + 12,912 full solutions) compiled into **40,241 SFT samples** (~28.5M tokens) in `workspace/build/r2/` with a **99.99% validation pass rate**.
- **Phase 13 (Phase 2.5 Agentic & Study Coaching Expansion):** `Active & Operational` — Expansion into holistic academic coaching and on-device agentic workflows across 9 task families (`intake`, `study_plan`, `weak_topic_diagnosis`, `exam_strategy`, `study_guide_section`, `revision_session`, `paper_walkthrough`, `paper_prep_guide`, `page_worker`, `distress_signal`). Backed by deterministic Python arithmetic (`stage-2/agentic/sampler_agentic.py`) and multi-provider generation fleet (`stage-2/agentic/run_agentic_fleet.py`).
- **Phase 14 (Context Compaction & Stage 2 Pass 2 Fleet):** `Active & Running` — Implemented on-device context compaction engine (`stage-2/agentic/sampler_ops.py`) for low-RAM mobile speed, and launched background Pass 2 fleet generation (`python stage-2/run_stage2_fleet.py --pass 2`) across all 225 exam papers to generate alternate pedagogical strategy lessons into `workspace/verified/stage2_pass2/`.

---

## Native Application Architecture: Transient Page-Worker Pattern

To run smoothly on budget South African hardware (4GB RAM phones, legacy Celeron laptops, and GTX 1650 desktops) without GPU memory exhaustion or attention degradation, the application implements a **Map-Reduce Transient Page-Worker Pattern**:

```
[ Multi-Page PDF / Photos ] 
            │
            ▼ (App slices into 300 DPI PNG screenshots)
[ Page 1 PNG ] ──> [ Transient Vision Worker (gariep-flash 2B) ] ──> [ KaTeX / Markdown Text ]
                                  │
                                  ▼ (Wipe KV Cache & Release VRAM)
[ Page 2 PNG ] ──> [ Transient Vision Worker (gariep-flash 2B) ] ──> [ KaTeX / Markdown Text ]
                                  │
                                  ▼ (Wipe KV Cache & Release VRAM)
            ...
            │ (App stitches transcripts & resolves question continuity)
            ▼
[ Clean Extracted Exam / Homework Text ]
            │
            ▼
[ Central Tutor Agent (kendal-stage-1 4B / gariep-stage-1 2B) ]
(100% Text Socratic Guidance • Fast Token Speed • Zero Vision Overhead • Flat Battery/RAM Footprint)
```

### Key Architectural Principles:
1. **Separation of Concerns:**
   - **The App:** Manages high-resolution page rendering, sequential dispatch, cross-page question continuity, and text stitching.
   - **The Vision Worker (`gariep-flash-stage-1`):** Acts strictly as a **high-fidelity digitizer and transcriber** (extracts printed/handwritten text, KaTeX formulas, and structured diagram descriptions). It does NOT tutor or solve problems.
   - **The Central Tutor (`kendal-stage-1` / `gariep-stage-1`):** Focuses 100% of its reasoning capacity on Socratic pedagogy, hint ladders, and CAPS curriculum alignment.
2. **Zero KV-Cache Bloat:** Processing one page at a time with immediate memory deallocation guarantees that VRAM usage stays flat (~1.5–2GB) regardless of whether an exam is 2 pages or 20 pages.
3. **Custom Architecture Branding:** Supported via custom Hugging Face modeling (`model_type: "eishkom"`, `configuration_eishkom.py`, and `modeling_eishkom.py` with `trust_remote_code=True`) while maintaining optimized C++/CUDA runtime execution in local GGUF engines.

---


- **Pedagogical Strategy & Architectural Roadmap (Stages 1–4):**
  - **Stage 1 (Current):** Employs **subject-adaptive teaching styles** (Polya 4-step for Maths; concept mapping & SI units for Physics; context clues & visual literacy for Languages; frustrated learner de-escalation across all subjects) balanced in a **1:2 Multi-Task Curriculum Ratio** (1 full solution demonstration per 2 Socratic hint dialogues across 5,755 SFT samples).
  - **Stage 2 (v2 Models) — Multi-Strategy Permutations & Cumulative SFT Scaling:**
    - **Production Fleet Pipeline (`stage-2/run_stage2_fleet.py`):** 10-strategy weighted rotation (`step_walkthrough`, `worked_example`, `faded_example`, `error_spotting`, `mnemonic_memory_hook`, `frustrated_learner_de-escalation`, `rapid_recall_drill`, `compare_and_contrast`, `exam_technique_focus`, `concept_first`) paired with 6 student persona states across dual coaching profiles (35% short 2-turn mode, 65% deep Socratic mode).
    - **14-Worker Parallel Fleet:** 8 dedicated OpenAI `gpt-6-luna` workers exclusively focused on STEM (Mathematics & Physical Sciences in English & Afrikaans), alongside 4x Google Gemini workers (`gemini-3.5-flash-lite` & `gemini-3.1-flash-lite` across Key 1 and Key 2) dedicated to Languages, Nemotron Ultra 550B (Maths P2), and Fast DeepSeek (Physical Sciences) targeting 15,000 samples.
    - **Multi-Provider API Expansion (Standby Verification):** Onboarded APInex (13 active models), APMix (2 models), Refuseless (1 model), and Vertex AI (eishkom service account) for agentic and Stage 2 Pass 2 tasks pending user role allocation.
    - **Mandatory Final Turn Consolidation:** Every lesson concludes with a clean final answer, a dedicated `📖 Formula Breakdown (How It Works)` (for STEM) or `📖 Concept & Thought Process (How to Understand It)` (for Languages), and a practical `🎯 Exam Tip`.
    - **10-Point Quality Rubric (`stage-2/quality/rubric_checker.py`):** Automated multi-dimensional scoring catching reasoning omissions, turn count deviations, anti-spoiler violations, and language mismatches before accepting items. All rejections logged to `workspace/rejected/stage2/` for full diagnostic auditing.
    - **Cumulative Dataset Rule:** Fresh base models are trained on combined datasets (`r1` + `r2` = 15,000+ samples) into `workspace/build/r2/` to prevent catastrophic forgetting.
    - **Base Model Adaptability:** If newer models release (e.g. `Qwen3.8-4B`), the compiled dataset plugs in directly with zero data rework.
    - **LoRA Capacity Scaling:** Scale from Rank 16 (0.5% weights) up to Rank 32/64 (1%–2% weights) as data expands to 15k–30k+ samples.
  - **Stage 3 (v3 Models) — Baby Jake (1B) & Cross-Tier Self-Distillation:**
    - Release **`baby-jake-stage-3`** (or `atom-stage-3`), an ultra-lightweight 1B model (~650–850 MB) achieving 10–14 tokens/sec on 4GB Celeron laptops.
    - Train 1B via **self-distillation** using Stage 3 `kendal-4b` and `koeberg-27b` as certified local teachers.
    - The automated SymPy and DBE marking memorandum pipeline validates all math steps ($0.00 API cost).
  - **Stage 4 — Autonomous Cross-Style Expansion:**
    - Use verified Stage 3 local models to generate diverse teaching styles and subject expansions with authentic South African classroom pedagogy.

## Quick Navigation

- **Live Item Extraction Checklist:** [`EXTRACTION_TRACKER.md`](EXTRACTION_TRACKER.md)
- **Detailed Progress & Checklist:** [`PROGRESS.md`](PROGRESS.md)
- **Execution Runbook:** [`GUIDE.md`](GUIDE.md)
- **Model Specs & Distillation Plan:** [`MODELS.md`](MODELS.md)
- **Phase 1 Data Inventory:** [`CORPUS.md`](CORPUS.md)
- **Master Decisions Archive:** [`../sa-tutor-kit/sa-tutor-kit/workspace/DECISIONS.md`](../sa-tutor-kit/sa-tutor-kit/workspace/DECISIONS.md)
