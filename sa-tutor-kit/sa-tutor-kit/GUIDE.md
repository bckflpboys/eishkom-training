# GUIDE: Building the Eishkom Stage 1 South African Tutor Family

> [!NOTE]
> **Stage 1 Hub & Progress Tracker:** Live progress, phase checklists, Phase 1 verified corpus statistics (600 PDFs / 378 MB), and model architectures are tracked in [`PROGRESS.md`](PROGRESS.md) and the dedicated [`stage-1/`](stage-1/) release directory.

Follow this top to bottom. Every phase has the same structure:

- **Goal** what you will have at the end
- **Do** the exact steps and commands
- **Check** how you know it worked
- **Why** the reason, so you can change it when you disagree
- **If it goes wrong** the usual fixes

Costs and times are grounded in the **Google Cloud & Gen AI Credits Guide** and empirical Unsloth benchmarks on NVIDIA L4 GPUs.

---

## Eishkom Stage 1 — Finalized 5-Model Lineup

Eishkom AI follows a **Stage-based release cycle** (`stage-1`, `stage-1.1`, `stage-2`, etc.) rather than point versions.

### The Clean Branding Rule
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

## How to Read This Guide

**Two places things run:**
- **Your PC** (or any computer, no GPU needed): collecting curriculum data, extracting questions, running SymPy checks, generating training dialogues via teacher APIs, and human spot-checks. Commands look like `python pipeline/plan.py ...`. Run them from the kit folder.
- **Vertex AI Colab Enterprise** (funded by your **\$60 Google Cloud credits**): training with dedicated NVIDIA L4 GPUs (24GB VRAM) on Spot VMs (~$0.32/hr), evaluating checkpoints, and exporting multi-quant GGUF files. Use `colab/sa_tutor_colab.ipynb`.

**Folders.** The kit folder holds the code. A `workspace/` folder inside it (created in phase 0) holds YOUR data. Scripts never overwrite earlier steps: each step reads one folder and writes the next, so you can always walk backwards to find where a problem came from.

**The files you will meet** (all in the kit folder):

| File | What it is |
|---|---|
| `tutor_spec.md` | The written spec of how the tutor teaches. The teacher model reads it; the judge uses its rubric |
| `SOURCES.md` | Where to get data, and what each licence allows |
| `tutor_data.py` | The record format (schema), the checker, the report and the builder |
| `board.py`, `answers.py`, `tools_sim.py`, `retrieval.py`, `llm.py` | Helpers: blackboard parser, math answer checking, tool results, curriculum search, API client |
| `pipeline/` | Steps that make training data |
| `eval/` | Steps that test a model on held-out DBE exam items |
| `training/` | Steps that train, improve and export a model |
| `examples/examples.jsonl` | 14 example records showing every feature. READ THESE FIRST |

**Rules that save you money and tears:**
1. Always do a tiny test (10 records, 20 questions) before a big run.
2. After every step that makes data, **read some of it**. Numbers do not show "this explanation is confusing".
3. Never train on your exam. Never change the exam to make a score look better.
4. Change one thing at a time, then run the exam.
5. Keep `MAX_SPEND_USD` in `.env` low. Every API call is logged: `python llm.py spend`.

---

## The Big Picture

```
 sources ──► text ──► items ───────────────────────┐
 (PDFs)     (ingest)  (questions + memos)          │
                         │                         │
                         ▼                         ▼
                      PLAN ──► TEACHER writes ──► VERIFY ──► REVIEW ──► BUILD ──► TRAIN (Colab Enterprise L4)
                  (what to       training records   (code checks,  (a human     (train/val   │
                   write)        (DeepSeek/Gemini)  judge model)   reads some)  files)       ▼
                                                                                          your model
   EXAM (held-out, never trained on) ◄───────────────── EVALUATE ◄───────────────────────────┘
        │                                                  │
        └──► scores, charts, failure analysis ─────────────┘
                         │
                         ▼
        fix the DATA (not the exam) ──► build again ──► train again ──► repeat until move-on rules pass
```

Three foundational principles:
1. **The teacher writes, code checks.** A frontier teacher model (DeepSeek V4.1 Flash 1017 under MIT license or Gemini Flash) writes tutoring conversations. Code verifies the maths, formatting, language, and answer policy. A human reads a sample. Your model only trains on verified records.
2. **The exam comes first.** You decide what "good" means (the held-out DBE exam) BEFORE generating training data.
3. **Skills in the weights, facts in the library.** Training teaches the model HOW to teach, answer in the right language, and call tools. CAPS curriculum facts stay in a searchable library (`retrieval.py`).

