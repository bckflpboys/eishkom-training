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

---

## Master Milestones at a Glance

- **Phase 0 (Environment Setup):** `90% Complete` — Python 3.12 verified, Colab Enterprise notebook ready, Spot VM configuration loaded, multi-model rotation active.
- **Phase 1 (Data Collection):** `100% Complete` — **600 PDFs downloaded (378.15 MB, 0 errors)** from DBE across Grades 10–12 for Mathematics, Physical Sciences, English, and Afrikaans. All 16 November 2024 Grade 12 papers are locked as held-out evaluation benchmarks in [`sources.csv`](../sa-tutor-kit/sa-tutor-kit/workspace/sources/sources.csv).
- **Phase 2 (Vision Ingestion & Quality Audit):** `100% Complete & Verified` — All 4 curriculum stages vision-extracted into **11,310,442 characters of clean KaTeX LaTeX and Markdown**. Two-pass verification audited all 301 exam pairs (**287 / 301 clean structural passes, 95.3%**; 47,299 equations; 1,005 diagrams; 137 documents sanitized via `pipeline/sanitize_text.py`).
- **Phase 2.5 (Item Extraction):** `100% Complete & Audited` — **265 / 265 exam papers extracted** (100% of real DBE papers in corpus, 3 zero-byte stubs skipped). **13,168 atomic items**, **31,278 marks accounted for** (100% agreement with DBE memorandums), **0 KaTeX delimiter errors** across all items. Quad-mirrored across `workspace/items/<subject>/`, `workspace/items/`, and `sa-tutor-kit/sa-tutor-kit/workspace/items/`.
- **Phase 3 (Benchmark Lock & Quarantine):** `100% Locked` — 33 held-out 2024 Grade 12 benchmark papers strictly quarantined in `workspace/eval/` (0% training contamination).
- **Phase 4 & 5 (Multi-Model Fleet Waves 1 & 2 & SymPy Verification):** `100% Complete` — 14 full DBE exam papers processed across OpenAI (`gpt-6-luna`), OpenRouter (`nemotron-3-ultra-550b`), and Google AI Studio (`gemini-3.8-flash`, `3.6-flash`, `3.5-flash-lite`, `3.1-flash-lite`). Generated over 540 multi-turn Socratic dialogues; verified **429 dialogues** against official memorandums (**80.3% Wave 2 pass rate, 94.1% on OpenAI Luna**). Forensic decimal comma normalization successfully recovered false negatives.
- **Phase 7 (SFT Dataset Packaging):** `1,099 Samples Ready` — 429 verified lessons compiled into canonical `tutor-v1` schema with 0 errors via `tools/package_all_verified_sft.py` and built via `tutor_data.py build` into `workspace/build/r1/` (`train.jsonl`: 882 turns, `val.jsonl`: 156 turns, `test.jsonl`: 61 turns). 100% ready for Vertex AI Colab Enterprise SFT fine-tuning.

---

## Quick Navigation

- **Live Item Extraction Checklist:** [`EXTRACTION_TRACKER.md`](EXTRACTION_TRACKER.md)
- **Detailed Progress & Checklist:** [`PROGRESS.md`](PROGRESS.md)
- **Execution Runbook:** [`GUIDE.md`](GUIDE.md)
- **Model Specs & Distillation Plan:** [`MODELS.md`](MODELS.md)
- **Phase 1 Data Inventory:** [`CORPUS.md`](CORPUS.md)
- **Master Decisions Archive:** [`../sa-tutor-kit/sa-tutor-kit/workspace/DECISIONS.md`](../sa-tutor-kit/sa-tutor-kit/workspace/DECISIONS.md)

