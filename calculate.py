#!/usr/bin/env python3
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MATRIX = ROOT / "SCORE_MATRIX.csv"

MAXIMA = {"C1":30,"C2":20,"C3":20,"C4":15,"C5":10,"C6":5}
TIE_KEYS = ("C1", "C2", "C4", "C5")

def load_rows():
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        raise SystemExit("SCORE_MATRIX.csv is empty")
    return rows

def validate_and_score(rows):
    scored = []
    for row in rows:
        total = 0
        for cid, max_score in MAXIMA.items():
            value = int(row[cid])
            if value < 0 or value > max_score:
                raise ValueError(f"{row['participant']}: {cid}={value} outside 0..{max_score}")
            total += value
        published = int(row["total"])
        if total != published:
            raise ValueError(f"{row['participant']}: calculated total {total} != published {published}")
        scored.append({"participant": row["participant"], "total": total, **{cid: int(row[cid]) for cid in MAXIMA}})
    scored.sort(key=lambda r: (-r["total"], *(-r[cid] for cid in TIE_KEYS), r["participant"].casefold()))
    return scored

def main():
    rows = load_rows()
    scored = validate_and_score(rows)
    print("rank,participant,total")
    for i, row in enumerate(scored, start=1):
        print(f"{i},{row['participant']},{row['total']}")

if __name__ == "__main__":
    main()
