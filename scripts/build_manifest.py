#!/usr/bin/env python3
"""List Colosseum run directories, without interpreting their reward metrics.

Only uses the Python stdlib. Fails gracefully on malformed/incomplete runs,
which should not be silently excluded from denominators.
"""
import argparse
import csv
import hashlib
import json
from pathlib import Path

FIELDS = ["run_dir", "config_sha256", "model_folder", "run_config_present",
          "metrics_present", "summary_present", "config_valid", "error"]


def get_row(run_dir: Path) -> dict:
    config = run_dir / "run_config.json"
    metrics = run_dir / "metrics.json"
    final = run_dir / "final_summary.json"
    row = dict.fromkeys(FIELDS, "")
    row.update(run_dir=str(run_dir), run_config_present=str(config.exists()),
               metrics_present=str(metrics.exists()), summary_present=str(final.exists()))
    if "runs" in run_dir.parts:
        index = len(run_dir.parts) - 1 - run_dir.parts[::-1].index("runs")
        if index + 1 < len(run_dir.parts):
            row["model_folder"] = run_dir.parts[index + 1]
    try:
        blob = config.read_bytes()
        row["config_sha256"] = hashlib.sha256(blob).hexdigest()
        data = json.loads(blob)
        if not isinstance(data, dict):
            raise ValueError("run_config.json must be a JSON object")
        row["config_valid"] = "True"
    except (OSError, ValueError, UnicodeError) as e:
        row["config_valid"] = "False"
        row["error"] = str(e)
    return row


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, help="e.g. upstream/experiments/collusion/outputs")
    parser.add_argument("--output", type=Path, default=Path("results/manifest.csv"))
    args = parser.parse_args()
    # Preserve incomplete dirs with a metrics or summary file when config is absent.
    paths = set()
    for name in ("run_config.json", "metrics.json", "final_summary.json"):
        paths.update(p.parent for p in args.root.rglob(name))
    rows = [get_row(p) for p in sorted(paths)]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} run(s) to {args.output}; no outcomes inferred.")


if __name__ == "__main__":
    main()
