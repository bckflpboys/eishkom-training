"""
tools/stage2_status.py - Real-Time Stage 2 Fleet Generation Monitor

Run from any terminal to check live progress:
    python tools/stage2_status.py
"""
import sys
import json
import time
import pathlib
from collections import defaultdict
from datetime import datetime

ROOT_DIR = pathlib.Path(__file__).resolve().parent.parent
VER_DIR = ROOT_DIR / "workspace" / "verified" / "stage2"
FULL_DIR = ROOT_DIR / "workspace" / "verified" / "stage2_full_solutions"
REJ_DIR = ROOT_DIR / "workspace" / "rejected" / "stage2"
PROGRESS_FILE = ROOT_DIR / "stage-2" / "progress.json"

TARGET_VERIFIED = 15000

PROVIDER_MAP = {
    "gpt-6-luna": "OpenAI Luna (Deactivated)",
    "gemma-4-31b-it": "Google AI Studio",
    "gemma-4-26b-a4b-it": "Google AI Studio",
    "gemini-3.5-flash-lite": "Google AI Studio",
    "gemini-3.1-flash-lite": "Google AI Studio",
    "gemini-4-hydrogen": "Google AI Studio",
    "nemotron-3-ultra-550b": "OpenRouter Free",
    "qwen-3.8-27b": "Cerebras WSE",
    "qwen3.8-27b": "Groq LPU",
    "gpt-oss-120b": "Groq / Cerebras",
    "deepseek-v4.1-flash-1017": "Intern-AI Free",
    "deepseek-fast": "Intern-AI Free",
    "nemotron-3.5-lightning": "NVIDIA NIM",
    "nemotron-3.5-super-vl": "NVIDIA NIM",
    "minimax-m3.1-flash": "NVIDIA NIM",
    "mistral-large-4": "NVIDIA NIM",
    "muse-glimmer-30b": "NVIDIA NIM",
    "command-a": "Cohere API",
    "command-r-plus": "Cohere API",
    "command-r": "Cohere API",
    "command-a-reasoning": "Cohere API",
    "command-a-plus": "Cohere API",
    "north-mini-code": "Cohere API",
}

def resolve_service_info(rec):
    meta = rec.get("meta", {})
    gen = meta.get("generator", "unknown")
    provider = meta.get("provider")
    lane_id = meta.get("lane_id", "")

    if lane_id.startswith("GMA1") or lane_id.startswith("GEM1"):
        svc = "Google AI Studio 1"
    elif lane_id.startswith("GMA2") or lane_id.startswith("GEM2"):
        svc = "Google AI Studio 2"
    elif lane_id.startswith("CRB"):
        svc = "Cerebras WSE"
    elif lane_id.startswith("GRQ"):
        svc = "Groq LPU"
    elif lane_id.startswith("NVD"):
        svc = "NVIDIA NIM"
    elif lane_id.startswith("COH"):
        svc = "Cohere API"
    elif lane_id.startswith("DSK"):
        svc = "Intern-AI Free"
    elif lane_id.startswith("NEM"):
        svc = "OpenRouter Free"
    elif lane_id.startswith("OAI"):
        svc = "OpenAI Luna (Deactivated)"
    elif provider:
        p_map = {
            "gemini": "Google AI Studio",
            "cerebras": "Cerebras WSE",
            "groq": "Groq LPU",
            "nvidia": "NVIDIA NIM",
            "cohere": "Cohere API",
            "intern": "Intern-AI Free",
            "openrouter": "OpenRouter Free",
            "openai": "OpenAI Luna (Deactivated)",
        }
        svc = p_map.get(provider, provider.capitalize())
    else:
        svc = PROVIDER_MAP.get(gen, "Unknown Provider")

    return svc, gen

