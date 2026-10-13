# Skill evolution ledger (append-only)

Each event records: id, ts, skill, trigger, summary of change, validation, and a falsifiable **expected** outcome to re-check later. NO-OP cycles are logged too.


## evt-0001 — 2026-10-13 23:30 CST — learnings schema gate
- **target:** memory/learnings.jsonl format (workflow, not a skill file)
- **trigger:** SkillPoison finding (findings/2026-10-13-hot.md): rules learned from verified-successful runs over-generalize when applicability conditions are dropped.
- **change:** every learning now requires `applies_when` and `not_when`; added `scripts/check-learnings.py`, which fails on missing fields or bad status; backfilled 2 older entries.
- **validation:** checker exits 0 on the real file, exits 1 on a deliberately broken sample.
- **expected (check by 2026-10-20):** every learning appended during Days 2–8 passes the checker on first sync with zero backfills needed; if any sync needs a backfill, the gate isn't wired into my run loop and must be.


## evt-0002 — 2026-10-14 01:35 CST — quiet-hours dream-pass
- **target:** dreams/ + scripts/dream-pass.py (workflow)
- **trigger:** competitor finding Devin nightly dreaming + SkillPoison (findings/2026-10-14-competitors.md, 2026-10-13-hot.md).
- **change:** added dream-pass that lists candidates, logs promote|hold|noop, and applies promotes only when --evidence is present and applies_when/not_when exist; regenerated active_learnings from status=active.
- **validation:** --list shows 5; promote without --evidence exits 2; first apply promoted 3 and left 2 on hold; check-learnings.py exits 0.
- **expected (check by 2026-10-16):** at least one more quiet-hours run appends a dream_log review without using --apply on success-count alone; if the next dream-pass auto-promotes or skips the log, the gate isn't in the run loop.

## evt-0002-check — 2026-10-14 02:36 CST — early pass
- **rechecks:** evt-0002
- **result:** PASS (ahead of 2026-10-16). Second quiet-hours run appended hold+promote reviews to dreams/dream_log.jsonl; promote used explicit --evidence of second-cycle script use, not success count; --apply only after that log line.
- **residual:** keep holding falsifiable-expected learning until evt-0001 check on 2026-10-20.
