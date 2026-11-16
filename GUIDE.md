# Eishkom Stage 1 — Developer Execution Guide

> **Release Cycle:** Stage 1  
> **Workflow:** End-to-End Pipeline from Raw DBE PDFs to Fine-Tuned GGUF Models & Cloud Run Hosting

---

## Quick Reference Command Cheatsheet

```bash
# ==============================================================================
# PHASE 1: COLLECT SOURCES (ALREADY COMPLETED & VERIFIED)
# ==============================================================================
python pipeline/download_dbe.py --dry-run
python pipeline/download_dbe.py

# ==============================================================================
# PHASE 2: MULTIMODAL VISION INGESTION & TWO-PASS VERIFICATION (COMPLETED)
# ==============================================================================
python pipeline/ingest_vision.py --pipeline-order
python pipeline/sanitize_text.py
python pipeline/verify_extractions.py

# ==============================================================================
# PHASE 2.5: ITEM EXTRACTION (QUESTIONS & MEMOS) — 100% COMPLETED
# ==============================================================================
python pipeline/extract_items.py --source <source_id>

# ==============================================================================
# PHASE 3: HELD-OUT EVALUATION BENCHMARK (QUARANTINED)
# ==============================================================================
python pipeline/build_eval.py --year 2024 --session nov --grade 12

# ==============================================================================
# PHASE 4: TEACHER GENERATION & SAMPLES EXPANSION (2,000+ SAMPLES REACHED)
# ==============================================================================
python tools/run_wave3_turbo.py

# ==============================================================================
# PHASE 5: CONVERT ITEMS TO FULL SOLUTIONS (1:2 MULTI-TASK RATIO)
# ==============================================================================
python tools/convert_raw_items_to_full_solutions.py

# ==============================================================================
# PHASE 6: SFT DATASET PACKAGING
# ==============================================================================
python tools/package_all_verified_sft.py
python sa-tutor-kit/sa-tutor-kit/tutor_data.py build workspace/verified/train_master_combined.jsonl --out workspace/build/r1 --val 0.15

# ==============================================================================
# PHASE 7 & 8: VERTEX AI COLAB ENTERPRISE SFT & GGUF EXPORT (STAGE 2 / R2 PRODUCTION)
# Runtime template: eishkom-gpu (g2-standard-4, 1x NVIDIA L4 24GB VRAM, 100GB SSD)
# Spot VM enabled (~$0.32/hr consuming promotional credits, Quota GPUS_ALL_REGIONS = 1 approved)
# ==============================================================================
# 1. Unpack dataset (37,179 production samples, ~20.0M tokens) and training scripts:
#    !unzip -q eishkom_colab_kit.zip
#    os.environ['SA_WORKSPACE'] = os.path.abspath('workspace')
#
# 2. Train kendal-stage-1 (4B) on unsloth/Qwen3.5-4B (4-bit QLoRA, bfloat16, FlashAttention):
#    # Note: For r2 (37k samples), 1 epoch (~2,324 steps, ~5.2 hrs on L4) is optimal for fine-tuning.
#    !python training/train_sft.py --model unsloth/Qwen3.5-4B --data workspace/build/r2 --out workspace/runs/r2-kendal --load-4bit --epochs 1 --show 0
#
# 3. Export clean branded GGUF models:
#    !python training/export_gguf.py --adapter workspace/runs/r2-kendal/adapter --out workspace/exports/kendal-stage-1 --quants q6_k q4_k q4_k_m
#
# 4. Train koeberg-stage-1 (27B) on unsloth/Qwen3.8-27B (~5.5 hrs, ~$1.76 credits):
#    !python training/train_sft.py --model unsloth/Qwen3.8-27B --data workspace/build/r2 --out workspace/runs/r2-koeberg --load-4bit --epochs 1
# ==============================================================================
# PHASE 9: DEPLOY KOEBERG-STAGE-1 TO GOOGLE CLOUD RUN (SCALE-TO-ZERO)
# ==============================================================================
gcloud run deploy koeberg-stage-1 \
  --image gcr.io/$PROJECT_ID/koeberg-stage-1:latest \
  --gpu 1 --gpu-type nvidia-l4 --cpu 8 --memory 32Gi \
  --min-instances 0 --max-instances 1 --concurrency 10
```

---

## Detailed Step-by-Step Instructions

