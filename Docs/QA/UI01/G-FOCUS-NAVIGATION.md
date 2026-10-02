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
reset and completed-attempt Pause access worked. Native PNG inspection of the
rapid, single-frame `keyretry` sequence nevertheless showed enlarged A clipped
at the bottom: retry cleared feedback text but left `bRevealFeedback` pending from
Hint/submission. Layout later scrolled toward that empty feedback instead of the
new focused answer. Retry now clears the pending reveal flag. A first follow-up
build/capture (`WordQuestEditor-20261002-042007.log`,
`20261002-042113-capture-keyretry`) still showed clipping: focus scrolling had used
the geometry before reflow. NativeTick now rechecks focused enabled controls on the
tick after changed layout is arranged, with explicit feedback scrolling retaining
priority. This sequence is a synthetic rapid transition, not a reproduced manual
keyboard test. The earlier successful package at clean `a225e58`,
`20261002-041631-646664`, predates these visibility corrections and is superseded.

Gameplay Next/Previous navigation now explicitly cycles through enabled controls
in semantic order A/B/C/D/Hint/Check/Pause. Refresh rebuilds the order after Hint,
submission and retry, skipping disabled controls. When the screen itself owns
focus, Tab enters at the first enabled control and Shift-Tab at the last. After
submission, Pause is the only enabled gameplay stop. The existing modal cycle
and focus restoration remain intact. Arrow/gamepad navigation is unchanged.

No art, fixture, renderer, module/target files or scoring changes are included.
Proof instrumentation/getters remain excluded from Shipping;
the focus correction applies to normal runtime builds.

## Native routes

Six new proof modes dispatch actual `FKeyEvent` key-down/up pairs through Slate,
including the Shift modifier. They do not call programmatic focus helpers or
Choose/Submit/Hint/TogglePause/ToggleTextSize/ResetAttempt directly. Each step logs
its full attempt state, focused semantic control and text percentage. Verification
requires every ordered key/state/focus/modifier/percentage, handled active down
and Space release, final state and PNG dimensions. At capture time it also requires
the expected focused control's full positive-size layout rectangle inside the
visible scroll region (or root viewport for modal controls), with one-pixel
rounding tolerance. This is a geometry check, not a contrast or legibility verdict.
Matching final state alone
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

Nine new Python focus tests pass: complete route, matching attempt state with
incorrect focus, incorrect modifier/text setting, missing focus metadata,
missing/extra/reordered steps, wrong proof, visible capture, missing/clipped capture
and incorrect/duplicate capture. All 22 combined focus/keyboard/
package-helper tests pass. These check evidence rejection, not physical input.

Final runtime evidence uses clean source
`554079e48665de83ae5cc2ed3c8df21a11de3f06`. The corrected editor compilation passed
(6 actions, 27.35 seconds, exit 0):
`Artifacts/Logs/Build/WordQuestEditor-20261002-042323.log`. Its preliminary dirty
`20261002-042351-capture-keyretry` passed focus/state/visibility checks and native
inspection showed full enlarged A; final clean packaged evidence follows below.

Package `Artifacts/Packages/Win64/20261002-042431-180556` passed the clean editor
recheck (1.60 seconds), real game build (5 actions, 49.02 seconds), full cook,
stage and archive (UAT 143.68 seconds), all exit 0. Manifest head/worktree/inputs
remain unchanged, with complete payload hashes. Manifest SHA-256:
`9bd54b7e9017f1461ec91d9dd9e8ff2373115fe164ff982197f2aa5f8867931f`.

All 14 packaged runs record this clean source/package revision, empty worktree,
verified archive hashes, exit 0, correct ordered attempt traces, final state and
PNG dimensions. The seven new focus captures below additionally pass every focus/
Shift/text-setting transition and capture-time control visibility. All seven PNGs
were directly inspected. Raw `run.json`, `Unreal.log`, `console.log` and `native.png`
remain local under `Artifacts/QA/UI01/` (ignored, not uploaded with the PR).

| New packaged run | Dimensions | Native observation |
| --- | --- | --- |
| `20261002-042715-packaged-capture-keytab` | 390x844 | Hint focused, no choice/evaluation |
| `20261002-042726-packaged-capture-keyback` | 390x844 | Check focused after reverse wrap |
| `20261002-042735-packaged-capture-keyskip` | 390x844 | D focused; Hint disabled and hint feedback visible |
| `20261002-042745-packaged-capture-keymodal` | 390x844 | Text-size control focused at 200%, modal above dimmed content |
| `20261002-042754-packaged-capture-keyretry` | 390x844 | Entire focused selected A visible at 200%; no stale result/hint feedback |
| `20261002-042803-packaged-capture-keydisabled` | 390x844 | Pause focused; completed A/result retained, answer/actions disabled |
| `20261002-042920-packaged-capture-keyretry` | 844x390 | Entire focused selected A visible at 200% after scrolling |

The seven earlier keyboard routes passed at 390x844, from this same package:
`20261002-042813-packaged-capture-keyswitch`,
`20261002-042823-packaged-capture-keyempty`,
`20261002-042832-packaged-capture-keysubmit`,
`20261002-042842-packaged-capture-keyhint`,
`20261002-042851-packaged-capture-keybuttons`,
`20261002-042901-packaged-capture-keypaused` and
`20261002-042910-packaged-capture-keyresumed`. Their existing key/state/dimension
checks passed; the new focus/visibility assertions apply only to the six new modes.

Both existing Unreal tests passed from the clean revision in
`20261002-042928-automation-initial` (2 succeeded, zero failed/not-run/in-process,
exit 0). These remain isolated attempt/draft-fixture tests, not campaign or
editorial qualification. All 22 Python tests, six supplied reference hashes, six
SVG source/runtime pairs, `git lfs fsck` and `git diff --check` passed. Dedicated
review against actual `origin/dev` is pending. Later commits record evidence only;
no art or device gate is passed by these checks.

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
