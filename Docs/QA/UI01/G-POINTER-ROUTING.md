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
Event identifiers compare case-insensitively, matching Unreal `FName`; the original
log spelling is retained. Target names, ordering, flags and state stay exact.

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

All 82 Python QA checks pass, including 14 pointer evidence tests: missing input,
wrong hit/target/clipping, early or disabled activation/repeated evaluation,
invalid flags, lost hover/capture/held state, malformed/order errors, unknown proof,
cleanup leaks/activation, cooked event display casing and incorrect automation labeling. Synthetic test fixtures
never count as runtime evidence. Six immutable references and ten staged SVG pairs
pass.

## Corrected harness defects

The first clean archive at `1f721cb` built successfully, but
`20261004-222542-packaged-capture-pointerpress` failed its validator: cooked `FName`
printed `Down`, whereas the editor printed `down`. The native state/press/capture/
cleanup were correct. Comparison now accepts event casing without discarding raw
evidence; an additional test still rejects unrelated event names.

The next archive at `691c1da` passed twelve cases but correctly rejected the final
260x640, safe .9, 200% resumed case (`20261004-223107-packaged-capture-pointerresumed`).
The new setup had incorrectly assumed Pause was fixed. Pause actually belongs to
the existing scrollable canvas; after selecting B, it was offscreen and failed hit
testing. No modal opened, and subsequent underlying clicks changed the attempt.
Setup now reveals Pause through the same scroll parent as all gameplay controls,
and the point uses that parent's clip. Production layout/handlers did not change.
The four-action Editor rebuild passes in 60.59s
(`Artifacts/Logs/Build/WordQuestEditor-20261004-223322.log`), followed by the passing,
inspected exact failing-case preflight `20261004-223527-capture-pointerresumed`.
Failed raw runs remain under ignored `Artifacts`; the failed second matrix is also
retained in `Pointer20261004/failed-scroll-setup-batch.json`.

## Final clean package and native matrix

Final source is `e7a343eeb60eb05908e263eb594891c4565c4025`. The Win64 Development
archive is `Artifacts/Packages/Win64/20261004-223707-418598`, with manifest SHA-256
`e22a18f4d86eb973664e4f449556c34ad01ec32c0d2b4c57812f366cb0a1beb1`.
BuildCookRun passes in 138.13s; the full cook reports 520 packages and zero errors/
warnings. Start worktree is clean; head, worktree and tracked inputs remain unchanged.
All 49 archived payload sizes/hashes verify again before each capture. Automatic
exact-executable firewall coverage passes on attempt one at
2026-10-04T22:39:44.4475719Z (Private/Public, LocalSubnet).

Each row below has native/helper exit zero and complete evidence, matching clean
source/package SHA, dimensions and manifest hash. Every applicable state, option
cue, pointer step, screenshot flag, cleanup, enlarged text and action-content check
passes. No native Error/Fatal lines were found. All thirteen PNGs were inspected.
Run prefixes below live under `Artifacts/QA/UI01/` and end in
`-packaged-capture-<mode>`; each retains `native.png`, raw log and `run.json`.

| Run prefix | Mode | Viewport | Text | Routed steps |
|---|---|---|---|---|
| `20261004-223950` | initial | 884x1780, safe 1 | 100% | baseline |
| `20261004-224005` | pointerhover | 390x844, safe .9 | 100% | 5 |
| `20261004-224018` | pointerpress | 390x844, safe .9 | 100% | 2 |
| `20261004-224028` | pointerhintpress | 390x844, safe .9 | 100% | 2 |
| `20261004-224038` | pointeranswerpress | 390x844, safe .9 | 100% | 2 |
| `20261004-224049` | pointerpausepress | 390x844, safe .9 | 100% | 2 |
| `20261004-224059` | pointerclick | 390x844, safe .9 | 100% | 15 |
| `20261004-224114` | pointerhint | 390x844, safe .9 | 100% | 12 |
| `20261004-224128` | pointerpaused | 390x844, safe .9 | 100% | 12 |
| `20261004-224142` | pointerresumed | 390x844, safe .9 | 100% | 15 |
| `20261004-224156` | pointerpress | 260x640, safe .9 | 200% | 2 |
| `20261004-224207` | pointerclick | 390x844, safe .9 | 200% | 15 |
| `20261004-224223` | pointerresumed | 260x640, safe .9 | 200% | 15 |

Native navy press outlines/overlays retain readable action labels and answer
identity. Held modes do not activate; released wrong/assisted-correct attempts
evaluate once and retain non-color markers; paused underlying targets miss the
hit path and preserve state. The initial PNG is exactly equal in RGB to PR #43's
`20261004-210417-packaged-capture-initial/native.png` (zero changed pixels, maximum
channel delta zero). This is regression evidence, not acceptance of the existing
art/material differences. At narrow enlarged sizes, reading still needs scrolling
and some words wrap across lines; this matrix does not qualify full typography or
manual reading/navigation.

`20261004-224239-automation-initial` records both Unreal Context tests succeeded,
zero failed/not-run/in-process, exit zero and complete evidence at the same clean
source. Python evidence is `Artifacts/Logs/UI01/pointer-python-final-checks.log`.
The local batch, verification (including every PNG hash) and pipeline records are
under `Artifacts/QA/UI01/Pointer20261004/`. No art/binary/reference files changed.
Review/publication documentation will not change the tested runtime source.
Dedicated read-only Codex review completes in `Artifacts/Reviews/20261004-224525`
against actual `origin/dev` base `baa03aabf874264a6bd4947a7ef0e4c335f732b2`,
reviewed head `dda891cf30d4e8c326a98958513910db3e344756`. Process exit is zero,
start worktree is clean and head/worktree remain unchanged. The report identifies
no actionable introduced defects and independently passes all 14 pointer tests.
It does not independently rerun Unreal builds, visual fidelity or device checks;
those evidence boundaries remain unchanged. Tested runtime source remains
`e7a343e`; subsequent commits update documentation only. Owner retains merge.
[PR #44](https://github.com/rloterh/WordQuest/pull/44) was owner-merged into `dev`
on 2026-10-05 at 01:17:57 UTC (`8f51a15`). The implementation/review helper did not
merge it; the recorded evidence and open acceptance gates remain unchanged.

## Open gates

These are synthetic virtual mouse events, not OS mouse/touch, physical-device,
manual pointer/keyboard or platform accessibility acceptance. They do not cover
pointer wheel/drag cancellation/double click, simultaneous physical/virtual users,
OS interruptions or physical target scale. Static art/type/material fidelity,
UI02 motion, draft fixture editorial approval, Android/phone, isolated offline,
performance and original release gates remain open. No later milestone, deployment,
release or owner merge occurs.
