# Eishkom Stage 1 — Model Architecture & Distillation Specifications

> **Release Cycle:** Stage 1  
> **Brand Family:** Eishkom AI  
> **Pedagogical Standard:** South African CAPS Curriculum (Grades 7–12)  
> **Supported Languages:** English (Home Language & FAL) & Afrikaans (Huistaal & EAT)

---

## 1. Clean Branding Mandate

In compliance with our brand guidelines:
- Public-facing model identifiers **must never include parameter sizes or quantization tags**.
- Users interact with clean, stage-based names:
  - `koeberg-stage-1`
  - `kendal-stage-1`
  - `kendal-flash-stage-1`
  - `gariep-stage-1`
  - `gariep-flash-stage-1`
- The technical parameter size and quantization level are internal engineering details, not customer-facing product names.

---

## 2. Model Specifications Matrix

### 1. `koeberg-stage-1` (Flagship Cloud Tutor)
- **Role:** High-reasoning teacher model, capable of complex Euclidean geometry proofs, multi-step stoichiometry, advanced calculus, and cross-tier dataset generation.
- **Base Architecture:** `unsloth/Qwen3.8-27B` (Unquantized Hugging Face base repo).
- **Training Method:** Unsloth 4-bit QLoRA on Vertex AI Colab Enterprise with NVIDIA L4 GPU (24GB VRAM).
- **Export Format:** `UD-Q4_K_XL` (Unsloth Dynamic Q4 GGUF).
- **Disk Size:** ~17.6 GB.
- **Target Deployment:** Google Cloud Run with Serverless NVIDIA L4 GPU (`--min-instances 0` for scale-to-zero at $0.00/hr idle).

### 2. `kendal-stage-1` (Budget PC & High-Quality Offline Tutor)
- **Role:** Primary offline model for South African high schools, computer labs, and teacher laptops. High reasoning with full Socratic dialogue capabilities.
- **Base Architecture:** `unsloth/Qwen3.5-4B` (Unquantized Hugging Face base repo).
- **Training Method:** Unsloth QLoRA on NVIDIA L4 GPU Spot VM (~1.0 hr).
- **Export Format:** `Q6_K` or `UD-Q6_K_XL` GGUF.
- **Disk Size:** ~3.53–4.15 GB.
- **Target Hardware:** Desktops with GTX 1650 (4GB VRAM) or budget laptops with 16GB/20GB system RAM.

### 3. `kendal-flash-stage-1` (Midrange Smartphone & Phone Profile)
- **Role:** High-speed mobile tutor for students studying on mid-tier Android smartphones (6GB–8GB RAM).
- **Base Architecture:** Fine-tuned from the same 4B training run as `kendal-stage-1`.
- **Export Format:** `Q4_K_M` GGUF.
- **Disk Size:** ~2.78–2.91 GB.
- **Single-Run Multi-Quant Export:** Generated in minutes from the `kendal-stage-1` LoRA weights without retraining.
- **Target Hardware:** Android phones (via PocketPal AI, Termux, or custom Flutter app) & 4GB PCs.

### 4. `gariep-stage-1` (Ultra-Budget Phone Tutor)
- **Role:** Accessible AI tutor for students on low-cost entry smartphones (3GB–4GB RAM) with zero data connection.
- **Base Architecture:** `empero-ai/Qwen3.8-2B-Distill` *(or unsloth 2B)*.
- **Training Method:** Unsloth QLoRA on NVIDIA L4 GPU Spot VM (~35 mins).
- **Export Format:** `Q6_K` or `Q8_0` GGUF.
- **Disk Size:** ~1.75–2.15 GB.
- **Target Hardware:** Budget Android devices (100% offline, fits in RAM alongside Android OS).

### 5. `gariep-flash-stage-1` (Budget Vision & OCR Specialist)
- **Role:** Multi-modal image interpreter for reading diagrams, exam scans, and student handwriting.
- **Base Architecture:** `LiquidAI/LFM3-VL-2B` (Liquid AI Edge Multi-Modal architecture).
- **Export Format:** `Q6_K` GGUF + `mmproj-gariep-flash-stage-1.gguf`.
- **Disk Size:** ~1.55 GB.
- **Target Hardware:** Mobile and laptop edge devices for visual tutoring.

---

## 3. Base Repositories vs. GGUF Files

> [!WARNING]
> **Fundamental Engineering Rule:** Never supply a compiled `-GGUF` repository (such as `unsloth/Qwen3.8-27B-GGUF` or `empero-ai/Qwen3.8-4B-Distill-GGUF`) to `train_sft.py`.
> GGUF is a compiled, read-only inference format designed for llama.cpp and Ollama. PyTorch cannot compute backward gradients or update LoRA adapters on GGUF files.

**The Workflow:**
```
[Base Hugging Face Repo] ──> [Unsloth 4-bit QLoRA Training] ──> [Fine-Tuned Adapters] ──> [export_gguf.py] ──> [Final Stage 1 GGUF Files]
  unsloth/Qwen3.8-27B             Vertex AI Colab Enterprise        workspace/runs/          Single-Run Multi-Quant     koeberg-stage-1-UD-Q4_K_XL.gguf
  unsloth/Qwen3.5-4B              NVIDIA L4 Spot VM ($0.32/hr)                                                          kendal-stage-1-Q6_K.gguf
  empero-ai/Qwen3.8-2B-Distill                                                                                          kendal-flash-stage-1-Q4_K_M.gguf
                                                                                                                        gariep-stage-1-Q6_K.gguf
```

---

## 4. Cross-Tier Knowledge Distillation Workflow

To achieve state-of-the-art pedagogical reasoning on mobile models (4B and 2B):
1. **Train Koeberg First:** Fine-tune `koeberg-stage-1` (27B) on the verified curriculum corpus.
2. **Generate Hard Problem Solutions:** Use fine-tuned Koeberg to generate detailed, Socratic step-by-step teacher explanations for 2,000–5,000 of the hardest DBE exam questions (Grade 11–12 Mathematics Paper 2 geometry, Physical Sciences Newton's laws, and Afrikaans grammar).
3. **Automated Verification:** Check Koeberg's answers against the DBE memorandums using SymPy and regex checkers (`pipeline/verify.py`).
4. **Distillation Injection:** Append these verified 27B reasoning traces into `workspace/build/r1/train.jsonl`.
5. **Train Kendal & Gariep:** Fine-tune `kendal-stage-1` (4B) and `gariep-stage-1` (2B) on this augmented dataset, transferring 27B-level reasoning down to compact models for under \$1.00 in extra GPU compute.

