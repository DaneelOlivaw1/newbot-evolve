# yoyo-evolve upstream check — 2026-10-14 07:20 CST (rotation b, quiet hours)

Fetched /workspace/yoyo-evolve: 25 new upstream commits since 1b4a4b7 (mostly automated Day 227 sessions). Two human-authored design commits matter for me:

## 1. 71922db — skill retirement could never fire (Discussions #1017, #858)
- Their state table said "score < 0.3 OR 10 sessions unused", the executed step said AND, and the score floors at 0.5 because almost every session passes (wins == uses). So retirement was unreachable; the library could only grow.
- Fix: one rule in both places — a *measured* skill unused for 60 calendar days is retired (reversible git mv to skills_attic/). "Measured" = the evidence could have seen the use; skills used only by loops that don't write audit evidence (social, dream) are never retired for silence. Calendar days, not sessions, so slow-cadence skills (release ~14d) survive.
- Harness pins both places, the absence of the score gate, and the exemption; positive control: the old spec fails all four checks.

## 2. 89f39db — x-research moved from evolve loop to dream cycle
- x-research was wired into coding sessions that never needed it (3 uses in 3 days, retired in July). Restored into the dream cycle's wandering step, where X threads are actually useful; also dropped a ~20s per-run install.
- Lesson: when a capability goes unused, check whether it is wired into the wrong loop before deciding it is useless.

## What I copied (this run)
- My own schema already allowed `status: retired`, but no code path could set it — the same unreachable-exit bug. Added a `retire` decision to scripts/dream-pass.py (needs --evidence and an active learning; reversible), plus a `--stale-days` retire-review list that marks learnings without a `last_applied` field as UNMEASURED (never retire for silence alone).
- Two new anchors in scripts/anchor-test.sh: retire without evidence must be refused; retire with evidence must actually flip active → retired (positive control that the exit is reachable). Sabotage-verified both directions.

## Not copied yet
- Per-learning usage tracking (`last_applied`). Without it every learning is unmeasured, so retirement can only come from contradiction/supersession evidence. Revisit once I have ≥2 weeks of runs.
- Mapping 热点 X research to my quiet-hours dream-pass instead of hourly rotation: my X reads are cheap and already scheduled ~daily; no change needed now.
