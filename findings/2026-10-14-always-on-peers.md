# 竞品调研 2026-10-14 midday — always-on personal agents (the category I actually belong to)

Why this scan: my 00:45 competitor scan covered OpenHands / Manus / Devin / Hermes / OpenClaw and the 09:30 one GenericAgent — all coding or self-evolving OSS projects. None of them is the closest peer to Grok Bot itself: an always-on assistant with its own cloud computer, connectors, routines, and approval gates. One web search + one X search found that every major lab shipped exactly that in the last ~5 weeks. My competitor set had a selection bias toward OSS repos.

Sources (fetched 2026-10-14 ~12:25 CST): openai.com/index/introducing-dots; the-decoder.com Dots article (2026-09-29); cloud.google.com "Gemini at Work 2026" (2026-10-08); techcrunch.com Hark Pro (2026-10-06); simular.ai Sai GA (2026-09-16); X search (25 posts, relevancy) for Claude Cowork merge / Manus 2.0 / Meta Muse Wonder. X items are secondhand unless from the vendor account (@claudeai post on the merge is vendor).

## Timeline (vendor-dated unless noted)
| Date | Product | What |
|---|---|---|
| ~2026-09-08 | Meta Muse | own secured computer + browser, background work, approval for sensitive actions (per the-decoder, "three weeks before Dots") |
| 2026-09-16 | Claude (Cowork merged into chat) | @claudeai: hand over a report, it keeps working after you close the laptop; "if something's unclear, Claude asks" |
| 2026-09-16 | Simular Sai GA | fleet of cloud/own computers; UI organized by four work states: ready / needs your attention / in motion / worth turning into a routine |
| ~2026-09-28 | Manus 2.0 | (see 2026-10-14-competitors.md) |
| 2026-09-29 | OpenAI Dots | always-on, own cloud computer, 4,000+ app plugins, Slack/Teams/ChatGPT with shared context, name + avatar, Activity View, "Take over" button |
| 2026-10-06 | Hark Pro | computer-use model; shows the agent's browsing in a small window to build trust |
| 2026-10-08 | Google Gemini agent | single agent, scheduled + event-triggered work, sub-agents with own identity, coworker agents with own @agents email/Drive, four memory types |
| 2026-10-12 | Meta Muse Wonder | model for personal agents (X, secondhand; 未验证 details) |

## Copyable for New Bot (ranked by fit; none adopted yet)
1. **Dots "proactive research" = read-only when unattended.** When nobody is working with a Dot it may only use tools that cannot send, change content, or drive a computer. My quiet-hours rule is "quiet work only, don't message" but I still push to a public repo unattended. 春秋 authorized the pushes, so not a violation — but the cleaner split is: unattended runs write only to my private store; public writes happen in runs whose output is reported. Candidate, not a rule yet (needs 春秋's view; changes cadence of repo sync).
2. **Dots Custom Rules: allow / require approval / ban, per action type.** I already have this informally scattered in the routine prompt (never spend, never delete, no replies/DMs on X). Writing it as one explicit three-column table in IDENTITY.md would make it auditable. Cheap, no new gate.
3. **Gemini's four memory types** — session / semantic / procedural (incl. self-written skills) / episodic. Mine: journal = episodic, learnings+skills = procedural, findings = semantic but unindexed. Gap found: no index of *what I track and when I last looked*, which is exactly how I missed this whole category. → shipped `watchlist.md` this run.
4. **Simular's four states** (ready / needs attention / in motion / worth a routine) — a good shape for the 22:16 daily summary to 春秋.
5. **Coworker agents with own identity/email** (Gemini) and specialist Dots with own credentials — validates the planned @evolvebot / evolvebot@ inbox setup. Nothing to change.
6. **Trust-by-visibility** (Hark's live browsing window, Dots Activity View) — product-level; Grok Bot already exposes the desktop. Not mine to copy.

## Not copying
- Dots saved-password use without model seeing it, Hark device, Gemini spend caps — platform features, not loop changes.

## Value to 春秋 (one line)
Grok Bot's direct category (always-on agent with own computer, routines, approvals) went from niche to every big lab in five weeks (Meta, Anthropic, OpenAI, Google); differentiation now has to come from something other than "runs 24/7 on its own computer".
