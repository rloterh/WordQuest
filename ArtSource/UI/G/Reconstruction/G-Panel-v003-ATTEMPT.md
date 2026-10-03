# Rejected panel v003 attempt

Built-in imagegen edit, 2026-10-03; genuine transparent-output request. Inputs were
the preserved blank panel v002 and immutable original G gameplay PNG. The output
still showed colored/white perimeter fringe and insufficient star reduction, so it
was rejected before any Unreal import. Earlier masters are unchanged. No fallback
CLI, API key or raster paintover was used.

Generated file: `exec-d07214eb-0469-420f-809f-8a4a68482998.png`; SHA-256
`b6fd9120664f9ec1f3e4e30b626b195c45ff8ed1b4d5b7b3acdf9bbf7e3f4699`.
A non-runtime local inspection copy is retained at
`Artifacts/QA/UI01/PanelRimAttempt/G-Panel-v003-Rejected.png` (ignored raw evidence).
It is not a contributor dependency or accepted art.

## Exact prompt

```text
Use case: precise-object-edit.
Asset type: ONE blank RGBA reading-panel reconstruction candidate for Unreal UMG.
Image 1 is the edit target: the existing G blank panel candidate. Image 2 is the immutable original G gameplay reference, used ONLY as panel geometry/material authority.
Change only the panel rim, outer alpha cleanup, top contour and small purple star to match the original more closely. Preserve the warm white/lilac softly mottled interior, centered peaked arch, curved shoulders, long vertical sides and shallow curved lower edge. Keep the canvas/framing and proportions of image 1 (1068 by 1472), and keep its whole panel visible.
The rim must be thin, subtle pale champagne gold with a narrow ivory highlight and soft lavender inner shadow, like image 2. Reduce the overbright orange/yellow rim and large lower glow; no saturated orange, gold flare or sparkles. Clean all scattered colored/white specks outside the perimeter; genuinely zero-alpha gutters with smooth antialiased edges and only a restrained contiguous soft shadow immediately beside the rim.
Lower the current high shoulders slightly toward the reference contour. Make the inset purple four-point star about 30 percent narrower and shorter, at the same centered position, with subdued lilac/ivory facets instead of a large bright diamond.
The central panel MUST remain entirely blank: no title, text, letters, numerals, dividers, controls, companion, scenery, background or extra ornament. Do not copy the full gameplay screen into this asset. No opaque or checkerboard backdrop. Preserve genuine transparency. Do not modify either input file. Output one complete straight-on panel, not a sheet or collage.
```