def get_live_counts():
    socratic_count = 0
    full_count = 0
    rej_count = 0
    by_service = defaultdict(int)
    by_svc_model = defaultdict(int)
    by_subject = defaultdict(int)
    by_strategy = defaultdict(int)
    by_mode = defaultdict(int)
    papers_socratic = set()
    papers_full = set()

    if VER_DIR.exists():
        for f in VER_DIR.glob("*.jsonl"):
            papers_socratic.add(f.stem)
            with open(f, encoding="utf-8") as fp:
                for line in fp:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        rec = json.loads(line)
                        socratic_count += 1
                        m = rec.get("meta", {})
                        svc, gen = resolve_service_info(rec)
                        by_service[svc] += 1
                        by_svc_model[f"[{svc}] {gen}"] += 1

                        subj = rec.get("control", {}).get("subject") or m.get("subject", "unknown")
                        by_subject[subj] += 1
                        strat = m.get("strategy_used", "unknown")
                        by_strategy[strat] += 1
                        mode = m.get("coaching_mode", "unknown")
                        by_mode[mode] += 1
                    except Exception:
                        pass

    if FULL_DIR.exists():
        for f in FULL_DIR.glob("*.jsonl"):
            papers_full.add(f.stem)
            with open(f, encoding="utf-8") as fp:
                for line in fp:
                    if line.strip():
                        full_count += 1

    if REJ_DIR.exists():
        for f in REJ_DIR.glob("*.jsonl"):
            with open(f, encoding="utf-8") as fp:
                for line in fp:
                    if line.strip():
                        rej_count += 1

    return {
        "socratic_count": socratic_count,
        "full_count": full_count,
        "total_verified": socratic_count,
        "total_combined": socratic_count + full_count,
        "rej_count": rej_count,
        "papers_done": len(papers_socratic),
        "by_service": by_service,
        "by_svc_model": by_svc_model,
        "by_subject": by_subject,
        "by_strategy": by_strategy,
        "by_mode": by_mode,
    }

def print_status_dashboard():
    counts = get_live_counts()
    v_tot = counts["socratic_count"]
    comb_tot = counts["total_combined"]
    rej_tot = counts["rej_count"]
    gen_tot = v_tot + rej_tot
    pass_rate = (v_tot / gen_tot * 100) if gen_tot > 0 else 0.0
    pct_target = (v_tot / TARGET_VERIFIED * 100) if TARGET_VERIFIED > 0 else 0.0

    print("=" * 80)
    print("       EISHKOM AI — STAGE 2 FLEET GENERATION LIVE STATUS DASHBOARD")
    print(f"       Checked at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)
    print(f"  Socratic Lessons Verified:    {v_tot:,} / {TARGET_VERIFIED:,} ({pct_target:.1f}% of goal)")
    print(f"  Full Solutions Generated:     {counts['full_count']:,}")
    print(f"  Total Stage 2 Samples:        {comb_tot:,} items")
    print(f"  Rejected Samples:             {rej_tot:,} (workspace/rejected/stage2/)")
    print(f"  Live Pass Rate:               {pass_rate:.1f}%")
    print(f"  Completed Exam Papers:        {counts['papers_done']} papers")
    print("-" * 80)

    print("  PRODUCTION BY API SERVICE / PROVIDER:")
    if counts["by_service"]:
        for svc, c in sorted(counts["by_service"].items(), key=lambda x: -x[1]):
            share = (c / v_tot * 100) if v_tot > 0 else 0.0
            print(f"    {svc:<35s}: {c:>5d} ({share:.1f}%)")
    else:
        print("    (No records yet)")

    print("\n  PRODUCTION BY MODEL & API SERVICE:")
    if counts["by_svc_model"]:
        for item, c in sorted(counts["by_svc_model"].items(), key=lambda x: -x[1]):
            share = (c / v_tot * 100) if v_tot > 0 else 0.0
            print(f"    {item:<45s}: {c:>5d} ({share:.1f}%)")
    else:
        print("    (No verified records yet)")

    print("\n  PRODUCTION BY SUBJECT:")
    if counts["by_subject"]:
        for subj, c in sorted(counts["by_subject"].items(), key=lambda x: -x[1]):
            print(f"    {subj:<35s}: {c:>5d}")
    else:
        print("    (No verified records yet)")

    print("\n  PRODUCTION BY COACHING MODE:")
    if counts["by_mode"]:
        for mode, c in sorted(counts["by_mode"].items(), key=lambda x: -x[1]):
            print(f"    {mode:<25s}: {c:>5d}")
    else:
        print("    (No records yet)")

    print("=" * 80)
    print("To refresh, rerun: python tools/stage2_status.py")
    print("=" * 80)

if __name__ == "__main__":
    print_status_dashboard()
