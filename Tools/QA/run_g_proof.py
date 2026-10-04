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

POINTER_PROOFS = ('pointerhover', 'pointerpress', 'pointerhintpress', 'pointeranswerpress',
                  'pointerpausepress', 'pointerclick', 'pointerhint', 'pointerpaused', 'pointerresumed')


def pointer_contract(proof):
    """Independent expected transitions: mouse-down cannot activate a button."""
    initial = (-1, 0, 0, 0, 0, 0)
    selected_b = (1, 0, 0, 0, 0, 0)
    wrong = (1, 1, 0, 0, 0, 1)
    assisted = (-1, 0, 0, 1, 0, 0)
    selected_a = (0, 0, 0, 1, 0, 0)
    correct = (0, 1, 1, 1, 0, 1)
    paused = (1, 0, 0, 0, 1, 0)
    steps = []
    def click(target, before, after, active=True):
        steps.extend([(event, target, before if event != 'up' else after, active)
                      for event in ('move', 'down', 'up')])
    if proof == 'pointerhover':
        steps = [('move', target, initial, True) for target in ('Answer0', 'Hint', 'Submit', 'Pause', 'Submit')]
    elif proof in POINTER_PROOFS and proof.endswith('press'):
        target = {'pointerhintpress': 'Hint', 'pointeranswerpress': 'Answer0',
                  'pointerpausepress': 'Pause'}.get(proof, 'Submit')
        steps = [(event, target, initial, True) for event in ('move', 'down')]
    elif proof == 'pointerclick':
        click('Submit', initial, initial); click('Answer1', initial, selected_b)
        click('Submit', selected_b, wrong); click('Submit', wrong, wrong, False)
        click('Answer0', wrong, wrong, False)
    elif proof == 'pointerhint':
        click('Hint', initial, assisted); click('Answer0', assisted, selected_a)
        click('Submit', selected_a, correct); click('Hint', correct, correct, False)
    elif proof in ('pointerpaused', 'pointerresumed'):
        click('Answer1', initial, selected_b); click('Pause', selected_b, paused)
        click('Answer0', paused, paused, False); click('Hint', paused, paused, False)
        if proof == 'pointerresumed': click('Resume', paused, selected_b)
    return steps


def check_pointer_steps(log, proof):
    pattern = r'WQ_POINTER_STEP proof=(\w+) step=(\d+) event=(\w+) target=(\w+) hit=(\d+) inside=(\d+) handled=(\d+) enabled=(\d+) hovered=(\d+) pressed=(\d+) captured=(\d+) selected=(-?\d+) submitted=(\d+) correct=(\d+) hint=(\d+) paused=(\d+) evaluations=(\d+)'
    rows = re.findall(pattern, log)
    expected = pointer_contract(proof)
    passed = bool(expected) and len(rows) == len(expected) and log.count('WQ_POINTER_STEP ') == len(rows)
    for index, (row, (event, target, state, active)) in enumerate(zip(rows, expected), 1):
        pressed = int(active and event == 'down')
        local_enabled = int(not state[1] and (target != 'Hint' or not state[3])) if target in ('Hint', 'Submit') or target.startswith('Answer') else 1
        passed = passed and row[:4] == (proof, str(index), event, target)
        passed = passed and all(value in ('0', '1') for value in row[4:11])
        passed = passed and row[5] == '1' and row[7] == str(local_enabled)
        passed = passed and row[9:11] == (str(pressed), str(pressed))
        passed = passed and tuple(map(int, row[11:17])) == state
        if active:
            passed = passed and row[4] == '1'
            if event != 'move': passed = passed and row[6] == '1'
            if event != 'up': passed = passed and row[8] == '1'
        elif state[4]:
            passed = passed and row[4] == '0'  # Modal shade blocks underlying controls.
    captures = re.findall(r'WQ_POINTER_CAPTURE proof=(\w+) target=(\w+) enabled=(\d+) hovered=(\d+) pressed=(\d+) captured=(\d+)', log)
    passed = passed and len(captures) == 1 and bool(expected) and log.count('WQ_POINTER_CAPTURE ') == 1
    if len(captures) == 1 and expected:
        event, target, state, active = expected[-1]
        pressed = int(active and event == 'down')
        passed = passed and captures[0][:2] == (proof, target)
        passed = passed and all(value in ('0', '1') for value in captures[0][2:6])
        passed = passed and bool(rows) and captures[0][2] == rows[-1][7]
        passed = passed and captures[0][4:6] == (str(pressed), str(pressed))
        if active and event in ('move', 'down'): passed = passed and captures[0][3] == '1'
    cleanup = re.findall(r'WQ_POINTER_CLEANUP proof=(\w+) pressed=(\d+) captured=(\d+) selected=(-?\d+) submitted=(\d+) correct=(\d+) hint=(\d+) paused=(\d+) evaluations=(\d+)', log)
    passed = passed and len(cleanup) == 1 and log.count('WQ_POINTER_CLEANUP ') == 1
    if len(cleanup) == 1 and expected:
        passed = passed and cleanup[0][:3] == (proof, '0', '0') and tuple(map(int, cleanup[0][3:9])) == expected[-1][2]
    return passed, rows, captures, cleanup

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


