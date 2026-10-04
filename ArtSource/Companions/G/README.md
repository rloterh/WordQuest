# G companion working art

The supplied original gameplay PNG remains the identity authority. Previous
generated `Reconstruction/G-Spirit-v001-Candidate.png` and genuinely imported
`G_Spirit` are preserved as the current missing-candidate fallback.

The new static source-mask candidate uses the original 228x205 RGB crop from
[72,266,300,471), with no resizing or character repaint. Working input:
`SourcePixels/G-Spirit-Reference-Detail-v001.png`; editable alpha:
`Masks/G-Spirit-Reference-v001.svg`; runtime export:
`Exports/G-Spirit-Reference-v001.png`. Source/mask/export/Unreal hashes and import
settings are in `Masks/G-Spirit-Reference-v001-PROVENANCE.json`.
Reproduce with `python Tools/AssetImport/render_g_reference_spirit.py --check`.
The existing pinned development-only resvg renderer is sufficient; normal builds
use the imported texture and do not run this tool. Genuine Unreal Python import
uses `Tools/AssetImport/import_g_reference_spirit.py` and creates `G_SpiritReference`.

This retains source RGB identity, not recovered original foreground alpha.
Translucent wisps may contain scene color; hand-traced edge decisions and the
unchanged small source resolution still need art review. The three mask paths
are not independent animation layers: overlapping body pixels include the lantern.
Hidden body/background reconstruction is required before independent lantern motion.
Do not move these masks independently or add duplicate companion art.

The owner authorized this alternative after another unsuitable built-in imagegen
retry. Exact retry prompt and corrected original-detail assessment are recorded in
`Reconstruction/G-Spirit-Retry-20261004-PROMPTS.md`; no generated retry output is
imported or adopted as the new visual target. Native evidence and remaining gates:
`Docs/QA/UI01/G-SPIRIT-SOURCE-MASK.md`. UI01/UI02 and device acceptance remain open.
