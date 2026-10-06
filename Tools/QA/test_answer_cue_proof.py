"""Synthetic evidence rejection checks; these are not runtime/device proof."""
import subprocess
import sys
import unittest
from pathlib import Path
from Tools.QA.run_g_proof import check_answer_cue_geometry


# Independent fixture based on the observed 260px native capture. The original
# 18px reservation was smaller than its 29px check-mark advance.
TRACE = ('WQ_ANSWER_CUE_CAPTURE proof=cuecorrect option=0 codepoint=10003 textpercent=200 enabled=0 '
         'markerleft=89.265 markertop=86.735 markerright=119.265 markerbottom=121.735 '
         'glyphwidth=29.000 glyphheight=34.000 '
         'labelleft=119.265 labeltop=36.765 labelright=207.794 labelbottom=69.765 '
         'clipleft=13.000 cliptop=32.000 clipright=247.000 clipbottom=608.000')


class AnswerCueEvidenceTests(unittest.TestCase):
    def rejected(self, trace, proof='cuecorrect', percent=200):
        self.assertFalse(check_answer_cue_geometry(trace, proof, percent)[0])

    def test_visible_correct_and_raw_geometry(self):
        passed, row = check_answer_cue_geometry(TRACE, 'cuecorrect', 200)
        self.assertTrue(passed)
        self.assertEqual(row['glyphwidth'], '29.000')

    def test_all_cue_states_and_long_variants(self):
        for name, option, code, enabled in [('selected', 2, 62, 1), ('correct', 0, 10003, 0), ('wrong', 1, 215, 0)]:
            for prefix in ['cue', 'cuelong']:
                proof = prefix + name
                trace = TRACE.replace('proof=cuecorrect', 'proof=' + proof).replace('option=0', 'option=' + str(option))
                trace = trace.replace('codepoint=10003', 'codepoint=' + str(code)).replace('enabled=0', 'enabled=' + str(enabled))
                with self.subTest(proof=proof):
                    self.assertTrue(check_answer_cue_geometry(trace, proof, 200)[0])

    def test_actual_text_size_required(self):
        self.rejected(TRACE, percent=100)
        self.assertTrue(check_answer_cue_geometry(TRACE.replace('textpercent=200', 'textpercent=100'), 'cuecorrect', 100)[0])

    def test_missing_duplicate_and_extra_fields(self):
        for trace in ['', TRACE + '\n' + TRACE, TRACE.rsplit(' ', 1)[0], TRACE + ' extra=1']:
            self.rejected(trace)

    def test_reordered_or_duplicate_keys(self):
        self.rejected(TRACE.replace('option=0 codepoint=10003', 'codepoint=10003 option=0'))
        self.rejected(TRACE.replace('labelleft=119.265', 'markerleft=119.265'))

    def test_wrong_identity_or_enable_state(self):
        for old, new in [('proof=cuecorrect', 'proof=cuewrong'), ('option=0', 'option=1'),
                         ('codepoint=10003', 'codepoint=62'), ('enabled=0', 'enabled=1'), ('enabled=0', 'enabled=2')]:
            with self.subTest(new=new):
                self.rejected(TRACE.replace(old, new))
        self.rejected(TRACE, proof='unknown')

    def test_malformed_and_nonfinite_geometry(self):
        for value in ['NaN', 'inf', '-inf', 'bad', '']:
            self.rejected(TRACE.replace('glyphwidth=29.000', 'glyphwidth=' + value))

    def test_original_narrow_width_failure(self):
        self.rejected(TRACE.replace('markerright=119.265', 'markerright=107.265').replace('labelleft=119.265', 'labelleft=107.265'))

    def test_glyph_cannot_overlap_label_even_if_box_fits(self):
        self.rejected(TRACE.replace('labelleft=119.265', 'labelleft=115.000'))

    def test_positive_glyph_and_rectangles_required(self):
        for old, new in [('glyphwidth=29.000', 'glyphwidth=0'), ('glyphheight=34.000', 'glyphheight=-1'),
                         ('markerright=119.265', 'markerright=89.265'), ('labelbottom=69.765', 'labelbottom=36.765'),
                         ('clipright=247.000', 'clipright=13.000')]:
            self.rejected(TRACE.replace(old, new))

    def test_glyph_height_must_fit(self):
        self.rejected(TRACE.replace('glyphheight=34.000', 'glyphheight=36.000'))

    def test_marker_and_label_must_be_inside_clip(self):
        for old, new in [('clipleft=13.000', 'clipleft=90'), ('cliptop=32.000', 'cliptop=40'),
                         ('clipright=247.000', 'clipright=200'), ('clipbottom=608.000', 'clipbottom=100')]:
            self.rejected(TRACE.replace(old, new))

    def test_half_pixel_rounding_tolerance(self):
        self.assertTrue(check_answer_cue_geometry(TRACE.replace('cliptop=32.000', 'cliptop=37.000'), 'cuecorrect', 200)[0])
        self.rejected(TRACE.replace('cliptop=32.000', 'cliptop=37.500'))

    def test_cue_proofs_cannot_be_reported_as_automation(self):
        helper = Path(__file__).with_name('run_g_proof.py')
        result = subprocess.run([sys.executable, str(helper), 'automation', '--proof', 'cuecorrect'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertIn('Answer cue proofs require capture mode.', result.stderr)


if __name__ == '__main__':
    unittest.main()
