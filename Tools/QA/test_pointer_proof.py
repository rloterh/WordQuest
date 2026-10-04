"""Synthetic trace fixtures exercise evidence rejection, not runtime/device proof."""
import unittest
import subprocess
import sys
from pathlib import Path
from Tools.QA.run_g_proof import check_pointer_steps


PRESS = '''WQ_POINTER_STEP proof=pointerpress step=1 event=move target=Submit hit=1 inside=1 handled=1 enabled=1 hovered=1 pressed=0 captured=0 selected=-1 submitted=0 correct=0 hint=0 paused=0 evaluations=0
WQ_POINTER_STEP proof=pointerpress step=2 event=down target=Submit hit=1 inside=1 handled=1 enabled=1 hovered=1 pressed=1 captured=1 selected=-1 submitted=0 correct=0 hint=0 paused=0 evaluations=0
WQ_POINTER_CAPTURE proof=pointerpress target=Submit enabled=1 hovered=1 pressed=1 captured=1
WQ_POINTER_CLEANUP proof=pointerpress pressed=0 captured=0 selected=-1 submitted=0 correct=0 hint=0 paused=0 evaluations=0'''

INITIAL = (-1, 0, 0, 0, 0, 0)
SELECTED = (1, 0, 0, 0, 0, 0)
WRONG = (1, 1, 0, 0, 0, 1)
# Values copied from the observed preflight; deliberately independent of the
# contract builder. Active-up may disable a button; disabled-down may be handled
# by its ancestor without activating the target.
CLICK_ROWS = [
    ('move', 'Submit', (1,1,1,1,0,0), INITIAL),
    ('down', 'Submit', (1,1,1,1,1,1), INITIAL),
    ('up', 'Submit', (1,1,1,1,0,0), INITIAL),
    ('move', 'Answer1', (1,1,1,1,0,0), INITIAL),
    ('down', 'Answer1', (1,1,1,1,1,1), INITIAL),
    ('up', 'Answer1', (1,1,1,1,0,0), SELECTED),
    ('move', 'Submit', (1,1,1,1,0,0), SELECTED),
    ('down', 'Submit', (1,1,1,1,1,1), SELECTED),
    ('up', 'Submit', (1,1,0,1,0,0), WRONG),
    ('move', 'Submit', (0,1,0,0,0,0), WRONG),
    ('down', 'Submit', (0,1,0,0,0,0), WRONG),
    ('up', 'Submit', (0,0,0,0,0,0), WRONG),
    ('move', 'Answer0', (0,1,0,0,0,0), WRONG),
    ('down', 'Answer0', (0,1,0,0,0,0), WRONG),
    ('up', 'Answer0', (0,0,0,0,0,0), WRONG),
]


def click_trace():
    rows = []
    for index, (event, target, flags, state) in enumerate(CLICK_ROWS, 1):
        hit, handled, enabled, hovered, pressed, captured = flags
        fields = ' '.join(f'{key}={value}' for key, value in zip(
            ('selected', 'submitted', 'correct', 'hint', 'paused', 'evaluations'), state))
        rows.append(f'WQ_POINTER_STEP proof=pointerclick step={index} event={event} target={target} '
                    f'hit={hit} inside=1 handled={handled} enabled={enabled} hovered={hovered} '
                    f'pressed={pressed} captured={captured} {fields}')
    rows += ['WQ_POINTER_CAPTURE proof=pointerclick target=Answer0 enabled=0 hovered=0 pressed=0 captured=0',
             'WQ_POINTER_CLEANUP proof=pointerclick pressed=0 captured=0 selected=1 submitted=1 correct=0 hint=0 paused=0 evaluations=1']
    return '\n'.join(rows)


