# G answer outcome cues and feedback reveal

After owner-merged PR #21 (`7e100c2`), this bounded G UI01 correction makes
selection and submission distinguishable on the live answer row. An unsubmitted
selection keeps `>`; a submitted correct choice shows a check, and a submitted
incorrect choice shows a cross. Unselected rows have no cue. Actual Slate button
accessible text uses `Selected.`, `Correct.` or `Not quite.`, followed by the
option letter and current choice text. Retry clears result cues; an interruption
and explicit Resume preserve the submitted result. Evaluation remains once per
attempt. Symbols supplement the existing selection outline and explanation.

Native inspection also found a partly clipped explanation at 390x844. The old
feedback scroll request used descendant geometry before reflow had settled.
The corrected reveal runs after layout, using the measured feedback canvas slot
and viewport height. Feedback that fits is fully revealed; oversized feedback
starts at its first line and remains scrollable. A deliberate control focus move
supersedes pending feedback scrolling, including restoring Pause-button focus.

Art, fonts, draft EQUIVOCAL fixture, scoring and engine-generated project files
are unchanged. The displayed `3 / 7` remains a fixture. This adds no campaign
progress, editorial approval, motion or release behavior.

## Build and package

Final clean implementation: `afb941f4642e135aac072d6d641fd03de707c4d2`.
Real editor build passed with 4 actions in 14.46 seconds, exit 0:
`Artifacts/Logs/Build/WordQuestEditor-20261002-142136.log`.
Clean package preparation rebuilt editor metadata/link outputs with 3 actions in
8.05 seconds: `...-142511.log`.

Full clean Win64 Development build/cook/stage/archive passed, UAT exit 0,
BuildCookRun 137.88 seconds. Game target: 5 actions, 33.93 seconds.
Package: `Artifacts/Packages/Win64/20261002-142511-832372`.
Manifest SHA-256:
`b3124ba778a47594081760d8595cec9f7a4282167c213caa57bbdf0ffd0998e4`.
All 48 archived payload hashes are recorded and verified before each launch.
Head, worktree and input invariants pass. Build output remains ignored.

An earlier editor build (`...-141934.log`) failed because local variable `Slot`
shadowed the inherited widget member. Renaming it to `FeedbackSlot` fixed the
compiler error. The preliminary package at `20261002-140858-287800` and its
13 captures (`G-Outcome-Batch.json`) predate the feedback correction and are
excluded from final acceptance. The clipped assisted explanation is visible in
`20261002-141328-packaged-capture-hint/native.png`; the dirty-worktree editor
preflight at `20261002-142300-capture-hint` confirmed the correction before the
final clean package.

## Native verification

All 14 fresh packaged captures pass their helper/state/dimensions/exit contracts
at the final clean implementation. All PNGs were visually inspected. Actual
UTextBlock marker codepoints and actual Slate accessible text are checked for all
four answer buttons. Feedback capture checks require full visibility when it fits,
or visibility of the first line when oversized. Existing keyboard, focus,
answer-start and lifecycle contracts also pass where applicable.

Runs are under `Artifacts/QA/UI01`; batch metadata is `G-Outcome-Final-Batch.json`.

| Run prefix (20261002-) | Proof / dimensions | Evidence |
|---|---|---|
| 143216 | initial, 884x1780 | Four empty cues; initial PNG byte-identical to PR #21 |
| 143239 | selected, same | Neutral `>` on option C; no premature correctness |
| 143253 | correct, same | Check on A, `Correct.` semantics, complete explanation |
| 143307 | wrong, same | Cross on B, `Not quite.` semantics, complete explanation |
| 143322 | hint, 390x844, simulated safe-area .9 | Assisted correct check; full five-line explanation visible |
| 143335 | empty, same | No selection/result cue; choose-answer instruction fully visible |
| 143349 | keysubmit, same | Routed Enter submits once despite repeat; complete explanation |
| 143404 | keybuttons, same | Routed Space/Enter produces one incorrect evaluation; cross and complete explanation |
| 143418 | keyretry, same | 200% text/retry route clears prior check and Hint; neutral selected A visible |
| 143431 | interruptsubmitted, same | Assisted incorrect result and cross survive notifications/explicit Resume; Pause focus restored, one evaluation |
| 143444 | keydisabled, same | Submitted correct check survives disabled-control traversal and Pause/Resume; Pause remains visible |
| 143457 | large, same | Existing 200% unselected layout retained; no result cue |
| 143510 | longselectedfocus, 260x640, simulated safe-area .9 | Existing 200% long option B retains neutral cue, letter and visible answer start |
| 143524 | keyhint, 200x200, simulated safe-area .5 | Oversized assisted explanation reveals its first line; routed state and check metadata pass |

The first four reference-size captures suppress tooltips for comparison; other
captures use normal tooltips. The final 100x100 safe-area viewport is an extreme
synthetic boundary check, not a supported phone size or physical-device result.
The final two submitted Pause-focus captures intentionally prioritize the focused
control over keeping the explanation visible. They do not claim feedback visibility.

Both existing `WordQuest.Context` Unreal tests pass, failed/notRun/inProcess zero:
`20261002-143621-automation-initial`. All 46 Python tests pass, including rejection
of premature/stale cues, wrong semantics, missing/duplicate rows and clipped
feedback. Six original reference hashes, seven SVG pairs, LFS and whitespace
checks pass. Native capture logs contain no Error/Fatal lines.

Read-only comparison: `G-Outcome-Final-Initial-Comparison.json`, zero changed pixels,
PNG SHA-256 `7aa62165b992c5599f993e3947bc5572ce901fde239e1290a34920addec1b99e`.
The current capture helper requires the new cue/feedback metadata: old packages
remain historical evidence and need a fresh build for this contract.

Dedicated read-only Codex review completed at clean
`6caed5c690d456e6b94a1454ee2d7503833a9d55` against actual `origin/dev`,
`7e100c2748390718430d52414bf89d960c301eb3`, exit 0 and no actionable introduced
defects. Head/worktree stayed unchanged. The reviewer independently passed all
nine new option-cue/feedback tests; it did not independently run engine builds,
packaged runtime or physical-device checks. Raw evidence:
`Artifacts/Reviews/20261002-144007`. Subsequent review/publication records change
documentation only. No merge is performed by the agent.

## Limits

These are synthetic native input/lifecycle and layout checks. Reading Slate's
custom accessible text is not a platform screen-reader test. Manual touch/keyboard,
real OS interruption, submitted outcome readability at 200% text, phone/offline,
performance, static fidelity, editorial, UI02 motion and release gates remain open.
Original visual targets are unchanged; current companion, typography and other art
remain unaccepted candidates. Android engine support and a connected physical
phone are still prerequisites; see [Android support](../../Setup/ANDROID-SUPPORT.md).
