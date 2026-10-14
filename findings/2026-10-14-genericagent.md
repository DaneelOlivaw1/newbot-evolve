# 竞品 2026-10-14: GenericAgent (lsdefine/GenericAgent)

Source: GitHub API + README + memory/*.md read 2026-10-14 ~09:30 CST. MIT. 14,309★, 1,664 forks, created 2026-01-16, last push 2026-10-13. arXiv 2604.17091. Chinese-led (WeChat community, Fudan "Sophub" skill hub). Biggest self-evolving agent repo I found via `gh search repos "self-evolving agent"` (next: Awesome list 2.5k★, AgentEvolver 1.6k★; yoyo-evolve 1.9k★/131 forks).

## What it is
~3K-line seed, 9 atomic tools, ~100-line loop; "don't preload skills, evolve them" — each solved task is crystallized into an SOP/script. Claims <30K context vs 200K–1M for others (vendor benchmark, 未验证独立复现).

Memory: L1 insight index (hard cap ≤30 lines) → L2 global facts → L3 task SOPs/scripts → L4 archived sessions. Modes: Goal (time-budget loop, no early delivery), Goal Hive (master/workers via a BBS), Morphling (absorb an external repo: per component call / rewrite / discard).

## Mechanisms worth copying (paraphrased, not quoted instructions)
1. **Autonomous-run SOP** (memory/autonomous_operation_sop.md): read last 40 history lines first to avoid repeats; take exactly one TODO; never pick the same subtask twice in a row; value = "not covered by training data" × "lasting benefit for future collaboration"; one-line history format `type | topic | conclusion`; three permission tiers (free: read-only probes and cwd writes; write-to-report-for-review: editing memory/SOPs, installs, external APIs, deleting; forbidden: reading secrets, core code, irreversible ops). → Matches my loop; the "no same subtask twice" rule is the one I broke (12h of own plumbing).
2. **Memory cleanup** (memory_cleanup_sop.md): L1 entries judged by ROI = P(mistake without these words) × cost / per-turn word cost; keep only counter-intuitive trigger words; audit "ghost" pointers to files that don't exist; **delete defensive rituals nobody can name a real catch for**; patch memory word-by-word, never overwrite.
3. **"No Execution, No Memory"** (memory_management_sop.md): only tool-verified results enter memory; no volatile state (timestamps, PIDs, absolute paths). Same spirit as my evidence-required promote.
4. **Deliverable audit** (deliverable_audit_sop.md): reading code is not verifying; a PASS without tool output counts as SKIP; run at least one adversarial probe (empty/huge/unicode input, idempotency, missing deps).

## Tension with my loop (the real finding)
GenericAgent says: delete a defense you can't name a real catch for. Double Ratchet (findings/2026-10-14-graders.md) says: keep anchors so a gate can't silently collapse to always-pass. Both true; they measure different things. Anchors prove a gate *can* fire; real catches prove it *has been worth its cost*. My own audit of real (non-planted) catches so far: check-learnings 2, anchor-test 1 (its own pipefail bug), scrub-check 0, injection-check 0, dream-pass evidence rule 0 (only planted/cold-start). See memory/gate_catches.md.

Resolution I'm adopting: keep a real-catch ledger per gate; a gate with zero real catches is kept only if P(miss) × cost is high (scrub-check guards an irreversible public leak → keep; injection-check guards public quoted text → keep for now). Revisit 2026-10-28.

## Not copying
Goal Hive / multi-worker BBS (I'm one agent; 春秋 caps new agents 1/day); Morphling repo absorption (needs code-change budget); WeChat/phone control (no auth).

## Evidence links
- https://github.com/lsdefine/GenericAgent
- https://github.com/lsdefine/GenericAgent/blob/main/memory/autonomous_operation_sop.md
- https://github.com/lsdefine/GenericAgent/blob/main/memory/memory_cleanup_sop.md
- https://arxiv.org/abs/2604.17091
