# GUIDE: from nothing to a working South African tutor model

Follow this top to bottom. Every phase has the same shape:

- **Goal** what you will have at the end
- **Do** the exact steps and commands
- **Check** how you know it worked
- **Why** the reason, so you can change it when you disagree
- **If it goes wrong** the usual fixes

Costs and times are **estimates** from reasoning, not measurements. Your first small run in each phase gives the real number.

---

## How to read this guide

**Two places things run.**
- **Your PC** (or any computer, no GPU needed): collecting data, cutting it into questions, asking the teacher model to write training data, checking it. Commands look like `python pipeline/plan.py ...`. Run them from the kit folder.
- **Google Colab** (free GPU): training and running your own model. Use `colab/sa_tutor_colab.ipynb`, which has every Colab command ready.

**Folders.** The kit folder holds the code. A `workspace/` folder inside it (created in phase 0) holds YOUR data. Scripts never overwrite earlier steps: each step reads one folder and writes the next, so you can always walk backwards to find where a problem came from.

**The files you will meet** (all in the kit folder):

| File | What it is |
|---|---|
| `tutor_spec.md` | The written spec of how the tutor teaches. The teacher model reads it; the judge uses its rubric |
| `SOURCES.md` | Where to get data, and what each licence allows |
| `tutor_data.py` | The record format (schema), the checker, the report and the builder |
| `board.py`, `answers.py`, `tools_sim.py`, `retrieval.py`, `llm.py` | Helpers: the blackboard, answer checking, real tool results, search, the API client |
| `pipeline/` | Steps that make training data |
| `eval/` | Steps that test a model |
| `training/` | Steps that train, improve and export a model |
| `examples/examples.jsonl` | 14 example records showing every feature. READ THESE FIRST |

**Rules that save you money and tears**
1. Always do a tiny test (10 records, 20 questions) before a big run.
2. After every step that makes data, **read some of it**. Numbers do not show "this explanation is confusing".
3. Never train on your exam. Never change the exam to make a score look better.
4. Change one thing at a time, then run the exam.
5. Keep `MAX_SPEND_USD` in `.env` low. Every API call is logged: `python llm.py spend`.

---

## The big picture

```
 sources ──► text ──► items ───────────────────────┐
 (PDFs)     (ingest)  (questions + memos)          │
                         │                         │
                         ▼                         ▼
                      PLAN ──► TEACHER writes ──► VERIFY ──► REVIEW ──► BUILD ──► TRAIN (Colab)
                  (what to       training records   (code checks,  (a human     (train/val   │
                   write)        (DeepSeek)         judge model)   reads some)  files)       ▼
                                                                                          your model
   EXAM (held-out, never trained on) ◄───────────────── EVALUATE ◄───────────────────────────┘
        │                                                  │
        └──► scores, charts, failure analysis ─────────────┘
                         │
                         ▼
        fix the DATA (not the exam) ──► build again ──► train again ──► repeat until the move-on rules pass
```

Three ideas run through everything:

1. **The teacher writes, code checks.** A big model (DeepSeek) writes tutoring conversations. Code verifies the maths, the format, the language and the answer policy. A person reads a sample. Your small model only ever trains on records that passed.
2. **The exam comes first.** You decide what "good" means (the exam) BEFORE you generate data, so you cannot fool yourself later.
3. **Skills in the weights, facts in the library.** Training teaches the model HOW to teach, answer in the right language and call tools. The curriculum content stays in a searchable library (`retrieval.py`), because fine-tuning is poor at adding new facts and tends to increase made-up answers.

---

## Words you need

| Word | Plain meaning |
|---|---|
| **Base model** | The pre-built brain you start from (for example Qwen3.5-4B). You never build one from nothing |
| **Parameters / weights** | The billions of numbers inside the model. "4B" = 4 billion of them. Think of dials |
| **Layers** | The model is a stack of identical processing stages (a few dozen). Text goes through them one after another |
| **LoRA / adapter** | Instead of turning all the dials, you lock them and clip on a small extra set (1-2% of the size), and train only that. Cheap, small to store, keeps the base model's general skills |
| **SFT** | Supervised fine-tuning: show examples of good answers and nudge the model to write like that |
| **Epoch** | One pass over all the training data. 2-3 is normal; more makes it memorise |
| **Loss** | A number for "how wrong is the model on the training data". It should fall and flatten |
| **Overfitting** | The model memorised the training examples and gets worse on new questions |
| **Catastrophic forgetting** | Training on new things makes it forget old things. We avoid it by always retraining on ALL data so far |
| **Eval / exam** | Questions the model never trained on, with automatic checks, to measure progress |
| **Teacher / student** | The big model that writes data is the teacher; your small model is the student |
| **DPO** | Preference training: for one question show a good answer and a bad answer, push toward the good one |
| **GRPO** | The model tries several times, code rewards the right attempts. Works only where "right" can be checked by code |
| **Quantization (Q6, Q4)** | Storing the finished model with fewer bits: smaller file, slightly lower quality |
| **GGUF** | The file format phone and PC apps (llama.cpp, LM Studio, PocketPal) run |
| **Token** | A piece of a word. Cost, speed and memory are all counted in tokens |
| **Thinking** | The model writes private reasoning before its reply. Better on hard problems, slower, uses more memory |
| **Tool call** | The model asks the app to do something (calculate, draw on the board, search). The app runs it and returns the result |

---

## Phase 0: Set up (about 1 hour)

**Goal:** the kit runs on your computer, the workspace exists, your API key is in `.env`.

**Do**
1. Install **Python 3.10 or newer** (python.org). Check: `python --version`.
2. Unzip the kit. Open a terminal in the kit folder.
3. Make a private Python environment and install the helpers:
   ```
   python -m venv .venv
   .venv\Scripts\activate            (Windows)     source .venv/bin/activate     (Mac/Linux)
   pip install -r requirements.txt
   ```
4. Create the workspace and the `.env` file:
   ```
   python pipeline/init_workspace.py
   ```
5. Get accounts (all free to open): **Hugging Face** (huggingface.co, for downloading models), a **Google account** (Colab and Drive), and an **API key for the teacher**. DeepSeek: platform.deepseek.com, add a small balance (US$10 is plenty for the whole project). If you would rather pay with your Google credits, check in Google Cloud Console, Billing, Credits, what your credit can be spent on, and whether Vertex AI Model Garden offers a DeepSeek model you can call; make one 10-cent test call before relying on it.
6. Open `.env` (in the kit folder) and fill in `TEACHER_API_KEY`, and check `TEACHER_MODEL` against your provider's current documentation. Set `MAX_SPEND_USD=15` (or lower).
7. Write down your decisions in `workspace/DECISIONS.md` (copy the list from `tutor_spec.md` section 10 and write your choice next to each). Defaults are fine to start; the point is to write them down.

