# G Pause controls in short windows

After owner-merged PR #24 (`7a464ed`), the native 260x200 baseline confirmed that
Text size and Retry could receive focus while clipped or offscreen. At least one
Pause button label exceeded its content bounds. The fixed-position panel could
not reveal them. Baseline `20261002-181520-capture-modalcycle` exited natively
with 0 but correctly failed its evidence contract.

Pause now places its controls in a separate safe-area scroll box above the
full-screen shade. Focus reveals the corresponding control, including after a
text-size reflow. Labels wrap within the button's measured available width and
grow its height when needed; the existing 54 layout-unit minimum is retained.
The title can wrap too. The scrollbar appears only when content exceeds the
viewport. Opening Pause starts its scroll at the beginning. Existing Next/Previous
control order, Resume focus restoration, retry semantics and question text scaling
are preserved. Pause typography retains its existing font sizes; this is not a
claim that every screen element doubles at 200%. No art, font asset, fixture,
scoring, supplied reference or Unreal-generated project file changes.

## Final build and package

Clean implementation: `77fed094dde02d4198af8e0c7ff7098aec416521`.
Package: `Artifacts/Packages/Win64/20261002-183406-619150`.
Editor preparation passed, 4 actions, 26.03 seconds, exit 0:
`Artifacts/Logs/Build/WordQuestEditor-20261002-183406.log`.
Real game target passed, 3 actions, 38.57 seconds. Full Win64 Development
build/cook/stage/archive passed; BuildCookRun 162.44 seconds, UAT exit 0.
Head/worktree/input invariants pass; all 48 archived payload hashes are verified
before every launch. Generated outputs remain ignored. Manifest SHA-256:
`a2b944386916cdf9a4378932c707608f35a2cdae591f60e1f85eae0b99bc6687`.

## Native input and captures

Development-only `modalcycle`, `modalresume` and `modalretry` routes send real Slate
key-down/up events. H, 1, Enter and P establish a correct assisted submitted attempt
and open Pause. Timed input then navigates forward/reverse through all three
controls and activates the Text size button with Space to reach 200%.
Every step is measured on a later arranged frame. No route directly sets button
focus, text scale or scroll offset. Cycle ends on Retry; Resume preserves the
submitted attempt and returns focus to Pause; Retry clears choice/Hint/result and
evaluation count, then Tab/Space selects A without submitting it.
`WQ_STATE` records the setup before timed input; the ordered traces and final
option-cue checks supply the later state evidence.

Each ordered trace requires handled input, Space release, exact Shift/focus/text
state, unchanged attempt during navigation, visible focused Pause controls and
measured label fit. Capture requires the final expected focus and visibility.
When the returned A row is oversized, Retry requires its option identifier,
selection cue and first line; full-row visibility cannot be claimed for such a
viewport. These native additions are excluded from Shipping builds.

All 17 final packaged contracts pass with checked hashes, exits, dimensions,
states and option cues. All PNGs were directly inspected; logs contain no
Error/Fatal lines. Eleven modal captures check all focused control transitions and
label bounds. Raw runs are under `Artifacts/QA/UI01`; data are
`pause-scroll-batch.json` and `pause-scroll-analysis.json`.

| Run prefix (20261002-) | Proof / dimensions | Evidence |
|---|---|---|
| 183751 | modalcycle, 260x200, safe-area .9 | Each focused control visible; wrapped Retry and scroll indicator |
| 183808 | modalresume, same | Submitted assisted attempt preserved; Pause focus restored |
| 183821 | modalretry, same | Reset succeeds; selected oversized A starts with identifier/cue/first line |
| 183834 | modalcycle, 844x390, safe-area .9 | All controls fit; scrollbar hidden |
| 183846 | modalresume, same | Attempt/focus restored |
| 183859 | modalretry, same | Reset and selection succeed; answer start visible |
| 183912 | modalcycle, 390x844, safe-area .9 | Controls/labels fit; scrollbar hidden |
| 183925 | modalresume, same | Attempt/focus restored |
| 183938 | modalretry, same | Reset and selected A visible at 200% |
| 183952 | modalcycle, 200x200, safe-area .9 | Wrapped labels and every focused control fit |
| 184004 | modalcycle, 200x200, safe-area .8 | Smaller simulated safe area; same contracts pass |
| 184017 | initial, 884x1780, normal text | PNG byte-identical to PR #24 |
| 184028 | correct, same | PNG byte-identical to PR #24 |
| 184039 | keyretry, 390x844, safe-area .9 | Existing rapid routed 200% retry remains correct |
| 184049 | scrollpaused, 844x390, safe-area .9 | Reading input blocked; Resume visible |
| 184101 | scrollfeedback, same | Reading paging, Home/End and Tab return still pass |
| 184113 | interruptsubmitted, 390x844, safe-area .9 | Lifecycle interruption/resume preserves submitted attempt |

Reference-size captures suppress tooltips for comparison only. They have identical
bytes and zero changed pixels against PR #24's `173348`/`173402` captures. Initial
SHA-256: `7aa62165b992c5599f993e3947bc5572ce901fde239e1290a34920addec1b99e`;
correct outcome: `595d4f94ca9452af4b8a22d27b2424d5ee5d2f75f050d9aceb065f20fb948406`.
Both `WordQuest.Context` Unreal tests pass with failed/notRun/inProcess zero:
`20261002-184201-automation-initial`. All 63 Python tests pass, including rejection
of hidden controls/clipped labels, missing/duplicate/reordered steps, unhandled
input, missing Space release, focus/Shift/text/attempt drift, missing capture and
an oversized retry answer without visible leading content. Six original reference
hashes, seven SVG pairs, LFS and whitespace checks pass.

Dirty preflights `182046` (cycle) and `182159` (resume) passed before final proof
metadata was added. `182220` (retry) was rejected because its initial contract
incorrectly required the full oversized A row to fit; final evidence instead
requires visible leading content and explicitly reports oversized rows. Preliminary
package `20261002-182459-784957` and its 17 successful contracts predate the
scroll-indicator correction and are excluded from final acceptance. Their metadata
is retained in `pause-scroll-preliminary-batch.json`/`pause-scroll-preliminary-analysis.json`.

## Limits and review

Short windows still require scrolling; controls are checked individually when
focused, not all simultaneously. Only the recorded sizes/safe-area ratios were
verified. Desktop simulated safe areas and synthetic Slate input do not establish
physical UI scale, actual phone notches, manual/OS keyboard, pointer/touch or
screen-reader acceptance. The accessible scroll description is not an announcement
test. Oversized answer rows and explanations remain scrollable.

Unfinished candidate art, the EQUIVOCAL draft and prototype `3 / 7` remain unapproved.
Static fidelity, editorial, offline/physical-phone, contrast/manual accessibility,
performance, motion and release gates remain open. Android engine support receipt
is absent and adb lists no device on this turn's recheck. UI01 acceptance precedes
UI02 and H/I; no merge, deployment or release is performed.
Dedicated read-only Codex review completed at clean
`727cf67e9940bffe0a0313e109f44ba7b34f4f19` against actual `origin/dev`,
`7a464ede7f6cbc1e48d63f9d19d447ee286fe12d`, with exit 0 and no actionable
introduced defects. Head/worktree stayed unchanged. The reviewer independently
passed all seven modal-proof tests; its broader QA run did not complete. It did
not independently repeat Unreal runtime/device verification. The implementation
run above passed all 63 Python tests. Raw review evidence:
`Artifacts/Reviews/20261002-184421`. Subsequent review/publication records change
documentation only. The owner retains merge authority.
