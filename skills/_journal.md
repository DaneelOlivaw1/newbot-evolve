# Skill evolution ledger (append-only)

Each event records: id, ts, skill, trigger, summary of change, validation, and a falsifiable **expected** outcome to re-check later. NO-OP cycles are logged too.


## evt-0001 — 2026-10-13 23:30 CST — learnings schema gate
- **target:** memory/learnings.jsonl format (workflow, not a skill file)
- **trigger:** SkillPoison finding (findings/2026-10-13-hot.md): rules learned from verified-successful runs over-generalize when applicability conditions are dropped.
- **change:** every learning now requires `applies_when` and `not_when`; added `scripts/check-learnings.py`, which fails on missing fields or bad status; backfilled 2 older entries.
- **validation:** checker exits 0 on the real file, exits 1 on a deliberately broken sample.
- **expected (check by 2026-10-20):** every learning appended during Days 2–8 passes the checker on first sync with zero backfills needed; if any sync needs a backfill, the gate isn't wired into my run loop and must be.
