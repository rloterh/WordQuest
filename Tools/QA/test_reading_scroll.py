"""Reject inert, out-of-bounds or state-changing synthetic scroll evidence."""
import unittest
from Tools.QA.run_g_proof import check_scroll_steps, check_feedback_capture


def trace(proof='scrollfeedback'):
    paused = proof == 'scrollpaused'
    focus = 'Resume' if paused else 'Pause' if proof == 'scrollfocus' else 'Screen'
    offsets = [600]*8 if paused else [0 if proof == 'scrollfocus' else 600,900,600,1000,1000,0,0,1000]
    keys = ('start','PageDown','PageUp','End','PageDown','Home','PageUp','End')
    if proof == 'scrollfeedback':
        keys += ('Tab','End'); offsets += [0,1000]
    rows=[]
    for i,(key,offset) in enumerate(zip(keys,offsets),1):
        last = 3 if not paused and i in (4,5,8,10) else -1
        step_focus = 'Pause' if proof == 'scrollfeedback' and i>=9 else focus
        visible = int(paused or (proof=='scrollfocus' and i==6) or (proof=='scrollfeedback' and i==9))
        rows.append(f'WQ_SCROLL_STEP proof={proof} step={i} key={key} down={0 if paused or i==1 else 1} up=0 offset={offset} end=1000 selected=0 submitted=1 correct=1 hint=1 paused={int(paused)} evaluations=1 focus={step_focus} textpercent=200 first=-1 last={last} focusvisible={visible}')
    if proof=='scrollfeedback': focus='Pause'
    rows.append(f'WQ_SCROLL_CAPTURE proof={proof} focus={focus} visible={int(paused)}')
    return '\n'.join(rows)


class ReadingScrollTests(unittest.TestCase):
    def test_complete_active_focus_and_paused_routes(self):
        for proof in ('scrollfeedback','scrollfocus','scrollpaused'):
            self.assertTrue(check_scroll_steps(trace(proof),proof)[0])

    def test_missing_duplicate_or_reordered_steps(self):
        log=trace()
        for bad in ('\n'.join(log.splitlines()[1:]),log+'\n'+log.splitlines()[0],log.replace('step=2','step=3')):
            self.assertFalse(check_scroll_steps(bad,'scrollfeedback')[0])

    def test_unhandled_or_inert_page_input(self):
        log=trace()
        self.assertFalse(check_scroll_steps(log.replace('down=1','down=0'),'scrollfeedback')[0])
        self.assertFalse(check_scroll_steps(log.replace('offset=900','offset=600'),'scrollfeedback')[0])

    def test_bad_bounds_or_hidden_last_line(self):
        log=trace()
        for bad in (log.replace('offset=1000','offset=1100'),log.replace('offset=0','offset=100'),log.replace('last=3','last=-1')):
            self.assertFalse(check_scroll_steps(bad,'scrollfeedback')[0])
        self.assertTrue(check_feedback_capture('WQ_FEEDBACK_CAPTURE proof=scrollfeedback visibility=3','scrollfeedback')[0])
        self.assertFalse(check_feedback_capture('WQ_FEEDBACK_CAPTURE proof=scrollfeedback visibility=2','scrollfeedback')[0])
        self.assertFalse(check_feedback_capture('WQ_FEEDBACK_CAPTURE proof=hint visibility=3','hint')[0])

    def test_attempt_focus_text_or_capture_drift(self):
        log=trace()
        for bad in (log.replace('evaluations=1','evaluations=2'),log.replace('hint=1','hint=0'),log.replace('focus=Screen','focus=Pause'),log.replace('textpercent=200','textpercent=100'),log.replace('WQ_SCROLL_CAPTURE','MISSING_CAPTURE')):
            self.assertFalse(check_scroll_steps(bad,'scrollfeedback')[0])

    def test_focus_return_requires_visible_control(self):
        self.assertFalse(check_scroll_steps(trace().replace('focusvisible=1','focusvisible=0'),'scrollfeedback')[0])
        self.assertFalse(check_scroll_steps(trace('scrollfocus').replace('focusvisible=1','focusvisible=0'),'scrollfocus')[0])

    def test_paused_input_cannot_move_reading_content(self):
        log=trace('scrollpaused')
        for bad in (log.replace('offset=600','offset=700',1),log.replace('down=0','down=1'),log.replace('visible=1','visible=0')):
            self.assertFalse(check_scroll_steps(bad,'scrollpaused')[0])


if __name__=='__main__': unittest.main()
