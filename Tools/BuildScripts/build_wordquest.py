"""Build with the recorded engine and retain its output; never install tools."""
import argparse
from datetime import datetime
import json
from pathlib import Path
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--engine-root', type=Path, default=Path(r'C:\Program Files\Epic Games\UE_5.8'))
    parser.add_argument('--target', choices=('Editor', 'Game'), default='Editor')
    args = parser.parse_args()
    repository = Path(__file__).resolve().parents[2]
    version = json.loads((args.engine_root / 'Engine/Build/Build.version').read_text())
    if tuple(version[k] for k in ('MajorVersion', 'MinorVersion', 'PatchVersion', 'Changelist')) != (5, 8, 2, 56702186):
        parser.error('Expected UE 5.8.2 CL 56702186; reconcile TOOLCHAIN-LOCK.md first.')
    project = repository / 'Game/WordQuest.uproject'
    if not project.is_file():
        parser.error(f'Missing generated Unreal project: {project}')
    target = 'WordQuestEditor' if args.target == 'Editor' else 'WordQuest'
    logs = repository / 'Artifacts/Logs/Build'
    logs.mkdir(parents=True, exist_ok=True)
    log = logs / f'{target}-{datetime.now():%Y%m%d-%H%M%S}.log'
    command = [str(args.engine_root / 'Engine/Build/BatchFiles/Build.bat'), target,
               'Win64', 'Development', f'-Project={project}', '-WaitMutex',
               '-NoHotReloadFromIDE', '-NoUBA', '-MaxParallelActions=2']
    print(f'Building {target} with UE 5.8.2 CL 56702186. Log: {log}', flush=True)
    with log.open('w', encoding='utf-8') as output:
        output.write(subprocess.list2cmdline(command) + '\n')
        with subprocess.Popen(command, cwd=repository, stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT, text=True, errors='replace') as process:
            for line in process.stdout:
                print(line, end='', flush=True)
                output.write(line)
                output.flush()
            code = process.wait()
        output.write(f'\nExit code: {code}\n')
    print(f'Build exit code: {code}. This does not imply a runtime or device test.')
    return code


if __name__ == '__main__':
    sys.exit(main())
