# 竞品调研 2026-10-14 (window ≈ 2026-09-14 → 10-14)

Sources: OpenHands GitHub releases; manus.im Manus 2.0 blog; docs.devin.ai release notes (Memory/dreaming Oct 9); NousResearch/hermes-agent + hermes-agent-self-evolution READMEs; X search (relevancy, 25 posts, -$YOYO).

## Snapshot

| Product | What moved (last ~30d) | Stars / note |
|---|---|---|
| **OpenHands** | v1.22→v1.27.1 (Sep 22–Oct 12): Agent Canvas automations (drafts, agent-assisted setup, Git Sync for org admins), MCP health on cloud, ACP agents (OpenCode/Pi), verify-openhands feature-map skill | Active OSS coding agent |
| **Manus 2.0** | Launched ~Sep 28: Cascade harness (lazy specialist tools; vendor claims −23% tokens/−28% time/−32% cost — 未验证独立基准), event-triggered Automations, Cloud Computer, Studio+Video Editor, Cue (agent owns email/phone/wallet/computer) | Closed product |
| **Devin** | Oct 9: personal Memory + nightly "dreaming" (reviews recent sessions, refines memory files); failure-notification backoff; native Jira agent; Fusion/SWE-2; heavy Teams/MCP/Review surface | Closed; Cognition |
| **Hermes-agent** | Self-improving loop (skills from experience, FTS5 recall, Honcho user modeling); `hermes claw migrate` from OpenClaw; companion **hermes-agent-self-evolution** (DSPy+GEPA on SKILL.md; Phase 1 done; PRs only, never direct commit; size caps) | ~253k★ hermes-agent; ~5.5k★ self-evolution (pushed 2026-06, quieter) |
| **OpenClaw** | Treated on X as peer personal assistant next to Hermes/OpenHands; Hermes ships first-class migration. Exact canonical repo stars 未验证 this run (gh search 404 on one query) | OSS personal agent |

Industry frame repeated on X: **Agent = Model + Harness** (paper reading 11 coding agents incl. OpenHands, Hermes, OpenClaw).

## Copyable for New Bot (ranked)

1. **Devin-style nightly dreaming** (highest fit) — Quiet-hours pass that re-reads recent journal entries + learnings.jsonl candidates, then either promotes with evidence, demotes, or logs NO-OP. Maps to yoyo "dream" and my 23:00–08:00 quiet rule. Do NOT auto-promote on success count alone (SkillPoison).
2. **Hermes evolution gates** — Any skill/workflow change: falsifiable `expected`, size/scope caps, human or later-check before treating as active. Already started (check-learnings.py + skills/_journal.md evt-0001); keep PR-style discipline on public repo.
3. **Manus Cascade / Grok Bot subagents** — Already partially true (executor / computerUse / knowledgeWork). Explicit rule: one specialist per task, don't load all tools into one prompt. Document as learning only after a measured token/time comparison (未验证).
4. **Failure backoff for reports** — Devin: notify on 1st, 3rd, 9th consecutive failure. Aligns with "batch minor into 22:16; quiet hours silent." Formalize if auth failures recur on a routine.
5. **Not copying now** — Manus Cue phone/wallet (no auth/spend without owner); OpenHands Canvas UI (different product surface); Hermes GEPA optimizer (needs eval harness + budget — never spend without yes).

## Evidence links
- https://github.com/OpenHands/OpenHands/releases (v1.27.1 2026-10-12)
- https://docs.openhands.dev/openhands/usage/agent-canvas/release-notes/v1.22.0 (MCP health, Git Sync)
- https://manus.im/en/blog/introducing-manus-2-0
- https://docs.devin.ai/release-notes/overview (Memory and dreaming)
- https://github.com/NousResearch/hermes-agent
- https://github.com/NousResearch/hermes-agent-self-evolution
