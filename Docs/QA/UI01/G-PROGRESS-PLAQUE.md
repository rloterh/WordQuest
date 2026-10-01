# G progress-plaque candidate — acceptance pending

After the owner merged PR #4 into `dev` (`70a8af0`), this bounded increment restores
a separate purple/gold plaque behind live `3 / 7`. The value still describes the
draft prototype fixture; it is not persisted campaign progress. The decorative
image is hit-test invisible, drawn before the label and collapsed with it in the
compact landscape hero. A missing texture leaves the existing live text available.

## Source and genuine Unreal import

Built-in imagegen reconstructed only the blank plaque from the immutable original
G reference, then attempted one edge/proportion correction. v001 was rejected and
not imported. The v002 working master is copied unchanged to
`ArtSource/UI/G/Reconstruction/G-Progress-Plaque-v002-Candidate.png`, 2141x734 RGBA,
with alpha zero at all four corners. Adjacent prompt and provenance files record
the exact prompts, SHA-256, alpha bounds, runtime UVs and remaining differences.
No manually edited raster, exact original-pixel extraction or layered source is claimed.

Unreal's texture-only Python commandlet generated
`Game/Content/UI/G/G_ProgressPlaque.uasset`. Import uses sRGB/UI compression,
bilinear filtering, no mips/streaming and maximum texture size 512. These are
settings, not a measured GPU-memory/performance qualification. PNG and uasset are
tracked through Git LFS; integrity checks pass. All six supplied references retain
their original hashes.

```powershell
& 'C:/Program Files/Epic Games/UE_5.8/Engine/Binaries/Win64/UnrealEditor-Cmd.exe' 'C:/Projects/WordQuest/Game/WordQuest.uproject' -EnablePlugins=PythonScriptPlugin -run=pythonscript '-script=C:/Projects/WordQuest/Tools/AssetImport/import_g_progress_plaque.py' -Unattended -NullRHI -NoSplash -NoSound
```

Verified import: `Artifacts/Logs/UI01/ProgressPlaqueImport-20261001-commandlet.log`,
exit 0, `WORDQUEST_PROGRESS_PLAQUE_IMPORT_COMPLETE`, zero errors/warnings.

The first native capture showed the export's margins making the plaque too short
and the text touching the top border. Runtime UVs now frame `[34,94,2108,608]`
(half-open source-pixel bounds); the image is drawn in reference slot
`[352,169,178,61]`. The label is vertically centered using its native desired size.
The source PNG is intact. The wider generated core is adapted to the reference slot;
this is an explicit reconstruction compromise, not identical source geometry.

## Native verification, 2026-10-01

Final implementation `99e724f` passed both real Win64 Development targets, exit 0:
`Artifacts/Logs/Build/WordQuestEditor-20261001-193131.log` and
`WordQuest-20261001-193510.log`. Both existing `WordQuest.Context` tests passed,
zero failures/skips, under
`Artifacts/QA/UI01/20261001-193643-automation-initial/Report`.

All final captures below ran from clean `99e724f`, exited 0, recorded their requested
dimensions and expected initial tuple (no selection, submission, hint, pause or
evaluation). PNGs were inspected directly. Each `run.json` records the command and
revision. The tuple/dimension checks do not measure fidelity.

| Run under `Artifacts/QA/UI01` | Observed result |
| --- | --- |
| `20261001-193229-capture-initial` | 884x1780; visible plaque at reference position, centered live text, compared directly with original |
| `20261001-193322-capture-initial` | 390x844, requested desktop safe-zone ratio 0.9; plaque/text inside the inset composition, narrow text reflow retained |
| `20261001-193426-capture-initial` | 844x390; plaque and label both hidden in compact hero; reading panel continues below viewport, not a full landscape interaction pass |

Earlier `20261001-192909-capture-initial` records the pre-correction placement from
a dirty worktree and is not final evidence. The ignored comparison page
`Artifacts/QA/UI01/g-progress-plaque-comparison.html` embeds the unchanged final
PNG and original with a 50% overlay. Browser interaction remains unverified; prior
local-navigation policy blocks were not bypassed. Direct image inspection is the
visual evidence here.

Dedicated read-only Codex review completed at clean `61fd184` against actual
`origin/dev` (`70a8af0`), exit 0, with no actionable introduced defects. Evidence:
`Artifacts/Reviews/20261001-194029`. HEAD/worktree were unchanged during review;
builds/runtime checks were not rerun by the reviewer. Subsequent changes only
record review/publishing status in documentation. Review does not authorize a merge.

## Differences and remaining gates

The native plaque is a candidate: gold thickness/brightness, bevel, purple lighting,
corners, faint fringe and text metrics differ from the original. Runtime framing
omits distant stray pixels but is not complete edge cleanup. Brand lettering,
spirit identity, panel, dividers and action skins are still unfinished/candidates;
fixture editorial approval remains pending.

No manual input, orientation-transition interaction, accessibility-service,
packaging, phone-touch, offline cold-launch or GPU/memory test was run for this
increment. Simulated desktop safe areas are not physical-device evidence. Android
engine support and a connected phone remain missing. UI01 static fidelity, UI02
motion, physical-device and release gates remain open.
