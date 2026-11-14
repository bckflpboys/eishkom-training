"""
tools/stage2_status.py - Real-Time Stage 2 Fleet Generation Monitor (Pass 1 + Pass 2 Live)

Run from any terminal to check live progress:
    python tools/stage2_status.py
"""
import sys
import json
import time
import pathlib
from collections import defaultdict, Counter
from datetime import datetime

ROOT_DIR = pathlib.Path(__file__).resolve().parent.parent
S1_VER_DIR = ROOT_DIR / "workspace" / "verified"
S2_P1_VER_DIR = ROOT_DIR / "workspace" / "verified" / "stage2"
S2_P1_FULL_DIR = ROOT_DIR / "workspace" / "verified" / "stage2_full_solutions"
S2_P1_REJ_DIR = ROOT_DIR / "workspace" / "rejected" / "stage2"

S2_P2_VER_DIR = ROOT_DIR / "workspace" / "verified" / "stage2_pass2"
S2_P2_GEN_DIR = ROOT_DIR / "workspace" / "gen" / "stage2_pass2"
S2_P2_REJ_DIR = ROOT_DIR / "workspace" / "rejected" / "stage2_pass2"

PROGRESS_FILE_P1 = ROOT_DIR / "stage-2" / "progress.json"
PROGRESS_FILE_P2 = ROOT_DIR / "stage-2" / "progress_pass2.json"

TARGET_SOCRATIC = 15000

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

def count_jsonl_records(directory, is_socratic=True):
    count = 0
    by_strat = Counter()
    by_subj = Counter()
    by_svc = Counter()
    by_mode = Counter()
    papers = set()

    if not directory.exists():
        return count, by_strat, by_subj, by_svc, by_mode, papers

    for f in directory.glob("*.jsonl"):
        papers.add(f.stem)
        try:
            with open(f, encoding="utf-8") as fp:
                for line in fp:
                    if line.strip():
                        try:
                            rec = json.loads(line)
                            count += 1
                            m = rec.get("meta", {})
                            strat = m.get("strategy_used") or m.get("teaching_strategy", "unknown")
                            by_strat[strat] += 1
                            subj = rec.get("control", {}).get("subject") or m.get("subject", "unknown")
                            by_subj[subj] += 1
                            svc, _ = resolve_service_info(rec)
                            by_svc[svc] += 1
                            mode = m.get("coaching_mode", "unknown")
                            by_mode[mode] += 1
                        except Exception:
                            count += 1
        except Exception:
            pass

    return count, by_strat, by_subj, by_svc, by_mode, papers

