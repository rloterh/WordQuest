# G visible answer cue proof

PR #48 is owner-merged at `e931166` (2026-10-06, 21:08:14 UTC). Its enlarged
selected/correct captures sometimes leave the chosen row offscreen, as disclosed
in [answer alignment](G-ANSWER-LABEL-ALIGNMENT.md). This bounded UI01 increment
adds direct native cue visibility checks and fixes the concrete width shortage
they exposed. No new assets, supplied-reference edits or editorial approval.

## Failure and correction

Real Editor build before the correction succeeds in 34.69s. Native preflight
`20261006-212111-capture-cuecorrect` at 260x640, safe-zone 0.9 and actual 200%
text exits zero but its evidence is incomplete: check-mark U+2713 measures 29px
wide while its reserved marker width is 18px. Marker left is 89.265, label left
107.265; the advance extends 11px into label space. The PNG was inspected and
the new geometry predicate correctly rejects it. The label and marker have
different vertical positions; this does not claim an 11px ink overlap on every
line. The defect is insufficient horizontal reservation for the native cue.

Runtime reserves the maximum native advance of `>`, U+2713 and U+00D7 using
the marker's actual Slate font, plus max(2 viewport-scaled units, 1px) clearance.
The existing reference-scaled reservation and 18px minimum remain lower bounds.
All cues are measured before laying out every row, including unselected rows,
so selection/submission does not change reserved width. Actual available width
continues to feed label wrapping and row growth. Font floors, font parameters,
reading-face optical padding and learning/control handlers remain unchanged.
The narrow case necessarily wraps labels into more lines; scrolling remains
required. Full responsive readability/accessibility is a separate gate.

Real corrected Editor build `WordQuestEditor-20261006-212443.log` passes in
12.38s. Inspected preflight `20261006-212456-capture-cuecorrect` passes with
29px advance, 30px reservation and label left 119.265, leaving 1px clearance.
Long correct preflight `20261006-212535-capture-cuelongcorrect` also passes at
260x640/200%. These dirty-worktree preflights diagnose the correction; clean
packaged evidence follows separately.

## Evidence protocol and limits

Capture-only Development harness modes are `cueselected`, `cuecorrect`,
`cuewrong` and their `cuelong*` variants. Selected uses C with `>`; correct uses
A with U+2713; wrong uses B with U+00D7. Submitted buttons remain disabled.
The long variants install existing draft long fixtures and use 200% text.
After direct state setup, a delayed `ScrollWidgetIntoView(...TopOrLeft)` reveals
the chosen row, then capture waits another layout interval. This is explicit
capture setup, not routed input, keyboard focus, manual scrolling or touch proof.
All harness methods, traces and timers are excluded from Shipping; the width
correction is ordinary runtime code.

`WQ_ANSWER_CUE_CAPTURE` records option, codepoint, actual text percentage,
button enable state, marker rectangle, native measured advance/line height,
label's first-line layout rectangle and ScrollBox viewport. Glyph width/height
are font-service metrics, not pixel ink bounds. The helper requires exactly one
ordered complete record, expected state/identity, finite positive geometry,
marker and first line wholly inside the viewport, advance/height fitting the
marker and advance ending before the label. Tolerance is 0.5 physical pixels.
This first-line test supports oversized rows; it does not assert the entire
answer or feedback is visible simultaneously. Result-reading and routed-input
regressions use their separate existing modes.

Fourteen new synthetic rejection tests exercise missing/duplicate/malformed
records, wrong identity/text size/enable state, nonfinite/nonpositive geometry,
clipping, overlap, the original 18px failure and capture-only CLI enforcement.
All 96 Python QA tests pass in 0.721s; log:
`Artifacts/Logs/UI01/answer-cue-python-checks.log`. Six original reference
hashes/dimensions and ten source/runtime SVG parity checks pass. No binary assets
are committed. Clean Win64 package, native cue/regression checks, baseline
comparison and dedicated review remain in progress.

Full static type/art/material fidelity, UI02 motion, manual/platform accessibility,
draft fixture editorial approval, Android/phone, isolated offline, performance
and original release gates remain open. Windows phone-shaped captures are not
physical-device evidence. No later milestone, deployment or release; the owner
retains merge decisions.
