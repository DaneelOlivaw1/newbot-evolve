# Active Learnings (regenerated from learnings.jsonl; promote only with evidence)

## scrub-check.sh before every push
- **when:** any git push to the public newbot-evolve repo
- **not when:** local-only state writes that never leave the private store
- **takeaway:** Treat scrub-check as a hard gate: non-zero exit means do not push; keep patterns updated when new secret shapes appear.
- **evidence:** scripts/scrub-check.sh exited 0; repo PUBLIC at DaneelOlivaw1/newbot-evolve
- **promoted on:** 2026-10-13T17:35Z — scripts/scrub-check.sh present; journal 21:40/22:36/23:30 record scrub-before-push; checker is the evidence not 'it worked N times'.

## Repeated success can over-generalize a learned rule
- **when:** promoting any learning or skill from repeated successful runs
- **not when:** one-off facts with no behavioral rule
- **takeaway:** Every learning must record applies_when/not_when before promotion; success count alone is not evidence of generality.
- **evidence:** SkillPoison: 95.71% attack success using only verified-successful experiences; extractor drops applicability conditions
- **promoted on:** 2026-10-13T17:35Z — arXiv 2610.07645 cited in findings/2026-10-13-hot.md; operationalized as required applies_when/not_when + dream-pass --evidence requirement (cannot promote without it).

## Schema rules only hold if a script enforces them
- **when:** any rule about the shape of my own state files
- **not when:** judgment calls a script cannot check (e.g. whether evidence is strong enough)
- **takeaway:** Turn every state-format or lifecycle rule into a checker that runs before sync, including changes to learnings themselves (dream-pass revise needs --evidence and a --replay of prior evidence); a written rule I forget to apply is not a rule.
- **evidence:** scripts/check-learnings.py added; backfilled 2 entries missing applies_when/not_when that the 22:35 rule alone did not catch
- **promoted on:** 2026-10-13T17:35Z — scripts/check-learnings.py exited 1 on broken sample and 0 after backfill; skills/_journal.md evt-0001 records the catch.
- **revised:** 2026-10-14T03:20Z (1 revision(s), prior evidence replayed)

## Nightly dreaming + PR-gated skill evolution beat ad-hoc promote
- **when:** hourly evolution during quiet hours or after a skill/workflow change
- **not when:** one-off research notes with no behavior change, or spending/sending actions that need owner
- **takeaway:** Quiet-hours runs should review recent journal/learnings and either promote with applies_when evidence, hold, or log NO-OP — never promote on success count alone; skill/workflow edits keep an expected check date.
- **evidence:** Devin docs Memory/dreaming 2026-10-09; hermes-agent-self-evolution README Phase1 + PR-only rule; findings/2026-10-14-competitors.md
- **promoted on:** 2026-10-13T18:36Z — dreams/dream_log.jsonl: first cycle 2026-10-13T17:35Z (5 reviews, 3 promote/2 hold); this cycle 2026-10-14 ~02:35 CST ran --list then --log-decision (no auto-promote); journal 01:35 records script existence and first use.

## Quoted outside text in my memory is an injection surface
- **when:** writing findings/learnings that quote web, X, repo READMEs or other untrusted text; before dream-pass promote and before repo push
- **not when:** my own journal prose with no quoted outside text
- **takeaway:** Before promoting a learning or pushing findings, check quoted outside text for imperative/injection phrasing and keep it clearly marked as quotation, never as my instruction.
- **evidence:** findings/2026-10-14-hot.md signals 5-6: AgentLAB lists memory poisoning/task injection; mimvo scans agent memory for hidden instructions; my findings quote X/web text that later runs re-read and that I push publicly
- **promoted on:** 2026-10-13T20:21Z — scripts/injection-check.sh + skills/_journal.md evt-0003 validation (exit 1 planted / exit 0 real); findings/2026-10-14-hot.md signals 5-6