def check_answer_start(log, proof):
    rows = re.findall(r'WQ_ANSWER_START proof=(\w+) focus=(\w+) textpercent=(\d+) visible=(\d+) oversized=(\d+)', log)
    passed = len(rows) == 1 and rows[0][:4] == (proof, 'Answer1', '200', '1') and rows[0][4] in ('0', '1')
    return passed, rows


def check_option_cues(log, proof, state):
    rows = re.findall(r'WQ_OPTION_CUE proof=(\w+) option=(\d+) codepoint=(\d+) label=([^\r\n]*)', log)
    selected, submitted, correct, *_ = state
    passed = len(rows) == 4
    for index, row in enumerate(rows):
        is_selected = selected == index
        code = 0 if not is_selected else (10003 if correct else 215) if submitted else 62
        prefix = '' if not is_selected else ('Correct. ' if correct else 'Not quite. ') if submitted else 'Selected. '
        label_prefix = f'{prefix}Option {chr(65 + index)}. '
        passed = passed and row[:3] == (proof, str(index), str(code))
        passed = passed and row[3].startswith(label_prefix) and bool(row[3][len(label_prefix):].strip())
    return passed, rows


SCROLL_PROOFS = ('scrollfeedback', 'scrollfocus', 'scrollpaused')
FEEDBACK_PROOFS = ('correct', 'wrong', 'hint', 'empty', 'keyempty', 'keysubmit', 'keyhint', 'keybuttons', 'scrollfeedback', 'scrollfocus')


def check_feedback_capture(log, proof):
    rows = re.findall(r'WQ_FEEDBACK_CAPTURE proof=(\w+) visibility=(-?\d+)', log)
    allowed = ('1', '3') if proof in SCROLL_PROOFS else ('1', '2')
    return len(rows) == 1 and rows[0][0] == proof and rows[0][1] in allowed, rows


def check_large_text_capture(log, proof):
    rows = re.findall(r'WQ_TEXT_CAPTURE proof=(\w+) textpercent=(\d+)', log)
    return rows == [(proof, '200')], rows


def check_action_content(log, proof):
    rows = re.findall(r'WQ_ACTION_CONTENT proof=(\w+) fits=(\d+)', log)
    return rows == [(proof, '1')], rows


