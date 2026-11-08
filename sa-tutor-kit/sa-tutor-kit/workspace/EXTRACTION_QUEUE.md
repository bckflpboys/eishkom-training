# Eishkom AI — Extraction Queue State

> **Generated:** 2026-11-05 07:40 (+02:00) · git `2f2af57`
> **Authority:** this file is the single source of truth for extraction pipeline state. Written by the EXTRACTION QUEUE SUPERVISOR. The orchestrator launches one agent per lane from the `NEXT ASSIGNMENT` sections below.
> **Basis:** `python workspace/tools/scan_queue.py` output, then independently re-derived from `workspace/sources/sources.csv` + a full census of every `*.jsonl` under `workspace/items/` (107 files audited individually — not a sample).
> **No files in `workspace/items/` were modified. `sync_tracker.py` was not run.**

---

## 1. Scoreboard

| Lane | Verified (`DONE_OK`) | Repair needed (`DONE_BAD`) | Pending (`TODO`) | Blocked | No text | Locked (2024 EVAL) |
|---|---:|---:|---:|---:|---:|---:|
| **mathematics** | **12** | **1** | **69** | 0 | 0 | 8 |
| **physical_sciences** | **11** | **0** | **71** | 0 | 0 | 8 |
| **english** | **16** | **0** | **36** | 0 | 0 | 8 |
| **afrikaans** | **14** | **0** | **38** | 0 | 0 | 8 |
| **TOTAL** | **53** | **1** | **214** | 0 | 0 | 32 |

Actionable work = 214 TODO + 1 repair = **215**.

**Scanner agreement:** my recomputation matches `scan_queue.py` exactly on every bucket, in all 4 lanes. No disagreement to report.

Corpus totals on disk (double-counted mirrors excluded — 53 papers): **2704 items / 5700 marks**, all `marks` sums equal to the printed paper total.

### Verification performed (all 53 DONE_OK papers, 100% census)

| Check | Result |
|---|---|
| Every line parses as JSON (no `json.JSONDecodeError`) | 0 failures / 107 files |
| `sum(marks)` == printed total (150 maths/physics, 70 HL, 80 FAL) | 53/53 exact; only exception is the 1 known `DONE_BAD` |
| Odd-count `$` in `question`/`memo`/`passage`/`final_answer` (KaTeX parity) | 0 lines, raw and escape-aware |
| `needs_review == true` flags | 0 |
| Dual mirror `items/<subject>/<id>.jsonl` **and** `items/<id>.jsonl` | 53/53 present, byte-identical (SHA-256) |
| `item_id` prefix matches its `source_id` | 2704/2704 |

Spot-check depth required was 2 files per lane; full census was run instead, so the spot-check requirement is satisfied with margin.

### 2024 quarantine — **PASS (no violation)**

- 33 `past_paper` rows carry `year == 2024` in `sources.csv`.
- `workspace/items/**/*2024*` → **0 matches**.
- Per-id lookup of all 33 2024 `source_id`s (root + subject folders, prefix match) → **0 matches**.

No 2024 paper has an items file anywhere under `workspace/items/`. Nothing to escalate.

---

## 2. NEXT ASSIGNMENT

Priority = newest exam session first (2025 Nov → 2025 May → 2023 Nov …), as ordered by `scan_queue.py` over `sources.csv`. All listed text files and memo text files exist and are non-empty.

### 2.1 mathematics — next 3

| # | `source_id` | `pair_with` (memo) | Expected | Question text | memo text | Note |
|---|---|---|---:|---|---|---|
| 1 | `dbe-mathematics-g12-p1-2025-nov` | `dbe-mathematics-g12-p1-2025-nov-memo` | **150** | `workspace/text/dbe-mathematics-g12-p1-2025-nov.txt` — **exists** (10,723 B) | exists (16,100 B) | English P1, Nov 2025 |
| 2 | `dbe-wiskunde-g12-v1-2025-nov` | `dbe-wiskunde-g12-v1-2025-nov-memo` | **150** | `workspace/text/dbe-wiskunde-g12-v1-2025-nov.txt` — **exists** (12,744 B) | exists (16,360 B) | Afrikaans translation of #1 (V1 = P1) |
| 3 | `dbe-mathematics-g12-p2-2025-nov` | `dbe-mathematics-g12-p2-2025-nov-memo` | **150** | `workspace/text/dbe-mathematics-g12-p2-2025-nov.txt` — **exists** (11,415 B) | exists (19,635 B) | English P2, Nov 2025 |

