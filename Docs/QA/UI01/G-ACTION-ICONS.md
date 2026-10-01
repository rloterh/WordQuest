# Separate G action icons — acceptance pending

The owner merged action-skin PR #6 at `3acca49` on 2026-10-01. This bounded static
follow-up adds separate Hint bulb and Check star candidates beside the existing
live labels. Scoring, draft fixture, motion and Pause behavior are unchanged.

## Source and layout

Editable SVG masters and provenance are under `ArtSource/UI/G/Vector`. These are
hand-authored reconstructions, not exact extracted art. The staging helper copies
them into `Game/Content/UI/G/Vector` and `--check` validates exact byte parity.
The six supplied reference hashes pass unchanged. There are no new binary assets.

The installed UE 5.8.2 defines `FSlateVectorImageBrush` in
`Runtime/SlateCore/Public/Brushes/SlateImageBrush.h`; its SVG rasterizer loads the
file through Unreal's file helper. Native captures demonstrate desktop rendering.
`DefaultGame.ini` declares `UI/G/Vector` for UFS staging. Cooking/packaging has
not been run, so packaged-resource availability remains unverified.

Each action now contains a centered icon/label row. Labels remain live text and
retain the existing button semantics; decorative icon widgets use
`NotAccessible` behavior. This is a code path, not a screen-reader-service pass.
Layout measures the complete desired group including slot padding, grows action
height and stacks actions when either group cannot fit or text is above 120%.
The existing 48-unit minimum height and focus outline are retained. Icons scale
with reading text. Missing files collapse both image space and icon/label gap.

At narrow width, the decorative spaced mode heading now falls back to intact
`CONTEXT DETECTIVE` before normal wrapping. Wide reference-size lettering remains
spaced. The development-only `actionfocus` proof focuses Check at normal reading
size without evaluating; the existing `actions` proof does so at 200%.

## Verification, 2026-10-01

Final source implementation: clean `82a9ec8ced27ca0bbdf3ed1bef3eece21fa0d8f0`.
Both real Win64 Development builds exited 0:

- `Artifacts/Logs/Build/WordQuestEditor-20261001-221209.log`
- `Artifacts/Logs/Build/WordQuest-20261001-221341.log`

Both existing `WordQuest.Context` Unreal tests passed, zero failures/skips, in
`Artifacts/QA/UI01/20261001-221523-automation-initial/Report`. Source/runtime
SVG parity passes. Native runs below used clean `82a9ec8`, exited 0, recorded
expected dimensions and passed their state tuples. Each `run.json` records the
command/revision. PNGs were inspected directly; state checks do not measure fidelity.

| Run under `Artifacts/QA/UI01` | Observation |
| --- | --- |
| `20261001-221600-capture-initial` | 884x1780; both icons beside live labels, no selection/evaluation; compared directly with original |
| `20261001-221636-capture-actions` | 390x844, requested simulated safe-zone ratio 0.9; both stacked 200% actions/icons fully visible, Check focus retained |
| `20261001-221658-capture-hint` | 390x844; assisted correct A, one evaluation; disabled icons and Hint used/Answer checked labels, complete feedback visible |
| `20261001-221718-capture-initial` | 260x640; intact mode words and automatically stacked 100% actions; Check is below the viewport |
| `20261001-221737-capture-actionfocus` | 260x640; programmatic focus scroll exposes both complete 100% action groups, no selection/evaluation |

An intentional missing-resource test temporarily moved only the two runtime SVGs.
`--check` then returned the expected exit 1. Native run
`20261001-221947-capture-actions` exited 0 at 390x844 with the expected unselected
state: live labels and Check focus remained visible with no reserved icon gap.
Its `run.json` explicitly records the two deleted runtime files, so this is dirty
negative-test evidence, not a clean-source capture. Both resources were restored;
parity and the clean worktree were rechecked.

Earlier captures from `11c3bbe` exposed the narrow heading's split final letters;
that issue was fixed before the final builds and captures. The ignored comparison
page `Artifacts/QA/UI01/g-action-icons-comparison.html` embeds the final normal PNG,
the original and a 50% overlay. Browser interaction is unverified; prior local
navigation policy blocks were not bypassed.

Dedicated read-only review is pending against the actual `origin/dev` base.

## Remaining differences and gates

The vector bulb outline and star faceting/light are reconstruction candidates.
Exact shape/material acceptance, action skins/font metrics, brand, spirit identity,
panel and divider remain unfinished. The original images remain the targets.
The fixture remains editorially unapproved. No UI01 fidelity pass is claimed.

No manual pointer/keyboard sequence, hover/press capture, screen-reader service,
packaged SVG check, offline cold launch, phone touch or GPU/memory qualification
was performed for this increment. Programmatic desktop focus and simulated safe
areas do not establish physical-device acceptance. On 2026-10-01 the Android
`UnrealGame.target` receipt was still absent and `adb devices -l` listed no phone.
UI01 static fidelity, UI02 motion, package/device and release gates remain open.
