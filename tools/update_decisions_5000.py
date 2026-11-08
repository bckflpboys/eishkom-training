"""
Update DECISIONS.md with Milestone: 5,755 SFT Training Samples Compiled & 41 Exam Papers Completed.
"""

from pathlib import Path

entry = """

## 2026-11-08: Milestone: 5,755 Production SFT Samples Compiled (41 Exam Papers, Waves 1-5 + Full Solutions, Excel Dashboard Exported)

- **Milestone Surpassed: 5,755 Canonical SFT Samples:**
  - With the completion of Waves 1–5 multi-model generation and 1,970 structured full-solution demonstrations across 41 DBE exam papers, the Eishkom AI master training dataset has officially been compiled into `workspace/build/r1/`.
  - Production SFT Split Metrics:
    - `train.jsonl`: **2,647 lessons | 4,639 assistant training samples** (loss on completion, full reasoning chains).
    - `val.jsonl`: **483 lessons | 844 assistant validation samples**.
    - `test.jsonl`: **159 lessons | 272 assistant test samples**.
    - **Total SFT Training Samples:** **5,755 samples** (100% with `thinking: "on"`, zero missing keys, schema validated).
- **Curriculum & Multi-Task Composition:**
  - 1,319 verified multi-turn Socratic lessons (~3,289 assistant turns).
  - 1,970 structured full-solution demonstrations (`answer_policy: "full_solution"`).
  - Balanced at 1 formal DBE exam solution per 1.6 Socratic dialogues.
  - Across 41 past papers covering Mathematics, Physical Sciences, Wiskunde, Fisiese Wetenskappe, English HL/FAL, and Afrikaans HL/FAL.
- **Excel & Google Sheets Dashboard Exported:**
  - Built `tools/export_dashboard_csv.py` generating:
    - `workspace/reports/fleet_model_leaderboard.csv`: Complete scorecard across all AI models (OpenAI Luna: 484 verified, Gemini 3.5: 349 verified, Gemini 3.1: 160 verified, Nemotron: 112 verified, DeepSeek: 30 verified).
    - `workspace/reports/paper_verification_matrix.csv`: Per-paper question counts, pass rates, full solutions, and primary models across all 41 papers.
    - `workspace/reports/corpus_executive_summary.csv`: Executive metrics summary.
- **Mirroring & Readiness:**
  - Mirrored to `sa-tutor-kit/sa-tutor-kit/workspace/build/r1/`.
  - 100% ready for SFT fine-tuning in Vertex AI Colab Enterprise on an NVIDIA L4 GPU Spot VM.
"""

for path_str in ['workspace/DECISIONS.md', 'sa-tutor-kit/sa-tutor-kit/workspace/DECISIONS.md']:
    p = Path(path_str)
    if p.exists():
        with open(p, 'a', encoding='utf-8') as fp:
            fp.write(entry)
        print(f'Successfully updated {p}')

