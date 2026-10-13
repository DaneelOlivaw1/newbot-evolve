#!/usr/bin/env python3
"""Quiet-hours dream-pass: review candidate learnings, log promote|hold|noop.

Never auto-promotes. Promotion requires an explicit --log promote decision
that cites evidence beyond success count (SkillPoison / Devin dreaming).

Usage:
  dream-pass.py --list [--learnings PATH]
  dream-pass.py --log DECISION --title TITLE --reason TEXT [--evidence TEXT]
  dream-pass.py --apply   # flip status to active only for unused promote logs
  dream-pass.py --regen   # rebuild active_learnings.md from status=active

DECISION is one of: promote | hold | noop
"""
from __future__ import annotations

import argparse
import json
import pathlib
import sys
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parent.parent
DEFAULT_LEARNINGS = ROOT / "memory" / "learnings.jsonl"
DEFAULT_LOG = ROOT / "dreams" / "dream_log.jsonl"
DEFAULT_ACTIVE = ROOT / "memory" / "active_learnings.md"
DECISIONS = {"promote", "hold", "noop"}


def load_learnings(path: pathlib.Path) -> list[dict]:
    rows = []
    if not path.exists():
        return rows
    for n, line in enumerate(path.read_text().splitlines(), 1):
        if not line.strip():
            continue
        r = json.loads(line)
        r["_line"] = n
        rows.append(r)
    return rows


def load_log(path: pathlib.Path) -> list[dict]:
    if not path.exists():
        return []
    out = []
    for line in path.read_text().splitlines():
        if line.strip():
            out.append(json.loads(line))
    return out


def append_jsonl(path: pathlib.Path, obj: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a") as f:
        f.write(json.dumps(obj, ensure_ascii=False) + "\n")


def cmd_list(learnings: pathlib.Path) -> int:
    rows = load_learnings(learnings)
    cands = [r for r in rows if r.get("status") == "candidate"]
    print(f"{len(cands)} candidate(s) of {len(rows)} total\n")
    for r in cands:
        print(f"[{r['_line']}] {r.get('title')}")
        print(f"    source={r.get('source')} evidence={r.get('evidence')}")
        print(f"    applies_when={r.get('applies_when')}")
        print(f"    not_when={r.get('not_when')}")
        print(f"    takeaway={r.get('takeaway')}")
        print()
    return 0


def cmd_log(args: argparse.Namespace) -> int:
    if args.decision not in DECISIONS:
        print(f"decision must be one of {sorted(DECISIONS)}", file=sys.stderr)
        return 2
    if args.decision == "promote" and not (args.evidence or "").strip():
        print("promote requires --evidence (not success count alone)", file=sys.stderr)
        return 2
    rows = load_learnings(args.learnings)
    match = next((r for r in rows if r.get("title") == args.title), None)
    if match is None:
        print(f"no learning titled: {args.title}", file=sys.stderr)
        return 1
    if args.decision == "promote":
        for k in ("applies_when", "not_when", "evidence"):
            if not str(match.get(k, "")).strip():
                print(f"cannot promote: learning missing {k}", file=sys.stderr)
                return 1
        if match.get("status") != "candidate":
            print(f"cannot promote: status is {match.get('status')}", file=sys.stderr)
            return 1
    entry = {
        "type": "review",
        "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ"),
        "decision": args.decision,
        "title": args.title,
        "reason": args.reason,
        "evidence": (args.evidence or "").strip() or None,
        "applied": False,
    }
    append_jsonl(args.log, entry)
    print(f"logged {args.decision}: {args.title}")
    return 0


def cmd_apply(args: argparse.Namespace) -> int:
    rows = load_learnings(args.learnings)
    by_title = {r.get("title"): r for r in rows}
    log = load_log(args.log)
    changed = 0
    for entry in log:
        if entry.get("decision") != "promote" or entry.get("applied"):
            continue
        title = entry.get("title")
        r = by_title.get(title)
        if r is None:
            print(f"skip missing learning: {title}")
            continue
        if r.get("status") != "candidate":
            entry["applied"] = True
            entry["apply_note"] = f"already {r.get('status')}"
            continue
        if not entry.get("evidence"):
            print(f"skip promote without evidence: {title}")
            continue
        for k in ("applies_when", "not_when", "evidence"):
            if not str(r.get(k, "")).strip():
                print(f"skip promote missing {k}: {title}")
                break
        else:
            r["status"] = "active"
            r["promoted_at"] = entry.get("ts")
            r["promote_evidence"] = entry.get("evidence")
            entry["applied"] = True
            changed += 1
            print(f"promoted: {title}")
    # rewrite learnings (drop helper keys)
    with args.learnings.open("w") as f:
        for r in rows:
            r.pop("_line", None)
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    # rewrite log with applied flags
    with args.log.open("w") as f:
        for entry in log:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    regen_active(args.learnings, args.active)
    print(f"apply done; {changed} promoted")
    return 0


def regen_active(learnings: pathlib.Path, active: pathlib.Path) -> None:
    rows = [r for r in load_learnings(learnings) if r.get("status") == "active"]
    lines = [
        "# Active Learnings (regenerated from learnings.jsonl; promote only with evidence)",
        "",
    ]
    if not rows:
        lines.append("_None promoted yet._")
        lines.append("")
    else:
        for r in rows:
            lines.append(f"## {r.get('title')}")
            lines.append(f"- **when:** {r.get('applies_when')}")
            lines.append(f"- **not when:** {r.get('not_when')}")
            lines.append(f"- **takeaway:** {r.get('takeaway')}")
            lines.append(f"- **evidence:** {r.get('evidence')}")
            if r.get("promote_evidence"):
                lines.append(f"- **promoted on:** {r.get('promoted_at')} — {r.get('promote_evidence')}")
            lines.append("")
    active.write_text("\n".join(lines))
    print(f"wrote {active} ({len(rows)} active)")


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--learnings", type=pathlib.Path, default=DEFAULT_LEARNINGS)
    p.add_argument("--log", type=pathlib.Path, default=DEFAULT_LOG)
    p.add_argument("--active", type=pathlib.Path, default=DEFAULT_ACTIVE)
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--list", action="store_true")
    g.add_argument("--log-decision", dest="decision", choices=sorted(DECISIONS))
    g.add_argument("--apply", action="store_true")
    g.add_argument("--regen", action="store_true")
    p.add_argument("--title")
    p.add_argument("--reason", default="")
    p.add_argument("--evidence", default="")
    args = p.parse_args()
    if args.list:
        return cmd_list(args.learnings)
    if args.decision:
        if not args.title or not args.reason:
            print("--log-decision needs --title and --reason", file=sys.stderr)
            return 2
        return cmd_log(args)
    if args.apply:
        return cmd_apply(args)
    if args.regen:
        regen_active(args.learnings, args.active)
        return 0
    return 2


if __name__ == "__main__":
    sys.exit(main())
