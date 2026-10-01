# G Hint, Check and Pause skin candidates — acceptance pending

After the owner merged PR #5 into `dev` (`8c105ac`), this bounded increment adds
three separate imported control surfaces behind live Hint, Check answer and Pause
labels. Buttons retain their hit regions, accessible names and existing behavior.
Decorative images are hit-test invisible and follow the button's enabled state.
Missing textures retain the prior flat-fill/text fallback. Pause uses white live
bars over its loaded purple skin; its fallback still uses the prior dark label.

Skinned action controls use their art border in normal/disabled states, preserving
native hover/press overlays and focus outlines. Their outline radius follows half
the shorter control dimension. Answer-option styles and scoring remain separate.
Hint/Check skins use framed nine-slice brushes and texture-sized widgets with
reference drawing scale, preserving bounded corners when enlarged actions stack.
Pause retains direct image drawing at its existing accessible bounds.

## Assets and genuine Unreal import

Built-in imagegen reconstructed three blank skins from the immutable G gameplay
reference. Hint v001, Check v001 and Pause v001 are retained candidates. Subsequent
Check/Pause cleanup attempts did not improve colored fringe and were rejected;
those outputs are neither imported nor committed. No successful perimeter cleanup
is claimed. The selected PNG masters are copied unchanged under
`ArtSource/UI/G/Reconstruction`. Exact prompts, generated filenames, SHA-256,
alpha bounds, runtime UVs and import settings are in `G-ACTION-SKINS-PROMPTS.md`
and `G-ACTION-SKINS-PROVENANCE.json` in that directory.

All three masters are genuine 8-bit RGBA with corner alpha zero. No manual raster
or alpha editing, exact extraction of original pixels or layered source is claimed.
UV framing omits large empty margins/excess shadow; it is not complete edge cleanup.
Generated core proportions are adapted to reference control dimensions.

Unreal generated `G_HintSkin.uasset`, `G_CheckSkin.uasset` and `G_PauseSkin.uasset`
under `Game/Content/UI/G`. The texture-only commandlet used
`Tools/AssetImport/import_g_action_skins.py`, with sRGB/UI compression, bilinear
filtering, no mips/streaming and maximum texture sizes 1024/1024/512 respectively.
These settings are not measured memory/performance qualifications. Verified log:
`Artifacts/Logs/UI01/ActionSkinsImport-20261001-commandlet.log`, exit 0,
`WORDQUEST_ACTION_SKINS_IMPORT_COMPLETE`, zero errors/warnings. PNG/uasset binaries
use Git LFS; integrity and master hashes pass. All six supplied references retain
their original hashes. Caches and ordinary outputs remain ignored.

## Native checks, 2026-10-01

The first editor build caught a const-pointer compilation error in the skin-state
helper; it was corrected. Final source implementation `4e78be0` passed both real
Win64 Development targets, exit 0: `Artifacts/Logs/Build/WordQuestEditor-20261001-211619.log`
and `WordQuest-20261001-211804.log`. Both existing `WordQuest.Context` tests passed,
zero failures/skips, in `Artifacts/QA/UI01/20261001-212021-automation-initial/Report`.

All final native runs below used clean `4e78be0`, exited 0, recorded the requested
dimensions and passed their expected state tuples. Each `run.json` records the
command/revision. PNGs were inspected directly; tuple/dimension checks do not measure
fidelity. The development-only `actions` proof enlarges reading text to 200% and
focuses Check after layout to expose both stacked controls without evaluating.

| Run under `Artifacts/QA/UI01` | Observation |
| --- | --- |
| `20261001-212103-capture-initial` | 884x1780; three separate skins, live labels, no selection/evaluation; compared directly with immutable original |
| `20261001-212207-capture-actions` | 390x844, requested simulated safe-zone ratio 0.9; both 200% actions fully visible, Check focus outline retained, no selection/evaluation |
| `20261001-212227-capture-hint` | 390x844; assisted correct A, one evaluation; disabled skins, Hint used/Answer checked labels and complete feedback visible |
| `20261001-212246-capture-paused` | 390x844; selected B remains unevaluated while paused; foreground modal/Resume focus preserved |

Earlier `20261001-211253-capture-initial` used `0b69282`; it exposed extra normal
rounded outlines over the art and is not final evidence. That normal/disabled
outline was removed for skinned actions before the final captures. Fallback and
answer-option outlines remain. `Artifacts/QA/UI01/g-action-skins-comparison.html`
embeds the unchanged final PNG and original with a 50% overlay. Browser interaction
is unverified; prior local-navigation policy blocks were not bypassed.

Dedicated review against actual `origin/dev` will be recorded after completion.
It does not authorize a merge or replace native/device evidence.

## Remaining differences and gates

Gold brightness/thickness, generated gloss/glints, corner geometry, purple lighting,
shadow/fringe and live font metrics still differ. The Hint bulb and large Check
star are missing; label grouping therefore differs from the original. Brand,
spirit identity, panel and divider art remain unfinished/candidates. Draft fixture
editorial approval is pending. These are working surfaces, not accepted UI01 fidelity.

No manual pointer/keyboard sequence, hover/press capture, screen-reader service,
packaging, offline cold launch, phone touch or GPU/memory test was performed for
this increment. Programmatically established native focus and desktop simulated
safe areas are not physical-device acceptance. Android engine support and a
connected phone remain missing. UI01 static fidelity, UI02 motion, device and
release gates remain open.