### Step 0: Environment Pre-Flight
1. Verify Python 3.12: `python --version`.
2. Install SymPy if missing: `pip install sympy`.
3. Check teacher API key in `.env`: `TEACHER_API_KEY=...`.
4. Run verification tests:
   ```bash
   python answers.py
   python board.py
   python tools_sim.py
   python retrieval.py test
   python llm.py test
   python tutor_data.py validate examples/examples.jsonl
   ```

### Step 1: Raw Exam Papers & Memorandums (Completed)
- 600 PDFs downloaded into `workspace/raw/dbe/` covering Grades 10–12 Mathematics, Physical Sciences, English, and Afrikaans.
- All documents paired in `workspace/sources/sources.csv`.

### Step 2: Multimodal Vision Ingestion & Two-Pass Verification (Completed & Audited)
- **Vision Extraction:** Ingested all 600 exam documents into `workspace/text/` using Gemini Multimodal Vision (**11,310,442 characters**, 354 KaTeX LaTeX documents, 1,005 geometric diagrams).
- **Deterministic KaTeX Sanitizer:** Cleaned 137 files via `pipeline/sanitize_text.py`, eliminating empty `$$ $$` blocks and closing unclosed environments in 0.5s.
- **Two-Pass Verification Audit:** Audited all 301 exam pairs via `pipeline/verify_extractions.py`, achieving **287 / 301 clean structural passes (95.3%)**, **47,299 KaTeX formulas**, and **1,005 verified diagrams**. Report persisted in `workspace/reports/extraction_verification_report.json`.

### Step 3: Segment into Structured Question-and-Answer Items (Phase 2.5 — 100% Completed)
- **Status:** **Completed 100%** (265 / 265 verified papers extracted, 13,168 atomic items, 31,278 marks accounted for, 0 KaTeX delimiter errors).
- **Autonomous Multi-Lane Fleet Extraction:**
  - Multi-lane turbo workers executed parallel code-style extraction with AI Studio (`gemini-3.5-flash-lite`) and OpenRouter models.
  - Live progress tracked in `workspace/EXTRACTION_TRACKER.md` across all 301 exam pairs (33 held-out benchmarks quarantined).
  - Sync tracker status anytime: `python workspace/tools/sync_tracker.py`.
- **Universal Extraction Standards (UDVES):**
  - **Mathematical Equations:** Standardized into LaTeX inside `$..$` (inline) or `$$..$$` (display block) with `$0{,}1$` comma spacing.
  - **Text-Describable Diagrams (~20%):** Geometry circles, triangles, circuits, coordinate graphs have spatial relations written into `"passage"`.
  - **Chemistry & Sciences:** Standardized into condensed IUPAC formulas (e.g. $\text{CH}_3\text{CH}_2\text{OH}$) with reaction coordinates; zero fragile 2D matrices.
  - **Languages & Visual Literacy:** Full reading passages, frame-by-frame cartoon descriptions, and advertising layouts preserved in `"passage"`.
  - **Pure Visual Figures:** Flagged `"needs_review": true`, excluded from text SFT, preserved for multimodal training on `LiquidAI/LFM3-VL-2B` (`gariep-flash-stage-1`).

### Step 4: Reserve the 2024 Benchmark
- The November 2024 Grade 12 items are compiled into `workspace/eval/eval_items.jsonl`.
- These items are never exposed during training (0% contamination benchmark).

### Step 5: Distill Socratic Dialogues & Multi-Task Curriculum (2,000+ SAMPLES)
- Multi-model teacher fleet: OpenAI (`gpt-6-luna`, `xhigh` reasoning), Google AI Studio (Gemini 3.5 & 3.1 Flash Lite, 24k thinking budget), OpenRouter (Nemotron Ultra), and Intern-AI (DeepSeek V4.1).
- **Pedagogical Standards:**
  - **Socratic Hint Ladder:** Do not give the answer away immediately. Diagnose misconception first, offer small clues, ask one question at a time and wait.
  - **Frustrated Learners:** Validate learner emotion, de-escalate anxiety ("Take a deep breath, let's break this down"), reduce cognitive load.
  - **Short-Answer Learners:** Provide punchy, concise single-question prompts that match the student's brief interaction style.
  - **Mnemonics & Memory Aids:** Ground abstract concepts in memorable rules (e.g., 'V' points down so vertical means up-and-down; 4IR letters).
