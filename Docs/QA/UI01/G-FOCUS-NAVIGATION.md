# G focus navigation and Pause actions

The owner merged PR #12 at `b2d7a0d` on 2026-10-02. This bounded UI01 increment
checks focus order and the existing text-size/retry controls through native Slate
input, following V02/V11 in the UI addendum's QA specification. It does not begin
UI02 motion or later milestones.

## Baseline and correction

The instrumented baseline editor build passed (6 actions, 59.33 seconds):
`Artifacts/Logs/Build/WordQuestEditor-20261002-041105.log`. Only non-Shipping proof
instrumentation was added before baseline runs; gameplay navigation was unchanged.
Dirty run `Artifacts/QA/UI01/20261002-041234-capture-keytab` showed forward Tab
visiting A/B/C/D/Hint/Check/Pause, then remaining on Pause at step 8. Reverse
traversal consequently reached Check/Hint/D rather than the expected wrapped
Pause/Check/Hint. Attempt checks passed but focus verification correctly failed.
This is a focus-cycle correction, not a claim that answers were unreachable.

Other dirty baseline routes passed focus/state checks:
`20261002-041329-capture-keymodal`, `20261002-041346-capture-keyretry` and
`20261002-041402-capture-keydisabled`. The existing Pause cycle, 200% toggle, retry
reset and completed-attempt Pause access worked; their handlers are preserved.

Gameplay Next/Previous navigation now explicitly cycles through enabled controls
in semantic order A/B/C/D/Hint/Check/Pause. Refresh rebuilds the order after Hint,
submission and retry, skipping disabled controls. When the screen itself owns
focus, Tab enters at the first enabled control and Shift-Tab at the last. After
submission, Pause is the only enabled gameplay stop. The existing modal cycle
and focus restoration remain intact. Arrow/gamepad navigation is unchanged.

No art, fixture, renderer, module/target files, scoring or release behavior changes
are included. Proof instrumentation/getters remain excluded from Shipping;
the focus correction applies to normal runtime builds.

## Native routes

Six new proof modes dispatch actual `FKeyEvent` key-down/up pairs through Slate,
including the Shift modifier. They do not call programmatic focus helpers or
Choose/Submit/Hint/TogglePause/ToggleTextSize/ResetAttempt directly. Each step logs
its full attempt state, focused semantic control and text percentage. Verification
requires every ordered key/state/focus/modifier/percentage, handled active down
and Space release, final state and PNG dimensions. Matching final state alone
cannot pass missing or incorrect focus evidence.

| Mode | Required route |
| --- | --- |
| `keytab` | Forward A/B/C/D/Hint/Check/Pause/A; reverse Pause/Check/Hint |
| `keyback` | Initial Shift-Tab enters Pause; forward wraps to A; reverse Pause/Check |
| `keyskip` | H uses Hint; forward A/B/C/D/Check/Pause and reverse Check/D skip disabled Hint |
| `keymodal` | P opens Resume; Tab to TextSize; Space sets 200%; forward/reverse cycle remains within Resume/TextSize/Retry |
| `keyretry` | H/1/Enter creates assisted submitted attempt; P/Tab/Space sets 200%; Tab/Space retries; Tab/Space selects A with cleared hint/submission/evaluation and retained 200% setting |
| `keydisabled` | 1/Enter submits; Tab/Shift-Tab stay on enabled Pause; P/Space opens/resumes without changing result |

## Verification

Six new Python focus-trace tests pass: complete route, matching attempt state with
incorrect focus, incorrect modifier/text setting, missing focus metadata,
missing/extra/reordered steps and wrong proof. All 19 combined focus/keyboard/
package-helper tests pass. These check evidence rejection, not physical input.

Final clean builds, package, native captures, existing Unreal tests and dedicated
review are pending. Raw evidence stays under ignored `Artifacts`; no art or device
gate is passed by these checks.

Reproduce after a clean commit:

```powershell
python -m unittest Tools.QA.test_focus_proof Tools.QA.test_keyboard_proof Tools.QA.test_package_helpers
python Tools/BuildScripts/package_g_win64.py
python Tools/QA/run_g_proof.py capture --proof keytab --width 390 --height 844 --package-run <printed-package-run>
python Tools/QA/run_g_proof.py capture --proof keyretry --width 390 --height 844 --package-run <printed-package-run>
```

## Limits and remaining gates

This is synthetic Tab traversal in an isolated real native process, not manual
keyboard/OS injection, assistive technology or physical-phone evidence. Only the
listed sequences and resolutions are verified; pointer/touch, arrow/gamepad,
screen-reader service, network-isolated offline play, device performance and
release qualification remain open. Static art identity/fringes/type, draft fixture
approval, Android prerequisites and cold D3D12 pipeline delay remain unresolved.
UI01 acceptance, UI02 motion and H/I expansion remain gated.
