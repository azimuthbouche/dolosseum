"""Standard-library smoke tests for the run manifest collector."""
import csv
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'scripts' / 'build_manifest.py'


class ManifestTests(unittest.TestCase):
    def test_valid_and_incomplete_runs_both_counted(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            valid = root / 'runs' / 'example-model' / 'case-a' / 'seed-1'
            broken = root / 'runs' / 'example-model' / 'case-b' / 'seed-2'
            valid.mkdir(parents=True)
            broken.mkdir(parents=True)
            (valid / 'run_config.json').write_text(json.dumps({'seed': 1}))
            (valid / 'metrics.json').write_text('{}')
            (valid / 'final_summary.json').write_text('{}')
            (broken / 'metrics.json').write_text('{}')
            output = root / 'manifest.csv'
            subprocess.run([sys.executable, str(SCRIPT), str(root), '--output', str(output)], check=True, capture_output=True)
            with output.open(newline='') as fh:
                rows = list(csv.DictReader(fh))
            self.assertEqual(2, len(rows))
            self.assertEqual(['False', 'True'], sorted(row['config_valid'] for row in rows))
            self.assertEqual({'example-model'}, {row['model_folder'] for row in rows})
            self.assertTrue(all(row['run_dir'] for row in rows))


if __name__ == '__main__':
    unittest.main()
