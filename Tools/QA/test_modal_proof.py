"""Reject modal evidence with hidden controls or changed attempt/navigation state."""
import unittest
from Tools.QA.run_g_proof import check_modal_steps


def trace(proof='modalcycle'):
    keys=['start','Tab','SpaceBar','Tab','Tab','Tab','Tab','Tab','Tab','Tab']
    focuses=['Resume','TextSize','TextSize','Reset','Resume','Reset','TextSize','Resume','TextSize','Reset']
    if proof=='modalresume': keys+=['Tab','SpaceBar']; focuses+=['Resume','Pause']
    if proof=='modalretry': keys+=['SpaceBar','Tab','SpaceBar']; focuses+=['Screen','Answer0','Answer0']
    rows=[]
    for i,(key,focus) in enumerate(zip(keys,focuses)):
        state=(0,1,1,1,1,1)
        if proof=='modalresume' and i==11: state=(0,1,1,1,0,1)
        if proof=='modalretry' and i>=10: state=(0 if i==12 else -1,0,0,0,0,0)
        selected,submitted,correct,hint,paused,evaluations=state
        rows.append(f'WQ_MODAL_STEP proof={proof} step={i+1} key={key} down={int(i>0)} up={int(key=="SpaceBar")} shift={int(5<=i<=7)} selected={selected} submitted={submitted} correct={correct} hint={hint} paused={paused} evaluations={evaluations} focus={focus} textpercent={100 if i<2 else 200} visible={int(focus!="Screen")} fits=1 answerstart={int(focus=="Answer0")} oversized=0')
    rows.append(f'WQ_MODAL_CAPTURE proof={proof} focus={focuses[-1]} visible=1 fits=1 answerstart={int(focuses[-1]=="Answer0")} oversized=0')
    return '\n'.join(rows)


class ModalProofTests(unittest.TestCase):
    def test_complete_cycle_resume_and_retry_routes(self):
        for proof in ('modalcycle','modalresume','modalretry'):
            self.assertTrue(check_modal_steps(trace(proof),proof)[0])

    def test_hidden_control_or_clipped_label(self):
        for bad in (trace().replace('visible=1','visible=0'),trace().replace('fits=1','fits=0')):
            self.assertFalse(check_modal_steps(bad,'modalcycle')[0])

    def test_missing_duplicate_or_reordered_input(self):
        log=trace()
        for bad in ('\n'.join(log.splitlines()[1:]),log+'\n'+log.splitlines()[0],log.replace('step=2','step=3')):
            self.assertFalse(check_modal_steps(bad,'modalcycle')[0])

    def test_unhandled_input_or_missing_button_release(self):
        log=trace()
        for bad in (log.replace('down=1','down=0'),log.replace('up=1','up=0')):
            self.assertFalse(check_modal_steps(bad,'modalcycle')[0])

    def test_focus_shift_text_or_attempt_drift(self):
        for bad in (trace().replace('focus=Reset','focus=Resume'),trace().replace('shift=1','shift=0'),trace().replace('textpercent=200','textpercent=100'),trace().replace('evaluations=1','evaluations=2')):
            self.assertFalse(check_modal_steps(bad,'modalcycle')[0])

    def test_incomplete_capture_or_wrong_final_state(self):
        for proof in ('modalcycle','modalresume','modalretry'):
            self.assertFalse(check_modal_steps(trace(proof).replace('WQ_MODAL_CAPTURE','MISSING'),proof)[0])
        self.assertFalse(check_modal_steps(trace('modalresume').replace('paused=0','paused=1'),'modalresume')[0])
        self.assertFalse(check_modal_steps(trace('modalretry').replace('hint=0','hint=1'),'modalretry')[0])

    def test_oversized_retry_answer_requires_visible_leading_content(self):
        log=trace('modalretry').replace('visible=1 fits=1 answerstart=1 oversized=0','visible=0 fits=1 answerstart=1 oversized=1')
        self.assertTrue(check_modal_steps(log,'modalretry')[0])
        self.assertFalse(check_modal_steps(log.replace('answerstart=1','answerstart=0'),'modalretry')[0])
        self.assertFalse(check_modal_steps(log.replace('oversized=1','oversized=0'),'modalretry')[0])


if __name__=='__main__': unittest.main()
