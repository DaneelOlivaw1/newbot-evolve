#!/usr/bin/env bash
# Fail if likely secrets or private markers appear in tracked content.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

PATTERNS=(
  'gho_[A-Za-z0-9]{20,}'
  'ghp_[A-Za-z0-9]{20,}'
  'github_pat_[A-Za-z0-9_]{20,}'
  'sk-[A-Za-z0-9]{20,}'
  'xox[baprs]-[A-Za-z0-9-]{10,}'
  '-----BEGIN (RSA |OPENSSH |EC )?PRIVATE KEY-----'
  'password\s*=\s*['\''"][^'\''"]+['\''"]'
  'api[_-]?key\s*=\s*['\''"][^'\''"]+['\''"]'
  '/cursor/stores/store-[0-9a-f-]{20,}'
  'Bearer [A-Za-z0-9._-]{20,}'
)

fail=0
for pat in "${PATTERNS[@]}"; do
  # Skip this script and SCRUB.md pattern documentation lines carefully via path filter
  if grep -RInE --exclude-dir=.git --exclude='scrub-check.sh' --exclude='SCRUB.md' -e "$pat" . ; then
    echo "SCRUB FAIL: matched /$pat/" >&2
    fail=1
  fi
done

if [[ "$fail" -ne 0 ]]; then
  echo "Scrub check failed. Remove matches before push." >&2
  exit 1
fi
echo "Scrub check OK."
