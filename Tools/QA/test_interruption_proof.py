"""Final state cannot hide incomplete lifecycle delivery or accidental resumption."""
import unittest
from Tools.QA.run_g_proof import check_interruption_steps


EVENTS = ('start', 'deactivate', 'background', 'slateinactive', 'slateactive', 'foreground', 'reactivate', 'blockedinput', 'resume')
TRACE = '\n'.join(
    f'WQ_INTERRUPT_STEP proof=interruptresumed step={i} event={event} selected=1 submitted=0 correct=0 hint=1 paused={int(1 < i < 9)} evaluations=0 focus={"Resume" if 1 < i < 9 else "Answer1"}'
    for i, event in enumerate(EVENTS, 1)) + '\nWQ_INTERRUPT_CAPTURE proof=interruptresumed focus=Answer1 visible=1'


class InterruptionTraceTests(unittest.TestCase):
    def test_complete_trace(self):
        self.assertTrue(check_interruption_steps(TRACE, 'interruptresumed')[0])

    def test_missing_extra_or_reordered_event(self):
        rows = TRACE.splitlines()
        self.assertFalse(check_interruption_steps('\n'.join(rows[1:]), 'interruptresumed')[0])
        self.assertFalse(check_interruption_steps(TRACE + '\n' + rows[1], 'interruptresumed')[0])
        rows[1], rows[2] = rows[2], rows[1]
        self.assertFalse(check_interruption_steps('\n'.join(rows), 'interruptresumed')[0])

    def test_duplicate_notification_or_return_cannot_resume(self):
        for event in ('deactivate', 'background', 'slateactive', 'foreground', 'reactivate'):
            lines = TRACE.splitlines()
            lines = [line.replace('paused=1', 'paused=0') if f'event={event} ' in line else line for line in lines]
            self.assertFalse(check_interruption_steps('\n'.join(lines), 'interruptresumed')[0])

    def test_paused_input_cannot_change_attempt(self):
        for changed in ('selected=0', 'submitted=1', 'hint=0', 'evaluations=1'):
            key = changed.split('=')[0]
            old = {'selected':'selected=1', 'submitted':'submitted=0', 'hint':'hint=1', 'evaluations':'evaluations=0'}[key]
            lines = [line.replace(old, changed) if 'event=blockedinput ' in line else line for line in TRACE.splitlines()]
            self.assertFalse(check_interruption_steps('\n'.join(lines), 'interruptresumed')[0])

    def test_wrong_focus_or_invisible_capture(self):
        self.assertFalse(check_interruption_steps(TRACE.replace('focus=Answer1', 'focus=Pause'), 'interruptresumed')[0])
        self.assertFalse(check_interruption_steps(TRACE.replace('visible=1', 'visible=0'), 'interruptresumed')[0])
        self.assertFalse(check_interruption_steps(TRACE.split('\nWQ_INTERRUPT_CAPTURE')[0], 'interruptresumed')[0])

    def test_wrong_proof(self):
        self.assertFalse(check_interruption_steps(TRACE.replace('proof=interruptresumed', 'proof=interruptpaused'), 'interruptresumed')[0])


if __name__ == '__main__':
    unittest.main()
