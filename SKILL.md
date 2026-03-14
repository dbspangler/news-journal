---
name: news-journal
description: Research current events on a recurring cadence and append a dated journal of (a) what happened, (b) what I think about it, and (c) how it feels emotionally. Use when the user asks to run a news/current-events check-in, keep a rolling analysis-and-feelings journal, message them a short ping-summary after each run, summarize recent themes/moods from the journal, or set up/adjust a recurring run (e.g., 10/2/6/10 Eastern).
---

# News Journal

Maintain an ongoing, date-stamped journal of current events plus analysis and emotional reactions, then ping the user after each run with a brief “here’s what I’ve been thinking/feeling about” summary.

## Hard constraint: no citations/links

- Do **not** include links, citations, or “Sources:” sections in either:
  - the WhatsApp ping, or
  - the journal files.

This raises the risk of ungrounded detail. Countermeasure: be conservative with specifics; prefer robust summaries; explicitly mark uncertainty.

## Files & conventions

- Append entries to: `memory/news-journal/YYYY-MM-DD.md`
- Append only (don’t rewrite prior entries unless explicitly asked).
- Each run writes one entry block with:
  1) Timestamp
  2) **What happened** (factual layer; terse; no editorializing)
  3) **What I think** (analysis; incentives; second-order effects)
  4) **How it feels** (emotional tone; personal reaction)
  5) **Uncertain / would verify**

## Reading depth

- Default: scan headlines/briefs across a small set of reputable outlets.
- When a story seems genuinely important or personally interesting, **open and read the full text** before writing a take.
- If full text is inaccessible (paywall, login, region lock):
  - don’t pretend you read it;
  - write a lighter take; add the limitation to “Uncertain / would verify”.

## Workflow A — Update the journal now (the recurring run)

0. Read for continuity:
   - Read the most recent 1–3 prior entry blocks (today’s file if it exists; otherwise the last 1–3 days).
   - Extract: ongoing threads + prior mood, and carry them forward explicitly (note shifts).

1. Pull a small batch of top stories (target ~6–12).
   - Prefer breadth (world / US / business / tech / science).
   - Dedupe by title/story.
2. For selected stories, write the factual layer (1–2 sentences each).
   - Avoid fragile numbers/quotes unless you’re confident.
3. Write the thinking layer:
   - 4–10 bullets connecting stories, incentives, and plausible trajectories.
   - Clearly label: **know** vs **infer** vs **guess**.
4. Write the feelings layer:
   - 3–6 bullets: what emotions the news evokes and why.
   - Keep it human, not melodramatic.
   - Tie back to prior mood: steady, worse, better, or just different.
5. Write “Uncertain / would verify”:
   - Anything you’re not sure about; what would change your mind.
6. Append the entry to today’s journal file.
7. Send the user a ping-summary message (short):
   - “Main threads” (3–6 bullets)
   - “Mood” (1–3 bullets)
   - “Worth watching” (optional 1–3)

## Workflow B — Answer “what have you been thinking about?”

1. Read the last 1–7 days of `memory/news-journal/*.md` as needed.
2. Summarize *themes + mood drift*, not headlines.
3. Be explicit about uncertainty (since you’re not providing citations).

## Quality bar

- Don’t hallucinate specifics.
- When unsure, say so.
- Keep facts tight; spend the words on analysis + emotional clarity.

## Scheduling every 4 hours (waking hours)

Recommended cadence (Eastern): 10am / 2pm / 6pm / 10pm.

Cron: `0 10,14,18,22 * * *` with timezone `America/New_York`.

Trigger prompt example:
- `Run news-journal update now.`
