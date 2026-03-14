#!/usr/bin/env python3
"""Append a draft news journal entry WITHOUT links/citations.

This script is intentionally conservative: it drafts a structure and titles only.
The agent should still do the real reading (including full-text when relevant)
then replace/expand the draft with factual + analysis + feelings.

Usage:
  python3 skills/news-journal/scripts/news_journal.py --outdir memory/news-journal --titles "Title 1" "Title 2" ...

Rationale:
- The user requested no citations/links in the journal.
- Full web fetching/parsing varies by environment; keep this script stable.
"""

from __future__ import annotations

import argparse
import datetime as dt
from pathlib import Path


def ensure_dir(p: Path) -> None:
    p.mkdir(parents=True, exist_ok=True)


def now_utc() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def write_entry(outdir: Path, titles: list[str], ts: dt.datetime) -> Path:
    ensure_dir(outdir)
    day_path = outdir / f"{ts.strftime('%Y-%m-%d')}.md"

    lines: list[str] = []
    lines.append(f"## {ts.strftime('%Y-%m-%d %H:%M')} UTC")
    lines.append("")

    lines.append("**What happened (draft):**")
    if titles:
        for t in titles:
            t = " ".join(t.split()).strip()
            if t:
                lines.append(f"- {t}")
    else:
        lines.append("- (add 6–12 stories)")
    lines.append("")

    lines.append("**What I think (fill this in):**")
    lines.append("- (know) ")
    lines.append("- (infer) ")
    lines.append("- (guess) ")
    lines.append("")

    lines.append("**How it feels:**")
    lines.append("- ")
    lines.append("")

    lines.append("**Uncertain / would verify:**")
    lines.append("- ")
    lines.append("\n---\n")

    existing = day_path.read_text(encoding="utf-8") if day_path.exists() else ""
    day_path.write_text(existing + "\n".join(lines) + "\n", encoding="utf-8")
    return day_path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--titles", nargs="*", default=[])
    args = ap.parse_args()

    ts = now_utc()
    path = write_entry(Path(args.outdir), list(args.titles), ts)
    print(str(path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
