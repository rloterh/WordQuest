# G routed virtual pointer proof

The owner merged PR #43 into `dev` at `baa03aa` on 2026-10-04, 21:34:53 UTC.
This bounded UI01 increment tests hover/press/release on existing G controls.
Art, fixtures, scoring rules and production handlers are unchanged. C++ pointer
helpers, controller state, routing and teardown use `!UE_BUILD_SHIPPING` guards;
no Shipping binary was built for this increment.

## Route and evidence contract

An isolated virtual Slate user routes `FPointerEvent` mouse events through
`FSlateApplication::RoutePointerMoveEvent`, `RoutePointerDownEvent` and
`RoutePointerUpEvent`, following the installed engine's widget-interaction approach.
`LocateWindowUnderMouse` performs window/grid hit testing at a point inside the
rendered button's clipped geometry. The path must contain the active target.
These modes never call Choose, Submit, Hint or TogglePause directly. The desktop
cursor is not moved and no user's open editor receives injected input.

`ScrollWidgetIntoView` is explicit target setup; routing waits for layout on a later
frame. This is not a pointer-scroll/manual navigation proof. Setup never sets target
keyboard focus. Pointer-down can focus through Slate; physical keyboard focus is
not qualified. Local enabled flags are distinct from ancestor/modal blocking. An
ancestor may handle a disabled-target event, so handling alone cannot prove a click.

Ordered steps report event/target, hit, clipped point, handling, local enabled,
native hover/press, pointer capture and the six-field attempt state. Active down
must press/capture without activating; release must trigger its expected transition.
Disabled/modal targets cannot press or alter learning state. Screenshot-time flags
must retain held/hover state. Teardown cancels capture without a release-click and
must leave the same attempt with no pressed/captured state. Missing, extra,
reordered, malformed or incorrect intermediate/cleanup evidence fails even with
a correct final tuple. `automation --proof pointer*` is rejected rather than
mislabeling Context unit tests as pointer proof.

| Mode | Expected evidence |
|---|---|
| `pointerhover` | Move across answer, Hint, Check, Pause, then hover Check; no attempt change |
| `pointerpress` | Hold Check through screenshot; no submission; cancel cleanly |
| `pointerhintpress` | Hold Hint; no assistance before release; cancel cleanly |
| `pointeranswerpress` | Hold A; no selection before release; cancel cleanly |
| `pointerpausepress` | Hold Pause; modal stays closed before release; cancel cleanly |
| `pointerclick` | Empty Check cannot evaluate; release B selects; release Check evaluates wrong once; disabled Check/A do nothing |
| `pointerhint` | Hint activates on release; A/Check produce assisted correct feedback once; disabled Hint does nothing |
| `pointerpaused` | B/Pause releases open modal; underlying A/Hint fail hit testing and preserve attempt |
| `pointerresumed` | Same barrier checks, then Resume release closes modal retaining unsubmitted B |

From repository root, after the actual Editor build:

```powershell
python Tools/QA/run_g_proof.py capture --proof pointerpress --width 390 --height 844 --safe-zone .9 --no-tooltips
python Tools/QA/run_g_proof.py capture --proof pointerpress --width 260 --height 640 --safe-zone .9 --large-text --no-tooltips
```

Modes support completed-package `--package-run` and 200% `--large-text`, require
capture mode and retain raw ignored evidence under `Artifacts`.

## Preliminary checks

Real Editor builds pass at `Artifacts/Logs/Build/WordQuestEditor-20261004-215358.log`
(six actions, 62.79s) and `WordQuestEditor-20261004-220248.log` (cleanup/invalid-point
guard, 16.06s). Dirty native preflights `20261004-215748-capture-pointerpress` and
`20261004-220040-capture-pointerclick` passed the earlier route/state contract before
cleanup logging; they are not final cleanup evidence. `20261004-220622-capture-pointerresumed`
and `20261004-221220-capture-pointerpress` pass the final contract, including canceled
held Check at 260x640, safe .9, 200% text. All four PNGs were inspected. A first
enlarged CLI call was rejected by the old question-only text-size guard before any
Unreal launch; pointer captures now use the same enlarged-text evidence checks.

All 81 Python QA checks pass, including 13 pointer rejection tests: missing input,
wrong hit/target/clipping, early or disabled activation/repeated evaluation,
invalid flags, lost hover/capture/held state, malformed/order errors, unknown proof,
cleanup leaks/activation and incorrect automation labeling. Synthetic test fixtures
never count as runtime evidence. Six immutable references and ten staged SVG pairs
pass. Clean package/matrix and dedicated review are pending.

## Open gates

These are synthetic virtual mouse events, not OS mouse/touch, physical-device,
manual pointer/keyboard or platform accessibility acceptance. They do not cover
pointer wheel/drag cancellation/double click, simultaneous physical/virtual users,
OS interruptions or physical target scale. Static art/type/material fidelity,
UI02 motion, draft fixture editorial approval, Android/phone, isolated offline,
performance and original release gates remain open. No later milestone, deployment,
release or owner merge occurs.
