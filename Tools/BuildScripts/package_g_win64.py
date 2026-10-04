"""Build/cook/archive the bounded G proof locally; never deploy or release."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from local_firewall import refresh_local_firewall


def sha256(path):
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--engine-root', type=Path, default=Path(r'C:\Program Files\Epic Games\UE_5.8'))
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    version = json.loads((args.engine_root / 'Engine/Build/Build.version').read_text())
    if tuple(version[k] for k in ('MajorVersion', 'MinorVersion', 'PatchVersion', 'Changelist')) != (5, 8, 2, 56702186):
        parser.error('Expected UE 5.8.2 CL 56702186; reconcile TOOLCHAIN-LOCK.md first.')

    def git(*arguments):
        return subprocess.check_output(['git', *arguments], cwd=root, text=True).strip()

    head, status = git('rev-parse', 'HEAD'), git('status', '--porcelain')
    if status:
        parser.error('Commit the intended changes before packaging; a clean source revision is required.')
    # Fail before launching UAT if any editable SVG/runtime pair is missing or stale.
    parity = subprocess.run([sys.executable, str(root / 'Tools/AssetImport/stage_g_action_icons.py'), '--check'], cwd=root)
    if parity.returncode:
        return parity.returncode
    run = root / 'Artifacts/Packages/Win64' / datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S-%f')
    run.mkdir(parents=True)
    archive = run / 'Archive'
    command = [str(args.engine_root / 'Engine/Build/BatchFiles/RunUAT.bat'), 'BuildCookRun',
               f'-project={root / "Game/WordQuest.uproject"}', '-noP4', '-unattended',
               '-platform=Win64', '-clientconfig=Development', '-build', '-skipbuildeditor', '-cook',
               '-map=/Game/Maps/GPrototype', '-stage', '-pak', '-iostore', '-archive',
               f'-stagingdirectory={run / "Stage"}', f'-archivedirectory={archive}',
               '-utf8output', '-ubtargs=-NoUBA -NoHotReloadFromIDE -MaxParallelActions=2',
               f'-AdditionalCookerOptions=-ini:Engine:[DevOptions.Shaders]:NumUnusedShaderCompilingThreads={max((os.cpu_count() or 2) - 2, 0)}']
    inputs = [root / 'Game/Content/Data/G-Equivocal-Prototype.json',
              *sorted((root / 'Game/Content/UI/G/Vector').glob('*.svg'))]
    evidence = {'head': head, 'worktree_at_start': status, 'platform': 'Win64',
                'configuration': 'Development', 'command': command,
                'input_sha256': {str(p.relative_to(root)): sha256(p) for p in inputs},
                'evidence_complete': False}
    editor_command = [sys.executable, str(root / 'Tools/BuildScripts/build_wordquest.py'),
                      '--engine-root', str(args.engine_root)]
    evidence['editor_build_command'] = editor_command
    print(f'Local G package: {run}', flush=True)
    try:
        # UAT applies UbtArgs to the client, not its editor target. Build the editor
        # explicitly with the established helper before asking UAT to reuse it.
        for label, build_command in [('EditorBuild', editor_command), ('UAT', command)]:
            with (run / f'{label}.log').open('w', encoding='utf-8') as output:
                output.write(subprocess.list2cmdline(build_command) + '\n')
                with subprocess.Popen(build_command, cwd=root, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                      text=True, encoding='utf-8', errors='replace') as process:
                    for line in process.stdout:
                        print(line, end='', flush=True)
                        output.write(line)
                        output.flush()
                    evidence['exit_code'] = process.wait()
                    evidence[f'{label}_exit_code'] = evidence['exit_code']
            if evidence['exit_code']:
                break
        # UE 5.8.2 archives this single-platform run directly into Archive.
        package = archive
        executable = package / 'WordQuest.exe'
        evidence['package_directory'] = str(package)
        if evidence['exit_code'] == 0 and executable.is_file() and list(package.rglob('*.utoc')) and list(package.rglob('*.pak')):
            evidence['local_firewall'] = refresh_local_firewall(package / 'WordQuest/Binaries/Win64/WordQuest.exe')
            evidence['files'] = {p.relative_to(package).as_posix(): {'size': p.stat().st_size, 'sha256': sha256(p)}
                                 for p in sorted(package.rglob('*')) if p.is_file()}
            evidence['evidence_complete'] = True
    except (OSError, RuntimeError, ValueError, subprocess.SubprocessError) as error:
        evidence['exit_code'] = 1
        evidence['error'] = str(error)
        if isinstance(error, subprocess.CalledProcessError):
            # Captured task stderr explains a failure that str(error) omits.
            # Retain it locally without changing failure or retry behavior.
            evidence['subprocess_exit_code'] = error.returncode
            evidence['subprocess_stdout'] = error.stdout
            evidence['subprocess_stderr'] = error.stderr
    evidence['head_unchanged'] = git('rev-parse', 'HEAD') == head
    evidence['worktree_unchanged'] = git('status', '--porcelain') == status
    evidence['inputs_unchanged'] = all(p.is_file() and sha256(p) == evidence['input_sha256'][str(p.relative_to(root))] for p in inputs)
    evidence['evidence_complete'] &= evidence['head_unchanged'] and evidence['worktree_unchanged'] and evidence['inputs_unchanged']
    (run / 'run.json').write_text(json.dumps(evidence, indent=2) + '\n', encoding='utf-8')
    print(f'Package process exit: {evidence["exit_code"]}; archive evidence complete: {evidence["evidence_complete"]}.')
    print('Packaging is not runtime, offline, mobile, art or release acceptance.')
    return evidence['exit_code'] or (0 if evidence['evidence_complete'] else 1)


if __name__ == '__main__':
    sys.exit(main())
