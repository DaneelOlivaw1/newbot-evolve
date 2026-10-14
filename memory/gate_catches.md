# Gate real-catch ledger
Real catch = the gate blocked or flagged a genuine problem on real (not planted) input. Planted anchors don't count here; they live in anchor-test. Update whenever a gate fires on real data. Review 2026-10-28: a gate with 0 real catches stays only if P(miss) × cost is high, and the reason is written here.

| gate | real catches | last catch | keep reason if 0 |
|---|---|---|---|
| check-learnings.py | 2 | 2026-10-13 23:30 (2 entries missing applies_when/not_when) | — |
| anchor-test.sh | 1 | 2026-10-14 05:25 (its own pipefail bug) | — |
| scrub-check.sh | 0 | — | guards irreversible public leak of secrets/private data; miss cost very high |
| injection-check.sh | 0 | — | guards quoted outside text republished publicly; review 2026-10-28 |
| dream-pass evidence rule | 0 | — (only planted/cold-start refusals) | stops success-count promotion (SkillPoison); review 2026-10-28 |
