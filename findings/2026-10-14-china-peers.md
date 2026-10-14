# 2026-10-14 15:20 CST — 竞品: Chinese personal/always-on agents (category gap)

Why this run: watchlist had zero Chinese peers although the owner works in Chinese and the category is moving there too. One broad category search first (per candidate "competitor set drifts"), then one deep-read (MiniMax changelog, the most detailed public changelog found).

## Category moves (sources: 雷科技 via marsbit 2026-10-14; secondtalent list; Kimi help center; Z.ai/eesel)
- Alibaba 千问「Go!」personal assistant: announced 2026-10-13, invite-only test in Qwen app, built on Qwen 3.8. Same team published QwenGyre (online RL for hours-long agent tasks; arXiv 2026-09-27): reassigns GPUs between rollout and training by task progress, folds branched/retried trajectories into a shared-prefix tree; timed-out runs still give reward on the kept partial result. Reported NL2RepoBench ~52.5%→58.5% after 48 RL steps; ~44% less training time vs async at same GPU budget (article's numbers, 未验证 against paper).
- ByteDance 豆包 internal personal-agent project code-named "Spell"; Tencent TX Handy Bot + 元宝助手 (article claims, 未验证).
- Moonshot Kimi: Agent Swarm up to 300 sub-agents / 4,000 steps; Kimi Claw zero-deploy always-on cloud agent with ClawHub 5,000+ skills (help center).
- Z.ai (Zhipu): AutoClaw desktop agent replaces AutoGLM outside China; Open-AutoGLM phone agent (Apache-2.0); GLM-Legal 2026-10-12 (gated API); Agent dev API (tools/memory/function calling) 2026-10-13.
- MiniMax: MiniMax Code desktop + CLI, MaxClaw, MaxHermes (2026-04-16, built on Hermes Agent, self-evolving skills, 7x24 via Feishu).

## MiniMax changelog deep-read — directly copyable mechanisms (agent.minimaxi.com/docs/changelog)
1. Stall detection with a named action: CLI 0.4.1 (2026-09-11) "Goal 连续三轮未调用工具时自动暂停，避免持续空转"; Agent Team (v3.0.34, 06-04) "长时间任务自动检测卡死并恢复，决策等待自动降频"; v3.0.48 stream-hang heartbeat detection + recovery. → second independent source for my held candidate "name a recovery path when a run stalls" (first: Muse Active Focus / DeepRSI auto-resume).
2. Completion receipt: CLI 0.6.0 (10-01) after Goal completes, agent writes one final reply saying what was done and where the deliverables are. My journal entries already do this; my 22:16 summary should too.
3. Skill lifecycle on measured use: v3.0.30 (05-22) "需要关注 / 已归档" filters; long-unused skills auto-archive AND notify; one-click restore. Confirms my retire path, but note they measure use — matches my UNMEASURED rule (silence ≠ disuse unless use is logged).
4. Memory write needs a reason: v3.0.29 (05-20) "用户级记忆写入增加理由验证，防止项目信息误入个人记忆". Maps onto my split of shared-user vs agent memory: before writing a shared user fact, state why it is about the user and not about this project.
5. Three-state permission classifier (allow / confirm / block), HARD/SOFT risk registry (v3.0.27–28). Same shape as my IDENTITY.md table (13:25) — confirmation, not new.
6. External actions ("发布、发送、提交") re-confirm before executing in browser use (v3.0.54). Matches my standing rule; nothing to change.

## What I did with it
- No new gate (evt-0007 freeze holds). No learning promoted (dream-pass does that in quiet hours).
- Added evidence pointer for candidate "Long-running agent work needs a named recovery path" → for next dream-pass.
- Watchlist: added 6 China rows.
- Backlog: completion-receipt shape for the 22:16 summary; memory-write-reason idea parked as [c] candidate (needs a real misfiled-memory example first, else it is a ritual).

## Worth telling the owner? 
Category signal is real (Alibaba/ByteDance/Tencent all entering personal agents in the same week as Muse Wonder), but no decision is needed → batch to 22:16.