- **Embedded Tool-Calling Procedure:**
  - In calculation subjects (Maths, Wiskunde, Physical Sciences), the model embeds explicit calculator checks into its private reasoning:
    `[TOOL CHECK: calculator(expression="...") -> result]`
  - Trains the model to verify calculations with tools rather than hallucinating multi-digit arithmetic.
- **Multi-Task Curriculum Ratio (1:2):**
  - Balance 1 structured full worked solution (`answer_policy: "full_solution"`) per 2 Socratic hint dialogues (`answer_policy: "guided"`).
  - Grounded in official DBE mark schemes while anchoring conversational behavior in Socratic patience.

### Step 5b: Pedagogical Styles in Stage 1 vs Stage 2 Strategy Permutation (v2 Roadmap)

#### How Teaching Styles Work in Stage 1:
- **It is NOT 1 generic style for all subjects.** The teacher model trains on **different pedagogical styles adapted to the cognitive demands of each subject**:
  1. **Mathematics & Wiskunde:**
     - Uses **Polya's 4-step problem solving** (`understand_problem`, `devise_plan`, `carry_out_plan`, `look_back`).
     - Employs **factor-pair search**, **check by substitution**, and explicit **`[TOOL CHECK: calculator(...)]`** in private chain-of-thought so arithmetic is verified rather than guessed.
  2. **Physical Sciences & Fisiese Wetenskappe:**
     - Uses **concept mapping** and **formula-selection-first**.
     - Enforces **units checks** (e.g. converting $\text{km/h}$ to $\text{m/s}$, checking SI units $\text{N}$, $\text{J}$, $\text{W}$), identifying force directions (perpendicular normal force, frictional opposing force), and tool-checked arithmetic.
  3. **Languages (English & Afrikaans HL / FAL):**
     - Uses **context clues**, **quote extraction**, **paraphrasing**, and **mark-per-point** scoring.
     - Guides visual literacy (frame-by-frame cartoon body language, font emphasis, advertising target audiences).
  4. **Adaptive Student Personas Across All Subjects:**
     - **Frustrated / Anxious Learners:** Validates emotions first (*"Take a deep breath, let's break this into one small piece"*), lowers cognitive anxiety, and gives micro-clues.
     - **Short-Answer Learners:** Matches students who only reply with 1-3 words by providing tight, punchy, single-question nudges instead of lecturing.
     - **Memory Mnemonics & Analogies:** Uses memory hooks (e.g. '$V$' points down so vertical means up-and-down; '$H$' is flat like the horizon; 4IR initials for Fourth Industrial Revolution).
- **Multi-Task Curriculum Ratio (1:2):** 1 structured full worked solution demonstration (`answer_policy: "full_solution"`) per 2 Socratic hint dialogues (`answer_policy: "guided"`).

#### Stage 2 (v2 Models) Architecture: Strategy Permutation
> [!IMPORTANT]
> **Stage 2 (v2) Permutation Architecture:**
> In Stage 2 (v2 of the models), we will be retraining on the **exact same 265 question papers but across systematically rotated teaching styles**.
> For example:
> - If **November 2021 Mathematics P1** was trained using `step_walkthrough` (standard Socratic hint ladder) in Stage 1:
> - In Stage 2, that **same exam paper** will be regenerated and retrained under alternate pedagogical styles:
>   1. `worked_example`: The tutor provides a fully solved parallel problem first, then asks the student to solve the DBE question.
>   2. `mnemonic_memory_hook`: The tutor focuses heavily on cognitive memory tricks, analogies, and visual metaphors.
>   3. `faded_example`: The tutor provides a partially completed solution with key operational blanks for the student to complete.
>   4. `frustrated_learner_recovery`: Explicit training on emotional de-escalation and building learner confidence.
>   5. `rapid_short_prompt`: Ultra-concise, rapid-fire Q&A optimized for mobile chat.
> - **The Result:** This multiplies our training corpus **4x–5x (10,000+ to 15,000+ SFT samples)** entirely from our verified 265 DBE exam papers, giving the Stage 2 models unprecedented stylistic versatility without needing external or unverified question papers.
- In Stage 2 (v2 of the models), the exact same 265 core DBE question papers will be systematically re-prompted across multiple pedagogical styles:
  1. `step_walkthrough` (Standard Socratic hint ladder)
  2. `worked_example` (Full modelled problem followed by a parallel problem)
  3. `mnemonic_memory_hook` (Focus on cognitive memory aids and analogies)
  4. `faded_example` (Partially worked problem with missing blanks for the learner)
  5. `frustrated_learner_de-escalation` (Emotional regulation and confidence rebuilding)
  6. `rapid_short_prompt` (Ultra-concise Q&A for mobile micro-learning)
