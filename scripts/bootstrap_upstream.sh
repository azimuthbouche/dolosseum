#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
if [[ ! -d "$ROOT/upstream/.git" ]]; then
  git clone --branch paper-v0.1.1 --recurse-submodules \
    https://github.com/umass-ai-safety/colosseum.git "$ROOT/upstream"
fi
# Verify the paper tag rather than silently using an arbitrary existing checkout.
CURRENT="$(git -C "$ROOT/upstream" rev-parse HEAD)"
EXPECTED="$(git -C "$ROOT/upstream" rev-list -n 1 paper-v0.1.1)"
[[ "$CURRENT" == "$EXPECTED" ]] || { echo >&2 "upstream/ isn't at paper-v0.1.1. Restore/tag a separate checkout."; exit 1; }
git -C "$ROOT/upstream" submodule update --init --recursive
# The paper tag may not vendor CoLLAB as a submodule; keep a separate ignored checkout.
if [[ ! -d "$ROOT/vendor/CoLLAB/.git" ]]; then
  mkdir -p "$ROOT/vendor"
  git clone https://github.com/Saad-Mahmud/CoLLAB_SEA.git "$ROOT/vendor/CoLLAB"
fi
if ! command -v uv >/dev/null 2>&1; then
  echo >&2 "Install uv (https://docs.astral.sh/uv/) and rerun."; exit 1
fi
(
  cd "$ROOT/upstream"
  uv venv --python 3.11 .venv
  uv sync --no-install-project
  if [[ ! -e .env ]]; then cp .env.example .env; fi
)
printf 'Pinned Colosseum: %s\n' "$CURRENT"
printf 'CoLLAB: %s\n' "$(git -C "$ROOT/vendor/CoLLAB" rev-parse HEAD)"
echo 'Now set API credentials in upstream/.env, then run scripts/run_smoke.sh.'
