"""Run native Unreal checks and retain raw logs/captures; no device claims."""
import argparse
from datetime import datetime
import json
import re
from pathlib import Path
import struct
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=['automation', 'capture'])
    parser.add_argument('--proof', default='initial', choices=['initial', 'selected', 'correct', 'wrong', 'hint', 'empty', 'paused', 'resumed', 'pausefocus', 'large', 'long', 'longfocus', 'focus', 'actions', 'actionfocus'])
    parser.add_argument('--width', type=int, default=884)
    parser.add_argument('--height', type=int, default=1780)
    parser.add_argument('--safe-zone', type=float, default=1.0, help='Desktop simulated safe-area ratio, 0.5 to 1')
    parser.add_argument('--engine-root', type=Path, default=Path(r'C:\Program Files\Epic Games\UE_5.8'))
    args = parser.parse_args()
    if not .5 <= args.safe_zone <= 1 or args.width < 200 or args.height < 200:
        parser.error('Use safe-zone 0.5..1 and dimensions at least 200 pixels.')
    root = Path(__file__).resolve().parents[2]
    run = root / 'Artifacts/QA/UI01' / f'{datetime.now():%Y%m%d-%H%M%S}-{args.mode}-{args.proof}'
    run.mkdir(parents=True)
    command = [str(args.engine_root / 'Engine/Binaries/Win64/UnrealEditor-Cmd.exe'),
               str(root / 'Game/WordQuest.uproject'), '-Unattended', '-NoSplash', '-NoSound',
               f'-AbsLog={run / "Unreal.log"}']
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
    with (run / 'console.log').open('w', encoding='utf-8') as output:
        try:
            process = subprocess.run(command, cwd=root, stdout=output, stderr=subprocess.STDOUT, timeout=600)
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
        }.get(args.proof, (-1, 0, 0, 0, 0, 0))
        matches = re.findall(r'WQ_STATE proof=\w+ selected=(-?\d+) submitted=(\d+) correct=(\d+) hint=(\d+) paused=(\d+) evaluations=(\d+)', log)
        result['state_passed'] = len(matches) == 1 and tuple(map(int, matches[0])) == expected
        result['evidence_complete'] = result['state_passed'] and result.get('dimensions') == [args.width, args.height]
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
