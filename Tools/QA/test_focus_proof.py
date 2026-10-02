"""Reject incomplete focus/setting traces even when the attempt state matches."""
import unittest
from Tools.QA.run_g_proof import check_focus_steps, check_keyboard_steps


TRACE = '''WQ_KEY_STEP proof=keydisabled step=1 key=One down=1 up=0 selected=0 submitted=0 correct=0 hint=0 paused=0 evaluations=0 shift=0 focus=Screen textpercent=100
WQ_KEY_STEP proof=keydisabled step=2 key=Enter down=1 up=0 selected=0 submitted=1 correct=1 hint=0 paused=0 evaluations=1 shift=0 focus=Screen textpercent=100
WQ_KEY_STEP proof=keydisabled step=3 key=Tab down=1 up=0 selected=0 submitted=1 correct=1 hint=0 paused=0 evaluations=1 shift=0 focus=Pause textpercent=100
WQ_KEY_STEP proof=keydisabled step=4 key=Tab down=1 up=0 selected=0 submitted=1 correct=1 hint=0 paused=0 evaluations=1 shift=0 focus=Pause textpercent=100
WQ_KEY_STEP proof=keydisabled step=5 key=Tab down=1 up=0 selected=0 submitted=1 correct=1 hint=0 paused=0 evaluations=1 shift=1 focus=Pause textpercent=100
WQ_KEY_STEP proof=keydisabled step=6 key=P down=1 up=0 selected=0 submitted=1 correct=1 hint=0 paused=1 evaluations=1 shift=0 focus=Resume textpercent=100
WQ_KEY_STEP proof=keydisabled step=7 key=SpaceBar down=1 up=1 selected=0 submitted=1 correct=1 hint=0 paused=0 evaluations=1 shift=0 focus=Pause textpercent=100'''


class FocusTraceTests(unittest.TestCase):
    def test_complete_trace(self):
        self.assertTrue(check_keyboard_steps(TRACE, 'keydisabled')[0])
        self.assertTrue(check_focus_steps(TRACE, 'keydisabled')[0])

    def test_matching_state_with_wrong_focus(self):
        log = TRACE.replace('focus=Pause', 'focus=Answer0', 1)
        self.assertTrue(check_keyboard_steps(log, 'keydisabled')[0])
        self.assertFalse(check_focus_steps(log, 'keydisabled')[0])

    def test_wrong_modifier_or_text_setting(self):
        self.assertFalse(check_focus_steps(TRACE.replace('shift=1', 'shift=0'), 'keydisabled')[0])
        self.assertFalse(check_focus_steps(TRACE.replace('textpercent=100', 'textpercent=200', 1), 'keydisabled')[0])

    def test_missing_focus_metadata(self):
        self.assertFalse(check_focus_steps(TRACE.replace(' focus=Pause', '', 1), 'keydisabled')[0])

    def test_missing_extra_or_reordered_step(self):
        rows = TRACE.splitlines()
        self.assertFalse(check_focus_steps('\n'.join(rows[1:]), 'keydisabled')[0])
        self.assertFalse(check_focus_steps(TRACE + '\n' + rows[-1], 'keydisabled')[0])
        rows[0], rows[1] = rows[1], rows[0]
        self.assertFalse(check_focus_steps('\n'.join(rows), 'keydisabled')[0])

    def test_wrong_proof(self):
        self.assertFalse(check_focus_steps(TRACE.replace('proof=keydisabled', 'proof=other'), 'keydisabled')[0])


if __name__ == '__main__':
    unittest.main()