- This multiplies the corpus 4x–5x (10,000+ samples) purely from verified DBE past papers, achieving stylistic versatility with zero unverified external data.

### Step 6: Verify and Filter
- Run automated verification against SymPy and official DBE memorandums with forensic South African decimal comma normalization (`$13{,}32$` -> `13.32`).
- Rejects any generated dialogue where the mathematical calculation disagrees with SymPy or the official memo.

### Step 7: SFT Training & GGUF Quantization

#### 1. Hardware & Runner Notebooks:
- **Option A (Vertex AI Colab Enterprise - NVIDIA L4 GPU 24GB):**
  - Notebook: `colab/sa_tutor_colab.ipynb`
  - Runs inside Google Cloud Console with Spot VM pricing (~$0.32/hr) consuming promotional GCP credits.
  - Ideal for `koeberg-stage-1` (27B) and `kendal-stage-1` (4B).
  - *Note on Regional Stock:* If `us-central1` experiences L4 capacity shortages, standard on-demand instances or alternate regions (`us-east4`) can be utilized.
- **Option B (Google Colab Research - NVIDIA T4 GPU 15GB):**
  - Notebook: `colab/sa_tutor_colab_research.ipynb`
  - Packaged kit: `gariep_colab_research_kit.zip` (1.56 MB)
  - Runs in standard consumer Colab (`colab.research.google.com`) on free or Pro NVIDIA T4 GPUs.
  - Highly optimized for `gariep-stage-1` (2B): utilizes `batch=8, grad_accum=2` with FP16, saturating ~11-12GB VRAM for high-speed ~20-minute training.
- **Option C (Cloud TPU v5e-1 - 16GB HBM, 197 TFLOPs bfloat16):**
  - Notebook: `colab/sa_tutor_colab_tpu_v5e.ipynb`
  - Packaged kit: `gariep_colab_research_kit.zip` or `eishkom_colab_kit.zip`
  - Runs in Google Colab (Research or Enterprise) with hardware set to **TPU v5e-1**.
  - Uses native **PyTorch/XLA (`torch_xla`) + Hugging Face Transformers + PEFT LoRA** with hardware `bfloat16` (`--no-unsloth`).
  - Squeezes maximum matrix throughput: `batch=8, grad_accum=2` (~15–20 minutes for 2B). Exports GGUF via llama.cpp on the host CPU.

#### 2. Model Training & Checkpointing:
- Fine-tune unquantized base Hugging Face repositories using Unsloth QLoRA.
- Checkpoints saved after each epoch to Google Drive (`--resume` protects against preemption).
- Logging throttled with `disable_tqdm=True` and `logging_steps=25` to prevent browser tab freezing.

#### 3. Multi-Quant Export & Pure K Mandate:
- Run `training/export_gguf.py` on the trained adapter.
- Mandated quantization suite across all model tiers:
  - High fidelity: `UD-Q4_K_XL` (27B), `Q6_K` (4B), `Q8_0` (2B)
  - Pure K-quant: `Q4_K` (evaluates un-modified pure-K reasoning retention)
  - Edge/Mobile: `Q4_K_M` (lightweight packaging for mobile phones and low-RAM PCs)
- **Large File Download Protocol:** Colab's web UI truncates browser downloads at ~60MB. Always sync full `.gguf` binaries to Google Cloud Storage (`gs://${PROJECT}-models`) or save directly to mounted Google Drive.

### Step 8: Deploy Koeberg to Cloud Run
- Deploy `koeberg-stage-1` containerized to Google Cloud Run with scale-to-zero (`--min-instances 0`).
- Idle cost: $0.00/hour.
- Active cost: ~$0.015/minute.

### Step 9: Native Application Pipeline & Transient Page-Worker Architecture
To ensure seamless execution on budget South African client devices (4GB RAM phones, legacy Celeron school laptops, and GTX 1650 PCs), the desktop/mobile application implements the **Transient Chunked Page-Worker Pattern (Map-Reduce)**:

