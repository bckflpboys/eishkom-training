"""
tools/stage2_status.py - Comprehensive Eishkom AI Fleet Generation Live Status Dashboard.
Tracks both:
  1. Core Curriculum Fleet (Socratic Lessons & Full Solutions towards 15,000 goal)
  2. Agentic & Study Coaching Fleet (Operational, Coaching & Vision data towards 3,500 goal)

Shows:
  - Real-time progress bars for Socratic and Agentic targets
  - Production by API Service / Provider
  - Production by Model & API Service with Success Rate & Rejection/Failure Counts
  - Subject breakdown across all 7 CAPS subjects (English, Afrikaans, Maths, Physics)
  - Coaching mode breakdown (deep vs short)
  - Teaching strategy spread
  - Agentic task family breakdown
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

VER_AGENTIC_DIR = ROOT_DIR / "workspace" / "verified" / "agentic"
REJ_AGENTIC_DIR = ROOT_DIR / "workspace" / "rejected" / "agentic"

TARGET_SOCRATIC = 15000
TARGET_AGENTIC = 3500

PROVIDER_MAP = {
    "gpt-6-luna": "OpenAI Luna (Deactivated)",
    "gemma-4-31b-it": "Google AI Studio",
    "gemma-4-26b-a4b-it": "Google AI Studio",
    "gemini-3.5-flash-lite": "Google AI Studio",
    "gemini-3.1-flash-lite": "Google AI Studio",
    "gemini-4-hydrogen": "Google AI Studio",
    "gemini-2.5-flash": "Vercel AI Gateway",
    "qwen3.8-max": "Alibaba Model Studio",
    "kimi-k3.1-pro": "Alibaba Model Studio",
    "qwen-max": "Alibaba Model Studio",
    "nvidia/nemotron-3-ultra-550b-a55b": "Vercel AI Gateway",
    "openai/gpt-oss-120b": "Vercel AI Gateway",
    "nvidia/nemotron-3.5-super-vl": "Vercel AI Gateway",
    "nemotron-3.5-super-vl": "NVIDIA NIM",
    "nemotron-3.5-lightning": "NVIDIA NIM",
    "minimax-m3.1-flash": "NVIDIA NIM",
    "mistralai/mistral-large-4-1t-a52b": "NVIDIA NIM",
    "Gemma-4-31B-IT": "Token Lab AMD",
    "Qwen3.8-27B": "Token Lab AMD",
    "DeepSeek-V4-Flash": "Token Lab AMD",
    "deepseek-v4.1-flash:free": "TokenHarbor",
    "mimo-v2.6-flash:free": "TokenHarbor",
    "deepseek-v4-flash:free": "TokenHarbor",
    "mimo-v2.5:free": "TokenHarbor",
    "kilo-auto/free": "Kilo Gateway",
    "nemotron-3-ultra-550b-a55b:free": "Kilo Gateway",
    "nemotron-3.5-super-vl:free": "Kilo Gateway",
    "liquid/lfm-3-1.7b:free": "Kilo Gateway",
    "free/gemini-3.8-flash": "APInex",
    "free/mimo-v2.6-pro": "APInex",
    "free/qwen-3.8-max": "APInex",
    "free/kimi-k3": "APInex",
    "free/deepseek-v4.1-flash": "APInex",
    "free/glm-5.3-flash": "APInex",
    "free/glm-5.3": "APInex",
    "free/deepseek-v4-pro-0813": "APInex",
    "free/deepseek-v4-flash-0731": "APInex",
    "free/muse-spark-1.3": "APInex",
    "free/minimax-m3.1-flash": "APInex",
    "free/gpt-6-luna": "APInex",
    "free/hy4": "APInex",
    "deepseek-v4.1-flash-1017-free": "APMix",
    "nemotron-3.5-super-vl-free": "APMix",
    "deepseek-v4.1-flash-abliterated-free": "Refuseless",
    "nemotron-3-ultra-550b": "OpenRouter Free",
    "qwen-3.8-27b": "Cerebras WSE",
    "qwen3.8-27b": "Groq LPU",
    "qwen/qwen3.8-27b": "Groq LPU",
    "gpt-oss-120b": "Groq / Cerebras",
    "deepseek-v4.1-flash-1017": "Intern-AI Free",
    "deepseek-fast": "Intern-AI Free",
    "command-a": "Cohere API",
    "command-r-plus": "Cohere API",
    "command-r": "Cohere API",
    "command-a-reasoning": "Cohere API",
    "command-a-plus": "Cohere API",
    "north-mini-code": "Cohere API",
    "default": "LLM7.io",
    "glm-5.3-flash": "LLM7.io",
}

def resolve_service_info(rec):
    meta = rec.get("meta", {})
    gen = meta.get("generator") or rec.get("generator") or rec.get("model") or "unknown"
    provider = meta.get("provider") or rec.get("provider")
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
    elif lane_id.startswith("ALI"):
        svc = "Alibaba Model Studio"
    elif lane_id.startswith("VRC"):
        svc = "Vercel AI Gateway"
    elif lane_id.startswith("AMD"):
        svc = "Token Lab AMD"
    elif lane_id.startswith("THB"):
        svc = "TokenHarbor"
    elif lane_id.startswith("KLO"):
        svc = "Kilo Gateway"
    elif lane_id.startswith("APN"):
        svc = "APInex"
    elif lane_id.startswith("APM"):
        svc = "APMix"
    elif lane_id.startswith("RFS"):
        svc = "Refuseless"
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
            "alibaba": "Alibaba Model Studio",
            "dashscope": "Alibaba Model Studio",
            "vercel": "Vercel AI Gateway",
            "tokenlab": "Token Lab AMD",
            "tokenharbor": "TokenHarbor",
            "kilo": "Kilo Gateway",
            "llm7": "LLM7.io",
            "apinex": "APInex",
            "apmix": "APMix",
            "refuseless": "Refuseless",
        }
        svc = p_map.get(str(provider).lower(), str(provider).capitalize())
    elif gen in PROVIDER_MAP:
        svc = PROVIDER_MAP[gen]
    elif str(gen).startswith("free/"):
        svc = "APInex"
    elif ":free" in str(gen) and ("nemotron" in str(gen) or "kilo" in str(gen) or "lfm" in str(gen)):
        svc = "Kilo Gateway"
    elif ":free" in str(gen) and ("deepseek" in str(gen) or "mimo" in str(gen)):
        svc = "TokenHarbor"
    elif "abliterated" in str(gen):
        svc = "Refuseless"
    elif "apmix" in str(gen) or "-1017-free" in str(gen):
        svc = "APMix"
    elif "nemotron" in str(gen) or "mistral" in str(gen):
        svc = "NVIDIA NIM"
    elif "gemini" in str(gen) or "gemma" in str(gen):
        svc = "Google AI Studio"
    elif "qwen" in str(gen) or "kimi" in str(gen):
        svc = "Alibaba Model Studio"
    elif "command" in str(gen) or "north" in str(gen):
        svc = "Cohere API"
    elif "glm" in str(gen):
        svc = "LLM7.io"
    else:
        svc = "Other Provider"

    return svc, gen

def scan_jsonl_directory(directory):
    records = []
    if not directory.exists():
        return records
    for f in directory.glob("*.jsonl"):
        try:
            with open(f, encoding="utf-8") as fp:
                for line in fp:
                    if line.strip():
                        try:
                            rec = json.loads(line)
                            records.append(rec)
                        except Exception:
                            pass
        except Exception:
            pass
    return records

def print_status_dashboard():
    # 1. Baseline Counts
    s1_socratic = 1319
    s1_fullsol = 1970

    # 2. Collect Pass 1 Records
    p1_ver = scan_jsonl_directory(S2_P1_VER_DIR)
    p1_rej = scan_jsonl_directory(S2_P1_REJ_DIR)
    p1_fullsol_cnt = sum(sum(1 for _ in open(f, encoding="utf-8") if _.strip()) for f in S2_P1_FULL_DIR.glob("*.jsonl")) if S2_P1_FULL_DIR.exists() else 0

    # 3. Collect Pass 2 Records
    p2_ver = scan_jsonl_directory(S2_P2_VER_DIR)
    p2_rej = scan_jsonl_directory(S2_P2_REJ_DIR)

    # 4. Collect Agentic Records
    ag_ver = scan_jsonl_directory(VER_AGENTIC_DIR)
    ag_rej = scan_jsonl_directory(REJ_AGENTIC_DIR)

    # Aggregations
    total_socratic = s1_socratic + len(p1_ver) + len(p2_ver)
    total_fullsol = s1_fullsol + p1_fullsol_cnt
    total_records = total_socratic + total_fullsol
    est_sft_samples = int(total_socratic * 2.5 + total_fullsol)

    all_ver_s2 = p1_ver + p2_ver
    all_rej_s2 = p1_rej + p2_rej

    # Counters
    by_svc = Counter()
    by_model_svc = Counter()
    by_model_ver = Counter()
    by_model_rej = Counter()
    by_subj = Counter()
    by_strat = Counter()
    by_mode = Counter()
    papers_seen = set()

    for r in all_ver_s2:
        svc, gen = resolve_service_info(r)
        key = f"[{svc}] {gen}"
        by_svc[svc] += 1
        by_model_svc[key] += 1
        by_model_ver[key] += 1
        m = r.get("meta", {})
        subj = r.get("control", {}).get("subject") or m.get("subject", "unknown")
        by_subj[subj] += 1
        strat = m.get("strategy_used") or m.get("teaching_strategy", "unknown")
        by_strat[strat] += 1
        mode = m.get("coaching_mode", "unknown")
        by_mode[mode] += 1
        pid = m.get("paper_id")
        if pid:
            papers_seen.add(pid)

    for r in all_rej_s2:
        svc, gen = resolve_service_info(r)
        key = f"[{svc}] {gen}"
        by_model_rej[key] += 1

    # Agentic counters
    ag_by_task = Counter()
    ag_by_model = Counter()
    for r in ag_ver:
        m = r.get("meta", {})
        task = m.get("task_type") or r.get("task_type") or "unknown"
        ag_by_task[task] += 1
        gen = m.get("generator") or r.get("worker") or "unknown"
        ag_by_model[gen] += 1

    # Formatting UI
    bar_len = 30
    # Socratic progress
    filled_soc = int(bar_len * (total_socratic / TARGET_SOCRATIC))
    bar_soc = "█" * min(filled_soc, bar_len) + "░" * max(0, bar_len - filled_soc)
    pct_soc = (total_socratic / TARGET_SOCRATIC * 100) if TARGET_SOCRATIC > 0 else 0.0

    # Agentic progress
    total_ag = len(ag_ver)
    filled_ag = int(bar_len * (total_ag / TARGET_AGENTIC))
    bar_ag = "█" * min(filled_ag, bar_len) + "░" * max(0, bar_len - filled_ag)
    pct_ag = (total_ag / TARGET_AGENTIC * 100) if TARGET_AGENTIC > 0 else 0.0

    print("=" * 80)
    print("       EISHKOM AI — STAGE 2 FLEET GENERATION LIVE STATUS DASHBOARD")
    print(f"       Checked at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)

    print(f"\n  🎯 1. CORE SOCRATIC LESSONS PROGRESS (Target: {TARGET_SOCRATIC:,}):")
    print(f"  [{bar_soc}] {pct_soc:.1f}% ({total_socratic:,} / {TARGET_SOCRATIC:,} lessons)")
    print(f"  Remaining to Goal:        {max(0, TARGET_SOCRATIC - total_socratic):,} lessons")
    print(f"  Full Solutions Generated: {total_fullsol:,} items (100% complete across all 266 papers)")
    print(f"  Total Project Records:    {total_records:,} (Socratic: {total_socratic:,} + Full Sol: {total_fullsol:,})")
    print(f"  Estimated SFT Samples:    ~{est_sft_samples:,} samples (~{est_sft_samples * 700 / 1e6:.1f}M tokens)")
    print(f"  Stage 2 Verified Total:   {len(all_ver_s2):,} (Pass 1: {len(p1_ver):,}, Pass 2: {len(p2_ver):,})")
    print(f"  Stage 2 Rejected Total:   {len(all_rej_s2):,} (Pass 1: {len(p1_rej):,}, Pass 2: {len(p2_rej):,})")
    tot_attempts = len(all_ver_s2) + len(all_rej_s2)
    overall_pass_rate = (len(all_ver_s2) / tot_attempts * 100) if tot_attempts > 0 else 0.0
    print(f"  Stage 2 Pass Rate:        {overall_pass_rate:.1f}% across {len(papers_seen)} papers")

    print(f"\n  🤖 2. AGENTIC & STUDY COACHING FLEET (Target: {TARGET_AGENTIC:,} - 10-15% Mix):")
    print(f"  [{bar_ag}] {pct_ag:.1f}% ({total_ag:,} / {TARGET_AGENTIC:,} samples)")
    print(f"  Remaining to Goal:        {max(0, TARGET_AGENTIC - total_ag):,} samples")
    print(f"  Agentic Rejections:       {len(ag_rej):,}")

    print("\n" + "-" * 80)
    print("  ⚡ PRODUCTION BY API SERVICE / PROVIDER:")
    tot_s2_ver = max(1, len(all_ver_s2))
    for svc, cnt in by_svc.most_common():
        print(f"    {svc:<35s}: {cnt:>5d} ({cnt / tot_s2_ver * 100:4.1f}%)")

    print("\n" + "-" * 80)
    print("  🏆 PRODUCTION BY MODEL & API SERVICE (Success vs Failure / Rejection Rate):")
    all_models = sorted(set(list(by_model_ver.keys()) + list(by_model_rej.keys())), key=lambda k: by_model_ver[k], reverse=True)
    for k in all_models:
        v_cnt = by_model_ver[k]
        r_cnt = by_model_rej[k]
        att = v_cnt + r_cnt
        rate = (v_cnt / att * 100) if att > 0 else 0.0
        print(f"    {k:<46s}: {v_cnt:>5d} passed, {r_cnt:>4d} rejected ({rate:5.1f}% pass | {v_cnt / tot_s2_ver * 100:4.1f}% share)")

    print("\n" + "-" * 80)
    print("  📚 SUBJECT BREAKDOWN (South African CAPS Curriculum):")
    for subj, cnt in by_subj.most_common(8):
        print(f"    {subj:<30s}: {cnt:>5d} lessons ({cnt / tot_s2_ver * 100:4.1f}%)")

    print("\n" + "-" * 80)
    print("  ⏱️ PRODUCTION BY COACHING MODE:")
    for mode, cnt in by_mode.most_common():
        print(f"    {mode:<30s}: {cnt:>5d} lessons ({cnt / tot_s2_ver * 100:4.1f}%)")

    print("\n" + "-" * 80)
    print("  🎯 TEACHING STRATEGY SPREAD (Pedagogical Diversity):")
    for strat, cnt in by_strat.most_common(10):
        print(f"    {strat:<30s}: {cnt:>5d} lessons ({cnt / tot_s2_ver * 100:4.1f}%)")

    if ag_by_task:
        print("\n" + "-" * 80)
        print("  🧩 AGENTIC TASK FAMILY BREAKDOWN:")
        for task, cnt in ag_by_task.most_common():
            print(f"    {task:<30s}: {cnt:>5d} verified samples")

    print("=" * 80)
    print("To refresh live status at any time, run:")
    print("    python tools/stage2_status.py")
    print("=" * 80)

if __name__ == "__main__":
    print_status_dashboard()