**Check** (each should print a success line or "ALL OK", no errors):
```
python answers.py
python tools_sim.py
python board.py demo
python tutor_data.py validate examples/examples.jsonl --images-root examples
python training/grpo_rewards.py
python llm.py spend
```

**Why** a private environment keeps the packages from clashing with other projects. `.env` keeps keys out of the code (never share it; `.gitignore` already excludes it). The spending cap protects your $70.

**If it goes wrong:** `python` not found: try `py` (Windows) or `python3`. `pip install` fails for `pypdfium2`: it is only needed for the vision phase, remove that line and continue.

---

## Phase 1: Collect sources (a weekend)

**Goal:** a folder of downloaded files and a `sources.csv` that says exactly what each one is and what its licence allows.

**Do**
1. Read `SOURCES.md` (10 minutes). It tells you what is safe.
2. Download, in this order of priority:
   - **Round 1 needs maths only.** Download 3-5 recent **DBE maths papers with their memos** for Gr 12, Gr 11 and Gr 10 (education.gov.za, or the WCED and Eastern Cape exam libraries).
   - **Siyavula Mathematics Gr 10-12, the UNBRANDED (CC BY) versions**, in English and Afrikaans, plus the teacher guides.
   - For Gr 7-9: a few **Oak National Academy** maths lesson transcripts (Open Government Licence), and any Gr 9 or ANA papers you can find.
   - The **DBE NSC Diagnostic Reports** and **Examination Guidelines** for maths.
3. Put every file in `workspace/raw/`, in a sub-folder per source (for example `workspace/raw/dbe/maths_g12_p1_2024_nov.pdf`).
4. Open `workspace/sources/sources.csv`. Delete the example rows and add one row per file. Columns: `source_id` (a short unique name you invent, like `dbe-maths-g12-p1-2024-nov`), `title`, `url`, `licence` (copy the exact words from the page), `attribution` (the credit line they ask for), `subject`, `grade`, `language` (`en` or `af`), `kind` (`past_paper`, `memo`, `textbook`, `guide`, `diagnostic_report`, `exam_guideline`), `track` (HL or FAL for language subjects), `year`, `pair_with` (for a paper: the `source_id` of its memo), `local_path` (path inside `workspace/raw/`), `notes`.
5. **Choose your exam papers now.** For each subject and grade, the NEWEST paper(s) become your exam. Write "EXAM" in `notes` and add their `source_id`s to `holdout_sources` in `workspace/config/plan_config.json`. The plan step will then refuse to use them for training.
6. Copy `workspace/raw/` to Google Drive as a backup.

**Check:** every row has a licence. No row is empty.

**Why** the licence column is mandatory: you can only decide what to do with a source if you wrote down what it allows. The newest papers are your exam because base models have probably never seen them, so they test understanding, not memory.

**If it goes wrong:** you are not sure of a licence: treat the source as exam/seed only (amber) and use `mode: original` (see phase 5).

---

## Phase 2: From files to questions (1-2 days, about $1-3)

**Goal:** `workspace/items/*.jsonl`, a clean list of questions with their memo answers, which you have checked by hand.