---

## Words You Need

| Word | Plain meaning |
|---|---|
| **Base model** | The pre-built brain you start from (e.g. `unsloth/Qwen3.8-27B`, `unsloth/Qwen3.5-4B`, `empero-ai/Qwen3.8-4B-Distill`). You never train from scratch |
| **Parameters / weights** | The billions of numbers inside the model. "4B" = 4 billion numbers. "27B" = 27 billion |
| **LoRA / adapter** | We freeze all base weights and train tiny adapter matrices (1–2% of parameter count). Cheap, small file (~100–300 MB), prevents catastrophic forgetting |
| **QLoRA** | Quantized LoRA: base weights are loaded in 4-bit NormalFloat (NF4), reducing VRAM by ~70% during training |
| **Epoch** | One full pass over all training examples. 2–3 epochs is the sweet spot; 5+ causes robotic memorization |
| **Eval / exam** | Held-out real past exam questions the model never saw during training |
| **Distillation** | Using a big Teacher (27B Koeberg or 552B DeepSeek) to generate step-by-step reasoning that a smaller Student (4B Kendal or 2B Gariep) trains on |
| **Quantization (Q6, Q4, UD)** | Compressing weights to 6 or 4 bits per parameter at export time. Unsloth Dynamic (`UD`) protects attention and vision layers |
| **Scale-to-Zero** | Cloud hosting (Google Cloud Run) where instances turn off ($0.00/hr) when idle and boot on demand for requests (~$0.015/min) |

---

## Phase 0: Set Up (about 1 hour)

**Goal:** the kit runs on your computer, the workspace exists, your API keys and Google Cloud credits are connected.

**Do**
1. Install **Python 3.10 or newer** (python.org). Check: `python --version`.
2. Open a terminal in the kit folder.
3. Create a private Python virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate            # Windows
   # source .venv/bin/activate       # Mac/Linux
   pip install -r requirements.txt
   ```
4. Create the workspace hierarchy:
   ```bash
   python pipeline/init_workspace.py
   ```
5. **Google Cloud Billing & Credits Setup:**
   - Go to Google Developer Program Benefits and ensure your **\$10 monthly credits** are applied to your billing account (up to **\$60 total balance**).
   - In Google Cloud Console, ensure your active project is linked to `My Billing Account`.
   - **Request GPU Quota:** Go to **IAM & Admin > Quotas & System Limits**. Filter for `NVIDIA L4 GPUs` (and `Preemptible NVIDIA L4 GPUs`) in region `us-central1` or `europe-west4`. Submit a quota increase request to **1**. Approval is automated on credit-backed accounts.
6. **Teacher API Setup:**
   - Open `.env` (in the kit folder).
   - Fill in `TEACHER_API_KEY` (e.g. DeepSeek API key or Google Vertex AI Gemini API).
   - Set `MAX_SPEND_USD=15`.
7. Fill in decisions in `workspace/DECISIONS.md` using the Eishkom Stage 1 table above.

**Check** (each should print a success line or "ALL OK", no errors):
```bash
python answers.py
python board.py
python tools_sim.py
python retrieval.py test
python llm.py test
python tutor_data.py validate examples/examples.jsonl --images-root examples
```

---

## Phase 1: Collect Sources (a weekend)

**Goal:** Genuine South African curriculum exam papers and marking guidelines downloaded into structured folders under `workspace/raw/dbe/<language>/<subject>/<year>/`, and recorded in `workspace/sources/sources.csv`.

**Automated Downloader (`pipeline/download_dbe.py`):**
Run the automated DBE crawler to collect all Grade 10–12 past papers and official memorandums:
```bash
# Preview what will be downloaded
python pipeline/download_dbe.py --dry-run

