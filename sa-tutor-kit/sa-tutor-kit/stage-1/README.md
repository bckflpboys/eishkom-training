# Eishkom AI — Stage 1 Release Cycle

> **Stage 1 Release Documentation & Architecture Map**  
> South African Curriculum (CAPS) Multilingual AI Tutor Models  
> Release Cycle: **Stage 1** (`koeberg-stage-1`, `kendal-stage-1`, `kendal-flash-stage-1`, `gariep-stage-1`, `gariep-flash-stage-1`)

---

## Overview

The `stage-1/` directory is the master coordination center for **Eishkom AI's Stage 1 release cycle**. It tracks all progress, documentation, architectural specifications, and data artifacts for our initial release of five specialized models.

```
stage-1/
├── PROGRESS.md       # Master progress tracker, phase checklists, and execution logs
├── README.md         # This overview of the Stage 1 release cycle
├── GUIDE.md          # Step-by-step developer manual for Stage 1 execution
├── MODELS.md         # Detailed architectural specifications for all 5 models
└── CORPUS.md         # Inventory and statistics for the 600 Phase 1 downloaded PDFs
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
- **Phase 1 (Data Collection):** `100% Complete` — **600 PDFs downloaded (378.15 MB, 0 errors)** from DBE across Grades 10–12 for Mathematics, Physical Sciences, English, and Afrikaans. All 16 November 2024 Grade 12 papers are locked as held-out evaluation benchmarks in [`sources.csv`](../workspace/sources/sources.csv).
- **Phase 2 (Vision Ingestion Upgrade):** `100% Complete` — All 4 curriculum stages (Mathematics/Wiskunde, English HL/FAL, Afrikaans HT/EAT, Physical Sciences/Fisiese Wetenskappe) vision-extracted into **11,310,442 characters of clean KaTeX LaTeX and Markdown**, 354 LaTeX documents, and 1,005 geometric diagram notes with 0 DBE loss.
- **Phase 2.5 (Item Extraction) & Phase 3 (Benchmark Lock):** `Ready to Execute` — Slicing into atomic tutoring items and locking the 16 held-out November 2024 exam papers.

---

## Quick Navigation

- **Detailed Progress & Checklist:** [`PROGRESS.md`](PROGRESS.md)
- **Execution Runbook:** [`GUIDE.md`](GUIDE.md)
- **Model Specs & Distillation Plan:** [`MODELS.md`](MODELS.md)
- **Phase 1 Data Inventory:** [`CORPUS.md`](CORPUS.md)
- **Master Decisions Archive:** [`../workspace/DECISIONS.md`](../workspace/DECISIONS.md)

