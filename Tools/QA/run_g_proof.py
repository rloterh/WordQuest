"""Run native Unreal checks and retain raw logs/captures; no device claims."""
import argparse
from datetime import datetime
import hashlib
import json
import re
from pathlib import Path
import struct
import subprocess
import sys


# Expected routed steps: key, state tuple, require handled key-down. Paused
# shortcuts may be unhandled, but must leave selection/hint/evaluation unchanged.
KEYBOARD_STEPS = {
    'keyback': [('Tab', (-1,0,0,0,0,0), True)] * 4,
    'keyskip': [('H', (-1,0,0,1,0,0), True)] + [('Tab', (-1,0,0,1,0,0), True)] * 8,
    'keytab': [('Tab', (-1,0,0,0,0,0), True)] * 11,
    'keymodal': [('P', (-1,0,0,0,1,0), True), ('Tab', (-1,0,0,0,1,0), True),
                 ('SpaceBar', (-1,0,0,0,1,0), True)] + [('Tab', (-1,0,0,0,1,0), True)] * 6,
    'keyretry': [('H', (-1,0,0,1,0,0), True), ('One', (0,0,0,1,0,0), True),
                 ('Enter', (0,1,1,1,0,1), True), ('P', (0,1,1,1,1,1), True),
                 ('Tab', (0,1,1,1,1,1), True), ('SpaceBar', (0,1,1,1,1,1), True),
                 ('Tab', (0,1,1,1,1,1), True), ('SpaceBar', (-1,0,0,0,0,0), True),
                 ('Tab', (-1,0,0,0,0,0), True), ('SpaceBar', (0,0,0,0,0,0), True)],
    'keydisabled': [('One', (0,0,0,0,0,0), True), ('Enter', (0,1,1,0,0,1), True)] +
        [('Tab', (0,1,1,0,0,1), True)] * 3 + [('P', (0,1,1,0,1,1), True), ('SpaceBar', (0,1,1,0,0,1), True)],
    'keyswitch': [('One', (0,0,0,0,0,0), True), ('Three', (2,0,0,0,0,0), True),
                  ('Four', (3,0,0,0,0,0), True), ('Two', (1,0,0,0,0,0), True)],
    'keyempty': [('Enter', (-1,0,0,0,0,0), True)],
    'keysubmit': [('One', (0,0,0,0,0,0), True), ('Enter', (0,1,1,0,0,1), True),
                  ('Enter', (0,1,1,0,0,1), True)],
    'keyhint': [('H', (-1,0,0,1,0,0), True), ('One', (0,0,0,1,0,0), True),
                ('Enter', (0,1,1,1,0,1), True)],
    'keybuttons': [('SpaceBar', (1,0,0,0,0,0), True), ('SpaceBar', (1,1,0,0,0,1), True),
                   ('Enter', (1,1,0,0,0,1), True)],
    'keypaused': [('Two', (1,0,0,0,0,0), True), ('P', (1,0,0,0,1,0), True),
                  ('One', (1,0,0,0,1,0), False), ('H', (1,0,0,0,1,0), False)],
    'keyresumed': [('Two', (1,0,0,0,0,0), True), ('P', (1,0,0,0,1,0), True),
                   ('One', (1,0,0,0,1,0), False), ('H', (1,0,0,0,1,0), False),
                   ('SpaceBar', (1,0,0,0,0,0), True)],
}

# These routes use no programmatic button focus setup. Check the focused semantic
# control, Shift modifier and text setting at every routed transition.
FOCUS_STEPS = {
    'keyback': [('Pause',1,100), ('Answer0',0,100), ('Pause',1,100), ('Submit',1,100)],
    'keyskip': [('Screen',0,100), ('Answer0',0,100), ('Answer1',0,100), ('Answer2',0,100),
                ('Answer3',0,100), ('Submit',0,100), ('Pause',0,100), ('Submit',1,100), ('Answer3',1,100)],
    'keytab': [('Answer0',0,100), ('Answer1',0,100), ('Answer2',0,100), ('Answer3',0,100),
               ('Hint',0,100), ('Submit',0,100), ('Pause',0,100), ('Answer0',0,100),
               ('Pause',1,100), ('Submit',1,100), ('Hint',1,100)],
    'keymodal': [('Resume',0,100), ('TextSize',0,100), ('TextSize',0,200), ('Reset',0,200),
                 ('Resume',0,200), ('Reset',1,200), ('TextSize',1,200), ('Resume',1,200), ('TextSize',0,200)],
    'keyretry': [('Screen',0,100), ('Screen',0,100), ('Screen',0,100), ('Resume',0,100),
                 ('TextSize',0,100), ('TextSize',0,200), ('Reset',0,200), ('Screen',0,200),
                 ('Answer0',0,200), ('Answer0',0,200)],
    'keydisabled': [('Screen',0,100), ('Screen',0,100), ('Pause',0,100), ('Pause',0,100),
                    ('Pause',1,100), ('Resume',0,100), ('Pause',0,100)],
}