# Run full automated download for all sessions & subjects
python pipeline/download_dbe.py
```

**Directory Organization:**
Downloads are automatically sorted into clean, isolated language and subject hierarchies:
- **English Papers & Memos:**
  - `workspace/raw/dbe/english/mathematics/<year>/` (`mathematics_g12_<year>_<session>_p1.pdf`, `_p1_memo.pdf`, `_p2.pdf`, `_p2_memo.pdf`)
  - `workspace/raw/dbe/english/physical_sciences/<year>/` (`physical_sciences_g12_<year>_<session>_p1.pdf`, `_p1_memo.pdf`, etc.)
  - `workspace/raw/dbe/english/english_hl/<year>/` (`english_hl_g12_<year>_<session>_p1.pdf`, `_p1_memo.pdf`, etc.)
  - `workspace/raw/dbe/english/english_fal/<year>/` (`english_fal_g12_<year>_<session>_p1.pdf`, `_p1_memo.pdf`, etc.)
- **Afrikaans Papers & Memos:**
  - `workspace/raw/dbe/afrikaans/wiskunde/<year>/` (`wiskunde_g12_<year>_<session>_v1.pdf`, `_v1_memo.pdf`, `_v2.pdf`, `_v2_memo.pdf`)
  - `workspace/raw/dbe/afrikaans/fisiese_wetenskappe/<year>/` (`fisiese_wetenskappe_g12_<year>_<session>_v1.pdf`, `_v1_memo.pdf`, etc.)
  - `workspace/raw/dbe/afrikaans/afrikaans_hl/<year>/` (`afrikaans_hl_g12_<year>_<session>_v1.pdf`, `_v1_memo.pdf`, etc.)
  - `workspace/raw/dbe/afrikaans/afrikaans_fal/<year>/` (`afrikaans_fal_g12_<year>_<session>_v1.pdf`, `_v1_memo.pdf`, etc.)
- **Grade 10 & 11 Common Papers:**
  - Stored in the same subject trees with `_g10_` and `_g11_` markers (e.g. `workspace/raw/dbe/english/mathematics/2018/mathematics_g11_2018_nov_p1.pdf`).
- **Sources Ledger:**
  - `workspace/sources/sources.csv` is automatically appended with all metadata, linking each question paper to its memorandum via `pair_with`.
  - November 2024 Grade 12 NSC papers are flagged as `held out for EVAL (do not train on it)`.

> [!TIP]
> **Phase 1 Verified Corpus:** 600 PDFs (300 pairs, 378.15 MB total) downloaded cleanly across English (304 files) and Afrikaans (296 files) covering Grades 10–12 (2015–2025). All 16 Grade 12 November 2024 past papers are locked as held-out evaluation benchmarks in `workspace/sources/sources.csv`.

**Where to get additional legal material:**
1. **Department of Basic Education (DBE):** `education.gov.za` — Free NSC (Matric) and GET/Senior Phase past exam papers with official marking memorandums for Mathematics, Physical Sciences, English, and Afrikaans.
2. **Siyavula Open Textbooks:** `siyavula.com` — Creative Commons (CC-BY) textbooks for Mathematics (Grades 7–12), Physical Sciences (Grades 10–12), and Natural Sciences (Grades 4–9).
3. **WCED ePortal:** `wcedeportal.co.za` — CAPS revision booklets, Afrikaans begripstoetse, and grammar guides.
4. **African Storybook:** `africanstorybook.org` — Bilingual stories in English and Afrikaans for foundational reading.

> [!NOTE]
> Scanned exam papers are 99% pixel overhead. 30 GB of PDFs compresses down to 150–300 MB of clean `.jsonl` text (~40,000 to 100,000 Q&A pairs) once extracted.

---

## Phase 2: From Files to Questions (Completed & Audited)

**Goal:** Extract text from all downloaded documents and segment into structured questions and official marking guidelines in `workspace/items/`.

**1. Document Ingestion (`workspace/text/`) — COMPLETED & VERIFIED:**
All 600 downloaded exam papers and memorandums have been ingested into `workspace/text/`:
```bash
python pipeline/ingest.py --skip-existing
```
- **Audited Metrics:** 600 files, **14,959,351 total characters**, 0 failures.
- **DOCX Auto-Routing:** Magic byte sniffing automatically handled 4 DOCX papers misnamed as `.pdf` (2019 May Mathematics P1/P2 and Wiskunde V1/V2).
- **Text Quality:** 507 dense text files. The 87 Mathematics question papers with rasterized equation images are paired with rich marking memorandums containing **1,387,534 characters** of full questions, sub-questions, method marks, and worked solutions.

**2. Mathematical Equations & Diagrams Handling Strategy:**
- **Equations & Formulas:** Formatted in LaTeX syntax inside `$..$` (inline) and `$$..$$` (display block). Rendered seamlessly in client apps via KaTeX.
- **Text-Describable Diagrams (~20%):** Euclidean geometry (circles, tangents, triangles), electric circuits, velocity-time graphs, and coordinate geometry figures have their geometric properties, labels, and relationships explicitly written into the `"passage"` field of the item schema. This allows pure text language models (`koeberg-stage-1`, `kendal-stage-1`, `gariep-stage-1`) to tutor geometry questions with complete context.
- **Pure Visual Figures (~10%):** Questions requiring perceptual visual inspection (anatomical diagrams, unlabelled cartoons) are flagged `"needs_review": true`, excluded from pure text SFT, rendered to `workspace/images/` via `pipeline/render_pages.py`, and reserved for multimodal vision fine-tuning on `LiquidAI/LFM3-VL-2B` (`gariep-flash-stage-1`).
- **Memo-First Question Recovery:** For Mathematics question papers with rasterized formulas, question wording and step criteria are extracted directly from the paired DBE memorandum.

**3. Run Item Extraction:**
```bash
# Dry-run cost estimate (shows token count and estimated cost before spending):
python pipeline/extract_items.py --source dbe-physical_sciences-g12-p1-2024-nov --dry-run

