# G submitted-answer reading contrast

The owner merged [PR #25](https://github.com/rloterh/WordQuest/pull/25) into `dev`
at `2a9e372` on 2026-10-02, 19:27:41 UTC. Inspection of its final correct-state
capture found faded answer text, option letters and the result check. These remain
learning content after submission. Nine opaque-glyph/adjacent-background samples
measured 2.52–2.64:1, below even the 3:1 large-text engineering target in the
[acceptance specification](../../../Planning/WordQuest-UI-Realms-Addendum/docs/08-QA-and-Acceptance.md).

The bounded correction wraps each static answer row in `UReadingContentBox`.
Its Slate size box paints children without inherited disabled shading. The wrapper
is hit-test invisible; button enabled state, callbacks and navigation remain under
the existing button/attempt rules. Submitted buttons remain disabled and are
skipped by Tab. The normal layout and live text are preserved. There is no global
Slate setting or engine modification. Existing USizeBox slot/property/resource
handling is retained. Use this wrapper only for static reading content.

## Build and package

Clean implementation: `36972d16bc8577d5e50fb5f1bb62dbd71a9fc9e6`.
The real editor build passed, 6 actions, 63.44 seconds, exit 0:
`Artifacts/Logs/Build/WordQuestEditor-20261002-193933.log`.
The dirty-worktree preflight at `20261002-194116-capture-correct` passed and was
visually inspected; it is preliminary evidence, separate from the clean package.

Clean Win64 Development build/cook/stage/archive passed, UAT exit 0,
BuildCookRun 114.96 seconds. Editor preparation passed in 1.64 seconds; the real
Game target passed with 5 actions in 41.18 seconds. Package:
`Artifacts/Packages/Win64/20261002-194302-893747`.
Manifest SHA-256:
`a94032a087ac5eb47fd97a7efc84ed495d40069500545ab98c02084dfa133afa`.
All 48 payload hashes are recorded and verified before every packaged launch.
Head, worktree and input invariants pass. Outputs remain ignored.

## Native evidence

All 15 fresh packaged captures passed native exit, helper exit, requested
dimensions and their applicable state/cue/focus/reflow/scroll contracts. Every
PNG was visually inspected. Native logs contain no Error/Fatal lines. Raw batch
metadata: `Artifacts/QA/UI01/reading-contrast-batch.json`; reproduction script:
`reading-contrast-batch.py` in that directory. Run prefixes below are 20261002.

| Run | Proof / dimensions | Observed result |
|---|---|---|
| 194525 | initial, 884x1780 | Normal choices, no cue; PNG byte-identical to PR #25 |
| 194538 | selected, same | Neutral C marker and selection outline |
| 194548 | correct, same | Dark choice text, A–D and check; complete explanation |
| 194559 | wrong, same | Dark choice text and B cross; complete explanation |
| 194609 | hint, 390x844 | Assisted result, dark choices/check, full explanation |
| 194620 | correct, 390x844, 200% | Wrapped reading; visible lower choices and full explanation |
| 194631 | wrong, same, 200% | Visible B cross and full explanation |
| 194642 | hint, same, 200% | Assisted explanation fully visible; earlier rows scroll above viewport |
| 194652 | keydisabled, 390x844 | Submitted controls skipped; Pause/Resume preserves result and one evaluation |
| 194704 | keybuttons, same | Routed Space/Enter retains incorrect B and exactly one evaluation |
| 194715 | keyretry, same | Retry clears result/Hint; 200% selected A reveals its leading content |
| 194726 | keysubmit, same | Repeated routed Enter evaluates once |
| 194737 | interruptsubmitted, same | Assisted incorrect result survives synthetic interruptions/explicit Resume |
| 194748 | modalcycle, 260x200 | Shift/Tab and text toggle preserve visible, wrapped Pause controls |
| 194801 | scrollfeedback, 844x390 | Paging/boundary keys reach oversized explanation end |

Reference-size runs suppress tooltips for comparison. Other captures use normal
tooltips and simulated safe-area ratio .9. All keyboard/lifecycle events above
are synthetic native routes, not manual desktop/phone input. Large-text captures
prioritize feedback; they do not show every answer simultaneously. Oversized
content remains scrollable. The existing helper verifies actual text sizes,
accessible button labels, selection/result codepoints and visible leading content
on routes that require them; no new QA helper contract is introduced here.

Both `WordQuest.Context` Unreal tests passed at clean implementation, with
failed/notRun/inProcess zero, native exit 0:
`Artifacts/QA/UI01/20261002-194918-automation-initial`.
All 63 Python QA tests passed. Six original reference hashes, seven source/runtime
SVG pairs, LFS and whitespace checks passed. No binary asset was changed.

## Pixel measurements

The read-only analysis uses the actual packaged 884x1780 correct PNGs before/after.
Foreground samples are opaque glyph cores; backing samples are adjacent empty
pixels on the same row. RGB bytes are converted to linear sRGB using the .04045
threshold, then luminance `.2126 R + .7152 G + .0722 B`. Contrast is
`(lighter + .05) / (darker + .05)`. Coordinates are native top-left image pixels.
Raw RGB values, coordinates, image hashes and calculations are retained in
`Artifacts/QA/UI01/reading-contrast-analysis.json` and its `.py` reproduction file.

| Reading sample | Foreground x,y | Backing x,y | Before | After |
|---|---|---|---|---|
| Choice A | 546,1048 | 546,1064 | 2.640 | 11.773 |
| Choice B | 436,1160 | 436,1177 | 2.603 | 11.749 |
| Choice C | 455,1272 | 455,1289 | 2.596 | 11.577 |
| Choice D | 285,1385 | 285,1401 | 2.616 | 11.684 |
| Correct symbol | 231,1028 | 231,1064 | 2.517 | 12.220 |
| Option A | 167,1040 | 167,1063 | 2.543 | 9.763 |
| Option B | 174,1149 | 174,1175 | 2.545 | 9.763 |
| Option C | 165,1261 | 165,1287 | 2.570 | 9.763 |
| Option D | 179,1374 | 179,1400 | 2.559 | 9.763 |

All nine after foregrounds are `(24,20,83)`. These samples meet 4.5:1; they are
bounded static measurements, not a whole-screen contrast or accessibility pass.
No measurement of unseen glyphs, disabled action labels, motion extrema or
physical displays is inferred. The initial PNG has zero changed pixels and SHA-256
`7aa62165b992c5599f993e3947bc5572ce901fde239e1290a34920addec1b99e`.
Correct-state changes cover 29,458 pixels, bounding box `[137,1004,693,1410)`, all
inside the four existing answer-row rectangles. Pixels outside those rows are
unchanged. Final correct PNG SHA-256:
`ac9fdf62ae8f5866a6f10d92656732af0a26e7d4882d74100c83a4bc19d338ae`.
The baseline is PR #25's `20261002-184028-packaged-capture-correct`.

## Remaining gates

Candidate art/lettering, the draft EQUIVOCAL fixture and prototype `3 / 7` remain
unapproved. Manual pointer/touch, OS interruptions, screen-reader/platform
accessibility, full contrast audit, phone/offline behavior and performance remain
unverified. Android engine support receipt is still absent; adb lists no device
on this turn's recheck. UI01 fidelity, UI02 motion and release acceptance remain
open. The owner retains merge authority; no game deployment or release occurs.

Dedicated read-only Codex review completed at clean
`412a2af6d0d63133dbf323ceebfd374167061a9c` against actual `origin/dev`,
`2a9e372515407643c91bdbbdc261a1e8ccbe2162`, with exit 0 and no actionable
introduced defects. Head/worktree stayed unchanged. The reviewer checked the
paint override, Unreal size-box ownership/slot handling and declared evidence;
it did not independently repeat builds or runtime checks. Raw review evidence:
`Artifacts/Reviews/20261002-195153`. Subsequent review/publication records change
documentation only; the clean packaged source above remains the implementation.
Published as regular [PR #26](https://github.com/rloterh/WordQuest/pull/26)
against `dev`; no agent merge was performed.
The owner merged it into `dev` at `e2ef2b0` on 2026-10-02, 20:00:20 UTC.
