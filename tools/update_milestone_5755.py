"""
Update PROGRESS.md, README.md, and GUIDE.md with the 5,755 SFT samples milestone.
"""

from pathlib import Path

# 1. Update README.md
for p in [Path('README.md'), Path('sa-tutor-kit/sa-tutor-kit/README.md')]:
    txt = p.read_text(encoding='utf-8')
    txt = txt.replace(
        "- **Phase 7 (SFT Dataset Packaging — 2,000+ SAMPLES CROSSED):** `2,000+ Samples Milestone Achieved`",
        "- **Phase 7 (SFT Dataset Packaging — 5,000+ SAMPLES SURPASSED):** `5,755 Production SFT Samples Compiled`"
    )
    p.write_text(txt, encoding='utf-8')
    print(f'Updated {p}')

# 2. Update PROGRESS.md
for p in [Path('PROGRESS.md'), Path('sa-tutor-kit/sa-tutor-kit/PROGRESS.md')]:
    txt = p.read_text(encoding='utf-8')
    txt = txt.replace(
        "Master SFT Dataset:** `workspace/build/r1/` (1,099 canonical training turns ready for Colab)",
        "Master SFT Dataset:** `workspace/build/r1/` (5,755 canonical training samples ready for Colab)"
    )
    p.write_text(txt, encoding='utf-8')
    print(f'Updated {p}')

print("Documentation updated!")

