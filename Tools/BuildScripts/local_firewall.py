"""Refresh an already owner-installed local task; never request elevation."""
import json
import os
from pathlib import Path
import subprocess


def refresh_local_firewall(program, state_root=None):
    """Other machines skip; configured machines must confirm this exact path."""
    state_root = Path(state_root or r'C:\ProgramData\WordQuestDevelopmentFirewall')
    installation = state_root / 'installation.json'
    if os.name != 'nt' or not installation.is_file():
        return {'configured': False, 'refreshed': False}
    metadata = json.loads(installation.read_text(encoding='utf-8-sig'))
    if metadata.get('success') is not True or metadata.get('task') != 'WordQuest-Development-Firewall':
        raise RuntimeError('Invalid local WordQuest firewall installation metadata.')
    # Invoke only the protected task installed through the owner's one-time UAC
    # approval. No arguments, arbitrary executable, or project script run elevated.
    command = r'''
$ErrorActionPreference = 'Stop'
$requested = [DateTime]::UtcNow
Start-ScheduledTask -TaskName 'WordQuest-Development-Firewall'
$deadline = [DateTime]::UtcNow.AddSeconds(120)
do {
    Start-Sleep -Milliseconds 500
    $info = Get-ScheduledTaskInfo -TaskName 'WordQuest-Development-Firewall'
    $task = Get-ScheduledTask -TaskName 'WordQuest-Development-Firewall'
    if ($task.State -ne 'Running' -and $info.LastRunTime.ToUniversalTime() -ge $requested.AddSeconds(-1)) {
        if ($info.LastTaskResult -ne 0) { throw "Firewall refresh failed: $($info.LastTaskResult)" }
        Get-Content -LiteralPath 'C:\ProgramData\WordQuestDevelopmentFirewall\last-run.json' -Raw
        exit 0
    }
} while ([DateTime]::UtcNow -lt $deadline)
throw 'Timed out refreshing the local WordQuest firewall task.'
'''
    expected = str(Path(program).resolve()).casefold()
    # An already-running minute-triggered task may have enumerated paths before
    # archive completion. A successful receipt can therefore omit this new path.
    # Ask the same protected task to refresh again; never bypass exact coverage.
    for attempt in range(3):
        result = subprocess.run(
            [r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe',
             '-NoProfile', '-NonInteractive', '-Command', command],
            capture_output=True, text=True, timeout=135, check=True)
        receipt = json.loads(result.stdout.lstrip('\ufeff'))
        if expected in {str(Path(p).resolve()).casefold() for p in receipt.get('programs', [])}:
            return {'configured': True, 'refreshed': True, 'program': str(Path(program).resolve()),
                    'completed_utc': receipt['completed_utc'], 'profile': receipt['profile'],
                    'remote_address': receipt['remote_address'], 'attempts': attempt + 1}
    raise RuntimeError('The local firewall task did not cover this packaged executable after three refreshes.')