```
[ Multi-Page PDF / Exam Photos ] 
            │
            ▼ (App renders 300 DPI PNG screenshots)
[ Page 1 PNG ] ──> [ Transient Vision Worker (gariep-flash 2B) ] ──> [ KaTeX / Markdown Text ]
                                  │
                                  ▼ (Purge KV Cache & Release VRAM)
[ Page 2 PNG ] ──> [ Transient Vision Worker (gariep-flash 2B) ] ──> [ KaTeX / Markdown Text ]
                                  │
                                  ▼ (Purge KV Cache & Release VRAM)
            ...
            │ (App stitches transcripts & resolves question continuity)
            ▼
[ Clean Extracted Exam / Homework Text ]
            │
            ▼
[ Central Tutor Agent (kendal-stage-1 4B / gariep-stage-1 2B) ]
(Socratic Dialogue • Ultra-Fast Token Speeds • Zero Vision Overhead • Flat Memory Footprint)
```

1. **Application Layer Responsibilities:**
   - Slices input documents into high-resolution PNG page images (300 DPI).
   - Sequentially dispatches one page at a time to the Vision Worker.
   - Automatically detects and stitches cross-page questions (e.g. question statement ending at the bottom of Page 2 with sub-questions on Page 3).
   - Enforces a complete memory purge of the vision worker between pages (`torch.cuda.empty_cache()` / context termination) to keep VRAM usage flat (~1.5–2GB) regardless of document page count.
2. **Vision Worker Specialization (`gariep-flash-stage-1`):**
   - **Pure High-Fidelity Digitization:** The vision model is strictly an OCR, KaTeX, and diagram transcriber—it does NOT solve problems or conduct tutoring.
   - Transcribes printed exam text and student handwritten calculations.
   - Standardizes all mathematical formulas into KaTeX LaTeX (`$...$` inline, `$$...$$` display).
   - Encodes geometric circles, Cartesian curves, electric circuits, and chemical reaction pathways into structured diagram annotations (`[DIAGRAM: ...]`).
3. **Central Tutor Specialization (`kendal-stage-1` / `gariep-stage-1`):**
   - Operates 100% on the clean, aggregated text transcript.
   - Dedicated exclusively to Socratic pedagogy, hint ladders, CAPS curriculum alignment, and diagnosing student misconceptions at maximum tokens per second.

### Step 10: Vision Model Training & Ground-Truth Pipeline
To fine-tune `gariep-flash-stage-1` (2B) for high-accuracy South African exam and handwriting digitization:

1. **Synthetic Ground-Truth Generation:**
   - Run high-capacity multimodal models (Gemini Flash Multimodal Vision) across exam pages and student handwritten homework samples to generate structured Markdown + KaTeX transcripts.
   - Cross-check and reconcile extracted transcripts against the official DBE marking memorandums for exact mathematical and rubric fidelity.
2. **Handwritten Sample Collection:**
   - Collect 200–500 photographed student homework solutions on lined paper in varied lighting conditions and phone camera angles.
   - Annotate with ground-truth KaTeX to train the vision model on real-world classroom pencil work.
3. **Dataset Schema (Vision Multi-Turn JSONL):**
   ```json
   {
     "messages": [
       {
         "role": "user",
         "content": [
           {"type": "image", "image": "workspace/images/gr12_physics_circuit_p1.png"},
           {"type": "text", "text": "Transcribe this exam page exactly. Output all equations in KaTeX LaTeX and describe all diagrams."}
         ]
       },
       {
         "role": "assistant",
         "content": "### QUESTION 8\nIn the circuit diagram below...\n[DIAGRAM: Battery with emf $\\mathcal{E} = 12\\text{ V}$, internal resistance $r$, connected in series with...]"
       }
     ]
   }
   ```
4. **Fine-Tuning with Unsloth `FastVisionModel`:**
   - Load base multimodal model (e.g. `Qwen/Qwen2-VL-2B-Instruct` or `LiquidAI/LFM3-VL-2B`) in 4-bit QLoRA.
   - Fine-tune on Google Cloud Vertex AI / Colab GPU runtime (~2–3 hours on L4 GPU).
   - Export both the base language GGUF and the companion vision projector (`mmproj-*.gguf`).

### Step 11: Custom Architecture & Enterprise Branding Registration
To establish custom architecture identity without sacrificing C++/CUDA inference performance:

1. **Hugging Face Custom Architecture:**
   - In `config.json`, configure `"model_type": "eishkom"`.
   - Provide `configuration_eishkom.py` (defining `EishkomConfig`) and `modeling_eishkom.py` (defining `EishkomForCausalLM`).
   - Register architecture to Hugging Face Hub so users load it via `AutoModelForCausalLM.from_pretrained("...", trust_remote_code=True)`.
2. **GGUF & Local Engine Encapsulation:**
   - In compiled GGUF binaries, retain standard execution kernels (`general.architecture = "qwen2"`) to maintain compatibility with llama.cpp, Ollama, and LM Studio.
   - Brand model identity cleanly via GGUF metadata: `general.name = "Eishkom Kendal Stage 1"`, clean file names (`kendal-stage-1-Q6_K.gguf`), and complete UI brand encapsulation within the native Eishkom desktop/mobile app.

### Step 12: Multi-Stage Scaling & Evolution Architecture (Stages 2, 3 & 4)

#### 1. Stage 2 (v2 Models) — Cumulative Dataset Scaling & Multi-Strategy Fleet Generation:
- **Cumulative Dataset Rule:** Never train on only the new data! Combine Round 1 + Round 2 into `workspace/build/r2/` (5,755 + 10,000 = 15,755 total samples) to prevent catastrophic forgetting.
- **LoRA Capacity Scaling:** Scale from `--rank 16` (0.47% weights) up to `--rank 32` or `--rank 64` (1%–2% weights) to give the neural network sufficient capacity for the 15,000+ multi-style lessons.
- **Base Model Upgradability:** The dataset is vendor-neutral intellectual property (conforming to `tutor-v1` and `tutor-v2` schemas). If Alibaba releases `Qwen3.8-4B` or Google releases `Gemma 3`, simply point `train_sft.py` to the new base model to instantly upgrade Kendal with zero dataset rework.
- **Stage 2 Multi-Model Fleet Generation (`stage-2/run_stage2_fleet.py`):**
  - **14-Worker Fleet Allocation (8x OpenAI STEM Exclusive + 4x Gemini Languages + Nemotron + Fast DeepSeek):**
    * **OpenAI (8 Dedicated STEM Workers):** `gpt-6-luna` strictly dedicated to Mathematics and Physical Sciences (English & Afrikaans):
      - `OAI_MTH_1` & `OAI_MTH_2`: Mathematics (English) - 2x
      - `OAI_WSK_1` & `OAI_WSK_2`: Wiskunde (Afrikaans) - 2x
      - `OAI_SCI_E1` & `OAI_SCI_E2`: Physical Sciences (English) - 2x
      - `OAI_SCI_A1` & `OAI_SCI_A2`: Fisiese Wetenskappe (Afrikaans) - 2x
      - Cadence: Strictly cycling within STEM (`math_en`, `math_af`, `sci_en`, `sci_af`). Zero language assignments.
    * **Google AI Studio Key 1 & Key 2 (4 Dedicated Language Workers):**
      - `GEM1_35` & `GEM1_31`: `gemini-3.5-flash-lite` & `gemini-3.1-flash-lite` (English & Afrikaans FAL/HL)
      - `GEM2_35` & `GEM2_31`: `gemini-3.5-flash-lite` & `gemini-3.1-flash-lite` (English & Afrikaans FAL/HL)
      - Self-contained cross-key fallback keeps 100% of language items inside Gemini without leaking to OpenAI.
    * **OpenRouter (1 Worker - Free Model):** `nemotron-3-ultra-550b:free` (Maths P2)
    * **Intern-AI DeepSeek (1 Worker - Free DeepSeek):** `deepseek-v4.1-flash-1017` on Physical Sciences & Fisiese Wetenskappe, optimized directly on the free Intern-AI endpoint with 3.5s rate pacing, progressive 429 backoff, and dual content/reasoning extraction.
  - **Live Progress Monitor & Milestone Alerts:** Every 1,000 verified samples triggers a formatted milestone alert. Check live status at any time with `python tools/stage2_status.py` or `python stage-2/run_stage2_fleet.py --status`.
  - **Mandatory Final Turn Output Format:**
    * **STEM:** Final Answer + `📖 Formula Breakdown (How It Works):` (The Formula in KaTeX, What the letters mean in plain terms, Why we use it) + `🎯 Exam Tip:` (DBE mark allocation or common pitfall).
    * **Languages:** Model Answer + `📖 Concept & Thought Process (How to Understand It):` (The Rule/Device, Step-by-Step mental unpacking, 3-mark scoring formula) + `🎯 Exam Tip:`.
  - **Dual Coaching Profiles:** Short / Fast-Track Mode (35% of items, 2 turns) for rapid practice vs. Deep-Dive Socratic Mode (65% of items, 3–4 turns) for patient conceptual scaffolding.
  - **Zero-Cost Verification & Rejection Forensics:** Deterministic SymPy execution for STEM and rule-based rubric scoring for Languages ($0.00 second LLM judge cost). Every rejected item is logged to `workspace/rejected/stage2/` with full diagnostic metadata (`rejection_reason`, `sympy_out`, `memo_target`, `verify_code`, `rubric_score`, `parsed_record`, `raw_response`) for human inspection.
  - **10 Teaching Strategies:** Dynamic weighted rotation across `step_walkthrough`, `worked_example`, `faded_example`, `error_spotting`, `mnemonic_memory_hook`, `frustrated_learner_de-escalation`, `rapid_recall_drill`, `compare_and_contrast`, `exam_technique_focus`, and `concept_first`.
  - **6 Student Personas:** Simulates varied cognitive states (`lost`, `stuck`, `frustrated`, `partially_correct`, `on_track`, `advanced`) across 2 to 5 dialogue turns.
  - **10-Point Quality Rubric (`stage-2/quality/rubric_checker.py`):** Multi-dimensional scoring (0–100) checking turn counts, assistant reasoning fields, anti-spoiler compliance, language markers, and strategy alignment with automated 2-attempt retries.
  - **Automated Deduplication:** Scans and excludes all 41 papers touched in Stage 1, pulling from the 225 untouched papers (11,193 atomic items) in `workspace/items/`.
  - **Self-Contained Safe Build (`stage-2/compile_stage2_dataset.py`):** Compiles verified Stage 1 + Stage 2 data into `workspace/verified/stage2_master_combined.jsonl` and builds `workspace/build/r2/` with zero modification to `workspace/build/r1/`.
  - **Execution Commands:**
    ```bash
    # Test pipeline and paper assignment without calling APIs:
    python stage-2/run_stage2_fleet.py --dry-run

    # Run live single-item end-to-end verification test:
    python stage-2/run_stage2_fleet.py --test-item

    # Launch full generation fleet targeting 10,000+ SFT samples:
    python stage-2/run_stage2_fleet.py
    ```


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
- Uses verified Stage 3 local models to generate diverse teaching styles across additional grades and technical subjects with authentic South African classroom pedagogy.