class PointerEvidenceTests(unittest.TestCase):
    def test_automation_cannot_be_labeled_pointer_evidence(self):
        helper = Path(__file__).with_name('run_g_proof.py')
        result = subprocess.run([sys.executable, str(helper), 'automation', '--proof', 'pointerpress'],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertIn('Pointer proofs require capture mode.', result.stderr)

    def test_complete_press_and_release_routes(self):
        self.assertTrue(check_pointer_steps(PRESS, 'pointerpress')[0])
        self.assertTrue(check_pointer_steps(click_trace(), 'pointerclick')[0])

    def test_cooked_fname_event_casing_preserves_raw_trace(self):
        trace = PRESS.replace('event=down', 'event=Down').replace('event=move', 'event=Move')
        passed, rows, _, _ = check_pointer_steps(trace, 'pointerpress')
        self.assertTrue(passed)
        self.assertEqual(rows[1][2], 'Down')
        self.assertFalse(check_pointer_steps(trace.replace('event=Down', 'event=Drag'), 'pointerpress')[0])

    def test_final_state_without_input_trace_is_rejected(self):
        self.assertFalse(check_pointer_steps('WQ_STATE proof=pointerpress selected=-1 submitted=0 correct=0 hint=0 paused=0 evaluations=0', 'pointerpress')[0])

    def test_wrong_target_or_missed_hit_or_clipping(self):
        for old, new in [('target=Submit', 'target=Hint'), ('hit=1', 'hit=0'), ('inside=1', 'inside=0')]:
            with self.subTest(old=old):
                self.assertFalse(check_pointer_steps(PRESS.replace(old, new, 1), 'pointerpress')[0])

    def test_unhandled_active_press(self):
        self.assertFalse(check_pointer_steps(PRESS.replace('handled=1', 'handled=0'), 'pointerpress')[0])

    def test_hover_or_pointer_capture_missing(self):
        for old, new in [('hovered=1', 'hovered=0'), ('captured=1', 'captured=0')]:
            with self.subTest(old=old):
                self.assertFalse(check_pointer_steps(PRESS.replace(old, new, 1), 'pointerpress')[0])

    def test_activation_on_down_despite_correct_final_state(self):
        trace = click_trace().splitlines()
        trace[7] = trace[7].replace('submitted=0', 'submitted=1').replace('evaluations=0', 'evaluations=1')
        self.assertFalse(check_pointer_steps('\n'.join(trace), 'pointerclick')[0])

    def test_disabled_activation_or_second_evaluation(self):
        for old, new in [('selected=1', 'selected=0'), ('evaluations=1', 'evaluations=2')]:
            trace = click_trace().splitlines()
            trace[10] = trace[10].replace(old, new)
            self.assertFalse(check_pointer_steps('\n'.join(trace), 'pointerclick')[0])

    def test_missing_extra_and_reordered_steps(self):
        rows = PRESS.splitlines()
        for trace in ['\n'.join(rows[1:]), PRESS + '\n' + rows[0], '\n'.join([rows[1], rows[0], *rows[2:]])]:
            self.assertFalse(check_pointer_steps(trace, 'pointerpress')[0])

    def test_malformed_extra_trace_and_unknown_proof(self):
        self.assertFalse(check_pointer_steps(PRESS + '\nWQ_POINTER_STEP malformed', 'pointerpress')[0])
        self.assertFalse(check_pointer_steps(PRESS, 'unknown')[0])
        self.assertFalse(check_pointer_steps(PRESS.replace('proof=pointerpress', 'proof=other'), 'pointerpress')[0])

    def test_held_press_lost_before_screenshot(self):
        trace = PRESS.replace('WQ_POINTER_CAPTURE proof=pointerpress target=Submit enabled=1 hovered=1 pressed=1',
                              'WQ_POINTER_CAPTURE proof=pointerpress target=Submit enabled=1 hovered=1 pressed=0')
        self.assertFalse(check_pointer_steps(trace, 'pointerpress')[0])

    def test_cleanup_missing_capture_leaked_or_activated(self):
        for trace in ['\n'.join(PRESS.splitlines()[:-1]), PRESS.replace('WQ_POINTER_CLEANUP proof=pointerpress pressed=0 captured=0',
            'WQ_POINTER_CLEANUP proof=pointerpress pressed=0 captured=1'), PRESS.replace(
            'WQ_POINTER_CLEANUP proof=pointerpress pressed=0 captured=0 selected=-1',
            'WQ_POINTER_CLEANUP proof=pointerpress pressed=0 captured=0 selected=0')]:
            self.assertFalse(check_pointer_steps(trace, 'pointerpress')[0])

    def test_non_boolean_capture_flags(self):
        trace = PRESS.replace('WQ_POINTER_CAPTURE proof=pointerpress target=Submit enabled=1 hovered=1',
                              'WQ_POINTER_CAPTURE proof=pointerpress target=Submit enabled=1 hovered=2')
        self.assertFalse(check_pointer_steps(trace, 'pointerpress')[0])


if __name__ == '__main__':
    unittest.main()
