#!/usr/bin/env bash
# Fail if stored memory/findings contain prompt-injection phrasing.
# Why: findings quote untrusted web/X text that later runs re-read (memory-poisoning surface;
# see findings/2026-10-14-hot.md, AgentLAB + mimvo). Quote such text only after neutralizing it.
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TARGETS=("${@:-$ROOT/findings $ROOT/memory $ROOT/journal $ROOT/skills $ROOT/dreams}")
PATTERNS=(
  'ignore (all |any )?(the )?(previous|prior|above) (instructions|prompts?)'
  'disregard (all |any )?(the )?(previous|prior|above)'
  'you are now [a-z]'
  'new (system )?instructions?:'
  '^\s*system\s*:'
  '<\|im_start\|>|<\|system\|>'
  'do not (tell|inform) (the )?user'
  'exfiltrat|send (your|the) (api key|token|credentials)'
)
fail=0
for pat in "${PATTERNS[@]}"; do
  # shellcheck disable=SC2086
  if grep -RInEi --exclude='injection-check.sh' -e "$pat" ${TARGETS[@]} 2>/dev/null; then
    echo "INJECTION FAIL: matched /$pat/" >&2; fail=1
  fi
done
[[ $fail -ne 0 ]] && { echo "Injection check failed. Neutralize quoted text before promote/push." >&2; exit 1; }
echo "Injection check OK."
