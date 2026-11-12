import os
import sys
import json
import time
import ssl
import urllib.request
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

def load_env():
    keys = {}
    for env_path in [ROOT_DIR / ".env", ROOT_DIR / "sa-tutor-kit" / "sa-tutor-kit" / ".env"]:
        if env_path.exists():
            for line in env_path.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if "=" in line and not line.startswith("#"):
                    k, v = line.split("=", 1)
                    keys[k.strip()] = v.strip().strip("'\"")
    return keys

ENV_KEYS = load_env()
INTERN_KEY = ENV_KEYS.get("INTERN_API_KEY", "")
INTERN_BASE_URL = ENV_KEYS.get("INTERN_BASE_URL", "https://discovery-api.intern-ai.org.cn/v1")

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = f"{INTERN_BASE_URL}/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {INTERN_KEY}",
    "User-Agent": "curl/8.4.0"
}

sys.path.insert(0, str(ROOT_DIR / "stage-2"))
from run_stage2_fleet import TEMPLATE_V2, pick_strategy, pick_student_persona, get_few_shot_for_subject

test_item = {
    "subject": "physical_sciences",
    "grade": 12,
    "topic": "Newton's Second Law",
    "question": "A 5 kg block is pulled with a horizontal force of 20 N. If friction is 5 N, calculate acceleration.",
    "memo": "F_net = F_applied - f_k = 20 - 5 = 15 N; a = F_net / m = 15 / 5 = 3 m/s^2",
    "final_answer": "a = 3 m/s^2",
    "marks": 3
}

strategy = pick_strategy("physical_sciences")
persona = pick_student_persona("physical_sciences", marks=3)
few_shot = get_few_shot_for_subject("physical_sciences", mode="normal")

ctrl = {
    "subject": "physical_sciences",
    "grade": 12,
    "subject_language": "en",
    "response_language": "mirror",
    "strategy": strategy["name"],
    "answer_policy": "guided",
    "student_level": persona["student_level"],
    "tone": "encouraging",
    "response_length": "medium",
    "tools": ["calculator", "board"],
    "math_format": "latex"
}

final_turn_instr = (
    "   In the FINAL assistant message, you MUST include:\n"
    "   a) The consolidated final answer matching the memo.\n"
    "   b) '### 📖 Formula Breakdown (How It Works):'\n"
    "      * The Formula: [state the exact formula in KaTeX clearly]\n"
    "      * What the letters mean:\n"
    "        * [letter 1]: [meaning in plain everyday language]\n"
    "        * [letter 2]: [meaning in plain everyday language]\n"
    "      * Why we use it: [explain in simple, accessible, friendly terms why it works and why we chose it]\n"
    "   c) '🎯 Exam Tip:' [mark allocation tip or common exam pitfall to avoid]"
)

prompt = TEMPLATE_V2.format(
    few_shot=few_shot,
    strategy_instructions=strategy["prompt_fragment"],
    subject=test_item["subject"],
    grade=test_item["grade"],
    topic=test_item["topic"],
    passage="",
    question=test_item["question"],
    memo=test_item["memo"],
    final=test_item["final_answer"],
    lang="en",
    state=persona["state"],
    state_desc=persona["desc"],
    learner_script=" -> ".join(persona["script"]),
    turns=persona["turns"],
    coaching_mode="Deep-Dive Socratic Mode (3-4 turns)",
    control=json.dumps(ctrl, indent=2),
    strategy_name=strategy["name"],
    techniques_json=json.dumps(persona["techniques"]),
    tool_instruction="In your private reasoning, demonstrate the calculation as: [TOOL CHECK: calculator(expression=\"...\") -> result].",
    verify_code_instruction="In meta.verify_code, write a short Python snippet using sympy that prints the final answer.",
    final_turn_instruction=final_turn_instr,
)

system_msg = (
    "You are an expert South African CAPS physics teacher. "
    "Output raw JSON starting with { and ending with } immediately. "
    "Keep internal chain-of-thought concise and put all explanations inside the JSON."
)

payload = {
    "model": "deepseek-v4.1-flash-1017",
    "messages": [
        {"role": "system", "content": system_msg},
        {"role": "user", "content": prompt}
    ],
    "temperature": 0.2,
    "max_tokens": 3000
}

print("Sending full Stage 2 prompt to Intern-AI DeepSeek...")
t0 = time.time()
req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
with urllib.request.urlopen(req, context=ctx, timeout=60) as resp:
    raw = resp.read().decode("utf-8")
    dt = time.time() - t0
    data = json.loads(raw)
    choice = data["choices"][0]["message"]
    content = choice.get("content") or choice.get("reasoning_content") or ""
    print(f"Received in {dt:.2f}s! ({len(content)} chars)")
    print("Content preview:", content[:200])