def check_focus_steps(log, proof):
    rows = re.findall(r'WQ_KEY_STEP proof=(\w+) step=(\d+) key=\w+ down=\d+ up=\d+ selected=-?\d+ submitted=\d+ correct=\d+ hint=\d+ paused=\d+ evaluations=\d+ shift=(\d+) focus=(\w+) textpercent=(\d+)', log)
    expected = FOCUS_STEPS[proof]
    passed = len(rows) == len(expected)
    for index, (row, (focus, shift, percent)) in enumerate(zip(rows, expected), 1):
        passed = passed and row[0] == proof and int(row[1]) == index
        passed = passed and (row[3], int(row[2]), int(row[4])) == (focus, shift, percent)
    return passed, rows


def check_focus_capture(log, proof):
    rows = re.findall(r'WQ_FOCUS_CAPTURE proof=(\w+) focus=(\w+) visible=(\d+) textpercent=(\d+)', log)
    focus, _, percent = FOCUS_STEPS[proof][-1]
    passed = len(rows) == 1 and rows[0] == (proof, focus, '1', str(percent))
    return passed, rows


def check_keyboard_steps(log, proof):
    rows = re.findall(r'WQ_KEY_STEP proof=(\w+) step=(\d+) key=(\w+) down=(\d+) up=(\d+) selected=(-?\d+) submitted=(\d+) correct=(\d+) hint=(\d+) paused=(\d+) evaluations=(\d+)', log)
    expected = KEYBOARD_STEPS[proof]
    passed = len(rows) == len(expected)
    for index, (row, (key, state, require_down)) in enumerate(zip(rows, expected), 1):
        passed = passed and row[0] == proof and int(row[1]) == index and row[2] == key
        passed = passed and tuple(map(int, row[5:])) == state and (not require_down or row[3] == '1')
        passed = passed and (key != 'SpaceBar' or row[4] == '1')
    return passed, rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=['automation', 'capture'])
    parser.add_argument('--proof', default='initial', choices=['initial', 'selected', 'correct', 'wrong', 'hint', 'empty', 'paused', 'resumed', 'pausefocus', 'large', 'long', 'longfocus', 'focus', 'actions', 'actionfocus', *KEYBOARD_STEPS])
    parser.add_argument('--width', type=int, default=884)
    parser.add_argument('--height', type=int, default=1780)
    parser.add_argument('--safe-zone', type=float, default=1.0, help='Desktop simulated safe-area ratio, 0.5 to 1')
    parser.add_argument('--engine-root', type=Path, default=Path(r'C:\Program Files\Epic Games\UE_5.8'))
    parser.add_argument('--package-run', type=Path, help='Use a completed local package run instead of the editor (capture only)')
    args = parser.parse_args()
    if not .5 <= args.safe_zone <= 1 or args.width < 200 or args.height < 200:
        parser.error('Use safe-zone 0.5..1 and dimensions at least 200 pixels.')
    root = Path(__file__).resolve().parents[2]
    package_manifest = None
    package_directory = None
    if args.package_run:
        if args.mode != 'capture':
            parser.error('Packaged proof currently supports capture only; run automation with the editor.')
        manifest_path = args.package_run.resolve() / 'run.json'
        package_manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
        if not package_manifest.get('evidence_complete') or not package_manifest.get('files'):
            parser.error('Package run has no complete successful archive/hash evidence.')
        package_directory = Path(package_manifest['package_directory']).resolve()
        for relative, expected_file in package_manifest['files'].items():
            payload = (package_directory / relative).resolve()
            if not payload.is_relative_to(package_directory) or not payload.is_file() or payload.stat().st_size != expected_file['size']:
                parser.error(f'Missing/invalid packaged file: {relative}')
            with payload.open('rb') as source:
                if hashlib.file_digest(source, 'sha256').hexdigest() != expected_file['sha256']:
                    parser.error(f'Packaged file hash changed: {relative}')
    kind = 'packaged-capture' if package_manifest else args.mode
    run = root / 'Artifacts/QA/UI01' / f'{datetime.now():%Y%m%d-%H%M%S}-{kind}-{args.proof}'
    run.mkdir(parents=True)
    command = [str(args.engine_root / 'Engine/Binaries/Win64/UnrealEditor-Cmd.exe'),
               str(root / 'Game/WordQuest.uproject'), '-Unattended', '-NoSplash', '-NoSound',
               f'-AbsLog={run / "Unreal.log"}']
    if package_manifest:
        command = [str(package_directory / 'WordQuest/Binaries/Win64/WordQuest.exe'),
                   '-Unattended', '-NoSplash', '-NoSound', f'-AbsLog={run / "Unreal.log"}']
        if not Path(command[0]).is_file():
            parser.error('Missing archived native Development game executable.')
    if args.mode == 'automation':
        command += ['-NullRHI', '-ExecCmds=Automation RunTests WordQuest.Context',
                    '-TestExit=Automation Test Queue Empty', f'-ReportExportPath={run / "Report"}']
    else:
        command += ['-game', '-windowed', '-RenderOffscreen', '-ForceRes',
                    f'-ResX={args.width}', f'-ResY={args.height}', f'-WQProof={args.proof}',
                    f'-WQCapture={run / "native.png"}', '-WQExit']
        if args.safe_zone != 1:
            command += [f'-ExecCmds=r.DebugSafeZone.TitleRatio {args.safe_zone}']
    print(f'Running {args.mode}/{args.proof}: {run}', flush=True)
    result = {'command': command, 'head': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=root, text=True).strip(),
              'worktree': subprocess.check_output(['git', 'status', '--short'], cwd=root, text=True)}
    if package_manifest:
        result.update({'package_manifest': str(manifest_path), 'package_head': package_manifest['head'],
                       'package_hashes_verified': True,
                       'package_manifest_sha256': hashlib.sha256(manifest_path.read_bytes()).hexdigest()})
    with (run / 'console.log').open('w', encoding='utf-8') as output:
        try:
            process = subprocess.run(command, cwd=package_directory or root, stdout=output, stderr=subprocess.STDOUT, timeout=600)
            result['exit_code'] = process.returncode
        except subprocess.TimeoutExpired:
            result['exit_code'] = -1
            result['error'] = 'Unreal exceeded 600 seconds; verification incomplete.'
    log_path = run / 'Unreal.log'
    log = log_path.read_text(encoding='utf-8', errors='replace') if log_path.exists() else ''
    result['state_lines'] = [line for line in log.splitlines() if 'WQ_STATE' in line]
    if args.mode == 'capture':
        capture = run / 'native.png'
        if capture.is_file():
            with capture.open('rb') as source:
                header = source.read(24)
            result['dimensions'] = list(struct.unpack('>II', header[16:24])) if header[:8] == b'\x89PNG\r\n\x1a\n' else None
        expected = {
            'selected': (2, 0, 0, 0, 0, 0), 'correct': (0, 1, 1, 0, 0, 1),
            'wrong': (1, 1, 0, 0, 0, 1), 'hint': (0, 1, 1, 1, 0, 1),
            'paused': (1, 0, 0, 0, 1, 0),
            'resumed': (1, 0, 0, 0, 0, 0),
            **{proof: steps[-1][1] for proof, steps in KEYBOARD_STEPS.items()},
        }.get(args.proof, (-1, 0, 0, 0, 0, 0))
        matches = re.findall(r'WQ_STATE proof=\w+ selected=(-?\d+) submitted=(\d+) correct=(\d+) hint=(\d+) paused=(\d+) evaluations=(\d+)', log)
        result['state_passed'] = len(matches) == 1 and tuple(map(int, matches[0])) == expected
        result['evidence_complete'] = result['state_passed'] and result.get('dimensions') == [args.width, args.height]
        if args.proof in KEYBOARD_STEPS:
            passed, rows = check_keyboard_steps(log, args.proof)
            result.update({'keyboard_steps_passed': passed, 'keyboard_steps': rows})
            result['evidence_complete'] = result['evidence_complete'] and passed
        if args.proof in FOCUS_STEPS:
            passed, rows = check_focus_steps(log, args.proof)
            result.update({'focus_steps_passed': passed, 'focus_steps': rows})
            result['evidence_complete'] = result['evidence_complete'] and passed
            passed, rows = check_focus_capture(log, args.proof)
            result.update({'focus_visible_passed': passed, 'focus_capture': rows})
            result['evidence_complete'] = result['evidence_complete'] and passed
    else:
        report = run / 'Report/index.json'
        if report.is_file():
            data = json.loads(report.read_text(encoding='utf-8-sig'))
            result['automation'] = {k: data.get(k) for k in ['succeeded', 'failed', 'notRun', 'inProcess']}
            result['evidence_complete'] = data.get('succeeded') == 2 and data.get('failed') == 0
        else:
            result['evidence_complete'] = False
    (run / 'run.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
    print(json.dumps(result, indent=2), flush=True)
    return 0 if result['exit_code'] == 0 and result['evidence_complete'] else 1


if __name__ == '__main__':
    sys.exit(main())