# Run extraction on a source pair:
python pipeline/extract_items.py --source dbe-physical_sciences-g12-p1-2024-nov
```

**4. Build the curriculum retrieval database:**
```bash
python retrieval.py build
```

---

## Phase 3: Build Your Exam FIRST (1 day, about $0.50)

**Goal:** a held-out exam benchmark in `workspace/eval/eval_items.jsonl` that your models will NEVER see during training.

**Do**
1. Select 1–2 complete exam papers that will NEVER be used for training (e.g. November 2024 Grade 12 Maths Paper 1 & 2):
   ```bash
   python eval/make_eval_from_items.py --source dbe-maths-g12-p1-2024-nov-heldout
   ```
2. Run your teacher model on the exam to establish the "teacher ceiling" score:
   ```bash
   python eval/run_eval.py --name teacher --backend openai --base-url https://api.deepseek.com --api-key-env TEACHER_API_KEY --model deepseek-chat --think-style none
   python eval/score_eval.py --name teacher --judge
   ```

---

## Phase 4: Audition the Stage 1 Base Models (half a day, free)

**Goal:** confirm how the candidate base models perform on CAPS math and Afrikaans out-of-the-box before training.

Candidates:
- `unsloth/Qwen3.8-27B` (Koeberg Flagship Cloud)
- `unsloth/Qwen3.5-4B` (Kendal Desktop)
- `empero-ai/Qwen3.8-4B-Distill` (Kendal Flash Mobile)
- `empero-ai/Qwen3.8-2B-Distill` / `unsloth/Qwen3.5-2B` (Gariep Budget Tutor)
- `LiquidAI/LFM3-VL-2B` (Gariep Flash OCR/Vision)

**Do**
1. Open `colab/sa_tutor_colab.ipynb` in **Vertex AI Colab Enterprise** with an **NVIDIA L4 GPU**.
2. Run cell 5 across candidate base models on the starter exam.
3. Compare results:
   ```bash
   python eval/report_eval.py --runs base-qwen38-27b base-qwen35-4b base-qwen38-4b-distill base-qwen38-2b-distill --out audition
   ```

---

## Phase 5: Generate the Training Data (a few days, about $3–8)

**Goal:** 1,500 to 5,000 verified CAPS records in `workspace/verified/r1/accepted.jsonl`, built into `workspace/build/r1/`.

**Do**
1. Configure `workspace/config/plan_config.json` for Round 1: Mathematics, Grades 7–12.
2. Plan the curriculum targets:
   ```bash
   python pipeline/plan.py --round r1 --target 1500
   ```
3. Dry run to inspect prompt format and verify token budget:
   ```bash
   python pipeline/generate.py --round r1 --dry-run
   ```
4. Generate records in parallel using DeepSeek V4.1 Flash or Gemini Flash:
   ```bash
   python pipeline/generate.py --round r1 --workers 4
   ```
5. Multi-layer automated verification (SymPy arithmetic check, leak filter, judge):
   ```bash
   python pipeline/verify.py --round r1 --judge
   ```
6. Human spot-check (read 40 records, verify bad rate < 10%):
   ```bash
   python pipeline/review_sample.py export --round r1 --n 40
   # Review workspace/review/r1_sample.md and mark r1_sample.csv, then apply:
   python pipeline/review_sample.py apply --round r1
   ```
7. Merge and compile train/val/test splits:
   ```bash
   python pipeline/merge.py --rounds r1 --out workspace/verified/train_r1.jsonl
   python tutor_data.py build workspace/verified/train_r1.jsonl --out workspace/build/r1 --val 0.1 --test 0.05
   ```

---

## Phase 6: Train the Stage 1 Models in Colab Enterprise (half a day, ~$2–4)

**Goal:** fine-tune LoRA adapters using Unsloth QLoRA on NVIDIA L4 Spot VMs in Vertex AI Colab Enterprise.

### The 3-Run Training Order & Cross-Tier Distillation

```
                      +-----------------------------+
                      | Train koeberg-stage-1 (27B) |  (~5.5 hrs on L4 Spot, ~$1.76)
                      +--------------+--------------+
                                     |
                                     v
               +-------------------------------------------+
               | Koeberg solves 2,000-5,000 hard questions |  (Transfers 27B reasoning
               | & adds explanations to dataset.jsonl      |   into training pool)
               +---------------------+---------------------+
                                     |
             +-----------------------+-----------------------+
             |                                               |
             v                                               v
