"""Check optional setup, exact executable coverage and task failure propagation."""
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('local_firewall', ROOT / 'Tools/BuildScripts/local_firewall.py')
firewall = importlib.util.module_from_spec(spec)
spec.loader.exec_module(firewall)


class LocalFirewallTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(dir=ROOT / 'Artifacts/QA')
        self.addCleanup(self.temporary.cleanup)
        self.state = Path(self.temporary.name)
        self.program = self.state / 'WordQuest.exe'

    def configure(self):
        (self.state / 'installation.json').write_text(json.dumps(
            {'success': True, 'task': 'WordQuest-Development-Firewall'}))

    def test_unconfigured_machine_does_not_launch_task(self):
        with patch.object(firewall.subprocess, 'run') as launch:
            result = firewall.refresh_local_firewall(self.program, self.state)
        self.assertFalse(result['configured'])
        launch.assert_not_called()

    @unittest.skipUnless(firewall.os.name == 'nt', 'Windows task integration')
    def test_receipt_for_another_executable_is_rejected(self):
        self.configure()
        receipt = {'programs': [str(self.state / 'Other.exe')]}
        with patch.object(firewall.subprocess, 'run', return_value=subprocess.CompletedProcess([], 0, json.dumps(receipt))), self.assertRaises(RuntimeError):
            firewall.refresh_local_firewall(self.program, self.state)

    @unittest.skipUnless(firewall.os.name == 'nt', 'Windows task integration')
    def test_task_failure_propagates(self):
        self.configure()
        with patch.object(firewall.subprocess, 'run', side_effect=subprocess.CalledProcessError(1, ['powershell'])), self.assertRaises(subprocess.CalledProcessError):
            firewall.refresh_local_firewall(self.program, self.state)


if __name__ == '__main__':
    unittest.main()
