#!/usr/bin/env python3
"""
export_gguf.py - turn your trained adapter into the files people actually run (GGUF), in several sizes.

    # Koeberg Flagship Cloud (27B) -> UD-Q4_K_XL for Cloud Run / PC CPU
    python training/export_gguf.py --adapter workspace/runs/r1-koeberg/adapter --out workspace/exports/koeberg-stage-1 --quants ud-q4_k_xl

    # Kendal Desktop (4B Q6_K) and Kendal Flash Mobile (4B Q4_K_M) exported from a SINGLE 4B training run:
    python training/export_gguf.py --adapter workspace/runs/r1-kendal/adapter --out workspace/exports/kendal-stage-1 --quants q6_k q4_k_m

    # Gariep Budget Phone Tutor (2B) -> Q6_K and Q8_0:
    python training/export_gguf.py --adapter workspace/runs/r1-gariep/adapter --out workspace/exports/gariep-stage-1 --quants q6_k q8_0

    # Then test EACH file on your held-out exam before shipping:
    llama-server -m workspace/exports/kendal-stage-1/kendal-stage-1-Q6_K.gguf --jinja -c 8192 --port 8080
    python eval/run_eval.py --name test-kendal-q6 --backend openai --base-url http://localhost:8080/v1 --model local

EISHKOM STAGE 1 RELEASE & QUANTIZATION RULES (GUIDE.md phase 10)
  * Clean Branding Rule: The public model names must NOT show parameters or quant letters:
    - koeberg-stage-1        (Cloud Flagship, 27B UD-Q4_K_XL)
    - kendal-stage-1         (Budget PC & Laptop, 4B Q6_K)
    - kendal-flash-stage-1   (General Mobile & Phones, 4B Q4_K_M)
    - gariep-stage-1         (Cheaper Devices / Reasoning Tutor, 2B Q6_K / Q8_0)
    - gariep-flash-stage-1   (Cheaper Devices / Fast Vision & OCR, LiquidAI 2B Q6_K)
  * "UD" & "XL": Unsloth Dynamic 2.0 (UD) keeps sensitive attention and vision layers at higher precision.
    XL allocates ~0.2 GB extra precision to avoid math/grammar drops.
  * Multi-Quant Export: You do NOT train separately for Q6 and Q4. Train once on the 4B base model and export
    both files in ~3 minutes from the same trained adapter!
  * Vision: GGUF vision models also produce a separate 'mmproj' projector file; bundle it alongside the .gguf.
"""
import argparse
import json
import subprocess
import sys
import time
from pathlib import Path


def sizes(folder):
    return {f.name: round(f.stat().st_size / 1e9, 2) for f in sorted(Path(folder).rglob("*.gguf"))}


def resolve_adapter_path(adapter_arg):
    """Robustly resolve adapter path, auto-handling {ROUND}, uninitialized variables, or relative paths."""
    if not adapter_arg or adapter_arg.strip() in ("", "auto", "default"):
        adapter_arg = "workspace/runs/r1/adapter"

    # Always sanitize raw template variables
    if "{ROUND}" in adapter_arg:
        adapter_arg = adapter_arg.replace("{ROUND}", "r1")

    p = Path(adapter_arg)
    if p.exists() and (p / "adapter_config.json").exists():
        return str(p)

    candidates = [p]
    # Check common known folders
    for base in [Path("workspace/runs"), Path("runs"), Path(".")]:
        if base.exists():
            for cfg in sorted(base.glob("**/adapter_config.json"), key=lambda x: x.stat().st_mtime, reverse=True):
                candidates.append(cfg.parent)

    for cand in candidates:
        if cand.exists() and (cand / "adapter_config.json").exists():
            print(f"[AUTO-FIX] Adapter path '{adapter_arg}' auto-resolved to: '{cand}'")
            return str(cand)

    return str(p)


def export_unsloth(a, out):
    from unsloth import FastLanguageModel
    print(f"Loading adapter from {a.adapter} for GGUF export...")
    model, tok = FastLanguageModel.from_pretrained(model_name=str(a.adapter), max_seq_length=a.max_len, load_in_4bit=False)
    tokenizer = getattr(tok, "tokenizer", tok)
    clean_quants = [q.lower().strip() for q in a.quants]
    print(f"\n---> Compiling and quantizing GGUF: {clean_quants} into {out}...")
    try:
        # Fast batch pass: Unsloth converts F16 once and creates all quants
        model.save_pretrained_gguf(str(out), tokenizer, quantization_method=clean_quants)
        print(f"Successfully exported {clean_quants} in batch pass!")
    except Exception as e:
        print(f"Notice during batch export ({e}). Falling back to sequential per-quant export...")
        for q_clean in clean_quants:
            try:
                print(f"Exporting quant: '{q_clean}'...")
                model.save_pretrained_gguf(str(out), tokenizer, quantization_method=q_clean)
                print(f"Successfully exported {q_clean}!")
            except Exception as e2:
                print(f"Direct export failed for {q_clean}: {e2}")