+---------------------------+                   +---------------------------+
| Train kendal-stage-1 (4B) |                   | Train gariep-stage-1 (2B) |
| (~1.0 hr on Spot, ~$0.32) |                   | (~35 mins on Spot, ~$0.19)|
+---------------------------+                   +---------------------------+
```

### 1. Training Koeberg (Flagship Cloud 27B)
```bash
python training/train_sft.py --model unsloth/Qwen3.8-27B --data workspace/build/r1 \
       --out workspace/runs/r1-koeberg --epochs 3 --lr 1.5e-4 --rank 16 --batch 1 --grad-accum 16 --load-4bit
```
*VRAM used: ~21.5 GB on NVIDIA L4 (24GB). Time: ~5.5 hours. Cost: ~$1.76 on Spot VM.*

### 2. Training Kendal (Desktop & Mobile 4B)
```bash
python training/train_sft.py --model unsloth/Qwen3.5-4B --data workspace/build/r1 \
       --out workspace/runs/r1-kendal --epochs 3 --lr 2e-4 --rank 16 --batch 2 --grad-accum 8 --load-4bit
```
*(Or use `empero-ai/Qwen3.8-4B-Distill` if training the mobile-distill branch directly).*  
*VRAM used: ~6.5 GB on L4. Time: ~1.0 hour. Cost: ~$0.32 on Spot VM.*

### 3. Training Gariep (Budget Phone Tutor 2B)
```bash
python training/train_sft.py --model empero-ai/Qwen3.8-2B-Distill --data workspace/build/r1 \
       --out workspace/runs/r1-gariep --epochs 3 --lr 2e-4 --rank 16 --batch 4 --grad-accum 4 --load-4bit
```
*VRAM used: ~4.5 GB on L4. Time: ~35 mins. Cost: ~$0.19 on Spot VM.*

---

## Phase 7: Evaluate and Diagnose (after each run)

**Goal:** know exactly what improved, what degraded, and whether to proceed.

```bash
python eval/evaluate.py --name r1-kendal --backend hf --model unsloth/Qwen3.5-4B \
       --adapter workspace/runs/r1-kendal/adapter --compare base-qwen35-4b --ceiling teacher --analyze
