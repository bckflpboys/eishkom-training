#!/usr/bin/env python3
"""
export_gguf.py - turn your trained adapter into the files people actually run (GGUF), in several sizes.

    python training/export_gguf.py --adapter workspace/runs/r2/adapter --out workspace/exports/tutor-4b-r2 --quants q6_k q4_k_m
    # then test EACH file on your exam before you ship it:
    llama-server -m workspace/exports/tutor-4b-r2/<file>.gguf --jinja -c 8192 --port 8080
    python eval/run_eval.py --name r2-q6 --backend openai --base-url http://localhost:8080/v1 --model local

WHAT THE VARIANTS ARE (GUIDE.md phase 10)
  * "quantization" = storing each weight with fewer bits (like saving a photo as a smaller JPEG).
    Q6_K: bigger, closest to the original. Q4_K_M: about 25% smaller, slightly lossier. Q8_0: biggest.
    You do NOT train separately for each: you train ONCE and export several files from the same trained model.
  * A DIFFERENT SIZE (the 2B for 4 GB phones) is a different base model: train it again with the SAME data:
        python training/train_sft.py --model unsloth/Qwen3.5-2B --data workspace/build/r2 --out workspace/runs/r2-2b
    and export that adapter the same way.
  * "Q6_K_H" is not a built-in llama.cpp type (a community recipe); use Q6_K.

METHODS
  --method unsloth  (default) one call does merge + convert + quantize. Needs Unsloth + a GPU/Colab.
  --method manual   merges the adapter with peft, then runs llama.cpp's converter and quantizer
                    (pass --llama-cpp /path/to/llama.cpp built with cmake; otherwise the commands are printed for you).
Vision: GGUF vision models also need a separate 'mmproj' file; check your exporter's output folder for *mmproj*.gguf
and ship it next to the model.
"""
import argparse
import json
import subprocess
import sys
import time
from pathlib import Path


def sizes(folder):
    return {f.name: round(f.stat().st_size / 1e9, 2) for f in sorted(Path(folder).rglob("*.gguf"))}


def export_unsloth(a, out):
    from unsloth import FastLanguageModel
    model, tok = FastLanguageModel.from_pretrained(model_name=a.adapter, max_seq_length=a.max_len, load_in_4bit=False)
    model.save_pretrained_gguf(str(out), getattr(tok, "tokenizer", tok), quantization_method=a.quants)


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


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--adapter", required=True, help="the adapter folder written by train_sft.py")
    ap.add_argument("--out", required=True)
    ap.add_argument("--quants", nargs="+", default=["q6_k", "q4_k_m"])
    ap.add_argument("--method", choices=["unsloth", "manual"], default="unsloth")
    ap.add_argument("--base", help="base model name (manual method)")
    ap.add_argument("--llama-cpp", default="<path>")
    ap.add_argument("--max-len", type=int, default=4096)
    ap.add_argument("--eval-run", help="name of the eval run to copy into the model card")
    a = ap.parse_args()
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    (export_unsloth if a.method == "unsloth" else export_manual)(a, out)
    files = sizes(out)
    (out / "exports.json").write_text(json.dumps({"adapter": a.adapter, "quants": a.quants, "files_gb": files, "when": time.strftime("%Y-%m-%d %H:%M")}, indent=2), encoding="utf-8")
    card = ["# Model card (fill in the blanks)\n", f"- Base model: {a.base or '(name it)'}  - licence: (copy from the base model's page)",
            f"- Trained with: LoRA adapter {a.adapter}", "- Training data: (list sources + licences + attribution lines; see workspace/sources/sources.csv)",
            "- Intended use: tutoring for South African CAPS Grades 7-12 (maths, sciences, English, Afrikaans). Not a replacement for a teacher.",
            "- Known limits: (copy the weak slices from the eval report)", "- Files:"] + [f"  - {n}  ({gb} GB)" for n, gb in files.items()]
    (out / "MODEL_CARD.md").write_text("\n".join(card) + "\n", encoding="utf-8")
    print(json.dumps(files, indent=1))
    print("NEXT: serve each .gguf, run the exam on each, and ship the smallest one whose scores are still acceptable.")


if __name__ == "__main__":
    main()
