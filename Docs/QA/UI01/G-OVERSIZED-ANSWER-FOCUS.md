# G oversized-answer focus correction

This bounded UI01 correction follows the tested badge candidate in PR #15.
The owner reported a merge, but GitHub still reports that PR open; the follow-up
is stacked on `feature/g-answer-badge-material` at `cc1d584` until that merge is
confirmed. No agent merge is authorized. Its actual PR base must be used for review.
[PR #16](https://github.com/rloterh/WordQuest/pull/16) is a draft against that
branch. Once #15 is verified merged, retarget #16 to `dev` and check/review its
actual base before marking it ready. Draft status records this dependency.

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

## Final clean verification

Final implementation source `7e68d60696cf443c0cf2c950d37f02528e06973d` passes
the real editor target and Game target (three Game actions, 15.27 seconds), then
full Win64 build/cook/stage/archive (UAT 74.29 seconds, exit 0). Package:
`Artifacts/Packages/Win64/20261002-092241-088002`. The 48 recorded payload hashes,
head, worktree and input consistency checks pass. Manifest SHA-256:
`0f11d792997ce0ae4eb06d998634f3d9bae43dfbcd543e73871a1a905e9aad2e`.

All 24 packaged captures at that clean head pass their dimension/state contracts;
13 keyboard routes pass, including six focus-route/final-visibility contracts.
All six 200% long-answer leading-visibility checks pass. Raw batch evidence:
`Artifacts/QA/UI01/G-Oversized-Answer-Final-Batch.json`. Two native context tests
pass, zero failed/not run, in `20261002-092955-automation-initial` (exit 0).
All 27 Python tests pass; all six supplied reference hashes remain unchanged.
Git LFS is available; no binary assets or generated project files changed.

Fourteen final native PNGs were directly inspected, using the following directories
under `Artifacts/QA/UI01`. Other capture results are trace checks, not additional
visual-inspection claims.

| Capture directory | Inspected result |
| --- | --- |
| `20261002-092553-packaged-capture-keydisabled` | Returned Pause is visible and focused after submission. |
| `20261002-092603-packaged-capture-initial` | Normal 884x1780 layout retained. |
| `20261002-092613-packaged-capture-focus` | Fitting B row fully visible in landscape. |
| `20261002-092623-packaged-capture-longfocus` | Oversized B badge and first line visible in landscape. |
| `20261002-092633-packaged-capture-longselectedfocus` | Oversized B badge, selected marker and first line visible. |
| `20261002-092643-packaged-capture-longfocus` | Fitting 200% portrait B starts inside the reading clip. |
| `20261002-092652-packaged-capture-longselectedfocus` | Fitting portrait B retains centered selected identifier. |
| `20261002-092702-packaged-capture-longfocus` | 260x640 fitting B remains readable by wrapping/scrolling. |
| `20261002-092712-packaged-capture-longselectedfocus` | Narrow fitting B retains selected identifier. |
| `20261002-092723-packaged-capture-actions` | 200% Hint/Check controls visible. |
| `20261002-092803-packaged-capture-keymodal` | Paused text-size control visible and focused. |
| `20261002-092813-packaged-capture-keyretry` | Selected 200% A and first line visible after retry. |
| `20261002-092936-packaged-capture-correct` | Correct feedback starts below controls; further explanation requires scrolling. |
| `20261002-092946-packaged-capture-hint` | Hint-used state and feedback start retained. |

Read-only comparison with PR #15's `20261002-082919-packaged-capture-initial`
finds zero changed RGB pixels and byte-identical normal-size PNGs, SHA-256
`7d43a02275a016f9c2fbf9ed4a37727f64cf94a776c60e6740975e761ee297c0`.
Comparison evidence: `Artifacts/QA/UI01/G-Oversized-Answer-Normal-Comparison.json`.
This establishes baseline preservation, not fidelity approval against original art.
Raw captures/logs remain local and ignored under `Artifacts`.

Dedicated read-only Codex review completed with exit 0 at clean head
`475ecb31974f77a9605bee8158bb7e748642fb43` against the actual stacked base
`origin/feature/g-answer-badge-material`, SHA
`cc1d584785720e6a93eb5df16821acbd0ca0ee05`. It reported no actionable introduced
defects; head and worktree remained unchanged. Raw report:
`Artifacts/Reviews/20261002-093502`. The reviewer did not independently reproduce
Unreal builds or runtime captures. Subsequent review/publication records change
documentation only; `Game` remains identical to the verified package source.

## Remaining gates

The rest of an oversized answer requires scrolling. Manual reading/navigation,
physical input, screen-reader, art fidelity, editorial fixture approval, phone/
offline, performance, UI02 motion and release gates remain open. The prototype
still has one draft EQUIVOCAL question and fixture `3 / 7` progress.
