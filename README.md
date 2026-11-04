# Eishkom Stage 1 — SA Tutor Kit

A complete, production-ready pipeline for fine-tuning, evaluating, exporting, and deploying **Eishkom Stage 1**, a South African CAPS-aligned educational model family for Grades 7–12 (Mathematics, Mathematical Literacy, Natural Sciences, Physical Sciences, Life Sciences, English, and Afrikaans).

This `README.md` is the architectural map. [`GUIDE.md`](GUIDE.md) is the full operational manual: every phase has a goal, exact commands, verification checks, and fixes.

---

## Eishkom Stage 1 — Finalized 5-Model Lineup & Release Naming

Eishkom AI models follow a **Stage-based release cycle** (`stage-1`, `stage-1.1`, `stage-2`, etc.) rather than point versions (like 3.5 or 5.0). 

### Clean Branding Rule
Public release model names **must not** display parameter counts or quantization identifiers (`27B`, `4B`, `Q4`, `Q6`) in their primary titles. This ensures the public brand feels clean, professional, and accessible. Technical specifications are documented in model cards and metadata.

| Public Release Name | Internal Tier | Trainable Base Repo (Hugging Face) | GGUF Reference / Export Quant | Final File Size | Target Hardware & Deployment |
|---|---|---|---|---|---|
| **`koeberg-stage-1`** | Flagship Cloud (27B) | `unsloth/Qwen3.8-27B` | `UD-Q4_K_XL` (`unsloth/Qwen3.8-27B-GGUF`) | ~17.6 GB | **Cloud:** Google Cloud Run (Serverless NVIDIA L4 24GB, scale-to-zero)<br>**Local:** 16GB/20GB RAM PCs (CPU offload) |
| **`kendal-stage-1`** | Budget PC & Laptop (4B Q6) | `unsloth/Qwen3.5-4B` | `Q6_K` or `UD-Q6_K_XL` (`unsloth/Qwen3.5-4B-GGUF`) | ~3.53–4.15 GB | **Local:** GTX 1650 (4GB VRAM) desktops & 16GB/20GB RAM laptops (100% offline) |
| **`kendal-flash-stage-1`** | Mobile & Phone (4B Q4) | `empero-ai/Qwen3.8-4B-Distill` *(or unsloth 4B)* | `Q4_K_M` (`empero-ai/Qwen3.8-4B-Distill-GGUF`) | ~2.78–2.91 GB | **Local:** Midrange smartphones (6GB–8GB RAM) & 4GB PCs (100% offline) |
| **`gariep-stage-1`** | Budget Phone Tutor (2B Q6) | `empero-ai/Qwen3.8-2B-Distill` *(or unsloth 2B)* | `Q6_K` or `Q8_0` (`empero-ai/Qwen3.8-2B-Distill-GGUF`) | ~1.75–2.15 GB | **Local:** Budget smartphones (4GB RAM) & low-spec PCs (100% offline) |
| **`gariep-flash-stage-1`** | Budget Vision/OCR (2B LiquidAI) | `LiquidAI/LFM3-VL-2B` | `Q6_K` (`LiquidAI/LFM3-VL-2B-GGUF`) | ~1.55 GB | **Local:** Budget phones for high-speed document, diagram, and OCR reading |

### Critical Training Rule: Base Models vs. GGUF Files
- **Never pass a `-GGUF` repository or file into `train_sft.py`.** GGUF files are compiled, read-only inference files intended solely for `llama.cpp`, Ollama, LM Studio, and mobile runners like PocketPal AI. They cannot be trained directly.
- **Always train on the unquantized Transformers base repository** (`unsloth/Qwen3.8-27B`, `unsloth/Qwen3.5-4B`, `empero-ai/Qwen3.8-4B-Distill`, `empero-ai/Qwen3.8-2B-Distill`, `LiquidAI/LFM3-VL-2B`) using Unsloth QLoRA (4-bit base weights + 16-bit trainable adapters).
- **Export to GGUF at the very end:** After training completes in Colab, Unsloth compiles and quantizes the merged model into GGUF in 2 to 4 minutes (`save_pretrained_gguf`).
- **Unsloth Dynamic (UD) & XL:** Unsloth Dynamic 2.0 (`UD`) keeps sensitive attention and vision layers at higher precision while compressing standard feed-forward layers. The `XL` variant allocates ~0.2 GB of extra precision to critical math and grammar layers.

