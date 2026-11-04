# Eishkom AI — Project Rules & Operational Instructions

> [!IMPORTANT]
> **Mandatory AI Assistant Behavior Rule:**
> Every time the user interacts with you in this workspace, these rules are active and must be strictly followed.
> Whenever the user performs, verifies, or describes an important step, decision, training run, or successful procedure, you **MUST immediately record and persist it** into the appropriate project documentation files (`GUIDE.md`, `README.md`, `workspace/DECISIONS.md`, and transcript archives). Never leave important user milestones or verified procedures trapped only in chat history.

---

## 1. Documentation & File Updating Mandate

1. **Automatic Documentation Maintenance:**
   - If the user reports that a command, script, model run, or configuration worked, check whether it impacts the workflow. If so, immediately update:
     - `GUIDE.md` (both in the root `files/` and in `sa-tutor-kit/sa-tutor-kit/GUIDE.md`)
     - `README.md` (both in the root `files/` and in `sa-tutor-kit/sa-tutor-kit/README.md`)
     - `workspace/DECISIONS.md`
   - Keep all mirrors synchronized. If a change affects `sa-tutor-kit/`, ensure the root and internal copies match.

2. **No Data Loss / Immutable Pipeline Stages:**
   - The kit folder (`sa-tutor-kit/`) holds the code and pipeline tools.
   - The `workspace/` folder inside it (`sa-tutor-kit/sa-tutor-kit/workspace/`, created in Phase 0) holds **all user data**.
   - **Scripts must never overwrite an earlier step:** each pipeline stage reads from one folder and writes to the next (e.g., `raw/` -> `text/` -> `items/` -> `gen/` -> `verified/` -> `build/` -> `runs/` -> `exports/`). This guarantees that you can always walk backwards to diagnose any data or logic issue.

---

## 2. Infrastructure & Compute Rules

1. **Always Enable Spot VMs (Preemptible Instances):**
   - Spot VMs offer a **60% to 70% discount** off standard Google Cloud hourly GPU rates.
   - Fine-tuning with Unsloth saves checkpoints after each epoch to Google Drive, so even if a Spot VM is reclaimed, you resume with zero lost progress (`--resume`).

2. **Use Vertex AI Colab Enterprise for Training:**
   - Standard consumer Colab Pro ($9.99/mo) requires an external cash subscription and cannot consume Google Cloud credits.
   - **Vertex AI Colab Enterprise** inside Google Cloud Console directly consumes promotional Google Cloud & Gen AI credits ($10/month rolling grants, up to $60 balance) down to $0.00.
   - Workhorse GPU: **NVIDIA L4 (24GB VRAM)**. Fast Ada Lovelace architecture, runs 27B models in 4-bit QLoRA.
   - Pre-flight check: Verify that NVIDIA L4 GPU quota is requested and set to at least 1 in Google Cloud Console (`IAM & Admin > Quotas`).

3. **Deploy on Google Cloud Run with Scale-to-Zero:**
   - Dedicated 24/7 Compute Engine VMs or Vertex Prediction endpoints cost ~$20+/day and drain credits in < 3 days.
   - Deploy `koeberg-stage-1` (27B) containerized (Ollama / vLLM) on **Google Cloud Run** with Serverless NVIDIA L4 GPU.
   - Configure with `--min-instances 0` so it scales down to **$0.00/hour** when idle, billing only per second of active user chatting (~$0.015/minute).

---

## 3. Eishkom Stage 1 Model Architecture & Branding

1. **Clean Branding Rule:**
   - Public model names **must never display parameter numbers or quantization suffixes** (`27B`, `4B`, `Q4`, `Q6` do not show in user-facing brand names).
   - Use clean, stage-based release naming:
     - **`koeberg-stage-1`**: Flagship Cloud (27B, `UD-Q4_K_XL`, ~17.6 GB)
     - **`kendal-stage-1`**: Budget PC & Laptop (4B, `Q6_K` / `UD-Q6_K_XL`, ~3.53–4.15 GB)
     - **`kendal-flash-stage-1`**: General Mobile & Phones (4B, `Q4_K_M`, ~2.78–2.91 GB)
     - **`gariep-stage-1`**: Budget Phone Tutor (2B, `Q6_K` / `Q8_0`, ~1.75–2.15 GB)
     - **`gariep-flash-stage-1`**: Budget Vision/OCR (LiquidAI LFM3-VL 2B, `Q6_K`, ~1.55 GB)
   - Releases use Stage cycles (`stage-1`, `stage-1.1`, `stage-2`) rather than point increments.

2. **Base Repositories vs. GGUF Files:**
   - **Never pass a `-GGUF` repository or file to `train_sft.py`.** GGUF files are compiled, read-only inference files for llama.cpp/Ollama and cannot be trained.
   - Always fine-tune unquantized base Hugging Face repositories (`unsloth/Qwen3.8-27B`, `unsloth/Qwen3.5-4B`, `empero-ai/Qwen3.8-4B-Distill`, `empero-ai/Qwen3.8-2B-Distill`, `LiquidAI/LFM3-VL-2B`) using Unsloth QLoRA.
   - Export to GGUF (UD-Q4_K_XL, Q6_K, Q4_K_M) at the end of the training run via `training/export_gguf.py`.
   - Single-run export: From a single 4B training run, export both `kendal-stage-1` (Q6) and `kendal-flash-stage-1` (Q4) in minutes.

3. **Cross-Tier Distillation Trick:**
   - Train `koeberg-stage-1` (27B) first on the core South African CAPS dataset.
   - Use fine-tuned Koeberg to generate 2,000–5,000 step-by-step verified solutions to hard DBE past paper questions.
   - Add these solutions into `dataset.jsonl` to train `kendal-stage-1` (4B) and `gariep-stage-1` (2B), transferring 27B reasoning down to the smaller models.

4. **Pedagogical Standards:**
   - CAPS curriculum aligned for Grades 7–12.
   - Teach, do not just solve: hint ladder, diagnose before explaining, ask one question at a time and wait.
   - Socratic guidance with English and Afrikaans (Huistaal and FAL) support.

