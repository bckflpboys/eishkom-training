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

## Directory Structure

All of your data lives in `workspace/`. Kit code never overwrites an earlier step.

```
sa-tutor-kit/
├── README.md                          # This architecture map and model overview
├── GUIDE.md                           # Step-by-step manual from Phase 0 to Phase 12
├── tutor_spec.md                      # Pedagogical specification and grading rubric
├── tutor_data.py                      # Record schema validator and dataset split builder
├── SOURCES.md                         # South African curriculum source guide and licensing
├── llm.py                             # Unified OpenAI/DeepSeek/Gemini API client with spend cap
├── board.py, answers.py, tools_sim.py # Blackboard parser, math answer checkers, tool stubs
├── retrieval.py                       # Searchable curriculum textbook index
├── wspaths.py                         # Path manager for workspace subdirectories
├── colab/
│   └── sa_tutor_colab.ipynb          # Cloud Colab Enterprise notebook (audition, train, export)
├── pipeline/
│   ├── init_workspace.py             # Creates folder hierarchy and sample configs
│   ├── ingest.py                     # Extracts raw text from DBE/Siyavula PDFs
│   ├── extract_items.py              # Segments text into questions and memos
│   ├── plan.py                       # Generates pedagogical curriculum blueprints
│   ├── generate.py                   # Calls teacher model to write tutoring dialogues
│   ├── verify.py                     # Multi-layer checks (SymPy arithmetic, leak check, judge)
│   ├── review_sample.py              # CLI for human spot-check review
│   ├── merge.py                      # Combines verified rounds into single dataset
│   └── make_vision_records.py        # Converts exam questions into multi-modal vision records
├── eval/
│   ├── make_eval_from_items.py       # Cuts held-out exam questions
│   ├── run_eval.py                   # Executes exam against models
│   ├── score_eval.py                 # Scores answers against memo and policy rubrics
│   ├── report_eval.py                # Generates comparison tables and charts
│   └── analyze_failures.py           # Uses teacher LLM to categorize error patterns
├── training/
│   ├── train_sft.py                  # LoRA / QLoRA training script with Unsloth kernels
│   ├── export_gguf.py                # Multi-quant GGUF exporter (UD-Q4_K_XL, Q6_K, Q4_K_M)
│   ├── make_dpo_pairs.py             # Generates preference pairs from model errors
│   └── vision_prepare.py             # Formats image tokens for multi-modal training
└── workspace/                        # Your private project data (not committed to git)
    ├── raw/                          # Source PDFs
    ├── sources/sources.csv           # Source ledger with license tracking
    ├── eval/eval_items.jsonl         # Held-out examination benchmark
    ├── build/r1/                     # Final train.jsonl, val.jsonl, test.jsonl
    ├── runs/r1/                      # Trained LoRA adapter checkpoints and loss graphs
    └── exports/                      # Exported GGUF files for offline deployment
```

---

## Quick Start: Local PC Setup

Run these commands from inside `sa-tutor-kit/`:

```bash
# 1. Set up Python virtual environment
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS / Linux
pip install -r requirements.txt

# 2. Initialize workspace hierarchy
python pipeline/init_workspace.py

# 3. Validate starter schema
python tutor_data.py validate examples/examples.jsonl --images-root examples
```

The validator should confirm: `Checked 14 records: 0 errors, 0 warnings.`

### Configuring Environment & Sources:
1. Copy `.env.example` to `.env`. Set `TEACHER_API_KEY` (e.g., DeepSeek API key or Google Gemini key via OpenAI-compatible endpoint) and set `MAX_SPEND_USD=15`.
2. Place 3–5 recent DBE past exam papers **with official marking memos** into `workspace/raw/`.
3. Add entries to `workspace/sources/sources.csv` (recording source name, grade, subject, and license).
4. Run `python pipeline/ingest.py` to extract text.
5. Cut held-out exam items **before** generating any training records (`python eval/make_eval_from_items.py`).

---