Next after these: `dbe-wiskunde-g12-v2-2025-nov`, `dbe-mathematics-g12-p1-2025-may`, `dbe-wiskunde-g12-v1-2025-may`.

### 2.2 physical_sciences — next 3

| # | `source_id` | `pair_with` (memo) | Expected | Question text | memo text | Note |
|---|---|---|---:|---|---|---|
| 1 | `dbe-physical_sciences-g12-p1-2025-nov` | `dbe-physical_sciences-g12-p1-2025-nov-memo` | **150** | `workspace/text/dbe-physical_sciences-g12-p1-2025-nov.txt` — **exists** (18,893 B) | exists (22,699 B) | English P1 (Physics), Nov 2025 |
| 2 | `dbe-fisiese_wetenskappe-g12-v1-2025-nov` | `dbe-fisiese_wetenskappe-g12-v1-2025-nov-memo` | **150** | `workspace/text/dbe-fisiese_wetenskappe-g12-v1-2025-nov.txt` — **exists** (19,685 B) | exists (20,759 B) | Afrikaans translation of #1 |
| 3 | `dbe-fisiese_wetenskappe-g12-v2-2025-nov` | `dbe-fisiese_wetenskappe-g12-v2-2025-nov-memo` | **150** | `workspace/text/dbe-fisiese_wetenskappe-g12-v2-2025-nov.txt` — **exists** (20,073 B) | exists (21,446 B) | Afrikaans V2 = P2, Nov 2025 |

Next after these: `dbe-physical_sciences-g12-p1-2025-may`, `dbe-fisiese_wetenskappe-g12-v1-2025-may`, `dbe-physical_sciences-g12-p2-2025-may`.

> Note: Physical Sciences P2 Nov 2025 (`dbe-physical_sciences-g12-p2-2025-nov`) is **already verified** (68 items / 150 marks). Do not redo it.

### 2.3 english — next 3

| # | `source_id` | `pair_with` (memo) | Expected | Question text | memo text | Note |
|---|---|---|---:|---|---|---|
| 1 | `dbe-english_fal-g12-p1-2025-nov` | `dbe-english_fal-g12-p1-2025-nov-memo` | **80** | `workspace/text/dbe-english_fal-g12-p1-2025-nov.txt` — **exists** (14,915 B) | exists (14,246 B) | FAL P1 |
| 2 | `dbe-english_fal-g12-p2-2025-nov` | `dbe-english_fal-g12-p2-2025-nov-memo` | **80** | `workspace/text/dbe-english_fal-g12-p2-2025-nov.txt` — **exists** (28,413 B) | exists (31,369 B) | FAL P2 (largest text in lane) |
| 3 | `dbe-english_hl-g12-p1-2025-nov` | `dbe-english_hl-g12-p1-2025-nov-memo` | **70** | `workspace/text/dbe-english_hl-g12-p1-2025-nov.txt` — **exists** (18,893 B) | exists (16,952 B) | HL P1 — 70-mark total |

Next after these: `dbe-english_hl-g12-p2-2025-nov`, `dbe-english_fal-g12-p1-2025-may`, `dbe-english_fal-g12-p2-2025-may`.

### 2.4 afrikaans — next 3

