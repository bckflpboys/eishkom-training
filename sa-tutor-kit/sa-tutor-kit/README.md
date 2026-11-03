# SA Tutor Kit

A working kit for building a CAPS-aligned maths tutor by fine-tuning **Qwen3.5-4B** with LoRA.

This README is the map. [`GUIDE.md`](GUIDE.md) is the manual: every phase has a goal, exact commands, a check, and a fix. Read the guide before changing code.

## What you are building

A small tutor model that:

- teaches CAPS maths for Grades 7–12;
- asks one question at a time and hints before giving the answer;
- answers in the learner's language (English first, Afrikaans later);
- uses tools such as a calculator and a drawing board;
- runs offline as a GGUF file on a PC or phone.

The training method is **LoRA SFT on verified teacher-written conversations**, followed by DPO only if habits such as answer-leaking remain. The curriculum facts stay in a searchable library; the model learns *how* to teach.

## The one-page workflow

```
PC (no GPU)                         Google Drive              Colab (T4/L4)
-----------                         ------------              ------------
sources -> text -> items            kit/ + workspace/  --->   load Qwen3.5-4B
        -> exam (first)                                        train LoRA
        -> teacher conversations                               evaluate
        -> verify -> review                                    export GGUF
        -> build/r1/train.jsonl  --------------------------->  adapter + GGUF
                                                                    |
                                                                    v
                                                              PC / phone
```

Two rules make the rest make sense:

1. **The exam comes first.** Build `workspace/eval/eval_items.jsonl` before generating training data, and never train on it.
2. **The teacher writes, code checks, a human reads.** A large open-weight teacher writes conversations; the validator, SymPy, language checks and a judge filter them; you read a sample before training.

## Where everything lives

All of your data is in `workspace/`. The kit code never overwrites an earlier step.

| Folder | What it holds |
|---|---|
| `workspace/raw/` | Source PDFs exactly as downloaded |
| `workspace/sources/sources.csv` | One row per source, including its licence |
| `workspace/text/` | Text extracted from the PDFs |
| `workspace/items/` | Questions and memo answers cut from the text |
| `workspace/eval/` | The held-out exam. Never train on this |
| `workspace/plans/` | Which control settings to use for each item |
| `workspace/gen/` | Raw teacher output and candidate records |
| `workspace/verified/` | Records that passed every check |
| `workspace/build/r1/` | Final `train.jsonl`, `val.jsonl`, `test.jsonl` |
| `workspace/runs/r1/` | LoRA adapter, logs, `run.json` |
| `workspace/exports/` | GGUF files for llama.cpp, LM Studio, PocketPal |
| `workspace/reports/` | Evaluation charts and decisions |

The other important files:

| File | What it is |
|---|---|
| `tutor_spec.md` | The teaching spec. The teacher reads it; the judge uses its rubric |
| `tutor_data.py` | Schema, validator, report and train/val/test builder |
| `SOURCES.md` | Where to get CAPS material and what each licence allows |
| `examples/examples.jsonl` | 14 records showing every feature. These are examples, **not** a training set |
| `colab/sa_tutor_colab.ipynb` | The Colab runner: audition, train, evaluate, export |
| `training/train_sft.py` | The LoRA SFT script |
| `training/export_gguf.py` | Export Q4_K_M / Q6_K files |
| `eval/` | The exam runner, scorer and reports |

## Do I download the training data to my PC?

The **source material** goes on your PC, and the pipeline organises it there:

1. Download DBE papers, memos and Siyavula books into `workspace/raw/`.
2. Fill in `workspace/sources/sources.csv` (licence column mandatory).
3. Run `python pipeline/ingest.py` to extract text.
4. Run the item extraction, then generate, verify, review and build.

The **base model** is not downloaded to your PC. Colab pulls `unsloth/Qwen3.5-4B` from Hugging Face by name. A 4B model is about 9 GB. Downloading it to your PC and uploading it again is wasted time.

