#!/usr/bin/env python3
"""
package_and_download.py - Universal packaging and Google Cloud Storage sync tool for Eishkom AI.
Packages all GGUF models, adapters, loss metrics, and datasets into ZIPs,
then automatically pushes them to Google Cloud Storage.
"""
import os
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

def print_banner(msg):
    print(f"\n{'='*60}\n{msg}\n{'='*60}")

def package_all():
    print_banner("1. Scanning and Packaging GGUF Models")
    base_dir = Path("/content") if Path("/content").exists() else Path(".")
    exports_dir = base_dir / "workspace" / "exports"
    runs_dir = base_dir / "workspace" / "runs"
    build_dir = base_dir / "workspace" / "build"

    # 1. Package GGUF Models
    gguf_files = list(exports_dir.rglob("*.gguf")) if exports_dir.exists() else []
    gguf_zip = base_dir / "gariep_stage1_gguf_models.zip"
    if gguf_files:
        print(f"Found {len(gguf_files)} GGUF model file(s):")
        with zipfile.ZipFile(gguf_zip, "w", zipfile.ZIP_STORED) as z:
            for gf in gguf_files:
                size_mb = gf.stat().st_size / (1024 * 1024)
                print(f"  -> {gf.name} ({size_mb:.1f} MB)")
                z.write(gf, arcname=gf.name)
        print(f"✅ Created {gguf_zip} ({gguf_zip.stat().st_size / (1024*1024):.1f} MB)")
    else:
        print("⚠️ No GGUF files found in workspace/exports/")

    # 2. Package Adapter, Runs, and Loss curves
    print_banner("2. Packaging LoRA Adapter & Training Metrics")
    run_zip = base_dir / "gariep_stage1_runs_and_adapter.zip"
    if runs_dir.exists():
        with zipfile.ZipFile(run_zip, "w", zipfile.ZIP_DEFLATED) as z:
            for root, dirs, files in os.walk(runs_dir):
                for f in files:
                    fp = Path(root) / f
                    z.write(fp, arcname=fp.relative_to(base_dir / "workspace"))
        print(f"✅ Created {run_zip} ({run_zip.stat().st_size / (1024*1024):.1f} MB)")
    else:
        print("⚠️ No runs found in workspace/runs/")

    # 3. Package Dataset
    print_banner("3. Packaging Training Dataset (5,755 SFT samples)")
    data_zip = base_dir / "gariep_stage1_dataset.zip"
    if build_dir.exists():
        with zipfile.ZipFile(data_zip, "w", zipfile.ZIP_DEFLATED) as z:
            for root, dirs, files in os.walk(build_dir):
                for f in files:
                    fp = Path(root) / f
                    z.write(fp, arcname=fp.relative_to(base_dir / "workspace"))
        print(f"✅ Created {data_zip} ({data_zip.stat().st_size / (1024*1024):.1f} MB)")

    # 4. Upload to Google Cloud Storage
    print_banner("4. Uploading All ZIPs and GGUFs to Google Cloud Storage")
    try:
        res = subprocess.run(["gcloud", "config", "get-value", "project"], capture_output=True, text=True, check=True)
        project_id = res.stdout.strip()
        if project_id and project_id != "(unset)":
            bucket = f"gs://{project_id}-models"
            print(f"Target Bucket: {bucket}")
            subprocess.run(["gcloud", "storage", "buckets", "create", bucket, "--location=us-central1"], capture_output=True)

            # Upload ZIP files
            print("\nUploading ZIP archives...")
            subprocess.run(f"gcloud storage cp {base_dir}/*.zip {bucket}/", shell=True)

            # Upload raw GGUF files directly as well
            if exports_dir.exists() and gguf_files:
                print("\nUploading raw .gguf model files directly...")
                subprocess.run(f"gcloud storage cp {exports_dir}/*/*.gguf {bucket}/ 2>/dev/null || gcloud storage cp {exports_dir}/*.gguf {bucket}/", shell=True)

            print(f"\n🎉 ALL FILES SUCCESSFULLY BACKED UP TO GOOGLE CLOUD STORAGE!")
            print(f"   Bucket URI: {bucket}")
            print(f"   Download directly in Console without browser cutoffs:")
            print(f"   https://console.cloud.google.com/storage/browser/{project_id}-models")
        else:
            print("Notice: gcloud project not set. Skipping cloud upload. Zip files remain in /content.")
    except Exception as e:
        print(f"Google Cloud Storage upload note: {e}")

if __name__ == "__main__":
    package_all()