### Step 13: Phase 2.5 — Agentic Teacher & Study Coach Expansion (`stage-2/agentic/`)

To expand beyond pure question answering into holistic academic coaching and on-device agentic workflows:

1. **Stateless Atomic Architecture (Mobile Optimization):**
   - **Page Worker:** Reads ONE page at a time. Returns structured JSON notes (`issues`, `questions`, `passages`, `carry_out`). Never solves problems or provides tutoring. Purges KV-cache after each page to keep mobile VRAM flat (~1.5–2GB).
   - **Synthesiser / Study Coach:** Dialogue between learner and coach based exclusively on aggregated notes, Python tool results, or curriculum profiles.
2. **Deterministic Code Computation:**
   - Small models NEVER perform arithmetic, compute dates, sum marks, or rank topics.
   - Python functions in `stage-2/agentic/sampler_agentic.py` (`build_schedule()`, `rank_weak_topics()`, `time_plan()`, `aggregate_notes()`) calculate 100% of the numbers.
   - The tutor model ONLY reads, explains, and contextualizes code-computed results.
3. **9 Agentic Task Families & Exposure Guardrail:**
   - Target: **3,500 unique samples** trained for 2 epochs = **7,000 training exposures** (strictly 10–18% of the total dataset, preserving core STEM reasoning).
   - Task families: `page_worker`, `study_plan`, `study_guide_section`, `revision_session`, `paper_walkthrough`, `paper_prep_guide`, `intake`, `weak_topic_diagnosis`, `exam_strategy`, and `distress_signal`.
4. **South African Crisis & Wellbeing Protocol (`distress_signal`):**
   - Approximately 2% of agentic training data covers crisis de-escalation with official verified South African helplines (SADAG: 0800 567 567 / 0800 456 789; Childline: 116; LifeLine: 0861 322 322).
