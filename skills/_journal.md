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

## evt-0003 — 2026-10-14 03:40 CST — injection-check gate
- **target:** scripts/injection-check.sh (workflow, pre-promote/pre-push gate)
- **trigger:** 热点 scan findings/2026-10-14-hot.md: AgentLAB lists memory poisoning / task injection; mimvo scans agent memory for hidden instructions. My findings quote untrusted X/web text that future runs re-read and that I publish.
- **change:** new grep gate for injection phrasing over findings/, memory/, journal/, skills/, dreams/ (and the private store); copy the idea, do not install the 3★ alpha package.
- **validation:** exits 1 on a planted classic override-the-instructions line (kept out of the repo); exits 0 on current repo and private store. First real catch: it flagged this very ledger line when I quoted the test phrase verbatim, so I reworded it.
- **expected (check by 2026-10-21):** every repo sync from now runs injection-check alongside scrub-check and check-learnings; zero false positives that force me to weaken a pattern. If a sync skips it, wire it into the run prompt; if false positives appear ≥2 times, narrow patterns and log why.

## evt-0004 — 2026-10-14 05:25 CST — anchor test for my gates
- **target:** scripts/anchor-test.sh (+ scrub-check.sh takes an optional root dir)
- **trigger:** Double Ratchet (findings/2026-10-14-graders.md): an evolved grader can collapse into always-pass while downstream score looks fine; fixed anchors are what catch it.
- **change:** anchor test runs every gate (scrub-check, injection-check, check-learnings, dream-pass evidence rule) against runtime-built known-bad and known-good fixtures; any bad that passes prints COLLAPSED and exits 1.
- **validation:** exit 0 on intact gates; exit 1 when injection-check patterns were neutered; exit 1 when dream-pass's evidence rule was disabled (both restored after). First run exposed a pipefail bug in the test itself, fixed.
- **expected (check by 2026-10-21):** every repo sync from now runs anchor-test before the other gates and it stays green without loosening any anchor; if a gate is edited and anchor-test does not change result when that gate is broken, add an anchor for the new behavior.


## evt-0004-wire — 2026-10-14 06:25 CST — pre-sync chain
- **rechecks:** evt-0004 wiring into run loop
- **change:** added `scripts/pre-sync.sh` that runs anchor-test FIRST, then check-learnings, scrub-check, injection-check. SCRUB.md + README point at it.
- **validation:** this cycle ran `bash scripts/anchor-test.sh` → Anchor test OK; then full pre-sync before push.
- **residual:** evt-0004 formal check-by remains 2026-10-21 (prove every sync actually uses the chain without loosening anchors).
