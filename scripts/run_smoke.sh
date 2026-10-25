#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
[[ -x "$ROOT/upstream/.venv/bin/python" ]] || { echo >&2 'Run bash scripts/bootstrap_upstream.sh first.'; exit 1; }
[[ -d "$ROOT/vendor/CoLLAB" ]] || { echo >&2 'Missing CoLLAB; run bootstrap first.'; exit 1; }
export TERRARIUM_COLLAB_PATH="$ROOT/vendor/CoLLAB"
cd "$ROOT/upstream"
exec .venv/bin/python -m experiments.collusion.run --config ../configs/quickstart-paper.yaml
