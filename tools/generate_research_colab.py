#!/usr/bin/env python3
import json
import os

notebook = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Eishkom Stage 1: Gariep 2B Runner (Google Colab Research - NVIDIA T4 / Consumer GPU)\n",
                "Open this notebook in [Google Colab Research](https://colab.research.google.com) on a standard **NVIDIA T4 GPU** (15GB VRAM).\n",
                "\n",
                "### Hardware & Optimization Strategy for Gariep 2B:\n",
                "- **Target Model:** `empero-ai/Qwen3.8-2B-Distill` (`gariep-stage-1`).\n",
                "- **T4 Hardware Utilization:** 2B in 4-bit QLoRA is tiny (~1.5GB base weights). We saturate the 15GB VRAM by running `batch_size = 8` and `grad_accum = 2`.\n",
                "- **Speed:** Full 3-epoch training across all 5,755 South African CAPS samples finishes in **~20-25 minutes**.\n",
                "- **Multi-Quant Export:** Exports **Q8_0, Q6_K, pure Q4_K, and Q4_K_M** from the single trained adapter in minutes."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# 1. Verify NVIDIA T4 GPU\n",
                "!nvidia-smi"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 2. Setup Workspace & Unpack Gariep Kit\n",
                "Upload `gariep_colab_research_kit.zip` to the **Files** panel on the left."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# 2. Setup workspace & unpack kit\n",
                "import os, shutil, zipfile\n",
                "\n",
                "if os.path.exists('gariep_colab_research_kit.zip'):\n",
                "    print('Unpacking gariep_colab_research_kit.zip onto SSD...')\n",
                "    with zipfile.ZipFile('gariep_colab_research_kit.zip', 'r') as z:\n",
                "        z.extractall('.')\n",
                "    print('✅ Gariep 2B Kit unpacked successfully!')\n",
                "elif os.path.exists('eishkom_colab_kit.zip'):\n",
                "    print('Unpacking eishkom_colab_kit.zip...')\n",
                "    with zipfile.ZipFile('eishkom_colab_kit.zip', 'r') as z:\n",
                "        z.extractall('.')\n",
                "    print('✅ Kit unpacked!')\n",
                "else:\n",
                "    print('TIP: Please drag and drop gariep_colab_research_kit.zip into the Files panel on the left!')\n",
                "\n",
                "os.environ['SA_WORKSPACE'] = os.path.abspath('workspace')\n",
                "print('Workspace active at:', os.environ['SA_WORKSPACE'])\n"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 3. Install Fast Training Tools (about 2 minutes)\n",
                "Installs Unsloth fast patching, PyTorch utilities, and SymPy for mathematical verification."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "!pip install -q unsloth\n",
                "!pip install -q sympy pypdf matplotlib\n"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 4. Hugging Face Login (Optional)\n",
                "Only required if accessing private or gated repositories."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "from huggingface_hub import login\n",
                "# login()  # Uncomment if needed\n"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 5. Dry Run Smoke Test (5 seconds)\n",
                "Verifies tokenizer, prompt formatting, and dataset loading before starting the GPU training run."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "!python training/train_sft.py --model empero-ai/Qwen3.8-2B-Distill --data workspace/build/r1 --load-4bit --dry-run --show 2\n"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 6. TRAIN Gariep 2B on NVIDIA T4 GPU (~20–25 minutes)\n",
                "Trains `gariep-stage-1` for 3 epochs on all 5,755 CAPS SFT samples.\n",
                "Hardware configuration: `batch=8, grad_accum=2` saturates ~10–12 GB VRAM for maximum throughput with zero browser freezing."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Gariep 2B: Full training run\n",
                "!python training/train_sft.py --model empero-ai/Qwen3.8-2B-Distill --data workspace/build/r1 --out workspace/runs/r1-gariep --load-4bit --epochs 3 --batch 8 --grad-accum 2 --show 0\n"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 7. EXPORT GGUF Models (Multi-Quant: Q8_0, Q6_K, pure Q4_K, Q4_K_M)\n",
                "Compiles all requested quantization formats directly from your trained adapter in one pass:\n",
                "- **Q8_0**: Maximum 2B reasoning quality.\n",
                "- **Q6_K**: High fidelity for budget PCs/laptops.\n",
                "- **Q4_K**: Pure K-quantization variant without sub-modifiers.\n",
                "- **Q4_K_M**: Mobile format for phones and low-RAM devices (~1.3 GB)."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "!python training/export_gguf.py --adapter workspace/runs/r1-gariep/adapter --out workspace/exports/gariep-stage-1 --quants q8_0 q6_k q4_k q4_k_m\n"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 8. Package & Download Models and Training Runs\n",
                "Packages all GGUF models and adapter weights into clean archives for easy 1-click download."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "import os, zipfile\n",
                "from google.colab import files\n",
                "\n",
                "# 1. Package all exported GGUF models into one archive\n",
                "gguf_zip = '/content/gariep_stage1_gguf_models.zip'\n",
                "with zipfile.ZipFile(gguf_zip, 'w', zipfile.ZIP_STORED) as z:\n",
                "    for root, dirs, files_list in os.walk('/content/workspace/exports'):\n",
                "        for f in files_list:\n",
                "            if f.endswith('.gguf'):\n",
                "                p = os.path.join(root, f)\n",
                "                z.write(p, arcname=os.path.basename(p))\n",
                "\n",
                "# 2. Package adapter, loss plot, and training metrics\n",
                "run_zip = '/content/gariep_stage1_adapter_and_loss.zip'\n",
                "with zipfile.ZipFile(run_zip, 'w', zipfile.ZIP_DEFLATED) as z:\n",
                "    for root, dirs, files_list in os.walk('/content/workspace/runs/r1-gariep'):\n",
                "        for f in files_list:\n",
                "            p = os.path.join(root, f)\n",
                "            z.write(p, arcname=os.path.relpath(p, '/content/workspace'))\n",
                "\n",
                "if os.path.exists(gguf_zip):\n",
                "    print(f'✅ Created {gguf_zip} ({os.path.getsize(gguf_zip)/(1024*1024):.1f} MB)')\n",
                "if os.path.exists(run_zip):\n",
                "    print(f'✅ Created {run_zip} ({os.path.getsize(run_zip)/(1024*1024):.1f} MB)')\n",
                "    print('⬇️ Downloading adapter & metrics archive to browser...')\n",
                "    files.download(run_zip)\n",
                "\n",
                "print('\\nDone! To download the GGUF models, right-click gariep_stage1_gguf_models.zip in the Files panel or copy to Google Drive.')\n"
            ]
        }
    ],
    "metadata": {
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python"},
        "colab": {"provenance": []}
    },
    "nbformat": 4,
    "nbformat_minor": 5
}

with open("sa_tutor_colab_research.ipynb", "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=1)

os.makedirs("sa-tutor-kit/sa-tutor-kit/colab", exist_ok=True)
with open("sa-tutor-kit/sa-tutor-kit/colab/sa_tutor_colab_research.ipynb", "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=1)

print("Generated sa_tutor_colab_research.ipynb successfully!")

