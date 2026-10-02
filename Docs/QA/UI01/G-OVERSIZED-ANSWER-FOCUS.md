# G oversized-answer focus correction

This bounded UI01 correction follows the tested badge candidate in PR #15.
The owner reported a merge, but GitHub still reports that PR open; the follow-up
is stacked on `feature/g-answer-badge-material` at `cc1d584` until that merge is
confirmed. No agent merge is authorized. Its actual PR base must be used for review.

## Failure and resulting behavior

At 844x390 with 200% text and the existing artificial long-answer fixture, native
focus on B revealed the end of the row. Its option letter and beginning were
clipped above the viewport. Prior packaged evidence:
`Artifacts/QA/UI01/20261002-082958-packaged-capture-longfocus`; the previous-font
package comparison in `20261002-083402-packaged-capture-longfocus` reproduces
the same layout. These were state/dimension checks, not full-row visibility passes.

An answer taller than the reading viewport now reveals its top when focused.
The badge and selection marker align at the start of that oversized row; the live
answer remains fully scrollable. Fitting rows retain centered identifiers and
minimal IntoView scrolling. No font, row width/height, normal reference layout,
learning fixture, scoring, asset or image changes are made. This does not squeeze
an entire oversized answer into the window or claim full-row visibility.

The reveal helper uses the canvas slot's measured control height. Offscreen cached
widget geometry was stale (30 pixels for a measured 668.64-pixel row), so it cannot
reliably choose the scroll destination before reveal. The next-tick focus recheck
also prevents Slate's automatic focus-scroll request from replacing the explicit
destination. Feedback reveal retains priority unless a deliberate control focus
move supersedes it, including returning from Pause. This prevents a pending old
feedback request from scrolling the focused Pause control offscreen.
Hovered keyboard-focused controls retain their navy focus outline rather than
switching to the ordinary gold hover outline.

## Verification contract

Development-only native `longfocus` / `longselectedfocus` capture metadata now
records Answer1 focus, 200% setting, oversized state and leading-content visibility.
Visibility checks the full badge, first-line rectangle using the engine font
measure service and, when selected, the existing marker against the reading clip
with a one-pixel rounding allowance. It does not treat the whole oversized row as
visible. The capture helper rejects missing/duplicate, clipped or wrong-focus/scale
records even if the attempt tuple is correct. Five negative-path Python tests
exercise these failures; all 27 Python tests pass.

The selected mode uses the existing synthetic fixture and programmatic selection/
focus. It is not an OS keyboard, pointer/touch or screen-reader acceptance test.
Existing `key*` modes remain separate native Slate event-routing evidence.

## Preliminary native evidence

Early dirty landscape runs `20261002-085440-capture-longfocus`,
`20261002-085832-capture-longfocus` and `20261002-090222-capture-longfocus` correctly
failed the new leading-visibility gate despite game exit 0 and matching state.
The first two revisions still used stale geometry; temporary diagnostic logging
in the third established the 30-pixel cache mismatch. That logging is removed.
The corrected dirty `20261002-090418-capture-longfocus` passed and was inspected:
full B badge and first line visible, remainder extends below the viewport.

After stacking onto the unchanged badge candidate, clean source
`767e387f62634d7250b674dac9347e0667633823` passes the real editor build (six actions,
14.33 seconds, exit 0), log
`Artifacts/Logs/Build/WordQuestEditor-20261002-090641.log`.
Clean native `20261002-090656-capture-longselectedfocus` passes dimensions/state
and the new leading-visibility gate at 844x390, 200%, selected B without evaluation.
Direct inspection shows the SVG badge, selected ring, marker, beginning and focused
row outline visible together.

The first clean package at source `4e7efa2`,
`Artifacts/Packages/Win64/20261002-091044-759959`, passed building/cooking/archive
but its regression batch exposed the pending-feedback conflict in
`20261002-091637-packaged-capture-keydisabled`: state/key/focus-name checks passed,
while final Pause visibility failed. It is not the final passing regression package.
The focus callback now cancels that older pending reveal. Dirty native retest
`20261002-092001-capture-keydisabled` passes all state/key/focus/visibility checks
at 390x844 with simulated 0.9 inset. The remaining explanation is retained;
normal submission still requests its feedback reveal.

The helper's optional `--no-tooltips` applies the verified engine console variable
`Slate.EnableTooltips 0` only to comparison captures. Preliminary native capture
had a desktop pointer tooltip over part of the badge; comparison frames suppress
that overlay so viewport-bound evidence can be inspected clearly. Ordinary launches
and keyboard-route captures retain their normal tooltip behavior. This option is
not a tooltip interaction or physical-input pass. Exact flags remain in raw metadata.

Final clean package/regression captures and dedicated review are pending. Raw
captures/logs remain local and ignored under `Artifacts`.

## Remaining gates

The rest of an oversized answer requires scrolling. Manual reading/navigation,
physical input, screen-reader, art fidelity, editorial fixture approval, phone/
offline, performance, UI02 motion and release gates remain open. The prototype
still has one draft EQUIVOCAL question and fixture `3 / 7` progress.
