#!/usr/bin/env python3
"""Validate memory/learnings.jsonl. Exit non-zero on any violation.

Rules (from SkillPoison finding, 2026-10-13): every learning must state
where it applies and where it does not, so repeated success can't silently
over-generalize a rule. 'active' entries additionally need evidence.
"""
import json, sys, pathlib
path = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else
                    pathlib.Path(__file__).resolve().parent.parent / "memory/learnings.jsonl")
REQ = ["type", "day", "ts", "source", "title", "evidence", "status",
       "applies_when", "not_when", "takeaway"]
STATUS = {"candidate", "active", "retired"}
bad = 0
for n, line in enumerate(path.read_text().splitlines(), 1):
    if not line.strip():
        continue
    try:
        r = json.loads(line)
    except json.JSONDecodeError as e:
        print(f"line {n}: invalid JSON ({e})"); bad += 1; continue
    missing = [k for k in REQ if not str(r.get(k, "")).strip()]
    if missing:
        print(f"line {n} [{r.get('title','?')}]: missing {missing}"); bad += 1
    if r.get("status") not in STATUS:
        print(f"line {n}: status must be one of {sorted(STATUS)}"); bad += 1
print("learnings OK" if not bad else f"{bad} problem(s)")
sys.exit(1 if bad else 0)
