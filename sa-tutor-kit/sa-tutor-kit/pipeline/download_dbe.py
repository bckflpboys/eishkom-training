#!/usr/bin/env python3
"""
download_dbe.py - automated downloader for Department of Basic Education (DBE) past exam papers and memos.

Downloads NSC Grade 12 past papers and marking memorandums (plus Grade 10/11 common papers) for:
  - Mathematics (English & Afrikaans)
  - Physical Sciences (English & Afrikaans)
  - English (Home Language & First Additional Language, P1 & P2)
  - Afrikaans (Huistaal & Eerste Addisionele Taal, P1 & P2)

Organises them into:
  workspace/raw/dbe/<language>/<subject>/<year>/<clean_name>.pdf

And logs all pairs directly into:
  workspace/sources/sources.csv

Usage:
  python pipeline/download_dbe.py --dry-run
  python pipeline/download_dbe.py --years 2024 2023 2022
  python pipeline/download_dbe.py
"""
from __future__ import annotations

import argparse
import csv
import os
import re
import ssl
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

KIT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(KIT_ROOT))

SSL_CTX = ssl.create_default_context()
SSL_CTX.check_hostname = False
SSL_CTX.verify_mode = ssl.CERT_NONE

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

# Target sessions on education.gov.za
PAGES = {
    (2025, "nov"): "https://www.education.gov.za/Curriculum/NationalSeniorCertificate(NSC)Examinations/2025NovemberExamPapers.aspx",
    (2025, "may"): "https://www.education.gov.za/LinkClick.aspx?link=5475&tabid=338&portalid=0&mid=1741",
    (2024, "nov"): "https://www.education.gov.za/2024NSCNovemberpastpapers.aspx",
    (2024, "may"): "https://www.education.gov.za/Curriculum/NationalSeniorCertificate(NSC)Examinations/2024MayJuneExamPapers.aspx",
    (2023, "nov"): "https://www.education.gov.za/Curriculum/NationalSeniorCertificate(NSC)Examinations/2023NSCNovemberpastpapers.aspx",
    (2023, "may"): "https://www.education.gov.za/Curriculum/NationalSeniorCertificate(NSC)Examinations/2023MayJuneExamPapers.aspx",
    (2022, "nov"): "https://www.education.gov.za/Curriculum/NationalSeniorCertificate(NSC)Examinations/2022NovemberExams.aspx",
    (2022, "may"): "https://www.education.gov.za/Curriculum/NationalSeniorCertificate(NSC)Examinations/2022MayJuneExamPapers.aspx",
    (2021, "nov"): "https://www.education.gov.za/Curriculum/NationalSeniorCertificate(NSC)Examinations/2021NSCExamPapers.aspx",
    (2021, "may"): "https://www.education.gov.za/Curriculum/NationalSeniorCertificate(NSC)Examinations/2021MayJuneNSCExams.aspx",
    (2020, "nov"): "https://www.education.gov.za/Curriculum/NationalSeniorCertificate(NSC)Examinations/2020NSCExamPapers.aspx",
    (2019, "nov"): "https://www.education.gov.za/LinkClick.aspx?link=2556&tabid=338&portalid=0&mid=1741",
    (2019, "may"): "https://www.education.gov.za/2019JuneNSCExamPapers.aspx",
    (2018, "nov"): "https://www.education.gov.za/LinkClick.aspx?link=2268&tabid=338&portalid=0&mid=1741",
    (2018, "may"): "https://www.education.gov.za/LinkClick.aspx?link=2182&tabid=338&portalid=0&mid=1741",
}

COMMON_PAGES = {
    "gr11": "https://www.education.gov.za/LinkClick.aspx?link=1869&tabid=338&portalid=0&mid=1741",
    "gr10": "https://www.education.gov.za/LinkClick.aspx?link=1853&tabid=338&portalid=0&mid=1741",
}


def fetch_html(url: str, retries: int = 3) -> str:
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, context=SSL_CTX, timeout=30) as resp:
                return resp.read().decode("utf-8", errors="ignore")
        except Exception as e:
            if attempt == retries - 1:
                print(f"[ERROR] Failed to fetch {url}: {e}")
                return ""
            time.sleep(2)
    return ""


