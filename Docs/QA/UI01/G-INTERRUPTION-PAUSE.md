# G question interruption Pause

After owner-merged PR #20 (`7cc53bf`), the bounded G UI01 follow-up opens the
existing Pause modal when Slate reports application deactivation or core lifecycle
delegates report deactivation/backgrounding. Returning to active/foreground state
leaves it paused until the player activates Resume. Existing selection, Hint,
submission/result and evaluation count remain in memory. Repeated notifications
cannot toggle Pause or replace the saved gameplay focus. Delegate bindings follow
widget construction/destruction, with explicit handle removal.

This changes the live question interruption boundary only. It adds no persistence,
OS-kill recovery, motion system or platform qualification. Existing art, fixture,
scoring and engine-generated project files remain unchanged.

Implementation was checked against installed UE 5.8.2 headers/source and Epic's
[Slate application API](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Slate/FSlateApplication)
and [background delegate](https://dev.epicgames.com/documentation/unreal-engine/BlueprintAPI/EventDispatchers/ApplicationWillEnterBackgroundDe-)
documentation on 2026-10-02. Native delegates, not polling or global keyboard hooks,
drive the change.

## Build and package

Clean implementation: `373695df52877919dbc430f174b6c609088d3ed8`.
Real editor build passed with 6 actions in 16.24 seconds during implementation,
then the corrected proof build passed with 4 actions in 7.52 seconds. Clean
package preparation rebuilt editor metadata/link outputs with 3 actions in
4.70 seconds. Logs are `Artifacts/Logs/Build/WordQuestEditor-20261002-132957.log`,
`...-133251.log` and `...-133400.log`.

Full clean Win64 Development build/cook/stage/archive passed, UAT exit 0,
BuildCookRun 86.83 seconds. Game target: 5 actions, 25.46 seconds.
Package: `Artifacts/Packages/Win64/20261002-133400-325249`.
Manifest SHA-256:
`5123ab7498687a9c6c74995d049b87d6bbe07c4de5853a34a40e5318ee04879d`.
All 48 archived payload hashes are recorded and checked before each launch.
Head, worktree and input invariants pass; no generated build output is tracked.

## Native verification

All nine fresh packaged captures pass their helper/state/dimensions/exit contracts,
with clean worktrees. All PNGs were visually inspected. Runs are under
`Artifacts/QA/UI01`; full batch metadata is `G-Interruption-Batch.json`.

| Run prefix (20261002-) | Proof / dimensions | Evidence |
|---|---|---|
| 133603 | initial, 884x1780 | Original unselected state; zero changed pixels and identical PNG SHA-256 against PR #19 normal capture |
| 133614 | interruptpaused, 390x844, simulated safe-area .9 | Slate deactivation independently opens Pause; eight traced transitions preserve option B/Hint and zero evaluations; return remains paused with visible Resume |
| 133624 | interruptresumed, same | Core deactivation independently opens Pause; nine traced transitions; real Slate Space activation of Resume restores focused option B and unsubmitted assisted state |
| 133633 | interruptsubmitted, same | Core background independently opens Pause after an assisted incorrect submission; nine transitions; explicit Resume restores Pause-button focus; evaluation count remains exactly one |
| 133643 | interruptmanual, same | An already-open manual Pause survives duplicate notifications and return; eight transitions, visible Resume |
| 133653 | keytab, same | Existing forward/backward focus cycle and focused Hint visibility pass |
| 133703 | keyretry, same | Existing 200% text toggle/retry/first answer route and focus visibility pass |
| 133712 | longselectedfocus, 260x640, simulated safe-area .9 | Existing 200% long-option selected marker, letter and first line visible; remaining content scrollable |
| 133722 | pausefocus, same | Narrow focused Pause capture retained |

The four new modes deliver synthetic engine lifecycle notifications, not direct
calls to the screen's interruption handler. Notification order differs so each
of the three subscriptions must independently pause an active attempt. All modes
check duplicate notifications, foreground/reactivation and blocked selection/Hint
shortcuts. Resume uses real Slate key-down/up delivery. Enter/Space on the focused
Resume button are deliberate modal actions, not blocked gameplay input. An early
dirty-worktree proof at `20261002-133109-capture-interruptresumed` incorrectly
treated Enter on Resume as blocked; it failed and is excluded from final evidence.
The proof was corrected without disabling accessible modal activation.

Both existing `WordQuest.Context` Unreal tests pass at the clean implementation,
failed/notRun/inProcess zero: `20261002-133837-automation-initial`.
All 37 Python tests pass, including six new trace tests that reject missing,
extra/reordered notifications, automatic resumption, changed attempts, wrong focus
and missing/invisible capture evidence. Six original reference hashes, seven SVG
pairs, LFS status and whitespace checks pass. Native capture logs contain no
Error/Fatal lines; existing TSR/template warnings remain.

Read-only comparison: `G-Interruption-Initial-Comparison.json`, normal PNG SHA-256
`7aa62165b992c5599f993e3947bc5572ce901fde239e1290a34920addec1b99e`.

Dedicated read-only Codex review completed at clean
`688ccca744aca09f12e31eeee6987c37799c7948` against actual `origin/dev`,
`7cc53bfd389d9e71879d28faae1da18958833a96`, exit 0 and no actionable introduced
defects. Head/worktree stayed unchanged. The reviewer independently passed the
six interruption trace tests; it did not independently run engine builds or real
OS/device interruption checks. Raw evidence: `Artifacts/Reviews/20261002-134048`.
Subsequent review/publication records change documentation only.
[PR #21](https://github.com/rloterh/WordQuest/pull/21) was merged by the owner into
`dev` at `7e100c2748390718430d52414bf89d960c301eb3`,
2026-10-02 14:01:07 UTC. GitHub has no configured status checks; validation
above is local. No agent merge is performed.

## Limits and next prerequisites

These are synthetic native lifecycle/input checks. Real desktop Alt-Tab/minimize,
Android home/lock/call interruption, platform focus restoration, persistence after
termination and phone evidence are unverified. Listener removal/re-add is implemented
but has no separate runtime qualification. Static fidelity, fixture editorial
approval, manual/platform accessibility, phone/offline, performance, UI02 motion
and release acceptance remain open.

The owner confirmed Epic Games Launcher installation. Fresh records identify exact
UE 5.8.2 at the existing path, while Android receipt is absent and adb lists no
device. [Android support handoff](../../Setup/ANDROID-SUPPORT.md) describes the
owner-operated Options step; no installation completion is claimed.
