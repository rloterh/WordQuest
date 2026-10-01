# Native G answer controls — bounded follow-up

The owner merged PR #2 into `dev` at `eff9f50` on 2026-10-01. This follow-up
restores separate live A–D badges and the answer text column in the native prototype.
It is a control-layout increment; overall UI01 fidelity remains unaccepted.

## Changes

Each answer remains one native button, with a round badge, live letter, fixed-width
selection marker and live answer label. Selecting an option displays `>` and an
outline without moving the answer text or indicating correctness. Accessible button
labels retain the option letter, answer and selected state. Native keyboard focus,
pause restoration and completed-answer disabling continue through the same buttons.
No question, scoring, imported asset or original reference was changed.

At the 884-pixel reference width, badge bounds begin at x=137 with diameter 70;
answer label bounds begin at x=244, near the reference's x≈240. Existing row bounds
and typography candidates remain. These are layout coordinates, not an assertion
that the original artwork, font metrics, bevels or gradients are matched.

Badges and reading text enlarge with the existing 200% setting. Labels wrap within
the width left after badges, markers, style padding and native button-slot padding.
Oversized individual words may wrap within the word. Initial stress captures exposed
overflow of “noncommittal”; the final layout corrects both word wrapping and the
previously omitted slot padding.

The non-shipping `longfocus` proof enlarges and extends the draft fixture, then focuses
B after layout. The engine scrolls B into view before its native screenshot. This
exercises the actual focus/scroll layout without changing selection or evaluation.

## Evidence, 2026-10-01

Final implementation: `85cf6db`. Both real Win64 Development targets built with exit 0:

- Editor: `Artifacts/Logs/Build/WordQuestEditor-20261001-171244.log`.
- Game: `Artifacts/Logs/Build/WordQuest-20261001-171341.log`.

Native runs below exited 0 with expected state tuples and PNG dimensions. Their
`run.json` records the exact HEAD/worktree and command. PNGs were inspected directly.

| Run under `Artifacts/QA/UI01` | Observation |
| --- | --- |
| `20261001-171330-capture-initial` | Clean `85cf6db`, 884x1780, four badges, no selection/evaluation; compared with immutable G original |
| `20261001-171330-capture-longfocus` | Clean `85cf6db`, 390x844, enlarged extended answers; B focused, fully visible, no horizontal text overflow in the visible answer area |
| `20261001-170307-capture-selected` | Before wrapping corrections, 884x1780; C marker/outline, other text positions unchanged, no evaluation |
| `20261001-170626-capture-correct` | Clean `b70ff3f`, before slot-padding correction, 390x844; A checked, exactly one evaluation, disabled controls and complete feedback |

The two existing `WordQuest.Context` automation tests passed again on clean
`85cf6db`, zero failures/skips, under
`20261001-171459-automation-initial/Report`.

Dedicated read-only Codex review completed with exit 0 and no actionable introduced
defects at clean `924ffc6`, against actual base `origin/dev` (`eff9f50`). Raw report
and base/head/worktree metadata: `Artifacts/Reviews/20261001-171732`. The reviewer
did not rerun build/runtime checks and did not authorize a merge. Subsequent changes
only record review/publishing status in documentation; implementation is unchanged.

Reproduce the added stress capture with:

```powershell
python Tools/QA/run_g_proof.py capture --proof longfocus --width 390 --height 844
```

Comparison document: `Artifacts/QA/UI01/g-answer-controls-comparison.html`, generated
from the final initial PNG and unchanged original. Browser overlay interaction is
still unverified; prior local navigation policy blocks were not bypassed.

## Limits and next work

Manual Windows input verification was unavailable: the native computer-use pipe
failed after the prescribed retries/reset. Automated native rendering and focus
evidence does not certify manual clicking, screen-reader behavior or phone touch.
The long-focus screenshot can include a desktop hover tooltip; it is not final art.

Flat answer skins still lack the supplied bevel/shadow/gradient. Branding, panel,
companion identity, ornaments and action artwork remain candidates or unfinished;
the editorial fixture remains draft. Android engine support and a connected phone
are still missing. UI01, UI02 and physical-device/release gates remain open.
Continue the documented G static art work before motion or H/I expansion.
