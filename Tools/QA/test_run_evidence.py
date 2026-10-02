"""Exercise persisted QA verdicts after plausible late native failures."""
import contextlib
import io
import json
from pathlib import Path
import struct
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from Tools.QA import run_g_proof


class RunEvidenceTests(unittest.TestCase):
    def run_fixture(self, mode, exit_code=0, timeout=False, report=None):
        with tempfile.TemporaryDirectory(prefix='wordquest-evidence-') as directory:
            root = Path(directory)
            script = root / 'Tools/QA/run_g_proof.py'

            def native_run(command, **kwargs):
                log = Path(next(arg.removeprefix('-AbsLog=') for arg in command if arg.startswith('-AbsLog=')))
                log.write_text('WQ_STATE proof=initial selected=-1 submitted=0 correct=0 hint=0 paused=0 evaluations=0\n', encoding='utf-8')
                if mode == 'capture':
                    # Only the header is consumed by the runner; this is a test
                    # fixture, not a screenshot or native visual evidence.
                    (log.parent / 'native.png').write_bytes(b'\x89PNG\r\n\x1a\n' + b'\0' * 8 + struct.pack('>II', 884, 1780))
                else:
                    (log.parent / 'Report').mkdir()
                    data = report if report is not None else {'succeeded': 2, 'failed': 0, 'notRun': 0, 'inProcess': 0}
                    (log.parent / 'Report/index.json').write_text(json.dumps(data), encoding='utf-8')
                if timeout:
                    raise subprocess.TimeoutExpired(command, 600)
                return subprocess.CompletedProcess(command, exit_code)

            with patch.object(run_g_proof, '__file__', str(script)), \
                    patch.object(sys, 'argv', ['run_g_proof.py', mode]), \
                    patch.object(run_g_proof.subprocess, 'check_output', side_effect=['fixture-head\n', '']), \
                    patch.object(run_g_proof.subprocess, 'run', side_effect=native_run), \
                    contextlib.redirect_stdout(io.StringIO()):
                status = run_g_proof.main()
            paths = list((root / 'Artifacts/QA/UI01').glob('*/run.json'))
            self.assertEqual(len(paths), 1)
            return status, json.loads(paths[0].read_text(encoding='utf-8'))

    def test_successful_completed_runs(self):
        for mode in ('capture', 'automation'):
            with self.subTest(mode=mode):
                status, verdict = self.run_fixture(mode)
                self.assertEqual(status, 0)
                self.assertTrue(verdict['evidence_complete'])

    def test_late_nonzero_exit_rejects_existing_capture_or_report(self):
        for mode in ('capture', 'automation'):
            with self.subTest(mode=mode):
                status, verdict = self.run_fixture(mode, exit_code=3)
                self.assertEqual(status, 1)
                self.assertEqual(verdict['exit_code'], 3)
                self.assertFalse(verdict['evidence_complete'])

    def test_timeout_rejects_existing_capture_or_report(self):
        for mode in ('capture', 'automation'):
            with self.subTest(mode=mode):
                status, verdict = self.run_fixture(mode, timeout=True)
                self.assertEqual(status, 1)
                self.assertEqual(verdict['exit_code'], -1)
                self.assertIn('600 seconds', verdict['error'])
                self.assertFalse(verdict['evidence_complete'])

    def test_unfinished_or_missing_automation_counts_reject_report(self):
        complete = {'succeeded': 2, 'failed': 0, 'notRun': 0, 'inProcess': 0}
        for field in ('notRun', 'inProcess'):
            for value in (1, None):
                with self.subTest(field=field, value=value):
                    report = dict(complete)
                    if value is None:
                        del report[field]
                    else:
                        report[field] = value
                    status, verdict = self.run_fixture('automation', report=report)
                    self.assertEqual(status, 1)
                    self.assertFalse(verdict['evidence_complete'])


if __name__ == '__main__':
    unittest.main()
