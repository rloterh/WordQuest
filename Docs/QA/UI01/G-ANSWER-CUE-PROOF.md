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
are committed. Clean Win64 package, native cue/regression checks and baseline
comparison are recorded below. Dedicated review remains in progress.

## Clean archive and runtime checks

Clean source `1a7a918292e23234a8af0bbdcf0484354a6c699a` passes Win64 Development
BuildCookRun in 181.59s, cooking all 521 packages. Archive:
`Artifacts/Packages/Win64/20261006-212658-614300/`. Its complete manifest records
unchanged head/worktree/inputs and SHA-256
`555ef5b2b32aaf33b42c0e3085a5a3948ce000506e7da709ba66b98145d1eb6f`.
All 49 payload hashes and sizes verify before each launch. Existing scoped
Private/Public LocalSubnet firewall refresh succeeds automatically on attempt
two at 21:30:35.2812687 UTC; no permission/task/ACL policy changes.

All 20 packaged captures pass with native/helper exit zero, clean matching
source/package provenance and requested dimensions. Every applicable state,
accessible cue label, actual text scale, action-content, cue geometry, pointer,
focus and reading-scroll predicate is true; no native Error/Fatal lines occur.
All 20 full PNGs were inspected at their native dimensions. All 15 focused cue
frames show the chosen marker and first label line inside the reading viewport;
native cue advances fit with positive horizontal label clearance. At 260px/200%
the correct cue has 29px advance in 30px reservation. This is desktop offscreen
geometry/visual evidence, not pixel ink certification or manual/phone acceptance.
Some long rows extend beyond the viewport; their first-line and cue proof does
not establish simultaneous whole-answer/result visibility.

The reference-size initial PNG is RGB-identical to PR #48's packaged
`20261006-141609-packaged-capture-initial`: zero changed pixels. Current PNG
SHA-256 is also unchanged:
`b323f60730f9627a2458bd664c1373117aabc7cf10da69ed99ce870d15ca321d`.
Thus the normal initial composition and earlier optical improvements are
preserved in this exact comparison. Original G hash remains
`306dae4f6352749edcf1d8edf73f26339a4ba6407b4a394ec50b5898418bedae`.
Raw protocols, per-case hashes and verification scripts remain ignored in
`Artifacts/QA/UI01/AnswerCue20261006/verification.json` and adjacent files.

Raw capture folders are under `Artifacts/QA/UI01/`:

| Capture run | Case | Dimensions / text |
|---|---|---|
| `20261006-213041-packaged-capture-initial` | Initial baseline | 884x1780 / 100% |
| `20261006-213056-packaged-capture-cueselected` | Visible selected C | 884x1780 / 100% |
| `20261006-213107-packaged-capture-cuecorrect` | Visible correct A | 884x1780 / 100% |
| `20261006-213117-packaged-capture-cuewrong` | Visible wrong B | 884x1780 / 100% |
| `20261006-213128-packaged-capture-cueselected` | Visible selected C | 390x844 / 200% |
| `20261006-213139-packaged-capture-cuecorrect` | Visible correct A | 390x844 / 200% |
| `20261006-213149-packaged-capture-cuewrong` | Visible wrong B | 390x844 / 200% |
| `20261006-213201-packaged-capture-cueselected` | Visible selected C | 260x640 / 200% |
| `20261006-213212-packaged-capture-cuecorrect` | Visible correct A | 260x640 / 200% |
| `20261006-213224-packaged-capture-cuewrong` | Visible wrong B | 260x640 / 200% |
| `20261006-213236-packaged-capture-cuelongselected` | Long visible selected C | 260x640 / 200% |
| `20261006-213247-packaged-capture-cuelongcorrect` | Long visible correct A | 260x640 / 200% |
| `20261006-213258-packaged-capture-cuelongwrong` | Long visible wrong B | 260x640 / 200% |
| `20261006-213310-packaged-capture-cuelongselected` | Long visible selected C | 390x844 / 200% |
| `20261006-213322-packaged-capture-cuelongcorrect` | Long visible correct A | 390x844 / 200% |
| `20261006-213333-packaged-capture-cuelongwrong` | Long visible wrong B | 390x844 / 200% |
| `20261006-213344-packaged-capture-pointerclick` | Routed virtual answer/check | 260x640 / 200% |
| `20261006-213358-packaged-capture-pointerresumed` | Routed virtual pause/resume | 260x640 / 200% |
| `20261006-213414-packaged-capture-longselectedfocus` | Long selected focus | 260x640 / 200% |
| `20261006-213426-packaged-capture-scrollfeedback` | Feedback reading end | 844x390 / 200% |

Safe-zone is 1 for reference-size cases and 0.9 otherwise; tooltips are disabled.
Long/scroll modes intrinsically use 200%. Routed virtual click verifies no
activation on down, exactly one evaluation on enabled up and no subsequent
disabled activation. Pause/resume and result-reading checks retain their existing
contracts. Focus/pointer captures do not replace manual platform accessibility.
Both Unreal Context tests pass with complete clean-source evidence in
`20261006-213441-automation-initial` (two succeeded, zero failed/not-run/in-progress).

## Missing-font fallback

With the genuine Bold reading FontFace temporarily omitted, inspected Editor
captures `20261006-213539-capture-initial` (884x1780/100%) and
`20261006-213609-capture-cuecorrect` (260x640, safe-zone 0.9, actual 200%) both
pass. The initial fallback is RGB-identical to PR #48's
`20261006-135717-capture-initial`; the enlarged correct cue has 29px advance in
30px reservation and positive label clearance. The new minimum measurement also
applies when the reading face is unavailable. The asset is restored unchanged at
SHA-256 `ddb17ec624e8c6e8d68b607cbbd14e5302111b07e158074cc101e69de0a78715`.
These deliberately missing-asset Editor runs have transient dirty-worktree status;
they are not clean-package/corrupt-package or phone evidence. Raw summary:
`Artifacts/QA/UI01/AnswerCue20261006/fallback.json`.

Full static type/art/material fidelity, UI02 motion, manual/platform accessibility,
draft fixture editorial approval, Android/phone, isolated offline, performance
and original release gates remain open. Windows phone-shaped captures are not
physical-device evidence. No later milestone, deployment or release; the owner
retains merge decisions.