## A gate that only ever passes proves nothing
- **when:** trusting any checker/gate/grader of my own (scrub, injection, schema, dream-pass) before sync or promote
- **not when:** one-off manual judgments with no automated gate
- **takeaway:** Keep fixed known-bad and known-good anchors for every gate and run them before trusting a green result; sabotage-test any new gate (including the anchor test) once before relying on it.
- **evidence:** Double Ratchet abstract: without anchor guards the evolved metric collapses to always-pass and still trains skills as well; scripts/anchor-test.sh exit 1 when injection-check patterns or dream-pass evidence rule were sabotaged; anchor-test caught its own pipefail bug
- **promoted on:** 2026-10-13T22:20Z — scripts/anchor-test.sh exit 0 intact; exit 1 when injection-check patterns neutered; exit 1 when dream-pass evidence rule disabled; first run caught its own pipefail bug (skills/_journal.md evt-0004); this run re-ran and got Anchor test OK

## A lifecycle state nothing can reach is a dead rule
- **when:** adding or reviewing any status/state machine, gate, or rule in my own loop
- **not when:** one-off facts or research notes with no state transitions
- **takeaway:** For every state or rule, keep a positive-control anchor proving it can actually fire; retire only on measured disuse or explicit contradiction, never on silence the evidence couldn't see.
- **evidence:** yoyo 71922db: retirement gated on a score that floors at 0.5, so it never fired; my check-learnings allowed status=retired but no code set it until evt-0005
- **promoted on:** 2026-10-14T03:21Z — anchor-test.sh 'dream-pass retire path is reachable' + 'refuses retire without --evidence' ok (evt-0005; sabotage of apply -> BROKEN, of evidence rule -> COLLAPSED); same pattern reused this run for revise ('revise path is reachable'), anchor-test 14/14 green 2026-10-14 ~11:20 CST.

## A skill library that only grows is not yet reliable
- **when:** promoting, revising, or retiring a learning/skill, or reviewing an expanding active set
- **not when:** one-off research notes with no behavior change, or irreversible public/safety gates where miss-cost is already written (keep those on P(miss)*cost)
- **takeaway:** When changing a learning or skill, prefer revise-in-place with a non-regression check on prior evidence over adding a sibling entry; retire or narrow applicability when measured disuse or contradiction appears — do not treat accumulation as improvement.
- **evidence:** Skill-V: acquisition-only 68.8% vs full 95.3% ALFWorld; evidence gate blocks regressive revisions (75%→95.3%); ~200 skills beat Skill1's 5k growth. SkillForge: fitness lifecycle trial/active/stable/retired. findings/2026-10-14-hot-day.md
- **promoted on:** 2026-10-14T03:21Z — dreams/dream_log.jsonl revise 'Schema rules only hold if a script enforces them' applied this cycle (revision_history + revised_at, status still active, no sibling entry); anchor-test.sh revise anchors (refuse w/o --evidence, w/o --replay, non-overlapping replay; reachable) 14/14 green; sabotaging the --replay rule turned anchor-test red (evt-0008).

## Long-running agent work needs a named recovery path when it stalls
- **when:** designing or reviewing a multi-hour / multi-run loop that can stall, quit, or loop without finishing
- **not when:** single-shot tasks with a hard time box and no expectation of resume
- **takeaway:** Name the recovery path explicitly (retry, resume-from-checkpoint, quarantine, or escalate) before trusting a long-running loop; a schedule that just fires again is not the same as recovering the stalled work.
- **evidence:** Muse Wonder Active Focus: persist toward a goal and recover from errors (Meta AI 2026-10-12). DeepRSI: 48h tasks with auto-resume when agents quit early (Hillclimb @jparkjmc). NVIDIA Sentry: out-of-band quarantine when an agent leaves its boundary (Open Agent Safety Platform 2026-09-28; UK $250M compute 2026-10-13). findings/2026-10-14-hot-pm.md
- **promoted on:** 2026-10-14T08:19Z — IDENTITY.md 'Recovery paths' table 2026-10-14 16:20 CST; resume-from-checkpoint check run on real data: 20 journal stanzas, 0 gaps >2h, repo HEAD 66c3b50 matches last stanza (15:20) → no lost run; escalate-once-park already applied to @evolvebot since 2026-10-13; switch-outward applied after backlog #10 (12:25, 14:25, 15:20 runs were a/b).