---

## What You Are Building

An integrated family of 5 South African CAPS tutor models that:

- Teach CAPS Mathematics, Sciences, English, and Afrikaans for Grades 7–12 (and foundational Primary School concepts);
- Ask one question at a time, diagnose misunderstandings, and hint before revealing answers;
- Answer in the learner's language (English or Afrikaans), with bilingual support for Afrikaans FAL;
- Use external tools including a calculator, curriculum search, and a command-driven drawing board;
- Handle multi-modal vision: read exam photos, diagrams, and worksheets with native early-fusion vision;
- Run offline on consumer devices (phones, laptops, GTX 1650 PCs) and scale serverless in the cloud for complex Matric exam queries.

The training methodology is **QLoRA Supervised Fine-Tuning (SFT) on verified teacher-written conversations**, followed by DPO (Direct Preference Optimization) to eliminate undesirable habits (such as answer leaking or language drift), and optional GRPO for math verification. Curriculum facts live in a searchable retrieval index; the models learn *how to teach*.

---

## The End-to-End Workflow

```
PC (Local / No GPU Needed)          Google Drive              Vertex AI Colab Enterprise (L4 GPU / Spot)
-------------------------          ------------              -----------------------------------------
1. PDFs -> text -> items           sa-tutor-kit/      --->   1. Load Base Model (Koeberg / Kendal / Gariep)
2. Build held-out exam (first!)    + workspace/              2. Train 4-bit QLoRA (Unsloth Triton kernels)
3. Generate teacher conversations                            3. Evaluate on CAPS exam & diagnose
4. Verify (SymPy/Language/Judge)                             4. Multi-quant export to GGUF (UD-Q4, Q6_K, Q4_K_M)
5. Review sample (<10% bad)                                  5. Save .gguf + adapter back to Drive
6. Build train/val/test splits   ------------------------>                   |
                                                                             |
                                                 +---------------------------+---------------------------+
                                                 |                                                       |
                                                 v                                                       v
                                      Google Cloud Run (Serverless)                           Local Devices (100% Offline)
                                      ----------------------------                           ----------------------------
                                      • Deploy koeberg-stage-1 (UD-Q4_K_XL)                  • kendal-stage-1 (Q6_K) on GTX 1650 & Laptops
                                      • Scale-to-zero instances ($0/hr idle)                 • kendal-flash-stage-1 (Q4_K_M) on Midrange Phones
                                      • Active chat: ~$0.015/min                             • gariep-stage-1 (Q6_K) on Budget Phones
                                      • Covered by $60 Cloud Credits                         • gariep-flash-stage-1 (Q6_K) on Budget OCR Phones
```

Two foundational rules govern the pipeline:
1. **The exam comes first.** Build `workspace/eval/eval_items.jsonl` before generating training data, and never train on it.
2. **The teacher writes, code checks, a human reads.** An open-weight teacher model (DeepSeek V4.1 Flash 1017 under MIT license or Gemini Flash) writes dialogues; automated validators, SymPy arithmetic checkers, and an independent judge grade them; you read a 40-record sample before training.

---

## Google Cloud Credits, Colab Enterprise & Cloud Run

You do not need to burn out your local PC or spend thousands of rands on training compute. Your Google AI Pro membership includes **\$10 monthly Gen AI & Cloud credits** (stacking up to **\$60** over a 12-month rolling window).