5. **Execution Commands:**
   ```bash
   # Test deterministic arithmetic helpers and spec sampler:
   python stage-2/agentic/sampler_agentic.py

   # Run single-sample verification smoke test across task families:
   python stage-2/agentic/run_agentic_fleet.py --test-sample

   # Launch full agentic generation fleet (targeting 3,500 verified samples):
   python stage-2/agentic/run_agentic_fleet.py --target 3500 --workers 8
   ```

### Step 14: Phase 2.6 — Context Compaction (`sampler_ops.py`) & Pass 2 Fleet

1. **Context Compaction & Operations Engine (`stage-2/agentic/sampler_ops.py`):**
   - Implements on-device token tracking, soft triggers (55% budget between turns), hard triggers (80%), history pruning (`reasoning`/`thinking` stripped after turns), ledger management, and 5-field model-written state.
   - Test KV calculations and spec builders:
     ```bash
     python stage-2/agentic/sampler_ops.py
     ```

2. **Stage 2 Pass 2: Multi-Strategy Socratic Permutation Fleet:**
   - Runs across all 225 exam papers, actively excluding the strategy used in Pass 1 for every item to generate diverse pedagogical styles (`faded_example`, `worked_example`, `error_analysis`, `mnemonic`, `socratic_hints`, `exam_technique`, `concept_first`).
   - Execution commands:
     ```bash
     # Dry-run audit for Pass 2 lanes:
     python stage-2/run_stage2_fleet.py --dry-run --pass 2

     # Launch full Pass 2 generation fleet in background:
     python stage-2/run_stage2_fleet.py --pass 2

     # Check real-time progress of Pass 2:
     python stage-2/run_stage2_fleet.py --status
     ```

### Step 15: Phase 2.7 — Multi-Provider Fleet Generation & Agentic Coaching Fleet

1. **Provider Credentials & Speed Tuning:**
   - Multi-provider fleet operating across Alibaba DashScope, Vercel AI Gateway, Token Lab AMD, APInex, APMix, TokenHarbor, Kilo Gateway, LLM7.io, Groq, Google AI Studio, and Cohere.
   - Pacing accelerated for maximum throughput: Alibaba (0.05s), AMD (0.05s), Vercel (0.05s), TokenHarbor (0.1s), APMix (0.1s), LLM7 (0.2s), APInex (0.4s).
2. **Current Production Status:**
   - Core Socratic Lessons: **17,075+ verified dialogues** across all Grade 10–12 STEM and language subjects.
   - DBE Past Paper Full Solutions: **12,912 items (100% Complete across all 266 papers)**.
   - Total Unique Canonical Records: **25,981 items (~37,179 SFT training samples / ~20.0M tokens)**.

### Step 16: Phase 2.8 — Residual Redo & Unified Production Dataset Build

1. **100% Past Paper Coverage (Residual Redo):**
   - Redo runner (`tools/redo_rejected_samples.py`) resolved 100% of historical rejections (386 residual items across 3 progressive sprints: 290 solved -> 87 solved -> 9 solved -> **0 unsolved**).
   - Zero unsolved past paper questions remain across the entire 266-paper DBE archive.

2. **Master Dataset Compilation (`stage-2/compile_stage2_dataset.py`):**
   - Merges all 6 verified sources (Stage 1 Socratic, Stage 1 Full Solutions, Stage 2 Pass 1 Socratic, Stage 2 Pass 2 & Redo Socratic, Stage 2 Full Solutions, Stage 2 Agentic Coaching).
   - Executes standard schema canonicalization (`tutor-v1`), enforces `thinking: "on"`, and runs `tutor_data.py build` across 4 production targets:
     * **Master Combined (`workspace/build/r2`):** 20,856 train records | 37,179 train samples | 46,211 thinking-on samples (~20.0M tokens)
     * **Socratic Dialogues (`workspace/build/r2_socratic`):** 9,618 train records | 24,921 train samples | 30,888 thinking-on samples
     * **Full Solutions (`workspace/build/r2_fullsol`):** 10,352 train records | 10,352 train samples | 12,912 thinking-on samples
     * **Agentic Coaching (`workspace/build/r2_agentic`):** 886 train records | 1,906 train samples | 2,411 thinking-on samples
   - Execution command:
     ```bash
     python stage-2/compile_stage2_dataset.py
     ```
