"""Reject long-answer captures that omit or fail the leading-content evidence."""
import unittest
from Tools.QA.run_g_proof import check_answer_start


TRACE = 'WQ_ANSWER_START proof=longfocus focus=Answer1 textpercent=200 visible=1 oversized=1'


class AnswerStartTraceTests(unittest.TestCase):
    def test_visible_oversized_or_fitting_answer(self):
        self.assertTrue(check_answer_start(TRACE, 'longfocus')[0])
        self.assertTrue(check_answer_start(TRACE.replace('oversized=1', 'oversized=0'), 'longfocus')[0])

    def test_clipped_or_missing_leading_content(self):
        self.assertFalse(check_answer_start(TRACE.replace('visible=1', 'visible=0'), 'longfocus')[0])
        self.assertFalse(check_answer_start('WQ_STATE proof=longfocus selected=-1 submitted=0', 'longfocus')[0])

    def test_wrong_focus_scale_or_proof(self):
        for original, replacement in [('Answer1', 'Answer0'), ('200', '100'), ('longfocus', 'long')]:
            self.assertFalse(check_answer_start(TRACE.replace(original, replacement), 'longfocus')[0])

    def test_extra_or_invalid_metadata(self):
        self.assertFalse(check_answer_start(TRACE + '\n' + TRACE, 'longfocus')[0])
        self.assertFalse(check_answer_start(TRACE.replace('oversized=1', 'oversized=2'), 'longfocus')[0])

    def test_selected_answer_mode(self):
        self.assertTrue(check_answer_start(TRACE.replace('longfocus', 'longselectedfocus'), 'longselectedfocus')[0])


if __name__ == '__main__':
    unittest.main()