## Quick Start: Training & Exporting in Colab Enterprise

1. Upload the entire `sa-tutor-kit/` folder (including `workspace/`) to Google Drive.
2. In Google Cloud Console, open **Vertex AI > Colab Enterprise** (or open standard Google Colab).
3. Connect an **NVIDIA L4 GPU** (or T4 GPU) instance.
4. Open `colab/sa_tutor_colab.ipynb`.
5. Run cells 1–4 to verify GPU access, mount Google Drive, install Unsloth, and log in to Hugging Face.
6. **Audition (Cell 5):** Benchmark candidate base models on the starter exam before training.
7. **Train (Cells 6a–6c):**
   - **Koeberg (27B):** Set `MODEL = 'unsloth/Qwen3.8-27B'` -> Train on L4 Spot VM (~5.5 hrs, ~$1.76).
   - **Kendal (4B):** Set `MODEL = 'unsloth/Qwen3.5-4B'` -> Train on L4 Spot VM (~1.0 hr, ~$0.32).
   - **Gariep (2B):** Set `MODEL = 'empero-ai/Qwen3.8-2B-Distill'` -> Train on L4 Spot VM (~35 mins, ~$0.19).
8. **Export (Cell 9):**
   Export multi-quant files with clean Eishkom branding names:
   ```bash
   # Koeberg Flagship Export
   python training/export_gguf.py --adapter workspace/runs/r1-koeberg/adapter \
          --out workspace/exports/koeberg-stage-1 --quants ud-q4_k_xl

   # Kendal Desktop & Flash Mobile Export (from a single 4B training run!)
   python training/export_gguf.py --adapter workspace/runs/r1-kendal/adapter \
          --out workspace/exports/kendal-stage-1 --quants q6_k q4_k_m

   # Gariep Budget Tutor Export
   python training/export_gguf.py --adapter workspace/runs/r1-gariep/adapter \
          --out workspace/exports/gariep-stage-1 --quants q6_k q8_0
   ```

---

## What "Ready to Train" & "Good Enough to Ship" Look Like

### Ready to Train Checklist:
- `workspace/build/r1/train.jsonl` exists with balanced coverage across grades and strategies.
- The dry-run command (`train_sft.py ... --dry-run`) reports `too_long: 0` and `mismatch: 0`.
- Trainable token share is between 10% and 25%.
- The 20-sample overfit smoke test (`train_sft.py ... --limit 20 --epochs 15`) drives loss close to zero.
- A human has reviewed at least 40 generated records (`review_sample.py`) with a bad rate below 10%.

### Good Enough to Ship Checklist:
- Overall held-out exam pass rate ≥ 70%, or at least 85% of the teacher model's score.
- Policy compliance ≥ 90%; language consistency ≥ 95%; tool-calling execution ≥ 90%.
- No individual topic/grade slice drops by more than 3 points from the previous run (no catastrophic forgetting).
- Quantized GGUF files tested on local hardware via `llama-server` and verified on physical phones.

---

## Consultation Archives & Provenance

The design decisions and specifications in this kit were developed across two comprehensive consultations:
- **Claude Consultation:** [`chats/claude-transcript.md`](../../../chats/claude-transcript.md) and [`chats/claude-transcript.html`](../../../chats/claude-transcript.html) (Pedagogical spec, zero-budget local hardware constraints, schema design).
- **Gemini Consultation:** [`chats/gemini-transcript.md`](../../../chats/gemini-transcript.md) and [`chats/Google Cloud & Gen AI Credits Guide.pdf`](../../../chats/Google%20Cloud%20%26%20Gen%20AI%20Credits%20Guide.pdf) (Google Cloud & Gen AI credits utilization, Vertex AI Colab Enterprise, NVIDIA L4 Spot VM pricing, Google Cloud Run scale-to-zero serverless deployment, and the 5-model Eishkom Stage 1 lineup).
- **Consultation Index:** [`chats/README.md`](../../../chats/README.md).
