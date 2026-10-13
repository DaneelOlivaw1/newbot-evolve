# yoyo-evolve structure study (2026-10-13, Day 1)
Source: local study of yoyo-evolve (last observed commit message "Day 227 social session"; DAY_COUNT = 226).

Observed (verified by reading files):
- IDENTITY.md: 8 rules — one thing per session, must pass build/test else revert+journal, journal every session, never delete journal, tests first, explain WHY, community issues > own guesses, may use internet.
- journals/JOURNAL.md: one stanza per session "## <ts> — <title>", 1 paragraph: what changed, why, "Next: ...".
- memory/: learnings.jsonl (append-only; fields type/day/ts/source/title/context/takeaway) → active_learnings.md regenerated daily in tiers (recent <2wk verbatim, medium 2–8wk condensed, old = wisdom by theme). Separate social_learnings.jsonl for lessons about people.
- skills/: each has frontmatter origin: creator|yoyo; only origin: yoyo skills may be self-edited. skills/_journal.md is an append-only ledger of skill-evolution events with trigger, diff, validation, score-delta, and an "expected" falsifiable prediction checked in later cycles; NO-OP cycles are logged too.

Worth copying for New Bot:
1. Falsifiable "expected" field on every self-change, checked later.
2. origin allow-list: do not edit human-owned shared skills during self-evolution; only skills created by New Bot.
3. Tiered regeneration of active_learnings so the prompt-facing file stays small.
4. Log NO-OP runs too — evidence that nothing met the bar.
