# Stage 2 — Training Data Generation Pipeline

> **Target:** 10,000–15,000 cumulative SFT samples (Stage 1 + Stage 2)
> **Status:** Ready to run

## What Changed from Stage 1

| Feature | Stage 1 | Stage 2 |
|---------|---------|---------|
| **Strategies** | 1 (step_walkthrough only) | 10 with weighted rotation |
| **Student personas** | 1 (lost, 3 turns) | 6 states × 3+ styles × variable turns |
| **Few-shot exemplars** | None | 4 exemplars (math, science, language, Afrikaans) |
| **Quality check** | SymPy match only (language: `len >= 2`) | SymPy + 10-point rubric scoring |
| **Paper selection** | Hardcoded 12 papers | Auto-discovers from 225 untouched papers |
| **Deduplication** | None | Excludes all Stage 1 papers |
| **Retries** | None | Up to 2 retries for rubric-failed items |
| **JSON parsing** | Basic regex | Nested brace tracking + trailing comma cleanup |
| **Output schema** | `tutor-v1` | `tutor-v2` (adds `student_state`, `rubric_score`, `stage`) |
| **Prompt template** | ~40 lines | ~60 lines with strategy injection + exemplar |
| **Progress tracking** | None | `progress.json` with resumability |

## Teaching Strategies (10 total)

1. **step_walkthrough** — Socratic step-by-step guided walkthrough
2. **worked_example** — Show similar worked example, then transfer
3. **faded_example** — Progressively remove scaffolding
4. **error_spotting** — Present a deliberate mistake for the learner to find
5. **mnemonic_memory_hook** — Teach via mnemonics and analogies
6. **frustrated_learner_de_escalation** — Warm de-escalation for frustrated learners
7. **rapid_recall_drill** — Quick, efficient practice for confident learners
8. **compare_and_contrast** — Two valid approaches, learner picks
9. **exam_technique_focus** — Mark allocation and examiner expectations
10. **concept_first** — Verify concept understanding before solving

Strategies are weighted per subject category (math/science/language) and rotated within each paper for variety.

## Student Personas

| State | Description | Applicable Strategies |
|-------|-------------|----------------------|
| `lost` | No idea where to start | step_walkthrough, worked_example, mnemonic, frustrated, concept_first |
| `stuck` | Started but can't proceed | step_walkthrough, worked_example, faded_example, mnemonic, concept_first |
| `frustrated` | Wants to give up | frustrated_learner_de_escalation |
| `partially_correct` | Got part right, made an error | step_walkthrough, faded_example, error_spotting, compare, concept_first |
| `on_track` | Knows basics, needs confirmation | error_spotting, rapid_recall, compare, exam_technique |
| `advanced` | High achiever wanting depth | rapid_recall, exam_technique |

## Quality Rubric (10 checks)

1. Basic structure (messages array exists)
2. Turn count matches persona specification
3. Empty/trivially short content detection
4. Reasoning field presence in assistant messages
5. Anti-spoiler check (first response shouldn't reveal final answer)
6. Repetition detection (near-identical consecutive messages)
7. Language consistency (Afrikaans markers for AF subjects)
8. SymPy verification code presence (STEM)
9. Meta completeness (strategy_used, techniques)
10. Strategy compliance (output matches requested strategy)

Score >= 60/100 = PASS. Items scoring 50-59 get a soft pass if SymPy also verifies.

## File Structure

```
stage-2/
├── __init__.py
├── run_stage2_fleet.py       # Main fleet runner
├── progress.json             # Auto-generated, tracks completed papers
├── README.md                 # This file
├── prompts/
│   ├── __init__.py
│   ├── strategies.py         # 10 strategy definitions + weighted picker
│   └── few_shot_examples.py  # 4 few-shot exemplars (math, science, lang, AF)
└── quality/
    ├── __init__.py
    └── rubric_checker.py     # 10-point quality rubric
```

## Output & Audit Directories

- `workspace/gen/stage2/` — Raw model outputs (immutable record of all generations).
- `workspace/verified/stage2/` — Quality-checked Socratic lessons that passed mathematical and rubric verification.
- `workspace/verified/stage2_full_solutions/` — Complete worked solution demonstrations generated directly from official DBE marking memos.
- `workspace/rejected/stage2/` — **Dedicated User Rejection Audit Folder**: Every rejected item is logged with full forensic metadata (`rejection_reason`, `sympy_out`, `memo_target`, `verify_code`, `rubric_score`, `rubric_issues`, `parsed_record`, `raw_response`) so you can inspect whether the verification was too strict or caught genuine model errors.
- `workspace/build/r2/` — Final compiled SFT dataset (Stage 1 + Stage 2 combined). Stage 1 (`workspace/build/r1/`) remains completely untouched.

## Zero-Cost Deterministic Verification Policy

Per operational directives, **NO second LLM / judge API calls are used** for verification, saving thousands of tokens and API credits:
- **STEM Subjects (Maths, Wiskunde, Physical Sciences, Fisiese Wetenskappe):** Verified via local Python subprocess SymPy execution + tolerance-aware numeric matching (`_num` handling SA decimal comma `0,15`, LaTeX `\frac{a}{b}`, scientific notation, and 1% relative tolerance).
- **Language Subjects (English HL/FAL, Afrikaans HL/FAL):** Verified via deterministic rule-based rubric checking: turn count, minimum length, private reasoning presence, anti-spoiler compliance, and authentic Afrikaans language markers.


## How to Run

```bash
cd "h:\Users\Admin\Eishkom Lab\eishkom ai\fromm laude to start\files"
python stage-2/run_stage2_fleet.py
```

The script:
1. Auto-discovers 225 untouched papers from `workspace/items/`
2. Excludes all Stage 1 papers (41 papers)
3. Selects up to 80 papers (configurable via `MAX_PAPERS`)
4. Assigns papers to API models based on subject affinity
5. Generates Socratic dialogues with varied strategies + personas
6. Verifies with SymPy + rubric scoring
7. Saves to `workspace/verified/stage2/`
8. Auto-rebuilds the combined master dataset

## Training Protocol Reminder

> [!IMPORTANT]
> Stage 2 training uses a **FRESH base model** trained on OLD (Stage 1) + NEW (Stage 2) data combined.
> Do NOT fine-tune the Stage 1 checkpoint on new data alone.
> Increase LoRA rank from `--rank 16` to `--rank 32` or `--rank 64`.

## Configuration

Edit constants at the top of `run_stage2_fleet.py`:

| Variable | Default | Description |
|----------|---------|-------------|
| `TARGET_VERIFIED` | 4000 | Target verified Socratic lessons |
| `MAX_PAPERS` | 80 | Max papers per run |
| `MAX_RETRIES_PER_ITEM` | 2 | Retry count for rubric-failed items |
| `QUALITY_THRESHOLD` | 60 | Minimum rubric score (0-100) |

