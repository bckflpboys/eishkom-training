import json
import os
import zipfile
from pathlib import Path

def update_notebook(path):
    with open(path, "r", encoding="utf-8") as f:
        nb = json.load(f)

    for c in nb["cells"]:
        src = "".join(c.get("source", []))
        if "eishkom_colab_kit.zip" in src or "SA_WORKSPACE" in src:
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
                "elif os.path.exists('workspace/build/r1'):\n",
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
        elif "overfit" in src and "train_sft.py" in src:
            c["source"] = [
                "ROUND = globals().get('ROUND', 'r1')\n",
                "MODEL = globals().get('MODEL', 'unsloth/Qwen3.5-4B')\n",
                "!python training/train_sft.py --model {MODEL} --data workspace/build/{ROUND} --out workspace/runs/overfit --limit 20 --epochs 15 --show 0\n"
            ]
        elif "train_sft.py" in src and "--epochs 3" in src:
            c["source"] = [
                "ROUND = globals().get('ROUND', 'r1')\n",
                "MODEL = globals().get('MODEL', 'unsloth/Qwen3.5-4B')\n",
                "# VRAM Auto-Scaler automatically tunes batch size for 1B/2B/4B/27B for max speed without OOM\n",
                "!python training/train_sft.py --model {MODEL} --data workspace/build/{ROUND} --out workspace/runs/{ROUND} --load-4bit --epochs 3 --show 0\n"
            ]
        elif "evaluate.py" in src and "--adapter" in src:
            c["source"] = [
                "ROUND = globals().get('ROUND', 'r1')\n",
                "MODEL = globals().get('MODEL', 'unsloth/Qwen3.5-4B')\n",
                "!python eval/evaluate.py --name {ROUND} --backend hf --model {MODEL} --adapter workspace/runs/{ROUND}/adapter --compare base-qwen35-4b --ceiling teacher --analyze\n"
            ]
        elif "run_eval.py" in src and "--n 5" in src:
            c["source"] = [
                "ROUND = globals().get('ROUND', 'r1')\n",
                "MODEL = globals().get('MODEL', 'unsloth/Qwen3.5-4B')\n",
                "!python eval/run_eval.py --name {ROUND}-n5 --backend hf --model {MODEL} --adapter workspace/runs/{ROUND}/adapter --tags core --n 5 --temperature 0.7\n",
                "!python eval/score_eval.py --name {ROUND}-n5\n"
            ]
        elif "export_gguf.py" in src and "kendal-stage-1" in src:
            c["source"] = [
                "ROUND = globals().get('ROUND', 'r1')\n",
                "# Export Kendal Desktop (Q6_K), Kendal Q4_K (pure K), and Kendal Flash Mobile (Q4_K_M) from 1 run:\n",
                "!python training/export_gguf.py --adapter workspace/runs/{ROUND}/adapter --out workspace/exports/kendal-stage-1 --quants q6_k q4_k q4_k_m\n\n",
                "# If exporting Koeberg (27B), export UD-Q4_K_XL, Q4_K and Q4_K_M for Cloud Run:\n",
                "# !python training/export_gguf.py --adapter workspace/runs/r1-koeberg/adapter --out workspace/exports/koeberg-stage-1 --quants ud-q4_k_xl q4_k q4_k_m\n\n",
                "# If exporting Gariep (2B), export Q8_0, Q6_K, Q4_K and Q4_K_M:\n",
                "# !python training/export_gguf.py --adapter workspace/runs/r1-gariep/adapter --out workspace/exports/gariep-stage-1 --quants q8_0 q6_k q4_k q4_k_m\n"
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

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        # Add root python files
        for fname in file_list:
            fpath = kit_root / fname
            if fpath.exists():
                z.write(fpath, arcname=fname)
                print(f"Added {fname}")

        # Add tools folder
        tools_path = Path("tools/package_and_download.py")
        if tools_path.exists():
            z.write(tools_path, arcname="tools/package_and_download.py")
            print("Added tools/package_and_download.py")

        # Add folders
        for folder in folders_to_include:
            fdir = kit_root / folder
            if fdir.exists():
                for p in fdir.rglob("*"):
                    if p.is_file() and "__pycache__" not in p.parts:
                        rel = p.relative_to(kit_root)
                        z.write(p, arcname=str(rel).replace("\\", "/"))
                        print(f"Added {rel}")

        # Add workspace build r1 data
        r1_dir = kit_root / "workspace" / "build" / "r1"
        if not r1_dir.exists():
            r1_dir = Path("workspace/build/r1")
        if r1_dir.exists():
            for p in r1_dir.glob("*.json*"):
                arcname = f"workspace/build/r1/{p.name}"
                z.write(p, arcname=arcname)
                print(f"Added {arcname}")

    print(f"\nSuccessfully repacked {zip_path} (size: {zip_path.stat().st_size / (1024*1024):.2f} MB)")

if __name__ == "__main__":
    update_notebook("sa_tutor_colab.ipynb")
    update_notebook("sa-tutor-kit/sa-tutor-kit/colab/sa_tutor_colab.ipynb")
    repack_colab_kit()

