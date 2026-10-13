#!/usr/bin/env bash
# Pre-sync gate chain for newbot-evolve. Order matters:
#   1) anchor-test — prove gates still reject known-bad (Double Ratchet)
#   2) check-learnings — schema
#   3) scrub-check — secrets / private paths
#   4) injection-check — quoted outside text that looks like instructions
# Any non-zero exit blocks push. Run from repo root: ./scripts/pre-sync.sh
set -euo pipefail
DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$DIR/.." && pwd)"
cd "$ROOT"

echo "== 1/4 anchor-test =="
bash "$DIR/anchor-test.sh"

echo "== 2/4 check-learnings =="
python3 "$DIR/check-learnings.py" "$ROOT/memory/learnings.jsonl"

echo "== 3/4 scrub-check =="
bash "$DIR/scrub-check.sh" "$ROOT"

echo "== 4/4 injection-check =="
bash "$DIR/injection-check.sh" "$ROOT"

echo "Pre-sync OK: all gates green. Safe to commit/push (after manual review of diff)."