### 1. Vertex AI Colab Enterprise vs. Free Colab
- **Free Google Colab ($0):** Provides a standard NVIDIA T4 (15GB usable VRAM) with random session disconnects after 4–6 hours. Suitable for 1-epoch dry runs on sub-14B models.
- **Vertex AI Colab Enterprise (Covered by Cloud Credits):** Connects directly to your Google Cloud Billing account (`console.cloud.google.com/vertex-ai/colab/notebooks`). You choose dedicated hardware:
  - **NVIDIA L4 (24GB VRAM):** The recommended workhorse for Eishkom Stage 1. Fits Qwen3.8-27B in 4-bit QLoRA (~21.5 GB VRAM used).
  - **Spot VM Pricing (~65–70% Off):** An L4 Spot VM costs only **~$0.32/hour** (compared to $0.95/hr standard).
  - **Training Cost:**
    - `koeberg-stage-1` (27B, 3 epochs): ~5.5 hours = **~$1.76**
    - `kendal-stage-1` (4B, 3 epochs): ~1.0 hour = **~$0.32**
    - `gariep-stage-1` (2B, 3 epochs): ~35 mins = **~$0.19**
    - **Total credit spend to train all Stage 1 models is under $10!**

> [!IMPORTANT]
> **Pre-Flight GPU Quota Step:** New Google Cloud projects default GPU quotas to 0. Before launching an L4 notebook in Colab Enterprise:
> 1. Go to **Google Cloud Console > IAM & Admin > Quotas & System Limits**.
> 2. Filter for **NVIDIA L4 GPUs** (and Preemptible NVIDIA L4 GPUs if using Spot VMs) in your target region (e.g. `us-central1` or `europe-west4`).
> 3. Click **Edit Quotas** and request a limit of **1**. Approval is automated within minutes on active billing accounts.

### 2. Hosting `koeberg-stage-1` on Cloud Run (Scale-to-Zero)
Hosting a 27B model 24/7 on a dedicated Compute Engine VM or Vertex AI Prediction Endpoint costs ~$22.80/day ($684/month), which would deplete your \$60 credit balance in under 3 days.

**The Solution:** Deploy `koeberg-stage-1` (`UD-Q4_K_XL`, ~17.6 GB) to **Google Cloud Run with Serverless NVIDIA L4 GPU**:
- Cloud Run scales down to **zero instances** when no students are querying ($0.00/hour).
- When a student asks a complex question, Cloud Run boots the container in seconds, streams the response, and spins down after 1–5 minutes of inactivity.
- Billing is purely per second of active execution (~$0.015/minute), allowing your \$60 promotional credits to cover months of hosting.

---

## Cross-Tier Knowledge Distillation