def print_status_dashboard():
    # 1. Stage 1 Baseline Counts
    s1_socratic = 1319
    s1_fullsol = 1970

    # 2. Stage 2 Pass 1 Counts
    p1_socratic, p1_strat, p1_subj, p1_svc, p1_mode, p1_papers = count_jsonl_records(S2_P1_VER_DIR)
    p1_fullsol = sum(sum(1 for _ in open(f, encoding="utf-8") if _.strip()) for f in S2_P1_FULL_DIR.glob("*.jsonl")) if S2_P1_FULL_DIR.exists() else 0
    p1_rej = sum(sum(1 for _ in open(f, encoding="utf-8") if _.strip()) for f in S2_P1_REJ_DIR.glob("*.jsonl")) if S2_P1_REJ_DIR.exists() else 0

    # 3. Stage 2 Pass 2 Counts (Live Running)
    p2_socratic, p2_strat, p2_subj, p2_svc, p2_mode, p2_papers = count_jsonl_records(S2_P2_VER_DIR)
    p2_gen = sum(sum(1 for _ in open(f, encoding="utf-8") if _.strip()) for f in S2_P2_GEN_DIR.glob("*.jsonl")) if S2_P2_GEN_DIR.exists() else 0
    p2_rej = sum(sum(1 for _ in open(f, encoding="utf-8") if _.strip()) for f in S2_P2_REJ_DIR.glob("*.jsonl")) if S2_P2_REJ_DIR.exists() else 0
    p2_pass_rate = (p2_socratic / p2_gen * 100) if p2_gen > 0 else 0.0

    # 4. Project Grand Totals
    total_socratic = s1_socratic + p1_socratic + p2_socratic
    total_fullsol = s1_fullsol + p1_fullsol
    total_records = total_socratic + total_fullsol
    est_sft_samples = int(total_socratic * 2.5 + total_fullsol)
    pct_goal = (total_socratic / TARGET_SOCRATIC * 100) if TARGET_SOCRATIC > 0 else 0.0

    # Progress bar (30 chars)
    bar_len = 30
    filled = int(bar_len * (total_socratic / TARGET_SOCRATIC))
    bar = "█" * min(filled, bar_len) + "░" * max(0, bar_len - filled)

    print("=" * 80)
    print("       EISHKOM AI — STAGE 2 FLEET GENERATION LIVE STATUS DASHBOARD")
    print(f"       Checked at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)

    print(f"\n  🎯 SOCRATIC LESSONS PROGRESS TOWARDS {TARGET_SOCRATIC:,} TARGET:")
    print(f"  [{bar}] {pct_goal:.1f}% ({total_socratic:,} / {TARGET_SOCRATIC:,} lessons)")
    print(f"  Remaining to 15,000 Goal: {max(0, TARGET_SOCRATIC - total_socratic):,} lessons")
    print(f"  Total Project Records:    {total_records:,} (Socratic: {total_socratic:,} + Full Sol: {total_fullsol:,})")
    print(f"  Estimated SFT Samples:    ~{est_sft_samples:,} samples (~{est_sft_samples * 700 / 1e6:.1f}M tokens)")
    print("-" * 80)

    print("  🚀 PASS 2: STRATEGY PERMUTATION FLEET (LIVE IN BACKGROUND):")
    print(f"    Verified Socratic Lessons: {p2_socratic:,} (alternating strategies)")
    print(f"    Total Generated Items:     {p2_gen:,}")
    print(f"    Rejected Items:            {p2_rej:,} (workspace/rejected/stage2_pass2/)")
    print(f"    Pass 2 Quality Pass Rate:  {p2_pass_rate:.1f}%")
    print(f"    Active Papers in Pass 2:   {len(p2_papers)} papers")

    print("\n    Pass 2 Teaching Strategy Spread (Permuted vs Pass 1):")
    if p2_strat:
        for strat, count in p2_strat.most_common(8):
            print(f"      {strat:<25s}: {count:>4d} ({count/max(p2_socratic,1)*100:4.1f}%)")
    else:
        print("      (Starting generation...)")

    print("\n    Pass 2 Subject Breakdown:")
    if p2_subj:
        for subj, count in p2_subj.most_common(7):
            print(f"      {subj:<25s}: {count:>4d}")
    print("-" * 80)

    print("  📦 PASS 1: BASELINE MULTI-STRATEGY CORPUS (100% COMPLETE):")
    print(f"    Verified Socratic Lessons: {p1_socratic:,} / 10,000")
    print(f"    Full Solutions Generated:  {p1_fullsol:,}")
    print(f"    Pass 1 Quality Pass Rate:  {(p1_socratic/(p1_socratic+p1_rej)*100) if (p1_socratic+p1_rej)>0 else 0.0:.1f}%")
    print(f"    Completed Exam Papers:     {len(p1_papers)} / 225")
    print("-" * 80)

    print("  ⚡ ACTIVE FLEET PROVIDERS (PASS 2):")
    if p2_svc:
        for svc, count in p2_svc.most_common():
            print(f"    {svc:<30s}: {count:>5d} lessons ({count/max(p2_socratic,1)*100:4.1f}%)")
    else:
        print("    Google AI Studio, Groq LPU, Cohere API, NVIDIA NIM, Intern-AI Free")

    print("=" * 80)
    print("To refresh live status at any time, run:")
    print("    python tools/stage2_status.py")
    print("=" * 80)

if __name__ == "__main__":
    print_status_dashboard()
