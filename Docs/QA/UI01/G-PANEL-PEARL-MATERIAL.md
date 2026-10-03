# G pearl/mauve reading-panel material candidate

The owner merged PR #36 into `dev` at `b316266` on 2026-10-03, 12:36:52 UTC.
This bounded UI01 correction addresses the comparatively flat, pale authored
reading surface. The supplied original remains immutable. The prior native
baseline is `Artifacts/QA/UI01/20261003-115504-packaged-capture-initial/native.png`,
SHA-256 `d70d52a3d342153af94630b03b897c5516511f1f78d4fd4b26b784efc6cce7f2`.

## Editable source and integration

`ArtSource/UI/G/Vector/G-Reading-Panel-v002.svg` authors cooler mauve edges,
a lighter pearl center, diffuse fixed-seed mottling and a warm lower reflection.
The v001 contour, 790x1140 canvas, outer shadow and rim are unchanged. There are
no baked labels, controls, dividers or star. Earlier SVG/export/Unreal assets and
all original reference images are preserved. This is a hand-authored simplified
material candidate, not extraction of original pixels or accepted painterly fidelity.

`render_g_reading_panel.py --version v002` uses pinned development-only resvg-py
0.5.0 / resvg 0.48.1 to render 1185x1710 RGBA. `--check` reproduces exact bytes.
Default v001 reproduction remains intact. Builds use checked-in genuine Unreal
assets and do not depend on the development renderer.

The texture commandlet's explicit `-WordQuestPanelPearl` switch imports v002
as separate `G_ReadingPanelPearl`, verifying the pinned export and Texture2D/save.
It uses sRGB/UI compression/group, bilinear filtering, no mips or streaming.
Native loading prefers it, then the preserved `G_ReadingPanel`, then legacy
`G_Panel`. Both authored textures use the same fixed top/bottom cuts at 220/1010.
Only the body stretches; its diffuse material stretches with responsive content.
The independent star and all learning/input/layout behavior are unchanged.
The separate star is collapsed only on the legacy texture that already has one.

Each full-size BGRA8 panel is about 7.73 MiB before engine bookkeeping. A separate
candidate can add packaged bytes while preserving fallback; this is not measured
GPU memory or device performance. Native loading skips the old authored panel when
the candidate loads successfully. Fallback omission and cooked evidence are pending.

## Current verification

Source parsing confirms identical canvas and contour. RGBA alpha is 0–255,
nonzero bounds [17,21,1168,1677), with four transparent corners and no internal
row holes at alpha >=128. These are scoped contour checks only. Both versions
reproduce exactly. Actual import exited 0 with its completion marker and
0 errors/warnings in `Artifacts/Logs/UI01/reading-panel-v002-import.log`.
The saved texture is 931,404 bytes, SHA-256
`86a5d1155a40882bcf9593eba1e72406b3d4426c3e85f34f381b11f98359e449`.
Source/export hashes and settings are in adjacent v002 provenance.
Both the PNG and genuine Unreal asset use configured Git LFS.

Actual Editor compilation passed four actions in 89.41s, exit 0:
`Artifacts/Logs/Build/WordQuestEditor-20261003-125137.log`.
Dirty native preflight `20261003-125330-capture-initial` exited 0 with complete
dimension/state/cue evidence. Shutdown waited for DDC tasks and exited normally.
Its native PNG was inspected beside the original and prior baseline, with enlarged
surface/reflection crops and a diagnostic half-opacity overlay. It shows cooler
edges and subtle diffuse depth while retaining readable live content. Mottling
and lower reflection patterns remain simpler/different from the original.

Twelve fixed 5x5 median samples at x100/440/780, y680/775/880/970 avoid live text
and controls. Mean absolute RGB channel error against the original is 8.03 for
the prior baseline and 4.17 for this candidate. These selected material points
exclude lower geometry and control-shadow differences; they are not a global
fidelity score. Their minimum contrast against opaque native ink RGB(24,20,83)
is 10.92:1, not an all-state or antialiased-glyph accessibility qualification.
Matched initial comparison changes 446,762 RGB pixels within [67,530,817,1610),
with zero changes outside panel region [47,509,837,1650). This measures composited
rendering, not only raw texture pixels. Original/baseline hashes remain unchanged.
`Artifacts/QA/UI01/PanelPearl/comparison.json` records samples and input hashes.
All 66 Python checks, eight SVG pairs and six original reference hashes pass.
Missing-candidate texture runs `20261003-125828-capture-initial` (884x1780) and
`20261003-125934-capture-actions` (390x844, simulated .9 inset, 200%) exited 0
with complete applicable native checks. Both PNGs were inspected. Initial fallback
is RGB-identical to the merged PR #36 baseline; enlarged actions/focus remain
visible. The owned candidate was restored with its exact hash, recorded in
`PanelPearl/fallback.json`. Missing-package warnings are expected in this editor
omission test. This does not corrupt or qualify a packaged game.
Game compilation, packaging, final responsive/input captures and dedicated review
remain in progress.

## Remaining gates

Full UI01 material/brand/companion fidelity and art acceptance, editorial approval,
UI02 motion, manual/platform accessibility, Android/physical-phone evidence,
offline isolation, performance and the original release gates remain open.
Windows offscreen rendering and synthetic input do not pass manual/device gates.
