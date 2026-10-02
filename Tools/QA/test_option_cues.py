"""Reject premature correctness, stale retry/result markers and semantic drift."""
import unittest
from Tools.QA.run_g_proof import check_option_cues, check_feedback_capture, check_large_text_capture


def trace(proof, selected=-1, code=0, prefix=''):
    return '\n'.join(f'WQ_OPTION_CUE proof={proof} option={i} codepoint={code if i == selected else 0} label={prefix if i == selected else ""}Option {chr(65+i)}. Choice text' for i in range(4))


class OptionCueTests(unittest.TestCase):
    def test_large_text_rejects_wrong_proof_or_duplicate(self):
        log = 'WQ_TEXT_CAPTURE proof=correct textpercent=200'
        self.assertTrue(check_large_text_capture(log, 'correct')[0])
        self.assertFalse(check_large_text_capture(log, 'wrong')[0])
        self.assertFalse(check_large_text_capture(log+'\n'+log, 'correct')[0])

    def test_feedback_visible_or_oversized_first_line(self):
        for value in (1,2):
            self.assertTrue(check_feedback_capture(f'WQ_FEEDBACK_CAPTURE proof=hint visibility={value}', 'hint')[0])

    def test_feedback_clipped_or_missing(self):
        for value in (-1,0):
            self.assertFalse(check_feedback_capture(f'WQ_FEEDBACK_CAPTURE proof=hint visibility={value}', 'hint')[0])
        self.assertFalse(check_feedback_capture('', 'hint')[0])

    def test_feedback_wrong_proof_or_duplicate(self):
        log='WQ_FEEDBACK_CAPTURE proof=hint visibility=1'
        self.assertFalse(check_feedback_capture(log.replace('proof=hint','proof=correct'), 'hint')[0])
        self.assertFalse(check_feedback_capture(log+'\n'+log, 'hint')[0])

    def test_unselected_and_neutral_selection(self):
        self.assertTrue(check_option_cues(trace('initial'), 'initial', (-1,0,0,0,0,0))[0])
        self.assertTrue(check_option_cues(trace('selected',2,62,'Selected. '), 'selected', (2,0,0,0,0,0))[0])

    def test_submitted_correct_and_near_miss(self):
        self.assertTrue(check_option_cues(trace('correct',0,10003,'Correct. '), 'correct', (0,1,1,0,0,1))[0])
        self.assertTrue(check_option_cues(trace('wrong',1,215,'Not quite. '), 'wrong', (1,1,0,0,0,1))[0])

    def test_no_correctness_before_submit(self):
        self.assertFalse(check_option_cues(trace('selected',2,10003,'Correct. '), 'selected', (2,0,0,0,0,0))[0])

    def test_result_and_retry_cannot_keep_stale_marker(self):
        self.assertFalse(check_option_cues(trace('correct',0,62,'Selected. '), 'correct', (0,1,1,0,0,1))[0])
        self.assertFalse(check_option_cues(trace('initial',0,10003,'Correct. '), 'initial', (-1,0,0,0,0,0))[0])

    def test_wrong_result_or_semantics(self):
        self.assertFalse(check_option_cues(trace('wrong',1,10003,'Correct. '), 'wrong', (1,1,0,0,0,1))[0])
        self.assertFalse(check_option_cues(trace('correct',0,10003,'Selected. '), 'correct', (0,1,1,0,0,1))[0])
        self.assertFalse(check_option_cues(trace('initial').replace('Choice text',''), 'initial', (-1,0,0,0,0,0))[0])

    def test_missing_duplicate_or_wrong_option(self):
        log=trace('initial')
        self.assertFalse(check_option_cues('\n'.join(log.splitlines()[1:]), 'initial', (-1,0,0,0,0,0))[0])
        self.assertFalse(check_option_cues(log+'\n'+log.splitlines()[0], 'initial', (-1,0,0,0,0,0))[0])
        self.assertFalse(check_option_cues(log.replace('option=1','option=0'), 'initial', (-1,0,0,0,0,0))[0])


if __name__ == '__main__':
    unittest.main()
