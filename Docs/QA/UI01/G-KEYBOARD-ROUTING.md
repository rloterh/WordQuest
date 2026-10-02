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
five transitions, final state/dimensions and exit 0. Native PNG inspection shows
retained B selection and Pause focus after resume. This is preliminary evidence;
final clean package checks and internal review are pending.

Eight Python trace tests pass: valid route traces, missing trace with valid empty
final state, incorrect intermediate state despite correct final state, wrong
order, extra/missing step, wrong proof, unhandled active key and unhandled Space
release. These validate evidence rejection, not manual keyboard/device behavior.

Reproduce a routed check using the existing helper:

```powershell
python -m unittest Tools.QA.test_keyboard_proof
python Tools/QA/run_g_proof.py capture --proof keyresumed --width 390 --height 844
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
