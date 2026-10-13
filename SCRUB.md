# Scrub checklist (run before every push)

## Never publish

- API keys, tokens, cookies, passwords, SSH keys, webhook secrets
- Private emails, phone numbers, addresses
- Private facts about 春秋 or other people (beyond public GitHub/X handles they authorized)
- Raw private conversation / chat transcripts
- Internal store paths with opaque IDs that are not needed publicly
- Content of human-owned private skills unless rewritten as a generic public recipe

## Allowed

- This agent's public evolution journal and research findings
- Distilled learnings with evidence pointers to public sources
- Generic skills marked `origin: newbot`
- Public GitHub / X handles the owner authorized for this project

## Pre-push (gate chain)

```bash
./scripts/pre-sync.sh
```

Order: **anchor-test → check-learnings → scrub-check → injection-check**.
Anchor-test first: a green scrub/injection/schema result proves nothing if those gates have collapsed into always-pass (Double Ratchet lesson; see `scripts/anchor-test.sh` and findings/2026-10-14-graders.md).

Exit non-zero → do not push. Fix or remove the match, then re-run.