To make `kendal-stage-1` (4B) and `gariep-stage-1` (2B) think with the depth of a flagship model:
1. Train `koeberg-stage-1` (27B) first on your curated South African curriculum dataset.
2. Have fine-tuned Koeberg generate 2,000 to 5,000 step-by-step teacher explanations for the hardest Grade 11–12 Mathematics Paper 2 (geometry/trig), Physical Sciences (Newton's laws/electrodynamics), and Afrikaans grammatical nuance.
3. Automatically verify Koeberg's answers against the official DBE memorandums using `pipeline/verify.py`.
4. Inject these verified explanations into `workspace/build/r1/train.jsonl` before fine-tuning Kendal (4B) and Gariep (2B).
This transfers 27B-level pedagogical reasoning directly into your 4B and 2B models for under \$1.00 in extra training compute.

---

## Phase 1 Automated Downloader (`pipeline/download_dbe.py`)

To streamline data collection from the Department of Basic Education without manual clicking:
```bash
# Preview what will be collected across all subjects & sessions:
python pipeline/download_dbe.py --dry-run

# Run the automated crawler to download PDFs and update sources ledger:
python pipeline/download_dbe.py
```
- **Language & Subject Partitioning:** Exam papers and memorandums are downloaded into isolated folders under `workspace/raw/dbe/<language>/<subject>/<year>/`.
- **Bidirectional Ledger:** Auto-populates `workspace/sources/sources.csv` with paired question paper and memorandum references (`pair_with`).
- **Benchmark Protection:** Automatically flags November 2024 Grade 12 NSC papers with `held out for EVAL (do not train on it)` to prevent training contamination.

---

## Phase 2 Text Ingestion & Extraction Strategy

All 600 PDFs were ingested into plain text in `workspace/text/` using `pipeline/ingest.py --skip-existing`:
- **Audited Scale:** **600 text files**, **14,959,351 characters total**, 0 errors.
- **Auto-DOCX Conversion:** Magic byte detection routed 4 misnamed DOCX papers to `read_docx()`.
- **Mathematical Equations:** Standardized into LaTeX inside `$..$` (inline) and `$$..$$` (display block) for rendering via KaTeX.
- **Text-Describable Diagrams (~20%):** Euclidean geometry (circles, parallel lines, tangents), circuits, and coordinate graphs are written out in the `"passage"` field so language models receive complete spatial context.
- **Pure Visual Diagrams (~10%):** Flagged `"needs_review": true`, excluded from text SFT, rendered to PNG images in `workspace/images/` for multimodal vision training on `LiquidAI/LFM3-VL-2B` (`gariep-flash-stage-1`).
- **Memo-First Question Recovery:** Mathematics question papers with rasterized formulas have their question text and marking rubrics extracted directly from the paired DBE memorandum (1.38M characters of memo text across math papers).


---

## Directory Structure

All of your data lives in `sa-tutor-kit/sa-tutor-kit/workspace/`. Kit code never overwrites an earlier step.

```
files/
├── PROGRESS.md                          # Master progress tracker, checklists, and compute ledger
├── README.md                            # High-level architecture map and model overview
├── GUIDE.md                             # Step-by-step manual from Phase 0 to Phase 12
├── SOURCES.md                           # South African curriculum source guide and licensing
├── stage-1/                             # Dedicated Stage 1 release cycle hub
│   ├── PROGRESS.md                      # Detailed Stage 1 roadmap and verification logs
│   ├── README.md                        # Stage 1 model overview and release philosophy
│   ├── GUIDE.md                         # Quick reference developer execution runbook
│   ├── MODELS.md                        # Architectural specs for all 5 Stage 1 models
│   └── CORPUS.md                        # Inventory of 600 Phase 1 downloaded PDFs (378 MB)
└── sa-tutor-kit/sa-tutor-kit/           # Complete training, evaluation, and pipeline codebase
    ├── stage-1/                         # Synchronized Stage 1 documentation mirror
    ├── pipeline/                        # Data download, ingestion, and extraction tools
    ├── training/                        # Unsloth fine-tuning and GGUF export tools
    ├── colab/                           # Vertex AI Colab Enterprise notebook (L4 Spot VM)
    └── workspace/                       # User data directory (raw PDFs, text, items, models)
```

---

## Consultation Archives & Provenance

The design decisions and specifications in this kit were developed across two comprehensive consultations:
- **Claude Consultation:** [`../chats/claude-transcript.md`](../chats/claude-transcript.md) and [`../chats/claude-transcript.html`](../chats/claude-transcript.html) (Pedagogical spec, zero-budget local hardware constraints, schema design).
- **Gemini Consultation:** [`../chats/gemini-transcript.md`](../chats/gemini-transcript.md) and [`../chats/Google Cloud & Gen AI Credits Guide.pdf`](../chats/Google%20Cloud%20%26%20Gen%20AI%20Credits%20Guide.pdf) (Google Cloud & Gen AI credits utilization, Vertex AI Colab Enterprise, NVIDIA L4 Spot VM pricing, Google Cloud Run scale-to-zero serverless deployment, and the 5-model Eishkom Stage 1 lineup).
- **Consultation Index:** [`../chats/README.md`](../chats/README.md).

