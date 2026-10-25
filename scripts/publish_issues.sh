#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
command -v gh >/dev/null 2>&1 || { echo >&2 'Install GitHub CLI (gh) first.'; exit 1; }
gh auth status >/dev/null
cd "$ROOT"
REPO="$(gh repo view --json nameWithOwner --jq .nameWithOwner)"
if [[ -z "$REPO" ]]; then echo >&2 'Run gh repo create first.'; exit 1; fi
# A simple duplicate guard; intended for a new repo with a small issue backlog.
mapfile -t EXISTING < <(gh issue list --repo "$REPO" --state all --limit 200 --json title --jq '.[].title')
for file in issues/*.md; do
  title="$(head -n 1 "$file" | sed -E 's/^# //')"
  if printf '%s\n' "${EXISTING[@]}" | grep -Fxq "$title"; then
    printf 'SKIP %s\n' "$title"
  else
    gh issue create --repo "$REPO" --title "$title" --body-file "$file"
    printf 'CREATED %s\n' "$title"
  fi
done
