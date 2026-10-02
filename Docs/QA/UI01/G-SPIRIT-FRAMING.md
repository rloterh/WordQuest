# G companion framing — identity acceptance pending

The owner merged PR #10 at `2f3c3f6` on 2026-10-02. Two attempts to reconstruct
a closer transparent spirit were inspected and rejected: the first retained a
large lantern and invented spherical head ornament; the gold-element correction
introduced a conspicuous four-point circlet star and different proportions. Both
are genuine RGBA, but alpha alone does not establish character identity. Neither
is imported, committed as runtime art or adopted as a new visual target.

Exact built-in imagegen prompts are in
`ArtSource/Companions/G/Reconstruction/G-Spirit-Reconstruction-20261002-PROMPTS.md`.
Generated outputs remain at their original Codex paths with ignored local copies
under `Artifacts/QA/UI01/g-spirit-rejected-20261002`. Source/output hashes and
inspection results are in adjacent `G-SPIRIT-FRAMING-PROVENANCE.json`.
No CLI/API fallback, script raster editing, original-pixel extraction or layered
art source is claimed.

## Bounded native change

The existing v001 PNG and genuinely imported `G_Spirit.uasset` remain byte-identical.
Their identity remains unaccepted. Read-only Pillow 12.1.0 inspection found a
1405x1119 RGBA export, zero corner alpha and a core bounding box
x114..1243/y62..1116 at alpha>16; faint generated specks extend beyond that core.
The Slate UV frame x106..1251/y54..1119 retains an eight-source-pixel margin,
clamped at the original bottom. It excludes some faint gutter pixels without
editing the source. It is not successful alpha cleanup; existing edge/face/
lantern differences remain.

The previous whole export was drawn at 207x165. Native layout now contains the
framed 1145x1065 image in the documented x82/y276, 207x185 reference region,
giving x86.052/y276, about 198.897x185 at reference size. The companion/lantern
retain that frame's aspect instead of stretching to the target rectangle.
Responsive composition scale and landscape hiding remain as before. No new
texture, import helper, animation, emission layer, learning or interaction change
is introduced. The six SVGs and all supplied references remain unchanged.

## Verification

The initial dirty editor capture `20261002-031244-capture-initial` was inspected
against the original and showed the framed candidate's main wisps and lantern
tip visible in the intended region. It is preliminary evidence, superseded by
the clean packaged runs below. The editor implementation built successfully in
six actions (`Artifacts/Logs/Build/WordQuestEditor-20261002-031014.log`, exit 0).

Final runtime source: clean `30b58f886101c6e9646eda092f7911810b3cb0b3`.
`python Tools/BuildScripts/package_g_win64.py` passed its clean editor build check,
rebuilt/linked the game in five actions, fully cooked 510 packages, staged and
archived, with all exits 0. UAT completed in about 2m31s. Logs/manifests are under
`Artifacts/Packages/Win64/20261002-031511-853620`; the editor check also records
`Artifacts/Logs/Build/WordQuestEditor-20261002-031511.log`.
The package `run.json` SHA256 is
`beb19064dc1f78ff56963aa515bc215190b9466b72850ddded4bf6e8461283f1`.
HEAD, worktree and input-hash invariants remained unchanged. This is local Win64
Development only. The PNG/Unreal texture hashes match the ArtSource provenance
and neither binary differs from `origin/dev`.

Each native packaged run verified archived payload hashes before launch, exited
0, and passed requested dimensions/initial unselected, unevaluated state. Clean
source and package provenance are in each `run.json`. All PNGs were inspected:

| Run under `Artifacts/QA/UI01` | Observation |
| --- | --- |
| `20261002-031846-packaged-capture-initial` | 884x1780; framed existing companion visible, main wisps and lantern tip included, no opaque export rectangle; compared directly with unchanged reference |
| `20261002-031858-packaged-capture-initial` | 390x844, simulated 0.9 safe-zone ratio; companion keeps frame aspect/reference-region scale; live reading and controls remain visible |
| `20261002-031908-packaged-capture-large` | 390x844, simulated 0.9 inset; 200% live reading rows expand/scroll while the decorative companion retains its composition scale |
| `20261002-031918-packaged-capture-initial` | 844x390; companion and progress remain hidden in compact landscape; title/Pause/header visible and reading continues below viewport |

Both existing `WordQuest.Context` tests passed with zero failures/skips in
`20261002-031926-automation-initial/Report` (editor commandlet, not packaged tests).
All six original-reference hashes, six SVG source/runtime parity checks, LFS
integrity and diff whitespace checks pass. No new binary asset was committed.

`Artifacts/QA/UI01/g-spirit-framing-comparison.html` embeds the final native PNG,
immutable original and an adjustable 50% overlay. Browser/overlay interaction
remains unverified; prior local-navigation blocks were not bypassed. No physical
phone, manual pointer/keyboard, screen-reader service, offline-isolation or
performance verification is claimed.

Dedicated read-only Codex review of clean `b1cb19c` against actual `origin/dev`
(`2f3c3f6`) completed with exit 0 and no actionable introduced defects. It confirmed
that the UV/layout aspect calculation and the recorded limits matched the declared
scope; builds/runtime/device checks were not independently rerun. Raw evidence:
`Artifacts/Reviews/20261002-032154`; HEAD/worktree were unchanged. Optional connector
warnings did not prevent review completion. Subsequent changes only record review/
publication status in documentation. Review does not authorize merge or replace
art/device acceptance.

## Remaining gates

The existing face, eyes, circlet, lantern proportions and fine wisps still differ
from the original. Framing does not pass identity, alpha-edge or UI01 acceptance.
Material/lettering fidelity, fixture review, manual input/screen reader, offline
isolation, mobile tools/phone, frame-time/memory, UI02 motion and release remain
open. Cold D3D12 pipeline delay remains unresolved; renderer settings are unchanged.
