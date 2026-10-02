# G native keyboard routing — bounded synthetic evidence

After the owner's PR #11 merge (`f0b8c4c`, 2026-10-02), this increment checks
the native Slate input route. Earlier proof modes call screen methods directly;
they do not demonstrate that focused widgets receive keyboard events correctly.

Seven Development-only modes now send `FKeyEvent` key-down/up pairs through
`FSlateApplication::ProcessKeyDownEvent`/`ProcessKeyUpEvent` for Slate user 0 in
the isolated proof process. These modes do not call Choose, Submit, Hint or
TogglePause directly. `keybuttons` explicitly sets B/Check focus with the existing
proof helpers before Space activation; it does not test Tab traversal.
All new C++ proof functions, calls and includes are excluded from Shipping.
Gameplay handlers, fixture, scoring, art, renderer and module/target files are
unchanged. No user editor is closed or used for injected input.

Each key pair logs its ordinal/key, handled down/up flags and complete attempt
state. `run_g_proof.py` requires every expected ordered intermediate transition
and the final state/dimensions; active key-downs and Space releases must be
handled. Missing/extra/reordered steps or an incorrect intermediate state fail
the check, even if the final tuple happens to match. Paused `1`/`H` may be
unhandled but must not change selection, assistance or evaluation.

| Mode | Routed sequence | Expected behavior |
| --- | --- | --- |
| `keyswitch` | 1, 3, 4, 2 | Each choice selectable; final B, no evaluation |
| `keyempty` | Enter | Choose-before-check feedback; no evaluation |
| `keysubmit` | 1, Enter, Enter | Correct A, exactly one evaluation |
| `keyhint` | H, 1, Enter | Assisted correct A, exactly one evaluation |
| `keybuttons` | Focus B, Space; focus Check, Space; Enter | Real answer/Check UButton activation; incorrect B, one evaluation despite repeated submit |
| `keypaused` | 2, P, 1, H | Modal remains paused; B retained, no hint/evaluation |
| `keyresumed` | 2, P, 1, H, Space | Real focused Resume UButton activation; unpaused B with no hint/evaluation |

## Verification

The preliminary dirty editor run `20261002-035245-capture-keyresumed` passed all
five transitions, final state/dimensions and exit 0. Final evidence below uses clean
source `1fa4d137d65fcaa198f68b90d60c946f9f6ef049`; subsequent commits record evidence
and review only. No runtime source, fixture or asset changes follow that build.

The real editor build passed (6 actions, 66.48 seconds, exit 0):
`Artifacts/Logs/Build/WordQuestEditor-20261002-034943.log`. The package helper's
editor recheck also passed at the clean revision (1.47 seconds, exit 0):
`Artifacts/Logs/Build/WordQuestEditor-20261002-035604.log`.
Full Win64 Development game build/cook/stage/archive passed in
`Artifacts/Packages/Win64/20261002-035604-056775` (UAT 135.27 seconds, exit 0).
The manifest records unchanged head/worktree/inputs and successful editor/UAT
exits; its SHA-256 is
`924f00713c16c5e8f499e169e12923b3965d7d83c5684472dfb5ebca5192793b`.

All seven packaged checks below passed exit 0, every ordered intermediate state,
handled-key requirements, final state and 390x844 PNG dimensions. Each run records
the same clean source/package revision and verifies archived payload hashes before
launch. Raw `run.json`, `Unreal.log`, `console.log` and `native.png` remain locally
under `Artifacts/QA/UI01/` (ignored, not uploaded with the PR).

| Packaged run directory | Native PNG observation |
| --- | --- |
| `20261002-040000-packaged-capture-keyswitch` | B selected, no feedback/evaluation |
| `20261002-040011-packaged-capture-keyempty` | Choose-before-check feedback, no selection |
| `20261002-040020-packaged-capture-keysubmit` | Correct A, disabled controls, correct feedback |
| `20261002-040029-packaged-capture-keyhint` | Correct A, Hint used, assisted feedback |
| `20261002-040039-packaged-capture-keybuttons` | Incorrect B, disabled controls, incorrect feedback |
| `20261002-040048-packaged-capture-keypaused` | Modal above dimmed content, Resume focus outline |
| `20261002-040057-packaged-capture-keyresumed` | Modal closed, B retained, Pause focus outline |

All seven PNGs were directly inspected. This confirms the visible final state;
intermediate transitions are checked from the native per-key logs. Existing
`WordQuest.Context.Attempt` and `.Fixture` automation both passed with exit 0,
zero failed/not-run/in-process, from the same clean revision:
`Artifacts/QA/UI01/20261002-040105-automation-initial`. These remain isolated draft
fixture/attempt tests, not campaign or editorial qualification.

Eight Python trace tests pass: valid route traces, missing trace with valid empty
final state, incorrect intermediate state despite correct final state, wrong
order, extra/missing step, wrong proof, unhandled active key and unhandled Space
release. These validate evidence rejection, not manual keyboard/device behavior.
All 13 combined Python trace/package-helper tests passed. Six original reference
hashes, six source/runtime SVG pairs, `git lfs fsck` and `git diff --check` passed.
Dedicated review against actual `origin/dev` is pending.

Reproduce a routed check using the existing helper:

```powershell
python -m unittest Tools.QA.test_keyboard_proof
python Tools/QA/run_g_proof.py capture --proof keyresumed --width 390 --height 844
python Tools/QA/run_g_proof.py capture --proof keyresumed --width 390 --height 844 --package-run Artifacts/Packages/Win64/20261002-035604-056775
```

Pass a completed local package directory with `--package-run` for the same native
route in the archived Win64 Development executable. Package provenance/hash and
state/dimension checks remain in force.

## Remaining gates

These are synthetic events dispatched inside a real native process, not physical
keyboard/OS event injection or a manual input pass. They do not establish Tab/
Shift-Tab traversal, pointer/touch/hover/press behavior, screen-reader service,
phone, offline isolation, performance or release acceptance. Focus setup in
`keybuttons` is programmatic; pause/resume focus is observed in native captures,
not automatically asserted by these state tuples. UI01 art/fixture acceptance,
UI02 motion, Android prerequisites and the cold D3D12 pipeline delay remain open.
