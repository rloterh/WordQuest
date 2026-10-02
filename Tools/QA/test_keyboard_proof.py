"""Check that final state alone cannot validate an incomplete routed-input trace."""
import unittest
from Tools.QA.run_g_proof import check_keyboard_steps


SWITCH_TRACE = '''WQ_KEY_STEP proof=keyswitch step=1 key=One down=1 up=0 selected=0 submitted=0 correct=0 hint=0 paused=0 evaluations=0
WQ_KEY_STEP proof=keyswitch step=2 key=Three down=1 up=0 selected=2 submitted=0 correct=0 hint=0 paused=0 evaluations=0
WQ_KEY_STEP proof=keyswitch step=3 key=Four down=1 up=0 selected=3 submitted=0 correct=0 hint=0 paused=0 evaluations=0
WQ_KEY_STEP proof=keyswitch step=4 key=Two down=1 up=0 selected=1 submitted=0 correct=0 hint=0 paused=0 evaluations=0'''
BUTTON_TRACE = '''WQ_KEY_STEP proof=keybuttons step=1 key=SpaceBar down=1 up=1 selected=1 submitted=0 correct=0 hint=0 paused=0 evaluations=0
WQ_KEY_STEP proof=keybuttons step=2 key=SpaceBar down=1 up=1 selected=1 submitted=1 correct=0 hint=0 paused=0 evaluations=1
WQ_KEY_STEP proof=keybuttons step=3 key=Enter down=1 up=0 selected=1 submitted=1 correct=0 hint=0 paused=0 evaluations=1'''


class RoutedTraceTests(unittest.TestCase):
    def test_complete_route(self):
        self.assertTrue(check_keyboard_steps(SWITCH_TRACE, 'keyswitch')[0])
        self.assertTrue(check_keyboard_steps(BUTTON_TRACE, 'keybuttons')[0])

    def test_missing_trace_with_valid_empty_final_state(self):
        log = 'WQ_STATE proof=keyempty selected=-1 submitted=0 correct=0 hint=0 paused=0 evaluations=0'
        self.assertFalse(check_keyboard_steps(log, 'keyempty')[0])

    def test_wrong_intermediate_state_with_correct_final_state(self):
        log = SWITCH_TRACE.replace('selected=2', 'selected=1')
        self.assertFalse(check_keyboard_steps(log, 'keyswitch')[0])

    def test_wrong_order(self):
        rows = SWITCH_TRACE.splitlines()
        rows[0], rows[1] = rows[1], rows[0]
        self.assertFalse(check_keyboard_steps('\n'.join(rows), 'keyswitch')[0])

    def test_extra_or_missing_step(self):
        self.assertFalse(check_keyboard_steps(SWITCH_TRACE + '\n' + SWITCH_TRACE.splitlines()[-1], 'keyswitch')[0])
        self.assertFalse(check_keyboard_steps('\n'.join(SWITCH_TRACE.splitlines()[1:]), 'keyswitch')[0])

    def test_wrong_proof(self):
        self.assertFalse(check_keyboard_steps(SWITCH_TRACE.replace('proof=keyswitch', 'proof=other'), 'keyswitch')[0])

    def test_unhandled_active_key(self):
        self.assertFalse(check_keyboard_steps(SWITCH_TRACE.replace('down=1', 'down=0', 1), 'keyswitch')[0])

    def test_unhandled_button_release(self):
        self.assertFalse(check_keyboard_steps(BUTTON_TRACE.replace('up=1', 'up=0', 1), 'keybuttons')[0])


if __name__ == '__main__':
    unittest.main()
