#!/usr/bin/env python3
"""
tools/harden_notebook_and_scripts.py - Update Colab notebooks and repack colab kit for Stage 2 (r2).
"""
import json
import os
import shutil
import zipfile
from pathlib import Path

def update_notebook(path):
    with open(path, "r", encoding="utf-8") as f:
        nb = json.load(f)

    for c in nb["cells"]:
        src = "".join(c.get("source", []))
        if c.get("cell_type") == "markdown":
            if "# Eishkom Stage 1: Colab Runner" in src:
                c["source"] = [
                    "# Eishkom Stage 1 & Stage 2: Colab Runner (Vertex AI Colab Enterprise & Free Colab)\n",
                    "Open this notebook in **Vertex AI Colab Enterprise** (funded by your **$60 Google Cloud credits**) or free Google Colab.\n",
                    "Run the cells from top to bottom, **one at a time**, and inspect what each prints.\n\n",
                    "### Hardware & Budget Recommendations:\n",
                    "- **Vertex AI Colab Enterprise (Recommended):** Choose an **NVIDIA L4 GPU (24GB VRAM)** with **Spot VM pricing** (~$0.32/hr).\n",
                    "  - Zero random browser disconnects.\n",
                    "  - Large 24GB VRAM allows training **koeberg (27B)** in ~5.5 hrs (~$1.76) and **kendal (4B)** in ~1 hr for r1 / ~5.2 hrs for r2 (~$1.66).\n",
                    "  - *Quota Note:* Before first run, request NVIDIA L4 GPU quota = 1 in GCP Console (IAM & Admin > Quotas).\n",
                    "- **Free Google Colab ($0):** Standard NVIDIA T4 (15GB usable VRAM). Good for testing 4B and 2B models.\n\n",
                    "**Before you start:** upload `eishkom_colab_kit.zip` to the Files panel on the left.\n"
                ]
            elif "## 6. TRAIN Stage 1 Models" in src:
                c["source"] = [
                    "## 6. TRAIN Stage 1 & Stage 2 Models with Unsloth QLoRA\n",
                    "Fine-tune base models using Unsloth 4-bit QLoRA. Step 6a is a free dry-run that checks rendering and tokenizer alignment.\n\n",
                    "### Eishkom Model Lineup:\n",
                    "1. **Kendal (4B)**: `unsloth/Qwen3.5-4B` on L4 Spot VM (Budget PC & Mobile Tutor)\n",
                    "2. **Koeberg (27B)**: `unsloth/Qwen3.8-27B` on L4 Spot VM (Flagship Cloud Tutor)\n",
                    "3. **Gariep (2B)**: `empero-ai/Qwen3.8-2B-Distill` on L4 Spot VM (Budget Phone Tutor)\n",
                    "*(Tip: From a single 4B run, export both Kendal Desktop Q6_K and Kendal Flash Mobile Q4_K_M in minutes!)*\n"
                ]
            elif "## 9. EXPORT GGUF files" in src:
                c["source"] = [
                    "## 9. EXPORT GGUF files with clean Eishkom branding\n",
                    "Export deployable GGUF files for offline devices and Cloud Run.\n",
                    "**Clean Branding Rule:** Public model names must not show parameter or quant letters (e.g. `kendal-stage-2` and `kendal-flash-stage-2`).\n",
                    "From a single 4B training run, export both Q6_K, pure Q4_K, and Q4_K_M in minutes!\n"
                ]
        elif "eishkom_colab_kit.zip" in src or "SA_WORKSPACE" in src:
            c["source"] = [
                "# 2. Setup workspace & Manage Disks (Vertex AI Colab Enterprise & Free Colab)\n",
                "import os, shutil, zipfile\n\n",
                "# A. Clean up OS root disk (/root/.cache) to eliminate 'Disk is almost full' warning:\n",
                "if os.path.exists('/root/.cache/huggingface/hub'):\n",
                "    print('Cleaning root disk cache to free up space...')\n",
                "    shutil.rmtree('/root/.cache/huggingface/hub', ignore_errors=True)\n\n",
                "# B. Redirect all future Hugging Face downloads to the 100GB persistent SSD (/content):\n",
                "os.environ['HF_HOME'] = '/content/.cache/huggingface'\n",
                "os.makedirs('/content/.cache/huggingface', exist_ok=True)\n\n",
                "# C. Setup workspace:\n",
                "if os.path.exists('eishkom_colab_kit.zip'):\n",
                "    print('Unpacking eishkom_colab_kit.zip onto SSD...')\n",
                "    with zipfile.ZipFile('eishkom_colab_kit.zip', 'r') as zip_ref:\n",
                "        zip_ref.extractall('.')\n",
                "    os.environ['SA_WORKSPACE'] = os.path.abspath('workspace')\n",
                "    print('Workspace ready at:', os.environ['SA_WORKSPACE'])\n",
                "elif os.path.exists('workspace/build/r2') or os.path.exists('workspace/build/r1'):\n",
                "    os.environ['SA_WORKSPACE'] = os.path.abspath('workspace')\n",
                "    print('Workspace already active at:', os.environ['SA_WORKSPACE'])\n",
                "else:\n",
                "    print('TIP: Please upload eishkom_colab_kit.zip to the Files panel on the left!')\n\n",
                "# D. Display available disk space:\n",
                "total_ssd, used_ssd, free_ssd = shutil.disk_usage('/content')\n",
                "print(f'Persistent SSD Disk (/content): {free_ssd / (1024**3):.1f} GB available of {total_ssd / (1024**3):.1f} GB')\n",
                "total_root, used_root, free_root = shutil.disk_usage('/')\n",
                "print(f'Root OS Disk (/): {free_root / (1024**3):.1f} GB available of {total_root / (1024**3):.1f} GB')\n"
            ]
        elif "dry-run" in src and "train_sft.py" in src:
            c["source"] = [
                "# Choose target build split: 'r2' (Master Combined, 37k), 'r2_socratic' (25k), 'r2_fullsol' (10k), 'r2_agentic' (2k)\n",
                "ROUND = 'r2'\n",
                "# Choose base model: unsloth/Qwen3.5-4B (Kendal), unsloth/Qwen3.8-27B (Koeberg), empero-ai/Qwen3.8-2B-Distill (Gariep)\n",
                "MODEL = 'unsloth/Qwen3.5-4B'\n",
                "!python training/train_sft.py --model {MODEL} --data workspace/build/{ROUND} --load-4bit --dry-run --show 2\n"
            ]
        elif "overfit" in src and "train_sft.py" in src:
            c["source"] = [
                "ROUND = globals().get('ROUND', 'r2')\n",
                "MODEL = globals().get('MODEL', 'unsloth/Qwen3.5-4B')\n",
                "!python training/train_sft.py --model {MODEL} --data workspace/build/{ROUND} --out workspace/runs/overfit --limit 20 --epochs 15 --show 0\n"
            ]
        elif "train_sft.py" in src and "--epochs" in src and "overfit" not in src:
            c["source"] = [
                "ROUND = globals().get('ROUND', 'r2')\n",
                "MODEL = globals().get('MODEL', 'unsloth/Qwen3.5-4B')\n",
                "# For Master Combined r2 (37,179 samples), 1 epoch (~2,324 steps) is standard (~5.2 hrs on L4 GPU).\n",
                "# For smaller splits (e.g. r2_fullsol 10k), 1-2 epochs is recommended.\n",
                "EPOCHS = 1.0 if ROUND == 'r2' else 2.0\n",
                "# VRAM Auto-Scaler automatically tunes batch size for 1B/2B/4B/27B for max speed without OOM\n",
                "!python training/train_sft.py --model {MODEL} --data workspace/build/{ROUND} --out workspace/runs/{ROUND} --load-4bit --epochs {EPOCHS} --show 0\n"
            ]
        elif "evaluate.py" in src and "--adapter" in src:
            c["source"] = [
                "ROUND = globals().get('ROUND', 'r2')\n",
                "MODEL = globals().get('MODEL', 'unsloth/Qwen3.5-4B')\n",
                "!python eval/evaluate.py --name {ROUND} --backend hf --model {MODEL} --adapter workspace/runs/{ROUND}/adapter --compare base-qwen35-4b --ceiling teacher --analyze\n"
            ]
        elif "run_eval.py" in src and "--n 5" in src:
            c["source"] = [
                "ROUND = globals().get('ROUND', 'r2')\n",
                "MODEL = globals().get('MODEL', 'unsloth/Qwen3.5-4B')\n",
                "!python eval/run_eval.py --name {ROUND}-n5 --backend hf --model {MODEL} --adapter workspace/runs/{ROUND}/adapter --tags core --n 5 --temperature 0.7\n",
                "!python eval/score_eval.py --name {ROUND}-n5\n"
            ]
        elif "export_gguf.py" in src:
            c["source"] = [
                "ROUND = globals().get('ROUND', 'r2')\n",
                "STAGE_TAG = 'stage-2' if str(ROUND).startswith('r2') else 'stage-1'\n",
                "# 1. Export Kendal Desktop (Q6_K), Kendal Q4_K (pure K), and Kendal Flash Mobile (Q4_K_M) from 1 run:\n",
                "!python training/export_gguf.py --adapter workspace/runs/{ROUND}/adapter --out workspace/exports/kendal-{STAGE_TAG} --quants q6_k q4_k q4_k_m\n\n",
                "# 2. If exporting Koeberg (27B), export UD-Q4_K_XL, Q4_K and Q4_K_M for Cloud Run:\n",
                "# !python training/export_gguf.py --adapter workspace/runs/{ROUND}/adapter --out workspace/exports/koeberg-{STAGE_TAG} --quants ud-q4_k_xl q4_k q4_k_m\n\n",
                "# 3. If exporting Gariep (2B), export Q8_0, Q6_K, Q4_K and Q4_K_M:\n",
                "# !python training/export_gguf.py --adapter workspace/runs/{ROUND}/adapter --out workspace/exports/gariep-{STAGE_TAG} --quants q8_0 q6_k q4_k q4_k_m\n"
            ]
        elif "deploy koeberg" in src:
            c["source"] = [
                "# Cloud Run Deployment Command (run from Cloud Shell or local gcloud):\n",
                "# ROUND = globals().get('ROUND', 'r2')\n",
                "# STAGE_TAG = 'stage-2' if str(ROUND).startswith('r2') else 'stage-1'\n",
                "# gcloud run deploy koeberg-${STAGE_TAG} \\\n",
                "#   --image gcr.io/$PROJECT_ID/koeberg-${STAGE_TAG}:latest \\\n",
                "#   --gpu 1 \\\n",
                "#   --gpu-type nvidia-l4 \\\n",
                "#   --cpu 8 \\\n",
                "#   --memory 32Gi \\\n",
                "#   --min-instances 0 \\\n",
                "#   --max-instances 1 \\\n",
                "#   --region us-central1\n"
            ]

    with open(path, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1)
    print(f"Successfully updated {path}")

