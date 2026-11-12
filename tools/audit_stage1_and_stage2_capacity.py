import json
from pathlib import Path
from collections import defaultdict

# 1. Sources check
sources_file = Path('workspace/sources/sources.csv')
total_sources = 0
papers_in_sources = 0
held_out_papers = 0
if sources_file.exists():
    for line in open(sources_file, encoding='utf-8'):
        parts = line.strip().split(',')
        if len(parts) >= 6:
            total_sources += 1
            if parts[5] == 'paper':
                papers_in_sources += 1
                if 'held out' in line or '2024' in parts[3]:
                    held_out_papers += 1
print(f"Total entries in sources.csv: {total_sources}")
print(f"Total question papers in sources.csv: {papers_in_sources} (Held-out 2024 benchmarks: {held_out_papers})")

# 2. Text files in workspace/text
text_files = list(Path('workspace/text').glob('*.txt'))
qp_text_files = [f for f in text_files if not f.stem.endswith('-memo')]
memo_text_files = [f for f in text_files if f.stem.endswith('-memo')]
print(f"Total text files in workspace/text: {len(text_files)} (QP texts: {len(qp_text_files)}, Memo texts: {len(memo_text_files)})")

# 3. Items in workspace/items
subjects = ['mathematics', 'wiskunde', 'physical_sciences', 'fisiese_wetenskappe', 'english_hl', 'english_fal', 'afrikaans_hl', 'afrikaans_fal']
items_by_subject = defaultdict(lambda: {'papers': 0, 'items': 0, 'marks': 0})
all_item_ids = set()
all_paper_ids = set()
items_per_paper = []

for subj in subjects:
    s_dir = Path('workspace/items') / subj
    if s_dir.exists():
        for f in s_dir.glob('*.jsonl'):
            paper_id = f.stem
            all_paper_ids.add(paper_id)
            p_items = 0
            p_marks = 0
            for line in open(f, encoding='utf-8'):
                if line.strip():
                    it = json.loads(line)
                    all_item_ids.add(it.get('item_id'))
                    p_items += 1
                    try:
                        p_marks += int(it.get('marks') or 0)
                    except:
                        pass
            items_by_subject[subj]['papers'] += 1
            items_by_subject[subj]['items'] += p_items
            items_by_subject[subj]['marks'] += p_marks
            items_per_paper.append(p_items)

print(f"\nTotal unique papers with extracted items in workspace/items: {len(all_paper_ids)}")
print(f"Total unique atomic items in workspace/items: {len(all_item_ids)}")
for subj in subjects:
    st = items_by_subject[subj]
    print(f"  {subj:22s}: {st['papers']:3d} papers | {st['items']:5d} items | {st['marks']:6d} marks")

if items_per_paper:
    avg_items = sum(items_per_paper) / len(items_per_paper)
    print(f"\nAverage items per question paper: {avg_items:.1f} (min: {min(items_per_paper)}, max: {max(items_per_paper)})")

# 4. Stage 1 usage check
master_file = Path('workspace/verified/train_master_combined.jsonl')
used_item_ids = set()
used_paper_ids = set()
record_count = 0
socratic_count = 0
fullsol_count = 0

if master_file.exists():
    for line in open(master_file, encoding='utf-8'):
        if line.strip():
            record_count += 1
            rec = json.loads(line)
            strat = rec.get('control', {}).get('strategy')
            if strat == 'full_solution':
                fullsol_count += 1
            else:
                socratic_count += 1
            m = rec.get('meta', {})
            iid = m.get('item_id')
            if iid:
                used_item_ids.add(iid)
                parts = iid.split('-')
                if len(parts) >= 6:
                    pid = '-'.join(parts[:6])
                    used_paper_ids.add(pid)

print(f"\nStage 1 Dataset Composition (train_master_combined.jsonl):")
print(f"  Total records in master combined: {record_count}")
print(f"  - Full Solution demonstrations: {fullsol_count}")
print(f"  - Socratic hint dialogues: {socratic_count}")
print(f"  Unique atomic items used: {len(used_item_ids)} out of {len(all_item_ids)} ({len(used_item_ids)/len(all_item_ids)*100:.1f}%)")
print(f"  Unique exam papers touched: {len(used_paper_ids)} out of {len(all_paper_ids)} ({len(used_paper_ids)/len(all_paper_ids)*100:.1f}%)")

leftover_items = len(all_item_ids) - len(used_item_ids)
leftover_papers = len(all_paper_ids) - len(used_paper_ids)
print(f"\nLeftover / Untapped Capacity in Current Extracted Bank:")
print(f"  Untapped atomic items ready in bank: {leftover_items}")
print(f"  Untapped complete exam papers ready in bank: {leftover_papers}")

