# G authored reading-panel candidate

The owner merged PR #33 into `dev` at `373de75` on 2026-10-03, 09:20:43 UTC.
This bounded UI01 correction addresses the generated panel's bright/thick rim,
high shoulders, oversized star and outer fringe. The immutable original remains
the visual target. Its reference-size prior packaged native baseline is
`Artifacts/QA/UI01/20261003-084848-packaged-capture-initial`.

## Attempt and authored candidate

A built-in imagegen edit using the preserved panel v002 and original gameplay
reference was rejected: the outer fringe remained and the star stayed too large.
It was not imported. The exact prompt, output hash and disposition are recorded
in `ArtSource/UI/G/Reconstruction/G-Panel-v003-ATTEMPT.md`. No CLI/API fallback,
raster paintover or replacement of supplied references was used.

The subsequent authored `ArtSource/UI/G/Vector/G-Reading-Panel-v001.svg` contains
an editable contour, narrow pale champagne/ivory rim, restrained inner shading,
pearl/lilac gradients, subtle fixed-seed grain and local soft shadow. It contains
no text, dividers, controls or star. Its simplified surface is a candidate; it
does not reproduce every painterly detail or accept exact fidelity.
The separate `G-Panel-Star-v001.svg` is a small subdued lilac four-point ornament,
staged byte-identically as `Game/Content/UI/G/Vector/G_PanelStar.svg`.

Pinned development-only resvg-py 0.5.0 / resvg 0.48.1 renders the blank panel at
1.5x (1185x1710 RGBA). `render_g_reading_panel.py --check` reproduces it without
writing. Ordinary builds use checked-in export/Unreal assets without this renderer.
The full-size BGRA8 surface is approximately 7.73 MiB before engine bookkeeping,
versus about 6 MiB for the old source dimensions; this is a source-size calculation,
not measured GPU memory or phone performance. Earlier PNG/Unreal assets are preserved.

Unreal's actual texture commandlet imports a separate `G_ReadingPanel` with
sRGB/UI compression/group, bilinear filtering, no mips and no streaming. The helper
checks the pinned export hash, imported Texture2D type and successful save.
Both new PNG and genuine Unreal texture use configured LFS.

## Native integration

The logical panel is 790x1140. Fixed top/bottom cuts at 220/1010 preserve arch and
corners; only the body stretches as long/enlarged text or feedback grows. The
lower corner curves start exactly at the 1010 cut. Native placement retains the
existing 220/130 reference-unit top/bottom heights, panel bounds and 80-unit lower
padding. The separate 36x42 star occupies x424/y550 at the reference size and
scales with composition; it remains decorative and hit-test invisible.
Missing authored texture selects the preserved old texture and its original UV
cuts, and collapses the separate star to avoid a duplicate legacy ornament.
Missing star SVG omits only decoration. Reading text, actions, scoring, focus,
scrolling and draft fixture remain independent of this artwork.

## Verification in progress

Actual Editor compilation passed six actions in 78.95s, exit 0:
`Artifacts/Logs/Build/WordQuestEditor-20261003-094236.log`.
Dirty native preflight `20261003-094445-capture-initial` exited 0 with complete
dimension/state/cue evidence and was compared directly with the original. Its
thin rim, shoulder contour and smaller separate star are closer in those respects;
the surface remains simpler/flatter and final material acceptance is open.
The final source moves the start of the lower curves to the exact fixed-slice
boundary; fresh import/package evidence follows. All 66 Python QA tests and the
six original reference hashes pass; runtime SVG parity now checks eight pairs.

## Remaining gates

Final authored import exited 0, reporting 0 errors/warnings and its completion
marker in `Artifacts/Logs/UI01/reading-panel-import-final.log` / `.json`.
Export SHA-256 is `b179748f71d1977d1df26f0f7985418e867d94e0ac8d8f270fbe2981e8bfa734`;
the genuine saved asset is 557,502 bytes, SHA-256
`337cb0d335db5076c8bf69b4f2c351eea4ec461822780d1bfef14d9eee6aa5ac`.
The earlier preflight used the preliminary lower-curve start and export; it is
not final cooked evidence. Final source/export hashes are in adjacent provenance.

Missing-texture runs `20261003-095327-capture-initial` (884x1780) and
`20261003-095349-capture-actions` (390x844, simulated .9 inset, 200%) exited 0
with complete applicable native evidence. Initial fallback is RGB-identical to
the merged PR #33 packaged baseline; enlarged actions/focus were inspected.
The new owned texture was temporarily moved, then restored with its exact hash
in `reading-panel-fallback.json`. Its missing-package warnings are expected.
This is an editor omission test; it does not corrupt or qualify a packaged game.

Original-font/wordmark/companion identity, panel/surface finish and full UI01 art
acceptance remain open. Fixture editorial approval, manual/platform accessibility,
Android tooling/physical phone, offline isolation, performance, UI02 motion and
release gates remain. Native offscreen/synthetic proof is not physical-device evidence.
