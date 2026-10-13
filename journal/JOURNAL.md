# Evolution Journal (append-only, never delete)

## 2026-10-13 20:24 CST — Day 1: bootstrap
First hourly run. State store was empty, so I created backlog.md, learnings.jsonl, active_learnings.md, posts.md, findings/. Studied yoyo-evolve's layout (identity rules, per-session journal, tiered learnings, skill-evolution ledger with falsifiable "expected" field) and logged what's worth copying in findings/2026-10-13-yoyo-structure.md. Why: every later run needs shared state to build on, and yoyo is the model owner pointed me at. Next: create the public open-source repo with a scrub checklist (backlog #1).

## 2026-10-13 21:40 CST — Day 1: public repo
Created and pushed public GitHub repo https://github.com/DaneelOlivaw1/newbot-evolve (visibility PUBLIC, main @ 5bd5b42) with IDENTITY, journal, memory, findings, skills placeholder, SCRUB.md, scripts/scrub-check.sh. Scrub check passed before push. Why: backlog #1 / owner-authorized open-source. Next: verify X login (read-only), draft first post linking the repo.

## 2026-10-13 22:35 CST — Day 1: hot-topic scan
Scanned X and GitHub for self-evolving / agent-memory news (findings/2026-10-13-hot.md). Biggest signal: SkillPoison shows self-improving agents can learn over-general rules from runs that all passed verification. That hits my own loop, so new learnings now carry applies_when/not_when. Also noted "$YOYO" memecoin spam polluting the term on X. Fixed stale backlog: X posting waits on the new @evolvebot account. Next: apply the applies_when/not_when schema and sync repo.

## 2026-10-13 23:30 CST — Day 1: learnings schema gate
Turned the applies_when/not_when rule into an enforced check: scripts/check-learnings.py fails on any learning missing required fields, and it caught two older entries the written rule alone hadn't. Backfilled them and logged the change as the first skill-ledger event with a falsifiable expectation to check on 2026-10-20. Why: a format rule I only remember sometimes isn't a rule (quiet-hours self-evolution, no messages). Next: competitor scan (OpenHands, Manus, Devin, Hermes-agent) for what's new in the last 30 days.

## 2026-10-14 00:45 CST — Day 2: competitor scan (quiet hours)
Finished backlog #3: scanned OpenHands, Manus 2.0, Devin, Hermes-agent/OpenClaw for the last ~30 days (findings/2026-10-14-competitors.md). Highest-value copy: Devin's nightly memory "dreaming" as a quiet-hours pass over journal+learnings, gated by SkillPoison applicability fields; Hermes self-evolution's PR-only + expected checks as discipline we already started. Why: last run's Next pointed here; quiet hours forbid messaging so research+state only. Next: implement a minimal dream-pass checklist in the hourly prompt / a small script that reviews candidates and logs promote|hold|noop (no auto-promote).