```

**Move-On Rules:**
1. Overall exam pass rate ≥ 70%, or ≥ 85% of teacher ceiling.
2. Policy tests ≥ 90%; language checks ≥ 95%; tool checks ≥ 90%.
3. No grade/topic slice dropped by > 3 points (no catastrophic forgetting).

---

## Phase 8: Expanding Subjects (Sciences & Afrikaans, Rounds 2–4)

**Golden Rule:** Each round adds new data to ALL previous data and retrains FROM THE BASE MODEL.

| Round | Subject Added | Primary Sources |
|---|---|---|
| **r1** | Mathematics & Mathematical Literacy (English) | DBE past exams, Siyavula Maths (Gr 7–12) |
| **r2** | Natural Sciences & Physical Sciences | Siyavula Physical Sciences, DBE exam papers |
| **r3** | Drawing Board & Tool Mastery | Geometry diagrams, coordinate planes, circuit diagrams |
| **r4** | Afrikaans (Huistaal & FAL) & English Language | Siyavula Afrikaans, WCED begripstoetse, DBE FAL papers |

---

## Phase 9: Preference Training (DPO & GRPO)

**Goal:** eliminate residual bad habits (answer leaking, wrong language, rambling) that SFT did not remove.

1. Generate candidate answers to challenging prompts:
   ```bash
   python eval/run_eval.py --name r2-dpo-samples --items workspace/eval/dpo_prompts.jsonl \
          --backend hf --model unsloth/Qwen3.5-4B --adapter workspace/runs/r2/adapter --n 6 --temperature 0.8
   ```
2. Pair acceptable responses with failed responses:
   ```bash
   python training/make_dpo_pairs.py pairs --name r2-dpo-samples --items workspace/eval/dpo_prompts.jsonl \
          --out workspace/build/dpo_r2.jsonl
   ```
3. Run DPO in Unsloth.

---

## Phase 10: Exporting the 5 Stage 1 Models

**Goal:** produce the deployable GGUF files with clean public branding names.

### Multi-Quant Export from Single Training Runs
You do not train twice for Q6 and Q4. From a single training run, Unsloth exports multiple quantizations in minutes:

```bash
# 1. Export koeberg-stage-1 (UD-Q4_K_XL for Cloud Run & PC CPU)
python training/export_gguf.py --adapter workspace/runs/r4-koeberg/adapter \
       --out workspace/exports/koeberg-stage-1 --quants ud-q4_k_xl

# 2. Export kendal-stage-1 (Q6_K) and kendal-flash-stage-1 (Q4_K_M) from 1 run
python training/export_gguf.py --adapter workspace/runs/r4-kendal/adapter \
       --out workspace/exports/kendal-stage-1 --quants q6_k q4_k_m

# 3. Export gariep-stage-1 (Q6_K / Q8_0)
python training/export_gguf.py --adapter workspace/runs/r4-gariep/adapter \
       --out workspace/exports/gariep-stage-1 --quants q6_k q8_0

# 4. Export gariep-flash-stage-1 (LiquidAI LFM3-VL-2B Q6_K)
python training/export_gguf.py --adapter workspace/runs/r4-gariep-flash/adapter \
       --out workspace/exports/gariep-flash-stage-1 --quants q6_k
