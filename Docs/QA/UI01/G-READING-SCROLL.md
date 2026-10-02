# G keyboard reading scroll

After owner-merged PR #23 (`aa204ff`), native baseline input showed Page Up,
Page Down, Home and End all unhandled. At 844x390 with simulated safe-area .9
and 200% text, the reading offset stayed at 2577.670 while its maximum was
2904.091; the oversized assisted explanation's last line was hidden.

While gameplay is active, Page Up/Down now moves by 90% of the reading viewport,
Home jumps to its beginning and End to its end. Offsets clamp to valid bounds and
stop inertial scrolling. Reading input cancels pending automatic reveals, so
reflow does not immediately return to an offscreen focused control. Deliberate
control focus or retry restores focus-driven scrolling. The scroll area's
accessible text describes these keys. Pause blocks this input; choice, Hint,
submission and evaluation state are preserved. No art, fonts, learning fixture,
scoring or Unreal-generated project files change.

## Build and package

Clean implementation: `b97b940390c86fd453b473c86b17b06aaf8cf1da`.
Package: `Artifacts/Packages/Win64/20261002-172732-787013`.
Editor preparation passed, 3 actions, 6.05 seconds, exit 0:
`Artifacts/Logs/Build/WordQuestEditor-20261002-172732.log`.
Real game target passed, 5 actions, 38.45 seconds. Full Win64 Development
build/cook/stage/archive passed; BuildCookRun 191.46 seconds, UAT exit 0.
All 48 archived payload hashes are recorded and verified before every launch.
Head/worktree/input invariants pass; outputs remain ignored.
Manifest SHA-256:
`bc11dd0b6894b32e752519b91baf123393241523fe7b14d1bb20e7de4ddecfa4`.

## Native input and visual evidence

Development-only `scrollfeedback`, `scrollfocus` and `scrollpaused` modes use
actual Slate key-down/up events for H, 1 and Enter, then reading keys. The focused
route directly sets initial Pause-control focus; the paused route sends P.
No proof calls a scroll setter. Each input is measured after a later arranged
frame. Active routes check movement, bounds, Home/End and explanation end visibility;
the screen-focus route also sends Tab then End to verify control focus returns
into view before reading continues. The paused route checks unchanged offset,
unhandled reading keys and visible Resume. Every step requires unchanged selected
A, correct submitted assisted state, one evaluation, focus and actual 200% text.
These modes and getters are excluded from Shipping builds.

All 14 fresh packaged runs passed state/cue/dimensions/exit contracts. Eight
reading routes also require 200% metadata, fitted action content and their exact
ordered traces. All PNGs were directly inspected; logs have no Error/Fatal lines.
Runs are under `Artifacts/QA/UI01`; batch and comparison data are
`reading-scroll-batch.json` and `reading-scroll-analysis.json`.

| Run prefix (20261002-) | Proof / dimensions | Result |
|---|---|---|
| 173117 | scrollfeedback, 844x390 | End exposes last line; Tab restores Pause, then End returns |
| 173139 | scrollfocus, 844x390 | Reading keys bubble from focused Pause; Home returns to header |
| 173154 | scrollpaused, 844x390 | Reading keys leave offset/state unchanged; Resume visible |
| 173209 | scrollfeedback, 260x200 | Oversized explanation end reached; Tab restores control |
| 173226 | scrollfocus, 260x200 | Paging and both bounds pass; final line visible |
| 173243 | scrollpaused, 260x200 | Resume visible; no reading movement; modal limit below |
| 173309 | scrollfeedback, 390x844 | Full explanation visible at End; Tab return passes |
| 173328 | scrollfocus, 390x844 | Focused route, paging and bounds pass |
| 173348 | initial, 884x1780, normal text | Byte-identical to PR #23 |
| 173402 | correct, same | Byte-identical to PR #23 |
| 173416 | keyretry, 390x844 | Routed 200% retry preserves selected A/focus and clears result/Hint |
| 173428 | longselectedfocus, 260x640 | Oversized selected B starts with visible identifier/cue/first line |
| 173442 | keydisabled, 390x844 | Disabled controls skipped; final Pause focus visible |
| 173458 | interruptsubmitted, 390x844 | Application interruption/resume preserves submitted attempt |

All non-reference-size runs simulate safe-area .9; this is desktop geometry,
not an actual phone notch. Reference-size runs suppress desktop tooltips only.
For landscape screen focus, offsets are 2577.670, 2892.670, 2577.670, 2904.091,
2904.091, 0, 0, 2904.091, 26.652 (Tab), 2904.091. The short viewport reaches
1733.471; portrait reaches 1016.905. Paused routes stay at offset zero.
First-line and last-line visibility codes are distinct, so an oversized first
line cannot satisfy an end capture. Offscreen descendant cached geometry can
remain stale after culling; no offscreen visibility claim is made from those
fields. Active final focused-control visibility is deliberately not accepted:
End can leave its focused header offscreen. Tab return requires both offset
movement and visible control; final explanation PNGs supply direct visual evidence.

The two normal-size PNGs have zero changed pixels and identical bytes against
PR #23's `163542`/`163552` captures. Initial SHA-256:
`7aa62165b992c5599f993e3947bc5572ce901fde239e1290a34920addec1b99e`;
correct outcome: `595d4f94ca9452af4b8a22d27b2424d5ee5d2f75f050d9aceb065f20fb948406`.

Both `WordQuest.Context` Unreal tests passed with failed/notRun/inProcess zero:
`20261002-173523-automation-initial`. All 56 Python tests passed, including
refusal of inert/unhandled, missing/duplicate/reordered, out-of-bounds, hidden-end,
attempt/focus/text drift, missing capture and paused movement evidence.
Six original reference hashes, seven SVG pairs, LFS and whitespace checks pass.

Baseline `20261002-170418-capture-scrollfeedback` correctly failed its evidence
contract and is excluded from acceptance. Dirty editor preflights `171448`,
`172049`, `172528` and `172627` passed before clean packaging. The `172049`
screen-focus run includes the additional Tab/End sequence; `171448` predates it.

## Limits and review

At 260x200 the existing Pause panel exceeds the viewport: Resume is visible but
the bottom retry action is offscreen. This run establishes paused reading-input
isolation only, not complete modal/accessibility acceptance. Oversized explanations
and artificial long answers still require scrolling. Synthetic Slate events do
not establish physical/OS keyboard, screen-reader announcement, pointer/touch or
manual usability acceptance. Accessible text is not screen-reader verification.

Unfinished candidate art, the draft EQUIVOCAL fixture and prototype `3 / 7` remain
unapproved. Static fidelity, editorial, offline/physical-phone, contrast/manual
accessibility, performance, motion and release gates remain open. Android engine
platform support is still absent; see [installation handoff](../../Setup/ANDROID-SUPPORT.md).
UI01 acceptance precedes UI02 and H/I. No merge, deployment or release is performed.
Dedicated read-only Codex review completed at clean
`e3f40726cf5bf8385db69b37781c3fd8ee535af9` against actual `origin/dev`,
`aa204ff50fc08586ac1f64b4cf1cdb410cbb9eae`, with exit 0 and no actionable
introduced defects. Head/worktree stayed unchanged. The reviewer independently
passed all seven reading-scroll tests and the diff whitespace check; its broader
QA invocation did not complete. It did not independently rerun Unreal builds or
runtime evidence. The implementation run above passed all 56 Python tests.
Raw review evidence: `Artifacts/Reviews/20261002-173804`. Subsequent records change
documentation only. The owner retains merge authority.
