#!/usr/bin/env python3
"""
package_and_download.py - All-in-one cleanup, verification, and single-click packaging tool for Eishkom AI.
Run in Colab (in Terminal without ! or in a Notebook cell):
    python tools/package_and_download.py
"""
import os
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

def run_cmd(cmd):
    print(f"\n$ {' '.join(cmd) if isinstance(cmd, list) else cmd}")
    res = subprocess.run(cmd, shell=isinstance(cmd, str), capture_output=True, text=True)
    if res.stdout:
        print(res.stdout.strip())
    if res.stderr:
        print(res.stderr.strip())
    return res

def clean_disk():
    print("\n--- 1. Cleaning OS Root Disk Cache ---")
    hf_cache = Path("/root/.cache/huggingface/hub")
    if hf_cache.exists():
        size_gb = sum(f.stat().st_size for f in hf_cache.rglob('*') if f.is_file()) / (1024**3)
        shutil.rmtree(str(hf_cache), ignore_errors=True)
        print(f"-> Freed {size_gb:.2f} GB from /root/.cache/huggingface/hub!")
    else:
        print("-> /root/.cache/huggingface/hub is already clean.")

    total, used, free = shutil.disk_usage("/content" if os.path.exists("/content") else ".")
    print(f"-> Available on SSD disk: {free / (1024**3):.1f} GB of {total / (1024**3):.1f} GB")

def check_and_fix_gguf():
    print("\n--- 2. Checking GGUF Models & Merged Weights ---")
    export_dir = Path("workspace/exports/kendal-stage-1")
    gguf_dir = Path("workspace/exports/kendal-stage-1_gguf")

    files = list(gguf_dir.glob("*.gguf")) if gguf_dir.exists() else []
    files += list(export_dir.glob("*.gguf")) if export_dir.exists() else []

    needs_conversion = False
    if not files:
        needs_conversion = True
    else:
        for f in files:
            mb = f.stat().st_size / (1024 * 1024)
            print(f"  Found: {f.name} ({mb:.1f} MB)")
            if mb < 500:  # Under 500 MB for a 4B model means only adapter/projector was converted
                needs_conversion = True

    if needs_conversion:
        print("\n[Notice] GGUF file is small (~65MB). Re-converting merged full weights into complete GGUF...")
        merged_dir = None
        for candidate in [export_dir, export_dir / "merged", Path("workspace/runs/r1")]:
            if candidate.exists() and list(candidate.glob("*.safetensors")):
                merged_dir = candidate
                break

        if not merged_dir or not any("model" in f.name for f in merged_dir.glob("*.safetensors")):
            print("Merging LoRA adapter with base model unsloth/Qwen3.5-4B into full 16-bit weights...")
            try:
                from unsloth import FastLanguageModel
                adapter_path = "workspace/runs/r1/adapter"
                model, tok = FastLanguageModel.from_pretrained(model_name=adapter_path, max_seq_length=4096, load_in_4bit=False)
                tokenizer = getattr(tok, "tokenizer", tok)
                export_dir.mkdir(parents=True, exist_ok=True)
                print("Exporting full model directly via save_pretrained_gguf...")
                model.save_pretrained_gguf(str(export_dir), tokenizer, quantization_method=["q6_k", "q4_k_m"])
            except Exception as e:
                print(f"Unsloth direct export encountered: {e}")
        else:
            print(f"Found merged weights in {merged_dir}. Converting with llama.cpp...")
            llama_cpp = Path("/root/.unsloth/llama.cpp")
            converter = llama_cpp / "convert_hf_to_gguf.py"
            if converter.exists():
                f16_path = export_dir / "kendal-stage-1-f16.gguf"
                run_cmd([sys.executable, str(converter), str(merged_dir), "--outfile", str(f16_path), "--outtype", "f16"])
                quantizer = llama_cpp / "llama-quantize"
                if not quantizer.exists():
                    quantizer = llama_cpp / "build/bin/llama-quantize"
                if quantizer.exists():
                    for q in ["Q6_K", "Q4_K_M"]:
                        out_q = export_dir / f"kendal-stage-1-{q}.gguf"
                        run_cmd([str(quantizer), str(f16_path), str(out_q), q])
                    if f16_path.exists():
                        f16_path.unlink()

def create_zip_packages():
    print("\n--- 3. Creating Single-Click Download Packages (ZIP) ---")
    packages = []

    # 1. Package: Adapter + Training Metrics + Loss Curve (~80MB)
    r1_dir = Path("workspace/runs/r1")
    if r1_dir.exists():
        zip_r1 = Path("kendal_stage1_adapter_and_runs.zip")
        with zipfile.ZipFile(zip_r1, "w", zipfile.ZIP_DEFLATED) as z:
            for f in r1_dir.rglob("*"):
                if f.is_file() and not f.name.endswith(".tmp"):
                    rel = f.relative_to(r1_dir.parent)
                    z.write(f, arcname=str(rel))
        size_mb = zip_r1.stat().st_size / (1024 * 1024)
        print(f"-> Created: {zip_r1} ({size_mb:.1f} MB)")
        packages.append(zip_r1)

    # 2. Package: Complete Training Dataset (5,755 items)
    build_dir = Path("workspace/build/r1")
    if build_dir.exists():
        zip_data = Path("eishkom_stage1_dataset.zip")
        with zipfile.ZipFile(zip_data, "w", zipfile.ZIP_DEFLATED) as z:
            for f in build_dir.rglob("*"):
                if f.is_file():
                    rel = f.relative_to(build_dir.parent)
                    z.write(f, arcname=str(rel))
        size_mb = zip_data.stat().st_size / (1024 * 1024)
        print(f"-> Created: {zip_data} ({size_mb:.1f} MB)")
        packages.append(zip_data)

    # 3. Package: GGUF Models (Stored without recompression)
    for p in [Path("workspace/exports/kendal-stage-1"), Path("workspace/exports/kendal-stage-1_gguf")]:
        if p.exists():
            ggufs = list(p.glob("*.gguf"))
            if ggufs:
                zip_models = Path("kendal_stage1_gguf_models.zip")
                with zipfile.ZipFile(zip_models, "w", zipfile.ZIP_STORED) as z:
                    for g in ggufs:
                        z.write(g, arcname=g.name)
                        print(f"   Packed model: {g.name} ({g.stat().st_size / (1024*1024):.1f} MB)")
                size_mb = zip_models.stat().st_size / (1024 * 1024)
                print(f"-> Created: {zip_models} ({size_mb:.1f} MB)")
                packages.append(zip_models)
                break

    print("\n=== All Packages Ready For Download! ===")
    for p in packages:
        print(f"📦 {p.name} ({p.stat().st_size / (1024*1024):.1f} MB)")
    print("\nTo download them to your computer, simply right-click each of the 3 ZIP files in the left sidebar and click Download!")

if __name__ == "__main__":
    clean_disk()
    check_and_fix_gguf()
    create_zip_packages()