```

### Test Locally Before Releasing
```bash
llama-server -m workspace/exports/kendal-stage-1/kendal-stage-1-Q6_K.gguf --jinja -c 8192 --port 8080
python eval/evaluate.py --name test-kendal-q6 --backend openai --base-url http://localhost:8080/v1 --model local
```

---

## Phase 11: Multi-Modal Vision Fine-Tuning

**Goal:** models accurately read photos of textbook pages, handwritten questions, and geometry diagrams.

1. Create vision records:
   ```bash
   python pipeline/make_vision_records.py records --records workspace/verified/train_r3.jsonl \
          --out workspace/verified/vision_r3.jsonl --n 300
   ```
2. Fine-tune using Unsloth's vision notebook with frozen vision encoder (training language/attention adapters).
3. Export both the main GGUF and the `mmproj` vision projector file:
   ```bash
   # Both files are needed for vision inference in llama.cpp / PocketPal
   kendal-stage-1-Q6_K.gguf
   mmproj-kendal-stage-1.gguf
   ```

---

## Phase 12: Deploy `koeberg-stage-1` to Google Cloud Run (Scale-to-Zero)

**Goal:** host your 27B flagship model in the cloud for web and app users without burning your credits when idle.

1. Create a `Dockerfile` for Cloud Run with Ollama / vLLM:
   ```dockerfile
   FROM ollama/ollama:latest
   COPY workspace/exports/koeberg-stage-1/koeberg-stage-1-UD-Q4_K_XL.gguf /models/koeberg-stage-1.gguf
   COPY Modelfile /models/Modelfile
   RUN ollama serve & sleep 5 && ollama create koeberg-stage-1 -f /models/Modelfile
   ENTRYPOINT ["ollama", "serve"]
   ```
2. Deploy to Cloud Run with Serverless NVIDIA L4 GPU:
   ```bash
   gcloud run deploy koeberg-stage-1 \
     --image gcr.io/$PROJECT_ID/koeberg-stage-1:latest \
     --gpu 1 \
     --gpu-type nvidia-l4 \
     --cpu 8 \
     --memory 32Gi \
     --min-instances 0 \
     --max-instances 1 \
     --concurrency 10 \
     --region us-central1
   ```
*Why this works:* `--min-instances 0` scales instances completely down to zero. You pay \$0.00/hour when idle, and ~$0.015/minute when chatting. Your \$60 credit grant covers months of usage.

---

## End-to-End Budget Summary (Using \$60 Cloud Credits)

| Task | Infrastructure | Estimated Time | Credit Spend |
|---|---|---|---|
| Question Extraction from PDFs | Local PC (PyMuPDF) | 1–2 days | **\$0.00** |
| 10,000 Teacher Q&As | DeepSeek V4.1 Flash / Gemini Flash API | ~4 hours | **~$3.45** |
| Starter Exam Ceiling & Judge | DeepSeek / Gemini API | ~1 hour | **~$1.20** |
| Train `koeberg-stage-1` (27B, 3 epochs) | Colab Enterprise NVIDIA L4 Spot VM | ~5.5 hours | **~$1.76** |
| Train `kendal-stage-1` (4B, 3 epochs) | Colab Enterprise NVIDIA L4 Spot VM | ~1.0 hour | **~$0.32** |
| Train `gariep-stage-1` (2B, 3 epochs) | Colab Enterprise NVIDIA L4 Spot VM | ~35 mins | **~$0.19** |
| Train `gariep-flash-stage-1` (LiquidAI 2B) | Colab Enterprise NVIDIA L4 Spot VM | ~30 mins | **~$0.16** |
| Multi-Quant GGUF Exports | Colab Enterprise | ~15 mins | **~$0.10** |
| Cloud Run Hosting (`koeberg-stage-1`) | Cloud Run Serverless L4 GPU (Scale-to-zero) | Hundreds of active queries | **~$5.00 – $10.00** |
| **Total Estimated Spend** | | | **~$12.00 – $17.00** |
| **Remaining Credit Balance** | Available for future Stage 1.1 updates | | **~$43.00 – $48.00** |

---

## Cheat Sheet: Commands in Order

```bash
# === LOCAL PC (workspace & data preparation) ===
python pipeline/init_workspace.py
python pipeline/ingest.py
python pipeline/extract_items.py --source dbe-maths-g12-p1-2024-nov
python retrieval.py build
python eval/make_eval_from_items.py --source dbe-maths-g12-p1-2024-nov-heldout
python eval/run_eval.py --name teacher --backend openai --base-url https://api.deepseek.com --api-key-env TEACHER_API_KEY --model deepseek-chat --think-style none
python eval/score_eval.py --name teacher --judge

python pipeline/plan.py --round r1 --target 1500
python pipeline/generate.py --round r1 --workers 4
python pipeline/verify.py --round r1 --judge
python pipeline/review_sample.py export --round r1 --n 40
# (Review workspace/review/r1_sample.md, then apply):
python pipeline/review_sample.py apply --round r1
python pipeline/merge.py --rounds r1 --out workspace/verified/train_r1.jsonl
python tutor_data.py build workspace/verified/train_r1.jsonl --out workspace/build/r1 --val 0.1 --test 0.05

# === VERTEX AI COLAB ENTERPRISE (L4 Spot GPU) ===
# 1. Train Koeberg (27B)
python training/train_sft.py --model unsloth/Qwen3.8-27B --data workspace/build/r1 --out workspace/runs/r1-koeberg --load-4bit

# 2. Train Kendal (4B)
python training/train_sft.py --model unsloth/Qwen3.5-4B --data workspace/build/r1 --out workspace/runs/r1-kendal --load-4bit

# 3. Train Gariep (2B)
python training/train_sft.py --model empero-ai/Qwen3.8-2B-Distill --data workspace/build/r1 --out workspace/runs/r1-gariep --load-4bit

# 4. Evaluate Checkpoints
python eval/evaluate.py --name r1-kendal --backend hf --model unsloth/Qwen3.5-4B --adapter workspace/runs/r1-kendal/adapter --compare base-qwen35-4b --ceiling teacher --analyze

# 5. Multi-Quant GGUF Exports (Clean Eishkom Branding)
python training/export_gguf.py --adapter workspace/runs/r1-koeberg/adapter --out workspace/exports/koeberg-stage-1 --quants ud-q4_k_xl
python training/export_gguf.py --adapter workspace/runs/r1-kendal/adapter --out workspace/exports/kendal-stage-1 --quants q6_k q4_k_m
python training/export_gguf.py --adapter workspace/runs/r1-gariep/adapter --out workspace/exports/gariep-stage-1 --quants q6_k q8_0
```
