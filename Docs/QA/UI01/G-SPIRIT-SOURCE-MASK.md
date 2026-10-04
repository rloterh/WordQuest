# Static G companion from original pixels

PR #39 is merged at `51b6241`. The owner explicitly requested a retry and permitted
a better alternative if built-in imagegen was unsuitable. No permission/approval
block prevented generation. The exact-pixel diagnostic crop (72,266)-(300,471)
made the small reference character clearer without replacing the immutable original.

## Retry and corrected assessment

Built-in imagegen background-removal edit used only that inspected 228x205 crop.
It still redrew character details/proportions and left stray alpha pixels; it is
discarded, not imported or adopted as the target. Exact prompt/output provenance
is in `ArtSource/Companions/G/Reconstruction/G-Spirit-Retry-20261004-PROMPTS.md`.
Close-up inspection also shows that the original already contains substantial gold
banding and a tiny pink mouth detail. Earlier "thin circlet/no tongue" constraints
were too restrictive; those features alone are not introduced defects. The original
character, not an idealized description or previous generated output, is authoritative.

## Source-based static alternative

The owner's alternative authorization is used for a deterministic original-pixel
cutout, with a hand-traced editable SVG mask and pinned resvg renderer. No character
RGB paintover, generative reconstruction or resolution enhancement occurs in this
selected candidate. `SourcePixels/G-Spirit-Reference-Detail-v001.png` is a new working
crop under `ArtSource/Companions/G`, pixel-identical to the original region; the supplied
reference is unchanged. The three named mask paths are editable static alpha shapes
(body, top wisp, lantern), with a .35-source-pixel Gaussian edge feather.
They are not three separately reconstructed animation layers: the body region still
contains visible lantern pixels and hidden body art has not been painted. Do not
animate those masks independently or add a second companion over this one.

The 228x205 RGBA export has zero corner alpha, extrema 0..255 and nonzero-alpha
bounding box [9,12,200,200). All 10,821 fully opaque pixels are exactly equal in RGB
to their original x+72/y+266 pixels. This establishes retained source integrity, not
exact alpha recovery or full visual acceptance. Source wisps already contain baked
scene color/translucency; a traced mask cannot recover unknown foreground/background
components. Light/dark QA composites were inspected. Tight contour choices, fringe,
source softness and high-resolution quality still require art review. The source
resolution is unchanged; no new high-resolution detail or layered master is claimed.

Reproduce with `python Tools/AssetImport/render_g_reference_spirit.py --check` using
development-only resvg-py 0.5.0 / resvg 0.48.1 already used by the panel renderer.
Exact source/mask/export/import hashes and limits are recorded in adjacent provenance.
The genuine Unreal Python texture import sets sRGB, UI group, editor-icon compression,
bilinear filtering, no mips and never-stream. New texture: `/Game/UI/G/G_SpiritReference`.
The previous `G_Spirit` and its v001 source remain unchanged; original reference hashes
and all eight raw SVG resources are preserved. Binary art has one writer and LFS.

Native placement draws the full export at x72/y266, 228x205 reference units, including
transparent crop margins; this preserves source coordinate mapping and aspect ratio.
Missing candidate retains the previous framed texture and its exact containment path.
Compact hero/landscape hiding, responsive scale, live controls, scoring and draft
fixtures remain unchanged. This is a single static companion, not UI02 motion.

## Verification in progress

Genuine import exits 0 with zero errors/warnings and completion marker:
`Artifacts/Logs/UI01/reference-spirit-import.log` and adjacent JSON.
Editor compilation succeeds in six actions, 31.15 seconds;
`Artifacts/Logs/Build/WordQuestEditor-20261004-140241.log`.
All 67 Python QA checks, eight staged SVG pairs, six immutable reference hashes and
byte-exact PNG reproduction pass. Read-only source integrity and mask diagnostic
evidence are under `Artifacts/QA/UI01/SpiritRetry20261004`.
Dirty native preflight `20261004-140649-capture-initial` exits 0 at 884x1780,
initial state and option cues pass. The PNG and close-up were inspected against
the immutable original and PR #39's packaged baseline. Its 10,821 fully opaque
mask-corresponding pixels match the original RGB exactly at native coordinates;
mean absolute channel difference is 0.00 versus 42.30 for the earlier generated
companion at those same points. This is an interior correspondence check selected
by the mask, not a global fidelity/edge/alpha score. Comparison changes 20,250 pixels,
bounds [81,277,284,466), zero outside the crop region [72,266,300,471).
The prior larger generated face/lantern is removed; no second companion is added.
Final initial preflight PNG SHA-256:
`367a687da0de98c66ac9d745490d6b82afa80423555ebd553441d45effcacace`.
Raw comparison and reference/baseline/final crops:
`Artifacts/QA/UI01/SpiritRetry20261004/preflight-comparison.json`.
Omission fallback exits 0 with complete native checks in
`20261004-141220-capture-initial` (884x1780) and
`20261004-141239-capture-initial` (390x844, .9 simulated safe area, 200% text).
Both PNGs were inspected: the previous framed companion returns, enlarged reading
reflows/scrolls with live controls. The reference-sized fallback RGB is identical
over the entire screen to PR #39's initial baseline. The new owned texture was
temporarily moved into ignored QA storage and restored in `finally` with exact
SHA-256; source/old texture remained untouched. Raw metadata:
`Artifacts/QA/UI01/SpiritRetry20261004/fallback.json`.
Clean Win64 packaging and dedicated review are pending.

## Open gates

Static mask edge/matte acceptance, full UI01 art fidelity, high-resolution editable
companion source, independently reconstructed motion layers/UI02, fixture editorial
approval, manual/platform accessibility, Android/physical phone, isolated offline,
performance and original release gates remain open. Original-pixel retention is not
a phone or release qualification.
