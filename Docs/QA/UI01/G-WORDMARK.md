# G vector wordmark candidate — acceptance pending

Following the owner's PR #9 merge (`c3eece4`, 2026-10-02), this bounded UI01
increment adds a separate editable brand candidate. It replaces the plain visible
Cormorant title with outlined lettering, capital curls, pale-gold shading, a
separate Q swash and the under-title star/flourish. It is not accepted original
lettering or a visual-gate pass.

## Source and runtime behavior

The 430x140 editable master is `ArtSource/UI/G/Vector/G-Wordmark-v001.svg`;
`stage_g_action_icons.py` copies it exactly to
`Game/Content/UI/G/Vector/G_Wordmark.svg`. The existing raw-resource UFS staging
directory includes it. The previous five SVGs, supplied references, raster
masters, learning fixture and scoring are unchanged. No new binary asset or
fabricated Unreal asset is introduced.

`build_g_wordmark.py` outlines the repository's unmodified OFL Cormorant Garamond
SemiBold font and adds authored closed curves. Font provenance/redistribution
license remain adjacent to the original TTF; this is a derivative graphic, not
a new font or identification of the reference typeface. The vector README records
the optional pinned fontTools 4.61.1 reproduction command. Builds use the committed
SVG and do not require fontTools. No image generation/raster editing was used.

Native `FSlateVectorImageBrush` renders the mark at reference coordinates
x229/y23, 430x140, proportional to the existing composition width. It follows
the existing centered responsive hero in portrait/landscape and scrolls with the
screen; learning/control text retains its live 200% sizing path. The mark has a
custom `WordQuest` accessibility name and no pointer hit target. The original
live `Brand` text object is collapsed only when the SVG exists, preserving its
fallback when absent. No screen-reader service pass is claimed.

## Verification

The initial dirty editor capture `20261002-021319-capture-initial` exposed flat
amber shading from unit-valued gradient coordinates. That version is rejected
as final visual evidence; coordinates were changed to explicit SVG percentages.
The first narrow missing-resource capture kept the live label readable but too
close to Pause; its fallback font size was reduced from 108 to 95 reference pixels.

Final runtime source: clean `1d76858e60fd01570035e28608e1aa9cabea666e`.
`python Tools/BuildScripts/package_g_win64.py` completed editor/game builds,
full cook (510 packages), stage and archive with exit 0. Final editor build rebuilt
four actions (`Artifacts/Logs/Build/WordQuestEditor-20261002-022430.log`); UAT
rebuilt the game in three actions and completed in about 2m11s. Package evidence:
`Artifacts/Packages/Win64/20261002-022430-698363/run.json`, SHA256
`40ab48c1e88ec7b50a72f103953d15159cc703c0f0ef938d77b39d3bf9458618`.
HEAD, worktree and input invariants remained unchanged. `UAT.log`/`EditorBuild.log`
retain the actual commands and results. This is Win64 Development, not mobile or
Shipping. The earlier successful `9e04616` package/captures are superseded by this
final fallback-size revision.

UnrealPak extraction exited 0. `PakExtract.log` and `RawResources.json` in the final
run record the draft JSON and all six SVGs; extracted bytes match recorded input
hashes. The new SVG SHA256 is
`e397842f40e69c65cd16ef4bd44185adfc72f89bdc6b6c6765215416f05ffd9d`.
Native packaged captures below verified the archive hashes before each launch.
All exited 0, passed requested dimensions/expected state and record clean source
and package commits in `run.json`. Each PNG was directly inspected:

| Run under `Artifacts/QA/UI01` | Native observation |
| --- | --- |
| `20261002-022800-packaged-capture-initial` | 884x1780; pale-gold outlined title/curls/Q swash/star visible; initial no selection or evaluation; compared directly with unchanged original |
| `20261002-022811-packaged-capture-pausefocus` | 260x640, simulated safe-zone ratio 0.9; smaller mark remains readable and separate from focused minimum-size Pause |
| `20261002-022821-packaged-capture-large` | 390x844, simulated 0.9 safe zone; brand retains its decorative scale while live 200% reading rows expand/scroll |
| `20261002-022830-packaged-capture-initial` | 844x390; compact hero retains title/ornament and Pause; progress/spirit hidden as before; reading continues below viewport |
| `20261002-022839-packaged-capture-correct` | 390x844; A correct, submitted, one evaluation after two Submit calls; title independent of disabled controls/feedback |

Both existing `WordQuest.Context` tests passed with zero failures/skips in
`20261002-022848-automation-initial/Report` (editor commandlet, not packaged tests).
Five packaging-helper failure tests, six source/runtime SVG parity checks, all six
original-reference hashes, LFS integrity and diff whitespace checks pass.

The negative test temporarily moved only `G_Wordmark.svg`, then restored its exact
hash in a finally block. Parity failed with the expected exit 1 (log under
`missing-wordmark-20261002-0229`). `20261002-022916-capture-pausefocus` exited 0
at 260x640 with simulated 0.9 inset; its metadata explicitly records that one
runtime deletion, so this is dirty fallback evidence. Direct inspection shows the
smaller live title clear of focused Pause, unchanged reading layout and no
selection/evaluation. Resources were restored and clean status/parity rechecked.

`Artifacts/QA/UI01/g-wordmark-comparison.html` embeds the final native PNG,
immutable original and adjustable 50% overlay. Browser/overlay interaction remains
unverified; prior local-navigation blocks were not bypassed. This is not a static
fidelity acceptance record. No manual pointer/keyboard or screen-reader service
sequence was performed. Earlier cold D3D12 pipeline delays remain an unresolved
performance observation; renderer settings were not changed or qualified here.

Dedicated read-only Codex review of clean `0f9ed17` against actual `origin/dev`
(`c3eece4`) completed with exit 0 and no actionable introduced defects.
Raw evidence: `Artifacts/Reviews/20261002-023059`; HEAD/worktree were unchanged.
The reviewer checked SVG parity, original-reference hashes and whitespace, but
did not independently rerun builds/runtime/device checks. Optional connector and
ignored local-tool directory warnings did not prevent the review from completing.
Subsequent changes only record review/publication status in documentation. Review
does not authorize merge or replace native/device evidence.

## Remaining gates

Letter contours, W curls, Q connection/taper, precise bevel/light and spacing
still differ from the original; owner art acceptance is open. Existing spirit
identity, panel/surface finish and exact typography remain candidates. The fixture
remains editorially unapproved. No UI02 motion, H/I expansion, phone, offline
isolation, Shipping/release or performance qualification is established here.