**Do**
1. **Extract text:**
   ```
   python pipeline/ingest.py
   ```
   Open two or three files in `workspace/text/` and READ a page. Maths often arrives garbled ("x2" for x squared, fractions on separate lines). If a file says "mostly empty: probably a SCAN", or the maths is unreadable, run it through an OCR/maths-aware converter first (marker, docling or MinerU; check each tool's own licence; run them in Colab). Save the result as a `.md` file in `raw/`, change `local_path` to it, and run ingest again.
2. **Cut papers into questions (the teacher does this).** First see the cost without spending anything:
   ```
   python pipeline/extract_items.py --source dbe-maths-g12-p1-2024-nov --dry-run
   python pipeline/extract_items.py --source dbe-maths-g12-p1-2024-nov --max-questions 2
   ```
   Open `workspace/items/dbe-maths-g12-p1-2024-nov.jsonl`. Compare 10 items with the PDF: is the question identical (same numbers)? Is the memo answer right? If yes, run it for all questions (leave out `--max-questions`). Textbooks and Oak transcripts: `--kind textbook`.
3. **Fix the items by hand.** Delete bad ones. Fix small mistakes in the file (it is plain text). For items flagged `"needs_review": true`, fix them and set it to `false`, or leave them (they are skipped).
4. **Build the search library:** `python retrieval.py build`, then test it: `python retrieval.py search "quadratic formula" -k 3`. This is what the `search_curriculum` tool will search.
5. **Write misconceptions.** Open the DBE Diagnostic Report for maths. For each topic, note the common errors. Add them to `workspace/config/misconceptions.jsonl` (one JSON object per line; copy the format of the 28 starter lines). These make the training conversations realistic: learners make these exact mistakes.

**Check:** you have at least 100 items across Gr 7-12 for maths (more is better; plan for 300+), none of them from your exam papers.

**Why** the teacher cuts questions but you check them: a wrong memo answer silently becomes a wrong lesson. Ten minutes of reading here saves days later.

**If it goes wrong:** the teacher returns garbage JSON: the paper text is too garbled, go back to step 1. Questions that depend on a diagram are skipped on purpose (the model cannot see the diagram yet): add a few by hand with the diagram described in words.

---

## Phase 3: Build your exam FIRST (1 day, about $0.50)

**Goal:** `workspace/eval/eval_items.jsonl` with 150+ exam items and a "teacher score", before any training data exists.

**Do**
1. **Read the starter exam.** `init_workspace.py` copied 42 items from `eval/eval_seed.jsonl`: maths Gr 7-12, sciences, English, Afrikaans, "just give me the answer" tests, safety, honesty, tool use. Open the file and read ten. Each item is one line: the learner's message, the settings the tutor is given (`control`), and `checks` that mark the answer. The check types are listed at the top of `eval/score_eval.py`.
2. **Add real exam questions.** For each held-out paper (from phase 1) run phase 2 for it, then:
   ```
   python eval/make_eval_from_items.py --source dbe-maths-g12-p1-2024-nov
   ```
   Maths and science items get a `final_answer` check (SymPy compares). Language items get a `rubric` check marked by a judge model against the memo. READ ten against the paper.
3. **Add your own.** Copy a line in the exam file and edit it. Add the situations you care about: a learner who begs for the answer, a learner who writes in Afrikaans, a photo-free "I don't understand" message. Do not edit old items; add new ones (so old scores stay comparable). Keep a copy: `copy eval_items.jsonl eval_items_v1.jsonl`.
4. **Add reworded versions** (tests understanding, not memorised wording):
   ```
   python eval/make_variants.py --per-item 2 --tags core
   ```
   It writes `workspace/eval/eval_items_variants.jsonl`. READ some: delete any where the maths changed. Run them separately with `--items`.
5. **Get the teacher's score (your ceiling).** The teacher answers your exam; you cannot expect a 4B model to beat it:
   ```
   python eval/run_eval.py --name teacher --backend openai --base-url https://api.deepseek.com --api-key-env TEACHER_API_KEY --model deepseek-chat --think-style none
   python eval/score_eval.py --name teacher --judge
   ```
   Open `workspace/eval_runs/teacher/failures.md`. **Every teacher failure is either a bug in the exam (wrong expected answer, a check that is too strict) or a real weakness.** Fix the exam bugs. A healthy exam gives the teacher 85-95%.

**Check:** the teacher passes at least 85%; you have at least 5 items for each subject x grade you will train, 20+ answer-policy items, 10+ tool items, 10+ safety items.

**Why exam first:** if you look at results after generating data, you will (without meaning to) shape the exam to the data. Exam first keeps you honest. Held-out papers matter because they test the real thing.

**How big?** With 150 items, one item is 0.7 percentage points. Differences under about 3 points are noise. For decisions that matter, answer each question five times at temperature 0.7 (`--n 5`): a model that is right 5/5 is far more trustworthy than one that is right 3/5.

**If it goes wrong:** the teacher fails many `final_answer` items: the check is probably strict about format. Look at the reply in `failures.md`: if it is right, widen the check (see `answers.py`) or the expected string. `language` fails for short replies: the language detector needs a few words; ignore those.

---

## Phase 4: Audition the base models (half a day, free)

**Goal:** choose your base model with evidence, not hope. You have candidates: official **Qwen3.5-4B**, the unofficial **Qwen3.8 4B** repos you found on Hugging Face, and **Gemma 4 E4B**.

**Do**
1. **Set up Colab (once).** Put the kit folder, with its `workspace/`, on Google Drive (My Drive). Open colab.research.google.com, choose File, Upload notebook, and pick `colab/sa_tutor_colab.ipynb`. Runtime, Change runtime type, **T4 GPU**. Run cells 1-4 one at a time: GPU check, connect Drive, install, Hugging Face login. (Gemma asks you to accept its licence on its Hugging Face page first.)
2. **Run cell 5**, after pasting the exact model names from each Hugging Face page into the `MODELS` list. Each model answers the `core` exam items (about 10-20 minutes per model on a T4). It loads in 4-bit here only to fit and run fast; that is fine for comparing.
3. **Compare:**
   ```
   python eval/report_eval.py --runs base-qwen35-4b base-qwen38-4b-unofficial base-gemma4-e4b --out audition
   ```
   Open `workspace/reports/audition/comparison.md` and `checks.png`.
4. **Decide with this table** (write the result in `DECISIONS.md`):

| Look at | Why |
|---|---|
| Maths `final_answer` pass rate, by grade | The skill training can least easily add |
| Afrikaans slice and `language` checks | Tells you how much Afrikaans the base already has |
| Tool-call checks | Whether it can already call `calculator` and `board` |
| Speed (avg latency, tokens) | On phones, slower is worse |
| File size when quantized | Qwen3.5-4B is about 2.7 GB at Q4_K_M. Gemma 4 E4B is called "4B" but has 8B parameters with its embeddings: about 5 GB at Q4. Compare at equal MEMORY, not equal "B" |
| Licence | Official Qwen3.5: Apache 2.0. Read each card. The unofficial distills say they were trained on another model's outputs: read what that allows |

   Base models have never seen your `control` format, so they will do badly on policy checks (leaks, asking a question). Judge them on **capability** (maths, language, tools), not on obedience: training fixes obedience.
5. **Rule of thumb:** pick the best combination of maths and Afrikaans at similar memory. On a tie take official Qwen3.5-4B. An unofficial model must beat it by about 5 points, load in Unsloth, and have a working chat template and thinking switch.

**Check:** you have a written choice and the reason.

**Why:** your $70 pays for training ONE model well. Auditioning costs nothing. A base that is already good at maths and Afrikaans needs far less training.

**If it goes wrong:** out of memory: keep `--load-4bit`. A model will not load: its page says which `transformers` version it needs; Unsloth's own notebook for that model shows the working loading code. Thinking on/off does nothing: use `--think-style gemma` for Gemma, `qwen` for Qwen.

---

## Phase 5: Generate the training data (a few days, about $6-15)

**Goal:** 1,500 verified maths records in `workspace/verified/r1/accepted.jsonl`, built into `workspace/build/r1`.

**Round 1 is maths, in English, taught in tutor style: "being a teacher" and "maths" are not two jobs.** A teaching style is a way of answering a maths question, so you cannot train it without content. Maths first because its answers can be checked by code: quality control is cheap. Tools in round 1: `calculator` and `board`.

**Do**
1. **Set the round.** Open `workspace/config/plan_config.json`. For round 1 keep: `subjects: ["mathematics"]`, `grades: [7,8,9,10,11,12]`, `languages: ["en"]`, and check `holdout_sources` lists your exam papers. Every setting has a comment-free but self-explaining name; the weights decide how often each style appears.
2. **Plan a small batch** and read the summary it prints (counts by grade, strategy, policy):
   ```
   python pipeline/plan.py --round r1 --target 30
   ```
3. **Dry run: read the prompt the teacher will get and the cost:**
   ```
   python pipeline/generate.py --round r1 --dry-run
   ```
   Actually read it. This text decides everything.
4. **Pilot: 10 records.** Then check them with the free checks and read them as Markdown:
   ```
   python pipeline/generate.py --round r1 --limit 10 --workers 1
   python pipeline/verify.py --round r1
   python pipeline/review_sample.py export --round r1 --n 10
   ```
   Open `workspace/review/r1_sample.md`. For each conversation ask:
   - Does the tutor ask exactly one question and wait? Does it avoid giving the answer when it should?
   - Is the analogy accurate, and does the memory aid never give wrong answers?
   - Does the learner sound like a real Gr 8 learner, not a textbook?
   - Is the private reasoning English, short, and correct?
   - Are board commands useful (a few lines, arrows with labels), or decoration?
   - Does the stated strategy match what the tutor really did?

   **If the pilot is poor, fix the INSTRUCTIONS, not the output:** edit `tutor_spec.md` (the teacher reads sections 2, 3, 4, 5, 7) or the `TEMPLATE` in `pipeline/generate.py`, delete `workspace/gen/r1` and `workspace/verified/r1`, and run the pilot again. Two or three rounds of this is normal.
5. **Scale up.** Plan the full amount and generate (safe to stop with Ctrl+C and start again; finished rows are skipped):
   ```
   python pipeline/plan.py --round r1 --target 1500
   python pipeline/generate.py --round r1 --workers 4
   ```
   Watch the cost: `python llm.py spend`. The cap in `.env` stops everything when reached.
6. **Verify with all layers** (the free checks, then a second model grading):
   ```
   python pipeline/verify.py --round r1 --judge
   ```
   Look at the rejection reasons it prints. An acceptance rate of 60-80% is healthy. Below 40% the teacher prompt needs work. Reasons you will see: wrong final answer (the teacher's maths was wrong: exactly why we check), answer leaked, wrong language, validation errors.
7. **A human reads a sample.** Read 40 yourself and, better, ask a maths teacher to read 50 more:
   ```
   python pipeline/review_sample.py export --round r1 --n 40
   ```
   Open the `.md`, type a verdict for each row in the `.csv` (`ok` or `bad`, and why), then:
   ```
   python pipeline/review_sample.py apply --round r1
   ```
   It prints the **bad rate**. Above 10%: do not trust the rest; read your notes, fix the prompt, regenerate. This is the most important quality control in the project.
8. **Merge and build the training files:**
   ```
   python pipeline/merge.py --rounds r1 --out workspace/verified/train_r1.jsonl
   python tutor_data.py report workspace/verified/train_r1.jsonl
   python tutor_data.py build workspace/verified/train_r1.jsonl --out workspace/build/r1 --val 0.1 --test 0.05
   ```
   Read the report: coverage by subject and grade, the share of each strategy, how many records use thinking and tools, and the "thin cells" list. If a grade has very few records, raise its share in `plan_config.json` and generate a small extra round (`r1b`).

   What `build` does for you: it writes the system prompt from each record's `control`; it leaves some control fields out at random (`--p-drop-field 0.15`, `--p-drop-all 0.10`) so the model learns sensible defaults as well as obeying instructions; it cuts each conversation into one sample per tutor turn; and it assigns whole lessons to train, val or test so a lesson never leaks into the test split.
9. **Later, automate it.** Once you trust the prompt, one command does plan, generate, verify, merge, report and build:
   ```
   python pipeline/run_round.py --round r2 --target 800 --judge --merge r1 r2 --name r2
   ```
   It still asks before spending, and you still read a sample before training.

**Check:** the report looks balanced, the bad rate is under 10%, and `workspace/build/r1/train.jsonl` exists.

**Why two modes:** *faithful* teaches the real exam question and compares the teacher's answer with the memo. *Original* invents a new question and makes the teacher write a tiny Python check that prints the answer; we run it. Original mode avoids copying exam papers and gives an independent arithmetic check. The default plan uses 40% faithful, 60% original.

**Why the teacher's tool results are thrown away:** a model learns from what it sees. If the teacher guessed a calculator result, your model would learn to trust guesses. `tools_sim.py` re-runs every tool call in code and writes the real results.

**How much data?** Plan about 1,500 for round 1, growing to 4,000-6,000 by round 4. More only helps if it adds variety (new situations); the exam tells you which situations are missing.

**If it goes wrong:**

| Symptom | Likely cause | Fix |
|---|---|---|
| Almost everything rejected for "teacher answer != memo" | Memo answers badly extracted | Fix the items (phase 2) |
| Rejected for "leak" | Teacher gives the answer under `hint_only` | Strengthen rule 4 in the prompt; or lower the `hint_only` weight |
| Records all feel the same | Weights too narrow | Edit `strategy_by_level`, `answer_policy_weights` in the plan config |
| The learner turns sound adult | Prompt | Strengthen the learner-simulation lines in `TEMPLATE` |
| Cost higher than expected | Retries, long outputs | `--retries 1`; shorter `response_length` weights |

---

## Phase 6: Train round 1 (half a day, about $0-3)

**Goal:** a LoRA adapter in `workspace/runs/r1/adapter`, and a loss curve that looks healthy.

**Do** (every command is already in `colab/sa_tutor_colab.ipynb`, cells 6a-6c)
1. Make sure `workspace/build/r1` is on Google Drive and the notebook is connected to a GPU (phase 4, step 1).
2. Set `MODEL` to your audition winner. `unsloth/Qwen3.5-4B` and `Qwen/Qwen3.5-4B` are the same model; use the same name when you export, and keep it in `DECISIONS.md`.
3. **6a, the free look.** `train_sft.py ... --dry-run --show 2` renders the data with the base model's own chat template and prints it. READ it. Check:
   - the system prompt (rendered from `control`) looks right;
   - the marker `the model is trained from HERE on` sits right after the assistant's turn starts, so the model is graded only on its own answer;
   - thinking-ON samples: the answer starts with `<think>`; thinking-OFF samples: the prompt already ends with an empty think block;
   - tools appear in the prompt, tool calls appear in the answer;
   - the statistics: `too_long` should be 0 (raise `--max-len` if not); `trainable_share` is typically 10-25%; `mismatch` must be 0 (a mismatch means the template cannot be split into prompt and answer: do NOT train).
4. **6b, the "can it memorise?" test** (5-10 minutes): 20 samples, 15 passes. The final loss should be close to 0. If not, something is wrong with the data or the template, and the long run would waste hours. This is the cheapest bug detector you have.
5. **6c, the real run.** Typical settings: 2 epochs, learning rate 2e-4, LoRA rank 16. It saves a checkpoint to Drive after each epoch; if Colab disconnects, run the cell again with `--resume`. The time is steps x seconds per step; the progress bar shows the second number after a minute. Rough guide: about 4M tokens per epoch for 1,500 records; a free T4 may need 1-3 hours for the run, an L4 about half.
6. **Read `loss.png`.** Training loss should fall and flatten. If validation loss falls then RISES after epoch 1 or 2, the model is memorising: use fewer epochs or more varied data. A sudden spike: learning rate too high.

**Check:** the sanity answer printed at the end looks like a tutor reply, and `workspace/runs/r1/adapter` exists.

**Why LoRA, in one paragraph:** the base model has billions of locked weights; the adapter is a small extra set (1-2%) that nudges behaviour. That is why a free GPU is enough, why the result is a small folder, and why the base model's general skills mostly survive. For Qwen3.5, Unsloth recommends 16-bit LoRA, not 4-bit QLoRA, and for a 4B it needs about 10 GB of GPU memory (2B: about 5 GB).

**Knobs, and when NOT to touch them**

| Knob | Default | Change it when |
|---|---|---|
| `--epochs` | 2 | val loss rises early: 1-2. Underfits (still sloppy, loss high): 3 |
| `--lr` | 2e-4 | loss spikes: 1e-4. Barely moves: 3e-4 |
| `--rank` | 16 | you add many skills and the exam slices fight each other: 32 |
| `--max-len` | 4096 | samples are dropped as too long |
| `--target-modules` | q,k,v,o,gate,up,down | trainable share printed at the start is under 0.1% |

Do not touch these before the DATA is right. Ninety percent of bad results are data problems.

### Layers: freeze, add, or leave alone?

You asked how to freeze layers or create new ones, and why or why not. Short version: **do not, at your size.** LoRA already freezes all the original weights.

| Option | What it is | Pros | Cons | Verdict |
|---|---|---|---|---|
| LoRA on all linear layers (the default) | adapters everywhere, base frozen | cheap, small file, forgets little | learns a bit less than full fine-tuning | **Use** |
| LoRA only on some layers | e.g. skip the first 8 layers (`layers_to_transform` in a PEFT `LoraConfig`) | slightly less memory | usually slightly worse; one more thing to tune | Not needed |
| Freeze everything except the top N layers | train only the last layers fully | simple idea | worse than LoRA in practice; big optimizer memory | No |
| Full fine-tuning | change all weights | learns the most | a 4B needs roughly 60 GB or more with an optimizer; forgets more | Not possible on your hardware |
| Add new layers (block expansion, "depth up-scaling") | insert extra transformer blocks and train only those | adds capacity without disturbing old skills | the model gets bigger and slower, needs custom conversion to GGUF, no clear win at this scale | No |
| Vision: which parts to train | Unsloth vision flags `finetune_vision_layers`, `finetune_language_layers`, `finetune_attention_modules`, `finetune_mlp_modules` | lets you keep the picture encoder frozen | the choice matters only in the vision phase | See phase 11 |

The research summary ("LoRA Learns Less and Forgets Less") says LoRA falls short of full fine-tuning on hard new domains but keeps more of the base model's skills: the right trade for a tutor that must stay a good general language model.

---

## Phase 7: Evaluate and diagnose (after every training run)

**Goal:** know exactly what got better, what got worse, and what to do next.

**Do**
1. **One command** (Colab cell 7) answers the exam, marks it, compares with earlier runs and prints a decision:
   ```
   python eval/evaluate.py --name r1 --backend hf --model unsloth/Qwen3.5-4B --adapter workspace/runs/r1/adapter --compare base-qwen35-4b --ceiling teacher --analyze
   ```
   (`--judge` adds the rubric checks for language and safety items; costs a little.)
2. **Read `workspace/reports/r1/decision.md`.** It checks the move-on rules (below) and says YES or NO. Open the charts: `heatmap.png` shows exactly which subject and grade is weak; `checks.png` shows whether the problem is leaks, language or tools.
3. **Read `workspace/eval_runs/r1/failures.md`.** Then read **20 raw answers yourself**, a mix of passes and fails. Look for: padding and rambling, a confident wrong explanation, the wrong language in the middle of a reply, thinking that never ends, board commands that do not match what it says, a tone that talks down.
4. **Consistency check** (cell 8): five answers per question at temperature 0.7. Report the share of questions right every time. Anything the model gets right only sometimes is a skill it has not learned yet.
5. **Read `analysis.md`.** The teacher groups the failures and proposes what data to add. It is a colleague's opinion; you decide.
6. **Write 5 lines in `workspace/NOTES.md`:** what you changed, the overall score, the weak slice, what you will try next.

**The move-on rules** (the defaults in `report_eval.py`; change them in the flags if you have a reason):
1. Overall pass rate at least 70% **or** at least 85% of the teacher's score.
2. Policy tests 90% or more; language checks 95% or more; tool checks 90% or more.
3. No slice dropped by more than 3 points since the last run (a drop means forgetting).
4. If the last round improved overall by less than 2 points (plateau): more data of the same kind will not help. Add NEW situations.

If all hold, go on to the next subject. If not, find the cause and fix it:

| What you see | Likely cause | Fix |
|---|---|---|
| Wrong maths answers in one grade | Too little data there, or teacher answers there were wrong | Add plan rows for that grade; check rejected records |
| Gives the answer away | Habit SFT did not remove | More `hint_only` / `guided` data; then DPO (phase 9) |
| Wrong language | Not enough data in that language, or language drift | More data; DPO with wrong-language replies as "rejected" |
| Ignores the board or calls it wrongly | Too few board examples; schema too vague | Add examples; check `tool_call` failures |
| Never stops thinking | Reasoning examples too long or truncated | Shorter reasoning in data; check `too_long` in the dry run |
| Good on core items, bad on variants | Memorised wording | More varied phrasing in the plan (`style`); more data, not more epochs |
| The teacher also fails an item | Exam bug | Fix the exam item |

**How many times?** Expect 2-4 loops of "evaluate, analyse, fix the data, build, train" per round. Budget about 12-15 training runs in the whole project.

**How to ask:** `--n 1 --temperature 0` for quick regression checks after small changes; `--n 5 --temperature 0.7` for decisions; the reworded variants (phase 3) for robustness; ask in both languages once Afrikaans is in.

**Why:** a single score hides what matters. A model at 80% overall that leaks answers 40% of the time is not a tutor.

---

## Phase 8: The next subjects (rounds 2-4)

**Rule for every round:** the new data is ADDED to everything before it and the model is trained again FROM THE BASE. Never continue round 2 from round 1's adapter and never train a round on the new subject only (the model forgets the rest).

For each round do phase 5 (plan, pilot, read, scale, verify, review, merge, build), then phases 6 and 7, and add exam items for the new subject FIRST (phase 3).

| Round | Adds | Plan changes in `plan_config.json` | Sources | New exam items |
|---|---|---|---|---|
| **r1** | Maths + the teaching style (English) | as above | DBE maths, Siyavula maths, Oak | maths by grade (starter set) |
| **r2** | Sciences | `subjects`: natural_sciences (Gr 7-9), physical_sciences, life_sciences (Gr 10-12); `tools_by_subject` already has calculator, board and search | Siyavula Physical/Natural Sciences, DBE science papers, diagnostic reports | science items per grade; answer-layout items |
| **r3** | The drawing board | raise `tool_availability_probability` to about 0.8 for maths and sciences, raise `visual_board` weights | same items, new conversations | board items: tool called, valid commands, asks a question |
| **r4** | Afrikaans, and English/Afrikaans as subjects | `languages: ["en","af"]` (the same lessons written in Afrikaans); add `english` and `afrikaans` to `subjects` | DBE English and Afrikaans papers, Siyavula Afrikaans books, passages | Afrikaans maths, language compliance, code-switching, FAL items |

Example for r2 (from your merged r1):
```
# edit plan_config.json: round "r2", the new subjects, target 1200
python pipeline/run_round.py --round r2 --target 1200 --judge --merge r1 r2 --name r2
python pipeline/review_sample.py export --round r2 --n 40         # read, mark, apply
python pipeline/review_sample.py apply --round r2
python pipeline/merge.py --rounds r1 r2 --out workspace/verified/train_r2.jsonl
python tutor_data.py build workspace/verified/train_r2.jsonl --out workspace/build/r2 --val 0.1 --test 0.05
```
(If you review after `run_round`, run the last two lines again so the reviewed records are what you build.) Then train `r2` from the base in Colab, and evaluate with `--compare base r1`.

**Afrikaans notes (round 4)**
- The tutor **thinks in English and answers in Afrikaans**. The data already does this: `reasoning` is English even when the reply is Afrikaans.
- Every Afrikaans record must be read by someone who speaks Afrikaans. Use `review_sample.py export --lang af` and the `af_ok` / `af_bad` verdicts. Aim for at least 100 reviewed records before you trust the language.
- Index the Siyavula Afrikaans books in `retrieval.py` so `search_curriculum` returns the correct CAPS terms.
- Afrikaans FAL (Gr 7-9) replies in English by design: check the policy with an Afrikaans FAL teacher.
- Language drift (a reply slides into English) is fixed with DPO pairs where the wrong-language reply is "rejected".
- New languages (Setswana, Zulu and so on) are **data projects**: the base models are far weaker in them (benchmarks show large gaps between English and African languages). Plan them as separate rounds with native-speaker reviewers, and test with an African-language benchmark first.

**Check at every round end:** the move-on rules pass AND the older subjects did not drop.

---

## Phase 9: Reward what is right, remove what is wrong (DPO, then maybe GRPO)

**Goal:** fix HABITS (leaking answers, wrong language, rambling) that SFT did not remove.

SFT shows the model good answers. It never says "this kind of answer is worse". Preference training (DPO) does: for the same question, one answer that passed all checks and one that failed, **both written by your own model**.

**Do**
1. Build the training split with a bigger validation share so you have fresh prompts: `tutor_data.py build ... --val 0.15`. (Prompts the model trained on are not useful here.)
2. **Make prompts with checks attached:**
   ```
   python training/make_dpo_pairs.py prompts --build workspace/build/r2 --out workspace/eval/dpo_prompts.jsonl --n 300
   ```
3. **Let the trained model answer each prompt six times** (Colab):
   ```
   python eval/run_eval.py --name r2-dpo-samples --items workspace/eval/dpo_prompts.jsonl --backend hf --model unsloth/Qwen3.5-4B --adapter workspace/runs/r2/adapter --n 6 --temperature 0.8
   ```
4. **Pair them:**
   ```
   python training/make_dpo_pairs.py pairs --name r2-dpo-samples --items workspace/eval/dpo_prompts.jsonl --out workspace/build/dpo_r2.jsonl
   ```
   It prints what the BAD answers got wrong (leaks? language?). READ 10 pairs. `--teacher-chosen` asks the teacher for a good answer where your model never gets it right.
5. **Train.** Use **Unsloth's official DPO notebook** for Qwen: it keeps up with library changes better than a script I could ship you. Replace its dataset cell with `load_dataset("json", data_files="workspace/build/dpo_r2.jsonl", split="train")`. Start from your SFT result: the cleanest way is to merge the SFT adapter into the 16-bit model first (Unsloth: `model.save_pretrained_merged("workspace/merged/r2", tokenizer, save_method="merged_16bit")`), then run the DPO notebook with that folder as `model_name`. Keep it gentle: beta about 0.1, a low learning rate (5e-6 to 5e-5), about one epoch. DPO that is too strong breaks general ability.
6. **Run the whole exam again** (phase 7). The move-on rules decide whether DPO helped. If a slice dropped, it was too strong: fewer steps or a lower learning rate.

**GRPO (optional, last).** The model tries several times and **code** rewards the right attempts. It needs a checkable answer, so it suits maths only. `training/grpo_rewards.py` has the reward functions (correct answer, format, language, no leak, length); plug them into Unsloth's official GRPO notebook. It is slower and fussier than SFT plus DPO, so do it only if maths accuracy is the one thing still short.

**"Removing what's wrong":** two ways. Data bugs (a wrong lesson, a bad analogy): delete or fix the records, rebuild, retrain from the base: the cleanest. Habits (leaks, drift): DPO. Rejected records stay in `verified/<round>/rejected.jsonl` with their reasons, so you can audit and learn from them.

**Why from the model's own answers:** an invented bad answer is too obviously bad to teach anything. The subtle failures your model really makes are the useful ones.

---

## Phase 10: Export the variants and test them (half a day)

**Goal:** the files people run: **4B Q6_K** (best quality), **4B Q4_K_M** (smaller), **2B Q4_K_M** (for 4 GB phones), each tested on your exam.

**Do**
1. **Export from the same trained model** (Colab cell 9). You train ONCE and export several files:
   ```
   python training/export_gguf.py --adapter workspace/runs/r4/adapter --out workspace/exports/tutor-4b-r4 --quants q6_k q4_k_m
   ```
   Rough sizes for Qwen3.5-4B: Q4_K_M about 2.7 GB, Q6_K about 3.6 GB. "Q6_K_H" is a community recipe, not a standard type: use Q6_K.
2. **The 2B is a different base model**, so it is a separate training run on the SAME data, then the same export:
   ```
   python training/train_sft.py --model unsloth/Qwen3.5-2B --data workspace/build/r4 --out workspace/runs/r4-2b
   python training/export_gguf.py --adapter workspace/runs/r4-2b/adapter --out workspace/exports/tutor-2b-r4 --quants q4_k_m
   ```
   It needs about 5 GB of GPU memory. Expect lower scores than the 4B: make thinking OFF by default for it and keep replies short. One community test measured about 1.3 GB of RAM for a 2B at Q4 and about 2.7 GB for a 4B at Q4; on a 4 GB phone, Android and your app also need memory, so the 4B Q4 is a stretch there.
3. **Test every file on your exam.** Download llama.cpp (github.com/ggml-org/llama.cpp, releases). Serve a file and run the exam against it:
   ```
   llama-server -m tutor-4b-r4-Q6_K.gguf --jinja -c 8192 --port 8080
   python eval/evaluate.py --name r4-q6 --backend openai --base-url http://localhost:8080/v1 --model local --compare r4
   ```
   (`--jinja` makes the server use the model's own chat template, which tool calling needs; if tool calls do not appear, check llama.cpp's current function-calling notes.) Do the same for Q4_K_M and the 2B. A Q4_K_M that loses under 2 points against Q6_K can be the default; a larger drop means ship Q6_K to phones that can hold it.
4. **Test on a real phone.** Copy the file to a phone, open it in a GGUF app (PocketPal AI, or your own app), ask 10 questions with thinking off, and note tokens per second and whether the app is killed for memory. Cheap phones can be very slow: this test decides your minimum phone.
5. **Name and keep what you ship:** `sa-tutor-<size>-<round>-<quant>.gguf`, together with `exports.json`, the run's `run.json` (it holds the training-data hash), `eval_runs/<name>/summary.json`, and the model card (`MODEL_CARD.md`, which you fill in). Store them on Drive. A private Hugging Face repo is a good backup; do not make it public until the checklist below is done.

**Release checklist:** the base model's licence text copied with the files; every data source's attribution line in the model card and the app credits; safety exam items at 95% or more; the weak slices written down as "known limits"; the app says it does not replace a teacher; no learner personal data anywhere.

**Why test each file:** quantization is a trade of quality for size, and it does not hit all skills equally (Afrikaans and long reasoning usually suffer first). Your exam tells you the truth.

---

## Phase 11: Vision (after the text tutor passes its exam)

**Goal:** the tutor reads a photo or a page of a problem, says what it read, waits for a yes, then teaches. Start with **printed** questions; handwriting is a later, harder step.

**Do**
1. **Pictures and the confirm step.** From verified faithful maths records, make photo-problem records. Each one starts with a picture of the question, the tutor replies "I read this as ... Is that right?", the learner confirms, and the already-verified lesson continues. A share use a blurred picture where the correct reply is "please send a clearer photo" (this teaches it not to guess):
   ```
   python pipeline/make_vision_records.py records --records workspace/verified/train_r3.jsonl --out workspace/verified/vision_r3.jsonl --n 300
   python tutor_data.py validate workspace/verified/vision_r3.jsonl --images-root workspace/images
   ```
   The pictures are drawn from the question text so they are perfectly labelled. They are a start. Add **real rendered exam pages** (`python pipeline/render_pages.py --pdf ... --out workspace/images/<name>`) from papers that are NOT in your exam, and later real photos of handwriting. Handwriting photos need written consent from a parent or the school, no names, no faces.
2. **Merge them into the training file** with `merge.py` like any round (they are just more records), build, and make the vision file:
   ```
   python training/vision_prepare.py --data workspace/build/r5/train.jsonl --images-root workspace/images --out workspace/build/r5/vision_train.jsonl
   ```
3. **Train.** Vision fine-tuning goes through Unsloth's official vision notebook for your model: replace its dataset cell with `vision_train.jsonl` (the file's docstring shows the three lines that load the images). Start with the **vision encoder frozen** and only the language side trained; a modern encoder already reads printed text well. Unfreeze it only if reading is still poor after you add enough real examples. Use batch size 1 (pictures use a lot of memory). Keep your text exam in the loop: vision training must not hurt the text skills.
4. **Exam for vision.** Make items and run them against a server that has the vision file loaded:
   ```
   python pipeline/make_vision_records.py exam --source dbe-maths-g12-p1-2024-nov --max 20
   llama-server -m tutor-4b-r5-Q6_K.gguf --mmproj mmproj-tutor-4b-r5.gguf --jinja -c 8192 --port 8080
   python eval/run_eval.py --name r5-vision --items workspace/eval/eval_items_vision.jsonl --backend openai --base-url http://localhost:8080/v1 --model local
   python eval/score_eval.py --name r5-vision
   ```
   The checks: the numbers in the picture are copied correctly (transcription), it asks a question, it does not solve the problem before you confirm. Also test blurred pictures and a real phone photo yourself.
5. **Documents.** For PDFs, extract the text in the app (for example pdf.js) and give the model text, not page images: cheaper, faster and more accurate. For scanned pages, run OCR in the app before the model. Keep images for photos of single questions.

**Memory warning:** vision adds a separate file (the "mmproj") and picture tokens, so it costs RAM on a phone. The 2B for 4 GB phones should stay text-only.

**Why the confirm step:** photos and handwriting get misread, and a tutor that solves the wrong problem teaches wrong maths with great confidence. Asking "I read this as ..." is cheap insurance.

---

## Phase 12: Automate everything you can

**What is already one command**
- A whole data round: `python pipeline/run_round.py ...` (plan, generate, verify, merge, report, build).
- A whole evaluation: `python eval/evaluate.py ...` (answer, mark, compare, report, analyse).
- The Colab notebook runs train, evaluate and export in order.

**Habits that make it safe to automate**
1. **Keep a log.** `workspace/NOTES.md`: date, what you changed, the score, the next step. In six weeks you will not remember.
2. **Version control for the code and settings only.** `git init` in the kit folder; the `.gitignore` already keeps `.env`, data and models out. Commit after each change to `tutor_spec.md`, the plan config or a script, with a message like "stronger hint_only rule".
3. **One change, one run.** Change one thing, rebuild, train, run the exam, write down the result.
4. **Backups:** `workspace/` on Drive, plus a copy of `raw/` and `eval/` somewhere else. The exam is the most precious file you have.
5. **Never auto-train on automatic output without reading a sample.** Automation saves typing; it does not replace judgement.

**After you launch:** real learner conversations are the best future training data, but they contain children's personal information. South Africa's POPIA law treats children's data as special; get legal advice and written consent before logging anything, anonymise before it touches any dataset, and keep it out of the exam.

---

## Pros and cons of the choices you will face

| Choice | Pros | Cons | My pick |
|---|---|---|---|
| Teacher = DeepSeek (open weights) | cheap, strong, licence allows training on outputs (read it) | its Afrikaans and CAPS knowledge can be wrong: verify and review | Yes |
| Teacher = a closed model (Claude, GPT, Gemini) | very strong | their terms restrict training your own model on outputs | No |
| Synthetic data (teacher-written) | unlimited, fully labelled, checkable | can repeat the teacher's mistakes and style | Yes, with verification and human review |
| Faithful vs original questions | faithful = real exam wording; original = no copying, independently checked | faithful depends on clean extraction | 40/60 mix |
| Thinking on | much better multi-step maths | slow on phones, uses memory, can ramble | On for maths/science on PC and cloud, off by default on phones |
| 16-bit LoRA vs 4-bit QLoRA (Qwen3.5) | 16-bit keeps quality; Unsloth advises it | needs about 10 GB for the 4B | 16-bit |
| One bilingual model vs one per language | one model to ship, handles code-switching and FAL lessons | per-language quality can slip if capacity runs out | One model; per-language adapters only if the exam shows interference |
| Q6_K vs Q4_K_M | Q6 closer to the original; Q4 smaller and faster | Q4 loses a little, mostly in long reasoning and Afrikaans | Ship both; choose by your exam and phone tests |
| DPO after SFT | fixes habits SFT leaves | too strong a dose hurts general ability | Gentle, one epoch, re-run the exam |
| Hosting your own cloud model | control, your fine-tune | idle GPUs cost money (an always-on L4 is about $500 a month) | Start with a per-token API or scale-to-zero serverless; offline on-device costs you nothing to serve |

---

## The $70, as a budget (all estimates)

| Item | Estimate |
|---|---|
| Extracting questions from papers | $1-3 |
| Teacher-written training data, about 1,500-6,000 records over the rounds | $6-20 |
| Judge pass | $2-6 |
| Teacher ceiling run + exam runs + analyses | $1-3 |
| Training: free Colab T4 for pilots; paid L4 time (about $0.71 per hour on Google Cloud) for the long runs, 10-15 runs | $10-25 |
| Left for a small online demo | the rest |

Stay inside it by: always piloting with 10 records and 20 questions; keeping `MAX_SPEND_USD` low; using the free Colab GPU first; auditioning instead of training several bases; and training the winner only. Hosting a GPU all month is not affordable from $70; on-device models cost nothing to run for users.

---

## Things you may have forgotten (a checklist)

- **Credits file.** Every CC BY and Open Government Licence source needs its credit line in the model card and app. Keep `sources.csv` up to date: it is your credits file.
- **The app must match training exactly.** The system prompt text (`render_system` in `tutor_data.py`), the tool schemas, the tool result formats, the board rules (`board.py`) and the search result format (`retrieval.format_results`) are a contract. Port them to TypeScript carefully and test them against the Python versions. Version them (`RENDER_VERSION`).
- **Helplines live in the app, not in the model.** For a learner who is distressed or being hurt, the model should be kind and point to a trusted adult; the app shows current helpline numbers (numbers change and models make them up).
- **Prompt injection.** A photo or a pasted text can say "ignore your instructions". Tools must have the least power possible (the board only draws; the calculator only calculates), and your exam should include a few such attacks.
- **Hallucinated CAPS facts.** Keep the "unsure curriculum" exam items and let `search_curriculum` supply content.
- **Updating without retraining.** Curriculum changes go into the search index, not the weights.
- **Latency and context.** Keep the system prompt and tool schemas short: they are sent every turn and cost memory and time on a phone.
- **Real learners.** Before launch, let a teacher and 5-10 learners (with consent) try it and tell you what confuses them. Their feedback beats any metric.
- **Fairness across languages.** Report scores per language; do not average away a weak Afrikaans slice.

---

## When something breaks

| Problem | Try |
|---|---|
| `python pipeline/...` says module not found | Run from the kit folder; `pip install -r requirements.txt` |
| API errors or timeouts | Wait; the client retries with backoff. 401/403: check the key and balance in `.env` |
| "MAX_SPEND_USD reached" | Raise the cap deliberately, or stop. `python llm.py spend` |
| Teacher output is not JSON | Normal now and then; the script retries with feedback. If constant, shorten the item or lower the temperature |
| `verify.py` rejects almost everything | Read `rejected.jsonl` reasons; usually memo extraction (phase 2) or the prompt (phase 5) |
| `train_sft.py` says TEMPLATE PROBLEM | Do not train. Use the model's official tokenizer/template; ask for help with the printed first_error |
| Out of memory in Colab | Lower `--batch`, raise `--grad-accum`, lower `--max-len`; use a smaller model |
| Loss does not fall in the memorise test | Check the dry-run print: masking marker, thinking format, `trainable_share` |
| Scores fall after adding a subject | You trained on the new data only or too many epochs: rebuild from ALL data, from the base |
| The model answers in English to Afrikaans | More Afrikaans data and DPO with wrong-language rejects (phase 9) |
| llama-server shows no tool calls | Use `--jinja`; check the llama.cpp notes on function calling for your model |

---

## Cheat sheet: the commands in order

```
# PC
python pipeline/init_workspace.py
python pipeline/ingest.py
python pipeline/extract_items.py --source <paper> [--dry-run | --max-questions 2]
python retrieval.py build
python eval/make_eval_from_items.py --source <held-out paper>
python eval/run_eval.py --name teacher --backend openai --base-url https://api.deepseek.com --api-key-env TEACHER_API_KEY --model deepseek-chat --think-style none
python eval/score_eval.py --name teacher --judge
python pipeline/plan.py --round r1 --target 30
python pipeline/generate.py --round r1 --dry-run
python pipeline/generate.py --round r1 --limit 10 --workers 1
python pipeline/verify.py --round r1 [--judge]
python pipeline/review_sample.py export --round r1 --n 40      # read, then:
python pipeline/review_sample.py apply --round r1
python pipeline/merge.py --rounds r1 --out workspace/verified/train_r1.jsonl
python tutor_data.py report workspace/verified/train_r1.jsonl
python tutor_data.py build workspace/verified/train_r1.jsonl --out workspace/build/r1 --val 0.1 --test 0.05
# Colab (colab/sa_tutor_colab.ipynb)
python training/train_sft.py --model <base> --data workspace/build/r1 --dry-run
python training/train_sft.py --model <base> --data workspace/build/r1 --out workspace/runs/overfit --limit 20 --epochs 15
python training/train_sft.py --model <base> --data workspace/build/r1 --out workspace/runs/r1
python eval/evaluate.py --name r1 --backend hf --model <base> --adapter workspace/runs/r1/adapter --compare base-qwen35-4b --ceiling teacher --analyze
python training/make_dpo_pairs.py prompts|pairs ...            # phase 9
python training/export_gguf.py --adapter workspace/runs/r4/adapter --out workspace/exports/tutor-4b-r4 --quants q6_k q4_k_m
python pipeline/make_vision_records.py records|exam ...        # phase 11
```
