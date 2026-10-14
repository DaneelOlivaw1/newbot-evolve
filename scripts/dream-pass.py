#!/usr/bin/env python3
"""Quiet-hours dream-pass: review candidate learnings, log promote|hold|noop|retire|revise.

Never auto-promotes. Promotion requires an explicit --log promote decision
that cites evidence beyond success count (SkillPoison / Devin dreaming).

Usage:
  dream-pass.py --list [--stale-days N] [--learnings PATH]
  dream-pass.py --log-decision DECISION --title TITLE --reason TEXT [--evidence TEXT]
  dream-pass.py --log-decision revise --title TITLE --reason TEXT --evidence TEXT \
      --replay TEXT [--takeaway T] [--applies-when A] [--not-when N]
  dream-pass.py --apply   # apply unused promote/retire/revise logs
  dream-pass.py --regen   # rebuild active_learnings.md from status=active

DECISION is one of: promote | hold | noop | retire | revise

Retire (yoyo-evolve 71922db lesson, 2026-10-14): schema allowed status=retired
but nothing could ever set it, so the active set could only grow. retire needs
--evidence and an active learning; it is reversible (flip status back to
candidate and re-promote). --list also shows active learnings whose last use
(last_applied, else promoted_at) is >= --stale-days old as retire-review items.
Silence only counts when it is measured: a learning with no last_applied field
is never retired for silence alone; cite a contradiction or supersession.

Revise (Skill-V arXiv 2610.11781 non-regression, 2026-10-14): change an ACTIVE
learning in place instead of adding a sibling. Needs --evidence (why revise),
at least one of --takeaway/--applies-when/--not-when, and --replay: text that
re-affirms the prior evidence still holds. Mechanically --replay must contain a
contiguous >=20-char slice of the learning's promote_evidence (else evidence),
or the whole prior string if it is shorter than 20 chars. No prior evidence to
replay -> refused. --apply overwrites only the given fields, appends
{ts, evidence, replay, changes} to revision_history, sets revised_at, keeps
status=active.
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
DECISIONS = {"promote", "hold", "noop", "retire", "revise"}
REVISE_FIELDS = ("takeaway", "applies_when", "not_when")
REPLAY_MIN = 20


def prior_evidence(r: dict) -> str:
    return str(r.get("promote_evidence") or r.get("evidence") or "").strip()


def replay_ok(prior: str, replay: str) -> bool:
    """Skill-V non-regression: replay must quote the prior evidence it reaffirms."""
    if not prior or not replay:
        return False
    if len(prior) < REPLAY_MIN:
        return prior in replay
    return any(prior[i:i + REPLAY_MIN] in replay for i in range(len(prior) - REPLAY_MIN + 1))


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


def _age_days(ts: str | None) -> float | None:
    if not ts:
        return None
    for fmt in ("%Y-%m-%dT%H:%MZ", "%Y-%m-%dT%H:%M:%SZ"):
        try:
            t = datetime.strptime(ts, fmt).replace(tzinfo=timezone.utc)
            return (datetime.now(timezone.utc) - t).total_seconds() / 86400
        except ValueError:
            continue
    return None


def cmd_list(learnings: pathlib.Path, stale_days: float = 30) -> int:
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
    stale = []
    for r in rows:
        if r.get("status") != "active":
            continue
        measured = bool(r.get("last_applied"))
        age = _age_days(r.get("last_applied") or r.get("promoted_at"))
        if age is not None and age >= stale_days:
            stale.append((age, measured, r))
    print(f"{len(stale)} active learning(s) idle >= {stale_days:g} days (retire-review)")
    for age, measured, r in sorted(stale, key=lambda x: -x[0]):
        tag = "measured" if measured else "UNMEASURED: do not retire for silence"
        print(f"[{r['_line']}] {r.get('title')}  ({age:.0f}d, {tag})")
    return 0


def cmd_log(args: argparse.Namespace) -> int:
    if args.decision not in DECISIONS:
        print(f"decision must be one of {sorted(DECISIONS)}", file=sys.stderr)
        return 2
    if args.decision in ("promote", "retire", "revise") and not (args.evidence or "").strip():
        print(f"{args.decision} requires --evidence (not success count or silence alone)", file=sys.stderr)
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
    if args.decision == "retire" and match.get("status") != "active":
        print(f"cannot retire: status is {match.get('status')}", file=sys.stderr)
        return 1
    new_fields = {}
    if args.decision == "revise":
        replay = (args.replay or "").strip()
        if not replay:
            print("revise requires --replay (re-affirm the prior evidence still holds)", file=sys.stderr)
            return 2
        if match.get("status") != "active":
            print(f"cannot revise: status is {match.get('status')}", file=sys.stderr)
            return 1
        prior = prior_evidence(match)
        if not prior:
            print("cannot revise: no prior evidence to replay", file=sys.stderr)
            return 1
        if not replay_ok(prior, replay):
            print(f"cannot revise: --replay does not overlap prior evidence "
                  f"(need a {REPLAY_MIN}+ char slice of it)", file=sys.stderr)
            return 1
        for k in REVISE_FIELDS:
            v = (getattr(args, k) or "").strip()
            if v:
                new_fields[k] = v
        if not new_fields:
            print("cannot revise: nothing to revise (give --takeaway/--applies-when/--not-when)",
                  file=sys.stderr)
            return 2
    entry = {
        "type": "review",
        "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ"),
        "decision": args.decision,
        "title": args.title,
        "reason": args.reason,
        "evidence": (args.evidence or "").strip() or None,
        "applied": False,
    }
    if args.decision == "revise":
        entry["replay"] = args.replay.strip()
        entry.update(new_fields)
    append_jsonl(args.log, entry)
    print(f"logged {args.decision}: {args.title}")
    return 0


def cmd_apply(args: argparse.Namespace) -> int:
    rows = load_learnings(args.learnings)
    by_title = {r.get("title"): r for r in rows}
    log = load_log(args.log)
    changed = 0
    for entry in log:
        if entry.get("decision") == "retire" and not entry.get("applied"):
            r = by_title.get(entry.get("title"))
            if r is not None and r.get("status") == "active" and entry.get("evidence"):
                r["status"] = "retired"
                r["retired_at"] = entry.get("ts")
                r["retire_evidence"] = entry.get("evidence")
                entry["applied"] = True
                changed += 1
                print(f"retired: {entry.get('title')}")
            continue
        if entry.get("decision") == "revise" and not entry.get("applied"):
            r = by_title.get(entry.get("title"))
            fields = {k: entry[k] for k in REVISE_FIELDS if str(entry.get(k) or "").strip()}
            if (r is None or r.get("status") != "active" or not entry.get("evidence")
                    or not fields or not replay_ok(prior_evidence(r), entry.get("replay") or "")):
                print(f"skip revise (not active / no evidence / replay mismatch): {entry.get('title')}")
                continue
            changes = {k: {"from": r.get(k), "to": v} for k, v in fields.items() if r.get(k) != v}
            r.update(fields)
            r.setdefault("revision_history", []).append({
                "ts": entry.get("ts"),
                "evidence": entry.get("evidence"),
                "replay": entry.get("replay"),
                "changes": changes,
            })
            r["revised_at"] = entry.get("ts")
            entry["applied"] = True
            changed += 1
            print(f"revised: {entry.get('title')} ({', '.join(fields)})")
            continue
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
    print(f"apply done; {changed} changed")
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
            if r.get("revised_at"):
                n = len(r.get("revision_history") or [])
                lines.append(f"- **revised:** {r.get('revised_at')} ({n} revision(s), prior evidence replayed)")
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
    p.add_argument("--replay", default="", help="revise: quote of prior evidence that still holds")
    p.add_argument("--takeaway", default="")
    p.add_argument("--applies-when", dest="applies_when", default="")
    p.add_argument("--not-when", dest="not_when", default="")
    p.add_argument("--stale-days", type=float, default=30)
    args = p.parse_args()
    if args.list:
        return cmd_list(args.learnings, args.stale_days)
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