def repack_colab_kit():
    kit_root = Path("sa-tutor-kit/sa-tutor-kit")
    zip_path = Path("eishkom_colab_kit.zip")

    # Files to include in eishkom_colab_kit.zip
    file_list = [
        "answers.py",
        "board.py",
        "llm.py",
        "retrieval.py",
        "tools_sim.py",
        "tutor_data.py",
        "wspaths.py",
    ]

    folders_to_include = [
        "eval",
        "training",
    ]

    build_folders = [
        "r2",
        "r2_socratic",
        "r2_fullsol",
        "r2_agentic",
        "r1",
    ]

    print(f"\nBuilding {zip_path}...")
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        # Add root python files
        for fname in file_list:
            fpath = kit_root / fname
            if fpath.exists():
                z.write(fpath, arcname=fname)

        # Add tools helper
        tools_path = Path("tools/package_and_download.py")
        if tools_path.exists():
            z.write(tools_path, arcname="tools/package_and_download.py")

        # Add folders (training, eval)
        for folder in folders_to_include:
            fdir = kit_root / folder
            if fdir.exists():
                for p in fdir.rglob("*"):
                    if p.is_file() and "__pycache__" not in p.parts:
                        rel = p.relative_to(kit_root)
                        z.write(p, arcname=str(rel).replace("\\", "/"))

        # Add workspace build datasets
        for b_name in build_folders:
            b_dir = Path("workspace/build") / b_name
            if not b_dir.exists():
                b_dir = kit_root / "workspace" / "build" / b_name
            if b_dir.exists():
                print(f"Adding build folder: workspace/build/{b_name}...")
                for p in b_dir.glob("*"):
                    if p.is_file():
                        arcname = f"workspace/build/{b_name}/{p.name}"
                        z.write(p, arcname=arcname)

    size_mb = zip_path.stat().st_size / (1024 * 1024)
    print(f"\nSuccessfully repacked {zip_path} (size: {size_mb:.2f} MB)")

    # Mirror to sa-tutor-kit
    kit_zip = kit_root / "eishkom_colab_kit.zip"
    shutil.copy2(zip_path, kit_zip)
    print(f"Mirrored to {kit_zip}")

if __name__ == "__main__":
    update_notebook("sa_tutor_colab.ipynb")
    update_notebook("sa-tutor-kit/sa-tutor-kit/colab/sa_tutor_colab.ipynb")
    repack_colab_kit()