The **finished model** is downloaded to your PC only after training, as a GGUF file exported in Colab and saved to Google Drive.

## Do I upload it to Vertex AI?

No. Vertex AI is for running models on Google's servers, not for this training workflow. The kit trains in Colab, which gives you a free T4 GPU.

Use Vertex only if you later want to *serve* a model behind an API and are willing to build a custom container and pay for the GPU time. It is not part of the build path in `GUIDE.md`.

The path is:

```
PC: organise and verify data
Google Drive: keep the kit + workspace
Colab: mount Drive, train, evaluate, export
```

## Quick start: PC

Run these from the kit folder.

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS / Linux
pip install -r requirements.txt

python pipeline/init_workspace.py
python tutor_data.py validate examples/examples.jsonl --images-root examples
```

The validator should print:

```
Checked 14 records: 0 errors, 0 warnings.
```

Then:

1. Open `.env` and set `TEACHER_API_KEY`, `TEACHER_MODEL` and a low `MAX_SPEND_USD`.
2. Put 3–5 recent DBE maths papers **with memos** in `workspace/raw/`.
3. Fill in `workspace/sources/sources.csv`.
4. Run `python pipeline/ingest.py`.
5. Build the exam before generating any training data (phase 3 of the guide).

The 14 example records are only a schema demonstration. Do not train on them.

## Quick start: Colab

1. Upload the whole `sa-tutor-kit` folder, including `workspace/`, to Google Drive.
2. Open `colab/sa_tutor_colab.ipynb` in Colab.
3. Choose **Runtime → Change runtime type → T4 GPU**.
4. Run cells 1–4: GPU check, mount Drive, install, Hugging Face login.
5. Run cell 5 to audition `Qwen/Qwen3.5-4B` on the 42-item starter exam.
6. After `workspace/build/r1/` exists, run cell 6a (free dry run), 6b (overfit 20 samples), 6c (real training).
7. Run cell 7 to evaluate. Read `workspace/reports/r1/decision.md` and `failures.md`.
8. Run cell 9 to export GGUF files. Download only the finished files to your PC or phone.

## What "ready to train" looks like

- `workspace/build/r1/train.jsonl` exists and the report is balanced by grade and strategy.
- The dry run prints `too_long: 0` and `mismatch: 0`.
- The trainable share is roughly 10–25%.
- The 20-sample overfit test drives loss close to zero.
- A human has read at least 40 generated records and the bad rate is under 10%.

## What "good enough to ship" looks like

- Overall exam pass rate at least 70%, or at least 85% of the teacher's score.
- Policy checks at least 90%; language checks at least 95%; tool checks at least 90%.
- No slice dropped by more than 3 points since the previous run.
- Q4_K_M loses less than 2 points against Q6_K; otherwise ship Q6_K to devices that can hold it.

## Licensing and safety

- Use an open-weight teacher whose licence allows training on its outputs. The guide's default is DeepSeek. Do not build the dataset from Claude, ChatGPT or Gemini outputs.
- Keep the licence and attribution for every source and for the base model.
- Do not log learner conversations without consent. Children's data is protected under POPIA; anonymise before it touches a dataset.
- The app should say it does not replace a teacher.

## Current status

- `workspace/` has been created.
- The 14 example records validate with 0 errors and 0 warnings.
- The 42-item starter exam is in `workspace/eval/eval_items.jsonl`.
- No sources, generated records, build split or trained adapter exist yet.

## The conversation that produced this kit

The verbatim archive of the Claude conversation is here:

- [`claude-transcript.html`](../../../chats/claude-transcript.html) — standalone, searchable, with thinking and artifacts.
- [`claude-transcript.md`](../../../chats/claude-transcript.md) — plain-text mirror.

The archive covers 13 of 84 messages (1–10 and 82–84); messages 11–81 were not present in the saved page. It is a record, not a replacement for this guide.