def download_pdf(url: str, dest_path: Path, retries: int = 3) -> bool:
    if dest_path.exists() and dest_path.stat().st_size > 1000:
        return True  # Already downloaded
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, context=SSL_CTX, timeout=45) as resp:
                data = resp.read()
                if len(data) < 500:
                    raise ValueError(f"File too small ({len(data)} bytes)")
                dest_path.write_bytes(data)
                return True
        except Exception as e:
            if attempt == retries - 1:
                print(f"[FAIL] Download failed for {url}: {e}")
                return False
            time.sleep(2)
    return False


def parse_page_records(html: str, page_url: str, default_year: int, session: str, default_grade: str = "12"):
    """
    Parses subject sections from the DBE page and extracts structured items for:
    Mathematics, Physical Sciences, English (HL & FAL), Afrikaans (HL & FAL).
    """
    sections = re.findall(r'<h[234][^>]*>(.*?)</h[234]>(.*?)(?=<h[234]|\Z)', html, re.I | re.S)
    found_records = []

    for heading_raw, body in sections:
        heading = re.sub(r'<[^>]+>', '', heading_raw).strip()
        h_lower = heading.lower()

        # Check if heading specifies year (e.g., "Mathematics: 2018")
        yr_match = re.search(r'\b(20\d\d)\b', h_lower)
        year = int(yr_match.group(1)) if yr_match else default_year

        # Check grade
        gr_match = re.search(r'grade\s*(\d+)|gr\s*(\d+)', h_lower)
        grade = gr_match.group(1) or gr_match.group(2) if gr_match else default_grade

        # Identify subject
        if "technical mathematics" in h_lower or "mathematical literacy" in h_lower:
            continue
        elif "mathematics" in h_lower or "wiskunde" in h_lower:
            subject_cat = "mathematics"
        elif "physical sciences" in h_lower or "fisiese wetenskappe" in h_lower:
            subject_cat = "physical_sciences"
        elif "english" in h_lower:
            subject_cat = "english"
        elif "afrikaans" in h_lower:
            subject_cat = "afrikaans"
        else:
            continue

        # Extract links in this section
        links = re.findall(r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', body, re.I | re.S)
        items = []
        for href, text in links:
            t = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', text)).strip()
            if not t or t.lower() in ('download', 'click here', 'more', 'search', 'home'):
                continue
            if 'forcedownload=true' in href:
                continue
            full_href = urllib.parse.urljoin(page_url, href)
            items.append((t, full_href))

        # Group items into papers and memos
        if subject_cat in ("mathematics", "physical_sciences"):
            process_stem_items(items, subject_cat, year, session, found_records, grade)
        elif subject_cat in ("english", "afrikaans"):
            process_language_items(items, subject_cat, year, session, found_records, grade)

    return found_records


def process_stem_items(items, subject: str, year: int, session: str, records: list, grade: str = "12"):
    """Pair STEM papers: Paper 1 & 2 in English and Afrikaans with Memo 1 & 2."""
    p1_en, p1_af, p2_en, p2_af = None, None, None, None
    m1_en, m1_af, m1_both = None, None, None
    m2_en, m2_af, m2_both = None, None, None

    for title, url in items:
        tl = title.lower()
        if "answerbook" in tl or "data" in tl or "addendum" in tl:
            continue

        is_memo = ("memo" in tl or "memorandum" in tl)
        is_p1 = bool(re.search(r'\b(p1|paper\s*1|vraestel\s*1|memo\s*1|memorandum\s*1)\b', tl))
        is_p2 = bool(re.search(r'\b(p2|paper\s*2|vraestel\s*2|memo\s*2|memorandum\s*2)\b', tl))

        if is_p1:
            if is_memo:
                if ("afrikaans" in tl and "english" in tl) or ("&" in tl and "afrikaans" in tl):
                    m1_both = url
                elif "afrikaans" in tl:
                    m1_af = url
                else:
                    m1_en = url
            else:
                if "afrikaans" in tl:
                    p1_af = url
                else:
                    p1_en = url
        elif is_p2:
            if is_memo:
                if ("afrikaans" in tl and "english" in tl) or ("&" in tl and "afrikaans" in tl):
                    m2_both = url
                elif "afrikaans" in tl:
                    m2_af = url
                else:
                    m2_en = url
            else:
                if "afrikaans" in tl:
                    p2_af = url
                else:
                    p2_en = url

    af_sub_name = "wiskunde" if subject == "mathematics" else "fisiese_wetenskappe"
    en_sub_label = subject.replace('_', ' ').title()
    af_sub_label = "Wiskunde" if subject == "mathematics" else "Fisiese Wetenskappe"

    # Pair P1 English
    m1_en_url = m1_en or m1_both
    if p1_en and m1_en_url:
        records.append({
            "lang": "english", "subject": subject, "year": year, "session": session, "paper": "p1", "grade": grade,
            "paper_url": p1_en, "memo_url": m1_en_url,
            "paper_fname": f"{subject}_g{grade}_{year}_{session}_p1.pdf",
            "memo_fname": f"{subject}_g{grade}_{year}_{session}_p1_memo.pdf",
            "paper_id": f"dbe-{subject}-g{grade}-p1-{year}-{session}",
            "memo_id": f"dbe-{subject}-g{grade}-p1-{year}-{session}-memo",
            "title_p": f"{en_sub_label} P1 {session.upper()} {year} (Grade {grade})",
            "title_m": f"{en_sub_label} P1 {session.upper()} {year} Memorandum (Grade {grade})"
        })

    # Pair P1 Afrikaans
    m1_af_url = m1_af or m1_both
    if p1_af and m1_af_url:
        records.append({
            "lang": "afrikaans", "subject": af_sub_name, "year": year, "session": session, "paper": "p1", "grade": grade,
            "paper_url": p1_af, "memo_url": m1_af_url,
            "paper_fname": f"{af_sub_name}_g{grade}_{year}_{session}_v1.pdf",
            "memo_fname": f"{af_sub_name}_g{grade}_{year}_{session}_v1_memo.pdf",
            "paper_id": f"dbe-{af_sub_name}-g{grade}-v1-{year}-{session}",
            "memo_id": f"dbe-{af_sub_name}-g{grade}-v1-{year}-{session}-memo",
            "title_p": f"{af_sub_label} V1 {session.upper()} {year} (Graad {grade})",
            "title_m": f"{af_sub_label} V1 {session.upper()} {year} Memorandum (Graad {grade})"
        })

    # Pair P2 English
    m2_en_url = m2_en or m2_both
    if p2_en and m2_en_url:
        records.append({
            "lang": "english", "subject": subject, "year": year, "session": session, "paper": "p2", "grade": grade,
            "paper_url": p2_en, "memo_url": m2_en_url,
            "paper_fname": f"{subject}_g{grade}_{year}_{session}_p2.pdf",
            "memo_fname": f"{subject}_g{grade}_{year}_{session}_p2_memo.pdf",
            "paper_id": f"dbe-{subject}-g{grade}-p2-{year}-{session}",
            "memo_id": f"dbe-{subject}-g{grade}-p2-{year}-{session}-memo",
            "title_p": f"{en_sub_label} P2 {session.upper()} {year} (Grade {grade})",
            "title_m": f"{en_sub_label} P2 {session.upper()} {year} Memorandum (Grade {grade})"
        })

    # Pair P2 Afrikaans
    m2_af_url = m2_af or m2_both
    if p2_af and m2_af_url:
        records.append({
            "lang": "afrikaans", "subject": af_sub_name, "year": year, "session": session, "paper": "p2", "grade": grade,
            "paper_url": p2_af, "memo_url": m2_af_url,
            "paper_fname": f"{af_sub_name}_g{grade}_{year}_{session}_v2.pdf",
            "memo_fname": f"{af_sub_name}_g{grade}_{year}_{session}_v2_memo.pdf",
            "paper_id": f"dbe-{af_sub_name}-g{grade}-v2-{year}-{session}",
            "memo_id": f"dbe-{af_sub_name}-g{grade}-v2-{year}-{session}-memo",
            "title_p": f"{af_sub_label} V2 {session.upper()} {year} (Graad {grade})",
            "title_m": f"{af_sub_label} V2 {session.upper()} {year} Memorandum (Graad {grade})"
        })


def process_language_items(items, lang_family: str, year: int, session: str, records: list, grade: str = "12"):
    """Pair Language items: English/Afrikaans HL and FAL P1 and P2 with their memos."""
    grouped = {}
    for title, url in items:
        tl = title.lower()
        if "p3" in tl or "paper 3" in tl or "vraestel 3" in tl:
            continue  # Skip Paper 3 essays per spec
        if "sal" in tl:
            continue  # Skip Second Additional Language per spec

        stream = "fal" if "fal" in tl or "eerste addisionele" in tl or "first additional" in tl else ("hl" if "hl" in tl or "huistaal" in tl or "home" in tl else None)
        if not stream:
            continue

        is_p1 = bool(re.search(r'\b(p1|paper\s*1|vraestel\s*1|memo\s*1|memorandum\s*1)\b', tl))
        is_p2 = bool(re.search(r'\b(p2|paper\s*2|vraestel\s*2|memo\s*2|memorandum\s*2)\b', tl))
        p_num = "p1" if is_p1 else ("p2" if is_p2 else None)
        if not p_num:
            continue

        key = (stream, p_num)
        if key not in grouped:
            grouped[key] = {"paper": None, "memo": None}

        if "memo" in tl or "memorandum" in tl:
            grouped[key]["memo"] = url
        else:
            grouped[key]["paper"] = url

    for (stream, p_num), pair in grouped.items():
        if pair["paper"] and pair["memo"]:
            sub_name = f"{lang_family}_{stream}"
            records.append({
                "lang": lang_family, "subject": sub_name, "year": year, "session": session, "paper": p_num, "grade": grade,
                "paper_url": pair["paper"], "memo_url": pair["memo"],
                "paper_fname": f"{sub_name}_g{grade}_{year}_{session}_{p_num}.pdf",
                "memo_fname": f"{sub_name}_g{grade}_{year}_{session}_{p_num}_memo.pdf",
                "paper_id": f"dbe-{sub_name}-g{grade}-{p_num}-{year}-{session}",
                "memo_id": f"dbe-{sub_name}-g{grade}-{p_num}-{year}-{session}-memo",
                "title_p": f"{lang_family.title()} {stream.upper()} {p_num.upper()} {session.upper()} {year} (Grade {grade})",
                "title_m": f"{lang_family.title()} {stream.upper()} {p_num.upper()} {session.upper()} {year} Memorandum (Grade {grade})"
            })


def update_sources_csv(csv_path: Path, new_rows: list):
    """Update sources.csv with new entries, preventing duplicate source_ids."""
    existing_ids = set()
    header = ["source_id", "title", "url", "licence", "attribution", "subject", "grade", "language", "kind", "track", "year", "pair_with", "local_path", "notes"]
    rows = []

    if csv_path.exists():
        with open(csv_path, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for r in reader:
                existing_ids.add(r["source_id"])
                rows.append(r)

    added_count = 0
    for r in new_rows:
        grade_str = str(r.get("grade", "12"))
        is_eval = (r["year"] == 2024 and r["session"] == "nov" and grade_str == "12")

        # Question Paper row
        if r["paper_id"] not in existing_ids:
            clean_sub = r["subject"].split("_")[0]
            track_val = r["subject"].split("_")[1] if "_" in r["subject"] else ""
            rows.append({
                "source_id": r["paper_id"],
                "title": r["title_p"],
                "url": r["paper_url"],
                "licence": "DBE copyright - check terms",
                "attribution": "Department of Basic Education",
                "subject": clean_sub,
                "grade": grade_str,
                "language": "en" if r["lang"] == "english" else "af",
                "kind": "past_paper",
                "track": track_val,
                "year": str(r["year"]),
                "pair_with": r["memo_id"],
                "local_path": f"dbe/{r['lang']}/{r['subject']}/{r['year']}/{r['paper_fname']}",
                "notes": "held out for EVAL (do not train on it)" if is_eval else ""
            })
            existing_ids.add(r["paper_id"])
            added_count += 1

        # Memo row
        if r["memo_id"] not in existing_ids:
            clean_sub = r["subject"].split("_")[0]
            track_val = r["subject"].split("_")[1] if "_" in r["subject"] else ""
            rows.append({
                "source_id": r["memo_id"],
                "title": r["title_m"],
                "url": r["memo_url"],
                "licence": "DBE copyright - check terms",
                "attribution": "Department of Basic Education",
                "subject": clean_sub,
                "grade": grade_str,
                "language": "en" if r["lang"] == "english" else "af",
                "kind": "memo",
                "track": track_val,
                "year": str(r["year"]),
                "pair_with": "",
                "local_path": f"dbe/{r['lang']}/{r['subject']}/{r['year']}/{r['memo_fname']}",
                "notes": ""
            })
            existing_ids.add(r["memo_id"])
            added_count += 1

    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with open(csv_path, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(rows)

    return added_count


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--years", nargs="+", type=int, default=None, help="Years to download (defaults to all)")
    parser.add_argument("--sessions", nargs="+", default=["nov", "may"], help="Sessions to download ('nov', 'may')")
    parser.add_argument("--include-common", action="store_true", default=True, help="Include Grade 10 & 11 Common Papers")
    parser.add_argument("--dry-run", action="store_true", help="Inspect and list files without downloading")
    parser.add_argument("--limit", type=int, default=0, help="Limit number of pairs to download (for testing)")
    parser.add_argument("--delay", type=float, default=0.25, help="Polite delay between downloads (seconds)")
    args = parser.parse_args()

    ws_root = KIT_ROOT / "workspace"
    raw_root = ws_root / "raw"
    sources_csv = ws_root / "sources" / "sources.csv"

    print("================================================================================")
    print("Eishkom AI — DBE Past Exam Papers & Memorandums Downloader")
    print(f"Target Storage: {raw_root / 'dbe'}")
    print(f"Sources Ledger: {sources_csv}")
    print("================================================================================\n")

    all_pairs = []

    # 1. NSC Grade 12 subpages
    for (year, sess), url in sorted(PAGES.items(), reverse=True):
        if args.years and year not in args.years:
            continue
        if sess not in [s.lower() for s in args.sessions]:
            continue

        print(f"Discovering: {year} {sess.upper()} -> {url}", flush=True)
        html = fetch_html(url)
        if not html:
            continue
        records = parse_page_records(html, url, year, sess, default_grade="12")
        print(f"  -> Found {len(records)} verified paper+memo pairs for {year} {sess.upper()}.\n", flush=True)
        all_pairs.extend(records)

    # 2. Grade 10 & 11 Common Papers
    if args.include_common:
        for gr_key, gr_url in COMMON_PAGES.items():
            gr_num = "11" if gr_key == "gr11" else "10"
            print(f"Discovering: Grade {gr_num} Common Papers -> {gr_url}", flush=True)
            html = fetch_html(gr_url)
            if not html:
                continue
            records = parse_page_records(html, gr_url, default_year=2018, session="nov", default_grade=gr_num)
            print(f"  -> Found {len(records)} verified paper+memo pairs for Grade {gr_num}.\n", flush=True)
            all_pairs.extend(records)

    print(f"================================================================================", flush=True)
    print(f"Total target pairs found across all sessions: {len(all_pairs)} (Total PDFs: {len(all_pairs) * 2})", flush=True)
    print(f"================================================================================\n", flush=True)

    if args.dry_run:
        print("[DRY RUN] Preview of discovered files:")
        for r in all_pairs[:20]:
            print(f"  [{r['lang'].upper()} | Gr{r.get('grade','12')}] {r['title_p']}")
            print(f"    Paper: dbe/{r['lang']}/{r['subject']}/{r['year']}/{r['paper_fname']}")
            print(f"    Memo : dbe/{r['lang']}/{r['subject']}/{r['year']}/{r['memo_fname']}")
        if len(all_pairs) > 20:
            print(f"  ... and {len(all_pairs) - 20} more pairs.")
        return

    # Execute downloads
    pairs_to_process = all_pairs[:args.limit] if args.limit > 0 else all_pairs
    success_count = 0
    fail_count = 0

    print(f"Starting downloads for {len(pairs_to_process)} pairs ({len(pairs_to_process) * 2} PDFs)...")
    for i, r in enumerate(pairs_to_process, 1):
        paper_dest = raw_root / "dbe" / r["lang"] / r["subject"] / str(r["year"]) / r["paper_fname"]
        memo_dest = raw_root / "dbe" / r["lang"] / r["subject"] / str(r["year"]) / r["memo_fname"]

        print(f"[{i}/{len(pairs_to_process)}] Downloading {r['title_p']}...", flush=True)
        ok_p = download_pdf(r["paper_url"], paper_dest)
        time.sleep(args.delay)
        ok_m = download_pdf(r["memo_url"], memo_dest)
        time.sleep(args.delay)

        if ok_p and ok_m:
            success_count += 1
        else:
            fail_count += 1

    # Update sources.csv
    print(f"\nUpdating sources ledger: {sources_csv}...", flush=True)
    added = update_sources_csv(sources_csv, pairs_to_process)
    print(f"Added {added} new rows to sources.csv.", flush=True)

    print("\n================================================================================", flush=True)
    print(f"Download Summary: {success_count} pairs completed successfully, {fail_count} failed.", flush=True)
    print(f"Storage Directory: {raw_root / 'dbe'}", flush=True)
    print("================================================================================", flush=True)


if __name__ == "__main__":
    main()
