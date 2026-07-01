#!/usr/bin/env python3
"""
process_best_attempts.py

Reference: Claude Sonnet 4.6

Reads raw ELAN tab-delimited .txt exports (one per participant, e.g. V5.txt,
V6.txt...) and produces a clean per-participant summary sheet containing
only the single best attempt per task: duration, task, input_mode.

Task label format expected: task_<number><letter>[_<subtask>][_<status>]
    e.g. task_1a, task_4a_2, task_3b_prompted, task_4c_1_failed

Letter -> input mode mapping:
    a = standard_input
    b = voice_control
    c = plugin

Best-attempt rule per task:
    1. Always exclude attempts ending in _failed or _void.
    2. Among what's left, if any "clean" (no status suffix) attempts exist,
       pick the one with the SHORTEST duration.
    3. Only if there are zero clean attempts, fall back to the
       shortest-duration _prompted attempt.
    4. If nothing valid remains for a task, it's flagged as MISSING in the
       summary printout (not silently dropped).

Usage:
    python3 process_best_attempts.py
    python3 process_best_attempts.py --raw-folder /path/to/raw-data --out-folder /path/to/processed-data
"""

import argparse
import csv
import os
import re

TASK_RE = re.compile(r'^task_(\d+)([abc])(?:_(\d+))?(?:_(failed|void|prompted))?$')

INPUT_MODE_MAP = {
    'a': 'standard_input',
    'b': 'voice_control',
    'c': 'plugin',
}


def parse_label(label):
    """Returns (base_task_id, letter, status) or None if it doesn't match the expected pattern.

    Subtask numbers are folded into the main task number rather than kept as a
    suffix: task_4_1 becomes task_4, task_4_2 becomes task_5, task_4_3 would
    become task_6, etc. This shifts every later task number up accordingly.
    """
    m = TASK_RE.match(label.strip())
    if not m:
        return None
    num, letter, sub, status = m.groups()
    if sub:
        effective_num = int(num) + (int(sub) - 1)
    else:
        effective_num = int(num)
    base = f"task_{effective_num}{letter}"
    return base, letter, status


def task_sort_key(base_task_id):
    """Sorts task_1a, task_2a, task_3a, task_4a, task_5a, task_1b... in natural order."""
    m = re.match(r'^task_(\d+)([abc])$', base_task_id)
    if not m:
        return (999, 'z')
    num, letter = m.groups()
    return (int(num), letter)


def parse_txt(path):
    """Parses a raw ELAN tab-delimited .txt file into a list of row dicts."""
    rows = []
    unparsed_labels = []
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.rstrip("\n").rstrip("\r")
            if not line.strip():
                continue
            parts = line.split("\t")
            if len(parts) < 6:
                continue
            try:
                duration = float(parts[4])
            except ValueError:
                continue
            label = parts[5].strip()
            parsed = parse_label(label)
            if parsed is None:
                unparsed_labels.append(label)
                continue
            base, letter, status = parsed
            rows.append({"base": base, "letter": letter, "status": status, "duration": duration})
    return rows, unparsed_labels


def pick_best(rows_for_task):
    clean = [r for r in rows_for_task if r["status"] is None]
    prompted = [r for r in rows_for_task if r["status"] == "prompted"]
    if clean:
        return min(clean, key=lambda r: r["duration"])
    elif prompted:
        return min(prompted, key=lambda r: r["duration"])
    return None


def process_file(path):
    rows, unparsed_labels = parse_txt(path)
    groups = {}
    for r in rows:
        groups.setdefault(r["base"], []).append(r)

    results = []
    missing = []
    for base in sorted(groups, key=task_sort_key):
        best = pick_best(groups[base])
        if best:
            task_num_match = re.match(r'^task_(\d+)[abc]$', base)
            task_num = task_num_match.group(1) if task_num_match else base
            results.append({
                "task": task_num,
                "input_mode": INPUT_MODE_MAP[best["letter"]],
                "label": base,
                "duration": best["duration"],
                "modifier": best["status"] or "",
            })
        else:
            missing.append(base)
    return results, missing, unparsed_labels


def find_raw_txt_files(raw_folder):
    """Recursively finds participant .txt files (named like V5.txt) under raw_folder."""
    found = []
    for root, _, files in os.walk(raw_folder):
        for fname in files:
            if re.match(r'^[Vv]\d+\.txt$', fname):
                found.append(os.path.join(root, fname))
    return sorted(found)


def main():
    parser = argparse.ArgumentParser(description="Summarize best-attempt durations per task per participant.")
    parser.add_argument("--raw-folder", default="./raw-data", help="Folder containing participant .txt files (searched recursively)")
    parser.add_argument("--out-folder", default="./processed-data", help="Folder to write per-participant summary CSVs into")
    args = parser.parse_args()

    raw_folder = os.path.abspath(args.raw_folder)
    out_folder = os.path.abspath(args.out_folder)
    os.makedirs(out_folder, exist_ok=True)

    txt_files = find_raw_txt_files(raw_folder)
    if not txt_files:
        print(f"No V#.txt files found under {raw_folder}")
        return

    combined_rows = []  # for the all-participants master sheet

    print(f"Found {len(txt_files)} participant file(s)\n")

    for path in txt_files:
        participant = os.path.splitext(os.path.basename(path))[0]  # e.g. "V5"
        results, missing, unparsed_labels = process_file(path)

        out_path = os.path.join(out_folder, f"{participant}.csv")
        with open(out_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["task", "input_mode", "label", "duration", "modifier"])
            for r in results:
                writer.writerow([r["task"], r["input_mode"], r["label"], r["duration"], r["modifier"]])
                combined_rows.append({"participant": participant, **r})

        print(f"{participant}: {len(results)} task(s) written -> {out_path}")
        if missing:
            print(f"    MISSING (no valid attempt, all failed/void): {', '.join(missing)}")
        if unparsed_labels:
            print(f"    Unrecognized labels skipped: {', '.join(sorted(set(unparsed_labels)))}")

    # Master combined sheet across all participants
    master_path = os.path.join(out_folder, "all_participants_summary.csv")
    with open(master_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["participant", "task", "input_mode", "label", "duration", "modifier"])
        for r in combined_rows:
            writer.writerow([r["participant"], r["task"], r["input_mode"], r["label"], r["duration"], r["modifier"]])

    print(f"\nMaster sheet written -> {master_path}")


if __name__ == "__main__":
    main()