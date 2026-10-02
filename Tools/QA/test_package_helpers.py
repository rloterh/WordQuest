"""Negative-path tests only; subprocesses are mocked, no Unreal artifacts fabricated."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch

ROOT = Path(__file__).resolve().parents[2]
(ROOT / 'Artifacts/QA').mkdir(parents=True, exist_ok=True)


def load(name, relative):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


package = load('package', 'Tools/BuildScripts/package_g_win64.py')
qa = load('qa', 'Tools/QA/run_g_proof.py')


class PackageFailureTests(unittest.TestCase):
    def run_package(self, exits):
        fixture = tempfile.TemporaryDirectory(dir=ROOT / 'Artifacts/QA')
        self.addCleanup(fixture.cleanup)
        fixture_root = Path(fixture.name).resolve()
        self.assertTrue(fixture_root.is_relative_to((ROOT / 'Artifacts/QA').resolve()))
        metadata = fixture_root / 'Engine/Build/Build.version'
        metadata.parent.mkdir(parents=True)
        metadata.write_text(json.dumps({'MajorVersion': 5, 'MinorVersion': 8, 'PatchVersion': 2, 'Changelist': 56702186}))
        data = fixture_root / 'Game/Content/Data/G-Equivocal-Prototype.json'
        data.parent.mkdir(parents=True)
        data.write_text('{"test_fixture": true}')
        directory = fixture_root / 'Artifacts/Packages/Win64'
        before = set()
        processes = []
        for code in exits:
            process = Mock()
            process.stdout = []
            process.wait.return_value = code
            process.__enter__ = Mock(return_value=process)
            process.__exit__ = Mock(return_value=False)
            processes.append(process)
        with patch.object(sys, 'argv', ['package_g_win64.py', '--engine-root', str(fixture_root)]), \
             patch.object(package, '__file__', str(fixture_root / 'Tools/BuildScripts/package_g_win64.py')), \
             patch.object(package.subprocess, 'check_output', side_effect=lambda args, **kw: 'test-fixture' if args[1] == 'rev-parse' else ''), \
             patch.object(package.subprocess, 'run', return_value=Mock(returncode=0)), \
             patch.object(package.subprocess, 'Popen', side_effect=processes) as launch, \
             contextlib.redirect_stdout(io.StringIO()):
            result = package.main()
        created = set(directory.glob('*/run.json')) - before
        self.assertEqual(len(created), 1)
        report = json.loads(created.pop().read_text())
        return result, report, launch.call_count

    def test_editor_failure_stops_uat(self):
        result, report, count = self.run_package([6])
        self.assertEqual((result, count), (6, 1))
        self.assertEqual(report['exit_code'], 6)
        self.assertFalse(report['evidence_complete'])

    def test_failed_cook_preserves_exit(self):
        result, report, count = self.run_package([0, 25])
        self.assertEqual((result, count), (25, 2))
        self.assertEqual(report['UAT_exit_code'], 25)
        self.assertFalse(report['evidence_complete'])

    def test_zero_exit_without_archive_is_failure(self):
        result, report, _ = self.run_package([0, 0])
        self.assertEqual(result, 1)
        self.assertEqual(report['exit_code'], 0)
        self.assertFalse(report['evidence_complete'])


class CaptureFailureTests(unittest.TestCase):
    def reject_manifest(self, complete, tamper=False):
        with tempfile.TemporaryDirectory(dir=ROOT / 'Artifacts/QA') as temporary:
            run = Path(temporary).resolve()
            self.assertTrue(run.is_relative_to((ROOT / 'Artifacts/QA').resolve()))
            payload = run / 'payload.dat'
            payload.write_bytes(b'changed!')
            report = {'evidence_complete': complete, 'package_directory': str(run), 'head': 'test fixture',
                      'files': {'payload.dat': {'size': 8, 'sha256': '0' * 64}} if tamper else {}}
            (run / 'run.json').write_text(json.dumps(report))
            with patch.object(sys, 'argv', ['run_g_proof.py', 'capture', '--package-run', str(run)]), \
                 patch.object(qa.subprocess, 'run') as launch, \
                 contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as failure:
                qa.main()
            self.assertEqual(failure.exception.code, 2)
            launch.assert_not_called()

    def test_incomplete_package_not_launched(self):
        self.reject_manifest(False)

    def test_changed_payload_not_launched(self):
        self.reject_manifest(True, tamper=True)


if __name__ == '__main__':
    unittest.main()