| # | `source_id` | `pair_with` (memo) | Expected | Question text | memo text | Note |
|---|---|---|---:|---|---|---|
| 1 | `dbe-afrikaans_fal-g12-p1-2025-nov` | `dbe-afrikaans_fal-g12-p1-2025-nov-memo` | **80** | `workspace/text/dbe-afrikaans_fal-g12-p1-2025-nov.txt` — **exists** (21,637 B) | exists (20,680 B) | FAL P1 |
| 2 | `dbe-afrikaans_fal-g12-p2-2025-nov` | `dbe-afrikaans_fal-g12-p2-2025-nov-memo` | **80** | `workspace/text/dbe-afrikaans_fal-g12-p2-2025-nov.txt` — **exists** (23,486 B) | exists (22,811 B) | FAL P2 |
| 3 | `dbe-afrikaans_hl-g12-p1-2025-nov` | `dbe-afrikaans_hl-g12-p1-2025-nov-memo` | **70** | `workspace/text/dbe-afrikaans_hl-g12-p1-2025-nov.txt` — **exists** (16,939 B) | exists (19,429 B) | HL P1 — 70-mark total |

Next after these: `dbe-afrikaans_hl-g12-p2-2025-nov`, `dbe-afrikaans_fal-g12-p1-2025-may`, `dbe-afrikaans_fal-g12-p2-2025-may`.

---

## 3. REPAIR QUEUE

| Paper | Lane | Actual | Expected | Deficit | Where it is wrong |
|---|---|---:|---:|---:|---|
| `dbe-mathematics-g12-p1-2021-may` | mathematics | **41** | **150** | **−109** | 11 items only; extraction stops after Q2.2 (`…-1.1.1` → `…-2.2`). Q1 = 24 marks, Q2 partial = 17. **Root mirror only** — `workspace/items/mathematics/dbe-mathematics-g12-p1-2021-may.jsonl` is absent, so the dual-mirror rule is also broken for this paper. |

Repair inputs are present: `workspace/text/dbe-mathematics-g12-p1-2021-may.txt` (9,103 B) and `…-memo.txt` (12,677 B).
Repair must (a) re-extract the full 150-mark paper from Q2.3 onwards, and (b) write **both** mirrors.

Only 1 paper is in the repair queue. No other `DONE_BAD` paper exists in any lane.

---

## 4. Anomalies & advisories (non-blocking)

1. **Scanner blind spot — `dbe-maths-` prefix.** `scan_queue.py` maps lanes by prefix `dbe-mathematics-` / `dbe-wiskunde-`, but one 2024 row uses `dbe-maths-g12-p1-2024-nov`. It therefore matches no lane and is silently dropped from all 4 `LOCKED` counts (33 2024 rows exist; 32 are attributed: 8+8+8+8). Not a quarantine violation — it has no items file — but a *non*-2024 paper with a `dbe-maths-` id would vanish from the queue entirely. Recommend adding `dbe-maths-` to the maths lane prefixes before the next corpus import.
2. **`EXTRACTION_TRACKER.md` headline numbers are stale.** Tracker header claims 2667 items / 5661 marks across 53 papers; disk shows **2704 items / 5700 marks** across the same 53 papers. Paper count agrees; item and mark totals are behind by 37 / 39. `sync_tracker.py` (orchestrator-owned) will reconcile.
3. **Bilingual memo dedupe.** 36 `*-memo.txt` files under `workspace/text/` are byte-identical pairs (Afrikaans `fisiese_wetenskappe` memo == English `physical_sciences` memo). This is expected for combined DBE bilingual memos, not a copy error.
4. **Empty `final_answer` in `dbe-english_hl-g12-p1-2023-nov`** — 11 of 35 items. All 11 carry a non-empty `memo` rubric answer, so this is by design for discursive language items, not a data loss. Marks total is correct (70/70).
5. Zero `U+FFFD` replacement characters and zero `needs_review` flags across all 2704 items.

---

## 5. Handoff

- 4 lanes are clean and ready to launch: each lane's first paper has question text, memo text, correct expected total, and no pre-existing items file.
- Mathematics lane should launch with a repair job first (`dbe-mathematics-g12-p1-2021-may`) or run repair in parallel with the new extraction — the orchestrator decides; both are covered above.
- After the lanes finish, the orchestrator runs `sync_tracker.py` (deliberately not run here to avoid a write race with the 4 lane agents).