def export_manual(a, out):
    import torch
    from peft import PeftModel
    from transformers import AutoModelForCausalLM, AutoTokenizer
    if not a.base:
        sys.exit("--base (the base model name used for training) is required for --method manual")
    merged = out / "merged"
    base = AutoModelForCausalLM.from_pretrained(a.base, torch_dtype=torch.bfloat16)
    model = PeftModel.from_pretrained(base, a.adapter).merge_and_unload()
    model.save_pretrained(str(merged))
    AutoTokenizer.from_pretrained(a.base).save_pretrained(str(merged))
    f16 = out / "model-f16.gguf"
    cmds = [[sys.executable, f"{a.llama_cpp}/convert_hf_to_gguf.py", str(merged), "--outfile", str(f16), "--outtype", "f16"]]
    for q in a.quants:
        cmds.append([f"{a.llama_cpp}/build/bin/llama-quantize", str(f16), str(out / f"model-{q.upper()}.gguf"), q.upper()])
    for c in cmds:
        print("$", " ".join(c))
        if a.llama_cpp != "<path>":
            subprocess.run(c, check=True)
    if a.llama_cpp == "<path>":
        print("\n(llama.cpp path not given: run the commands above yourself after cloning and building llama.cpp)")


def consolidate_and_brand_gguf(out_dir, base_brand="kendal-stage-1"):
    """Finds all .gguf files in out_dir or out_dir_gguf, moves them to out_dir with clean Eishkom branding, and cleans up merged safetensors."""
    out = Path(out_dir)
    gguf_dirs = [out, out.parent / f"{out.name}_gguf"]

    found_ggufs = []
    for d in gguf_dirs:
        if d.exists():
            for f in d.glob("*.gguf"):
                found_ggufs.append(f)

    for f in found_ggufs:
        dest_name = f.name
        f_lower = f.name.lower()
        if "q6_k" in f_lower:
            dest_name = f"{base_brand}-Q6_K.gguf"
        elif "q4_k_m" in f_lower:
            flash_brand = base_brand.replace("-stage-1", "-flash-stage-1") if "-flash" not in base_brand else base_brand
            dest_name = f"{flash_brand}-Q4_K_M.gguf"
        elif "q4_k" in f_lower or "q4k" in f_lower:
            dest_name = f"{base_brand}-Q4_K.gguf"
        elif "q8_0" in f_lower:
            dest_name = f"{base_brand}-Q8_0.gguf"
        elif "ud-q4_k_xl" in f_lower or "q4_k_xl" in f_lower:
            dest_name = f"{base_brand}-UD-Q4_K_XL.gguf"

        dest_path = out / dest_name
        if f.resolve() != dest_path.resolve():
            import shutil
            shutil.move(str(f), str(dest_path))
            print(f"[Clean Branding] Moved {f.name} -> {dest_path.name}")

    # Remove temporary sibling _gguf directory if empty
    sibling = out.parent / f"{out.name}_gguf"
    if sibling.exists():
        try:
            import shutil
            shutil.rmtree(str(sibling))
        except Exception:
            pass

    # Clean up intermediate merged 16-bit safetensors in out_dir to save ~9GB disk space!
    for f in out.glob("*.safetensors"):
        try:
            f.unlink()
            print(f"[Disk Cleanup] Deleted intermediate 16-bit weight: {f.name} (freed disk space)")
        except Exception:
            pass


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--adapter", default="auto", help="the adapter folder written by train_sft.py (default: auto-detect)")
    ap.add_argument("--out", required=True)
    ap.add_argument("--quants", nargs="+", default=["q6_k", "q4_k", "q4_k_m"])
    ap.add_argument("--method", choices=["unsloth", "manual"], default="unsloth")
    ap.add_argument("--base", help="base model name (manual method)")
    ap.add_argument("--llama-cpp", default="<path>")
    ap.add_argument("--max-len", type=int, default=4096)
    ap.add_argument("--eval-run", help="name of the eval run to copy into the model card")
    a = ap.parse_args()

    a.adapter = resolve_adapter_path(a.adapter)
    if "{ROUND}" in str(a.out):
        a.out = str(a.out).replace("{ROUND}", "r1")
        print(f"[AUTO-FIX] Detected raw variable in --out. Resolved to: '{a.out}'")
    if a.base and "{MODEL}" in a.base:
        a.base = "unsloth/Qwen3.5-4B"

    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    (export_unsloth if a.method == "unsloth" else export_manual)(a, out)
    consolidate_and_brand_gguf(out, base_brand=out.name)
    files = sizes(out)
    (out / "exports.json").write_text(json.dumps({"adapter": a.adapter, "quants": a.quants, "files_gb": files, "when": time.strftime("%Y-%m-%d %H:%M")}, indent=2), encoding="utf-8")
    card = [
        "# Eishkom Stage 1 Model Card\n",
        f"- Release Brand: Eishkom AI (Stage 1 Cycle)",
        f"- Base model: {a.base or '(see training config)'}  - licence: Apache 2.0 / Permissive",
        f"- Trained with: LoRA adapter {a.adapter} via Unsloth QLoRA",
        "- Training data: South African CAPS curriculum (DBE past exam papers & Siyavula CC-BY textbooks)",
        "- Intended use: CAPS educational tutoring for Grades 7-12 (Maths, Sciences, English, Afrikaans).",
        "- Deployment Target: Offline inference (llama.cpp, Ollama, PocketPal AI) or Google Cloud Run serverless GPU.",
        "- Known limits: (copy the weak slices from eval report)",
        "- Exported Files:"
    ] + [f"  - {n}  ({gb} GB)" for n, gb in files.items()]
    (out / "MODEL_CARD.md").write_text("\n".join(card) + "\n", encoding="utf-8")
    print("\nExport Complete. Generated Files:")
    print(json.dumps(files, indent=1))
    print("\nNEXT: serve each .gguf file with llama-server, run your held-out exam, and deploy!")


if __name__ == "__main__":
    main()
