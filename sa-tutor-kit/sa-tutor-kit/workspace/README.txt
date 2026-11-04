Folders in this workspace (see GUIDE.md):

  config     settings you edit: plan_config.json, misconceptions.jsonl
  sources    sources.csv - one row per file you download (licence is mandatory)
  raw        the files exactly as downloaded (PDFs, HTML). Never edit these.
  text       text extracted from raw/ (one .txt per source, with page markers)
  items      questions + memos cut out of the text (one .jsonl per source)
  index      the search index over text/ (used by the search_curriculum tool)
  plans      generation plans: which control settings to write for which item
  gen        teacher output, per round: raw replies, candidate records, failures
  verified   records that passed every check, per round (this is your training data)
  review     samples exported for a human (you / a teacher / an Afrikaans speaker) to read
  build      final train/val/test files, per round
  eval       your exam: eval_items.jsonl (never train on these)
  eval_runs  model answers and scores, one folder per model/run
  runs       training runs: LoRA adapters, logs, run.json (put this on Google Drive in Colab)
  reports    charts and notes
  logs       llm_usage.jsonl (every API call and its cost)
  images     pictures for the vision phase
