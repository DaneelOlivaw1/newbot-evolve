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

## Pre-push

```bash
./scripts/scrub-check.sh
```

Exit non-zero → do not push. Fix or remove the match, then re-run.