def check_scroll_steps(log, proof):
    pattern = r'WQ_SCROLL_STEP proof=(\w+) step=(\d+) key=(\w+) down=(\d+) up=(\d+) offset=([\d.-]+) end=([\d.-]+) selected=(-?\d+) submitted=(\d+) correct=(\d+) hint=(\d+) paused=(\d+) evaluations=(\d+) focus=(\w+) textpercent=(\d+) first=(-?\d+) last=(-?\d+) focusvisible=(\d+)'
    rows = re.findall(pattern, log)
    keys = ('start', 'PageDown', 'PageUp', 'End', 'PageDown', 'Home', 'PageUp', 'End')
    if proof == 'scrollfeedback': keys += ('Tab', 'End')
    paused = proof == 'scrollpaused'
    focus = 'Resume' if paused else 'Pause' if proof == 'scrollfocus' else 'Screen'
    passed = len(rows) == len(keys)
    offsets, ends = [], []
    for index, (row, key) in enumerate(zip(rows, keys), 1):
        offset, end = float(row[5]), float(row[6])
        offsets.append(offset); ends.append(end)
        passed = passed and row[:3] == (proof, str(index), key)
        passed = passed and tuple(map(int, row[7:13])) == (0, 1, 1, 1, int(paused), 1)
        step_focus = 'Pause' if proof == 'scrollfeedback' and index >= 9 else focus
        passed = passed and row[13:15] == (step_focus, '200') and -1 <= offset <= end + 1 and end > 1
        passed = passed and row[3] == ('0' if index == 1 or paused else '1')
    if len(rows) == len(keys):
        passed = passed and max(ends) - min(ends) <= 1
        if paused:
            passed = passed and max(offsets) - min(offsets) <= 1 and all(row[17] == '1' for row in rows)
        else:
            passed = passed and offsets[1] > offsets[0] + 1 and offsets[2] < offsets[1] - 1
            passed = passed and all(abs(offsets[i] - ends[i]) <= 1 for i in (3, 4, 7))
            passed = passed and all(abs(offsets[i]) <= 1 for i in (5, 6))
            passed = passed and all(rows[i][16] in ('1', '3') for i in (3, 4, 7))
            if proof == 'scrollfocus': passed = passed and rows[5][17] == '1'
            if proof == 'scrollfeedback':
                passed = passed and offsets[8] < offsets[7] - 1 and rows[8][17] == '1'
                passed = passed and abs(offsets[9] - ends[9]) <= 1 and rows[9][16] in ('1', '3')
    captures = re.findall(r'WQ_SCROLL_CAPTURE proof=(\w+) focus=(\w+) visible=(\d+)', log)
    if proof == 'scrollfeedback': focus = 'Pause'
    passed = passed and len(captures) == 1 and captures[0][:2] == (proof, focus)
    if paused:
        passed = passed and len(captures) == 1 and captures[0][2] == '1'
    return passed, rows, captures


MODAL_PROOFS = ('modalcycle', 'modalresume', 'modalretry')


def check_modal_steps(log, proof):
    rows = re.findall(r'WQ_MODAL_STEP proof=(\w+) step=(\d+) key=(\w+) down=(\d+) up=(\d+) shift=(\d+) selected=(-?\d+) submitted=(\d+) correct=(\d+) hint=(\d+) paused=(\d+) evaluations=(\d+) focus=(\w+) textpercent=(\d+) visible=(\d+) fits=(\d+) answerstart=(\d+) oversized=(\d+)', log)
    keys = ['start','Tab','SpaceBar','Tab','Tab','Tab','Tab','Tab','Tab','Tab']
    focuses = ['Resume','TextSize','TextSize','Reset','Resume','Reset','TextSize','Resume','TextSize','Reset']
    if proof == 'modalresume': keys += ['Tab','SpaceBar']; focuses += ['Resume','Pause']
    if proof == 'modalretry': keys += ['SpaceBar','Tab','SpaceBar']; focuses += ['Screen','Answer0','Answer0']
    passed = len(rows) == len(keys)
    for index,(row,key,focus) in enumerate(zip(rows,keys,focuses)):
        attempt = (0,1,1,1,1,1)
        if proof == 'modalresume' and index == 11: attempt = (0,1,1,1,0,1)
        if proof == 'modalretry' and index >= 10: attempt = (0 if index == 12 else -1,0,0,0,0,0)
        passed = passed and row[:3] == (proof,str(index+1),key) and row[3] == ('0' if index == 0 else '1')
        passed = passed and row[5] == str(int(5 <= index <= 7)) and tuple(map(int,row[6:12])) == attempt
        passed = passed and row[12:14] == (focus,'100' if index < 2 else '200') and row[15] == '1'
        if focus == 'Answer0': passed = passed and row[16] == '1' and (row[14] == '1' or row[17] == '1')
        elif focus != 'Screen': passed = passed and row[14] == '1'
        if key == 'SpaceBar': passed = passed and row[4] == '1'
    captures = re.findall(r'WQ_MODAL_CAPTURE proof=(\w+) focus=(\w+) visible=(\d+) fits=(\d+) answerstart=(\d+) oversized=(\d+)',log)
    passed = passed and len(captures) == 1 and captures[0][:2] == (proof,focuses[-1]) and captures[0][3] == '1'
    if len(captures) == 1:
        passed = passed and (captures[0][4] == '1' and (captures[0][2] == '1' or captures[0][5] == '1')
                            if proof == 'modalretry' else captures[0][2] == '1')
    return passed,rows,captures


INTERRUPTION_PROOFS = ('interruptpaused', 'interruptresumed', 'interruptsubmitted', 'interruptmanual')


def check_interruption_steps(log, proof):
    rows = re.findall(r'WQ_INTERRUPT_STEP proof=(\w+) step=(\d+) event=(\w+) selected=(-?\d+) submitted=(\d+) correct=(\d+) hint=(\d+) paused=(\d+) evaluations=(\d+) focus=(\w+)', log)
    submitted = proof == 'interruptsubmitted'
    gameplay_focus = 'Pause' if submitted else 'Answer1'
    def state(paused):
        return (1, int(submitted), 0, 1, int(paused), int(submitted))
    expected = [('start', state(proof == 'interruptmanual'),
                 'Resume' if proof == 'interruptmanual' else gameplay_focus)]
    notifications = ('deactivate', 'background', 'slateinactive') if proof == 'interruptresumed' else (
        ('background', 'slateinactive', 'deactivate') if submitted else ('slateinactive', 'deactivate', 'background'))
    expected += [(event, state(True), 'Resume') for event in
        (*notifications, 'slateactive', 'foreground', 'reactivate', 'blockedinput')]
    if proof in ('interruptresumed', 'interruptsubmitted'):
        expected.append(('resume', state(False), gameplay_focus))
    passed = len(rows) == len(expected)
    for index, (row, (event, attempt, focus)) in enumerate(zip(rows, expected), 1):
        passed = passed and row[:3] == (proof, str(index), event)
        passed = passed and tuple(map(int, row[3:9])) == attempt and row[9] == focus
    capture = re.findall(r'WQ_INTERRUPT_CAPTURE proof=(\w+) focus=(\w+) visible=(\d+)', log)
    passed = passed and capture == [(proof, expected[-1][2], '1')]
    return passed, rows, capture


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=['automation', 'capture'])
    parser.add_argument('--proof', default='initial', choices=['initial', 'selected', 'correct', 'wrong', 'hint', 'empty', 'paused', 'resumed', 'pausefocus', 'large', 'long', 'longfocus', 'longselectedfocus', 'focus', 'actions', 'actionfocus', *KEYBOARD_STEPS, *INTERRUPTION_PROOFS, *SCROLL_PROOFS, *MODAL_PROOFS, *POINTER_PROOFS])
    parser.add_argument('--width', type=int, default=884)
    parser.add_argument('--height', type=int, default=1780)
    parser.add_argument('--safe-zone', type=float, default=1.0, help='Desktop simulated safe-area ratio, 0.5 to 1')
    parser.add_argument('--no-tooltips', action='store_true', help='Hide desktop tooltips for comparison captures; not a tooltip interaction test')
    parser.add_argument('--large-text', action='store_true', help='Use and verify 200%% text in simple question-state captures')
    parser.add_argument('--engine-root', type=Path, default=Path(r'C:\Program Files\Epic Games\UE_5.8'))
    parser.add_argument('--package-run', type=Path, help='Use a completed local package run instead of the editor (capture only)')
    args = parser.parse_args()
    if args.proof in POINTER_PROOFS and args.mode != 'capture':
        parser.error('Pointer proofs require capture mode.')
    if args.large_text and (args.mode != 'capture' or args.proof not in ('initial', 'selected', 'correct', 'wrong', 'hint', 'empty', *POINTER_PROOFS)):
        parser.error('--large-text supports question-state and pointer captures only.')
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
        if args.large_text:
            command.append('-WQLargeText')
        console = []
        if args.safe_zone != 1:
            console.append(f'r.DebugSafeZone.TitleRatio {args.safe_zone}')
        if args.no_tooltips:
            console.append('Slate.EnableTooltips 0')
        if console:
            command += [f'-ExecCmds={",".join(console)}']
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
            'longselectedfocus': (1, 0, 0, 0, 0, 0),
            'interruptpaused': (1, 0, 0, 1, 1, 0),
            'interruptmanual': (1, 0, 0, 1, 1, 0),
            'interruptresumed': (1, 0, 0, 1, 0, 0),
            'interruptsubmitted': (1, 1, 0, 1, 0, 1),
            **{proof: (0, 1, 1, 1, int(proof == 'scrollpaused'), 1) for proof in SCROLL_PROOFS},
            **{proof: (0, 1, 1, 1, 1, 1) for proof in MODAL_PROOFS},
            **{proof: steps[-1][1] for proof, steps in KEYBOARD_STEPS.items()},
            **{proof: pointer_contract(proof)[-1][2] for proof in POINTER_PROOFS},
        }.get(args.proof, (-1, 0, 0, 0, 0, 0))
        matches = re.findall(r'WQ_STATE proof=\w+ selected=(-?\d+) submitted=(\d+) correct=(\d+) hint=(\d+) paused=(\d+) evaluations=(\d+)', log)
        result['state_passed'] = len(matches) == 1 and tuple(map(int, matches[0])) == expected
        result['evidence_complete'] = result['state_passed'] and result.get('dimensions') == [args.width, args.height]
        cue_state = (0,0,0,0,0,0) if args.proof == 'modalretry' else expected
        passed, rows = check_option_cues(log, args.proof, cue_state)
        result.update({'option_cues_passed': passed, 'option_cues': rows})
        result['evidence_complete'] = result['evidence_complete'] and passed
        if args.large_text or args.proof in SCROLL_PROOFS:
            passed, rows = check_large_text_capture(log, args.proof)
            result.update({'large_text_passed': passed, 'text_capture': rows})
            result['evidence_complete'] = result['evidence_complete'] and passed
            passed, rows = check_action_content(log, args.proof)
            result.update({'action_content_passed': passed, 'action_content': rows})
            result['evidence_complete'] = result['evidence_complete'] and passed
        if args.proof in FEEDBACK_PROOFS:
            passed, rows = check_feedback_capture(log, args.proof)
            result.update({'feedback_visible_passed': passed, 'feedback_capture': rows})
            result['evidence_complete'] = result['evidence_complete'] and passed
        if args.proof in SCROLL_PROOFS:
            passed, rows, captures = check_scroll_steps(log, args.proof)
            result.update({'scroll_steps_passed': passed, 'scroll_steps': rows, 'scroll_capture': captures})
            result['evidence_complete'] = result['evidence_complete'] and passed
        if args.proof in MODAL_PROOFS:
            passed, rows, captures = check_modal_steps(log, args.proof)
            result.update({'modal_steps_passed': passed, 'modal_steps': rows, 'modal_capture': captures})
            result['evidence_complete'] = result['evidence_complete'] and passed
        if args.proof in INTERRUPTION_PROOFS:
            passed, rows, capture_rows = check_interruption_steps(log, args.proof)
            result.update({'interruption_steps_passed': passed, 'interruption_steps': rows,
                           'interruption_capture': capture_rows})
            result['evidence_complete'] = result['evidence_complete'] and passed
        if args.proof in POINTER_PROOFS:
            passed, rows, capture_rows, cleanup_rows = check_pointer_steps(log, args.proof)
            result.update({'pointer_steps_passed': passed, 'pointer_steps': rows,
                           'pointer_capture': capture_rows, 'pointer_cleanup': cleanup_rows})
            result['evidence_complete'] = result['evidence_complete'] and passed
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
        if args.proof in ('longfocus', 'longselectedfocus'):
            passed, rows = check_answer_start(log, args.proof)
            result.update({'answer_start_passed': passed, 'answer_start': rows})
            result['evidence_complete'] = result['evidence_complete'] and passed
    else:
        report = run / 'Report/index.json'
        if report.is_file():
            data = json.loads(report.read_text(encoding='utf-8-sig'))
            result['automation'] = {k: data.get(k) for k in ['succeeded', 'failed', 'notRun', 'inProcess']}
            result['evidence_complete'] = (data.get('succeeded') == 2 and
                all(data.get(key) == 0 for key in ('failed', 'notRun', 'inProcess')))
        else:
            result['evidence_complete'] = False
    # A capture/report may be written before Unreal crashes or times out. Keep
    # the persisted verdict consistent with the command's failure status.
    result['evidence_complete'] = result['exit_code'] == 0 and result['evidence_complete']
    (run / 'run.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
    print(json.dumps(result, indent=2), flush=True)
    return 0 if result['exit_code'] == 0 and result['evidence_complete'] else 1


if __name__ == '__main__':
    sys.exit(main())
