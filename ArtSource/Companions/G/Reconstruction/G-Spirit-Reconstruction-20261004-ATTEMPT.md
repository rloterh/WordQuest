# Rejected G spirit extraction candidate

Built-in `image_gen.imagegen`, transparent background requested, 2026-10-04.
Mode: edit / background-extraction. Input was the inspected immutable original
G gameplay PNG; no CLI/API fallback, raster paintover or runtime import occurred.

## Exact prompt

Use case: background-extraction.
Asset type: separate static transparent companion texture for the existing WordQuest G Celestial Reverie gameplay proof.
Input image 1: immutable original gameplay screenshot, the sole identity and composition authority. Its small white/lavender spirit is in the upper-left at x82–289, y276–461 in the 884x1780 image. Do not edit or reproduce the whole screenshot.
Primary request: isolate precisely this existing spirit with its lantern as a faithful clean RGBA cutout, with a small transparent margin and all wisps and lantern tip included. Keep its existing pose, tilted face, silhouette and relative proportions. The subject flows leftwards while facing slightly right; its main face sits in the right half. Reproduce the reference, rather than designing a new mascot.
Identity constraints: smooth rounded white face with two dark violet oval eyes, restrained highlights, tiny simple smile, no visible tongue. Thin simple curved gold circlet hugging the forehead with a tiny gold pointed crest beneath the top wisp; it is not a broad metal helmet, spherical jewel or four-point star. Exactly the reference's translucent white and lavender flowing ribbons, soft painterly shading, no added glitter or eye-stars. Preserve the fine curling wisp at the far left and top wisp shape.
Lantern: existing gold lantern hanging below-left of the face; in the reference its outer width is approximately 48px and height 82px versus the face approximately 90px wide. Preserve this relative scale, small pointed roof, slim straight frame, warm pale panes and tiny lower finial. No enlarged lantern or fancy arched panes.
Output: one complete isolated companion/lantern, genuine transparent background and clean soft antialiased alpha. No architecture, clouds, UI, lettering, panel, scene, painted checkerboard, extra props, stars, new limbs or new ornaments. Keep the original supplied file unchanged; this is a separate candidate for inspection, not an accepted visual target.

## Inspection and disposition

The result still has a broad metal headband, altered face/eye details and a
visible tongue despite the prompt's restrictions. Fine edge residue and scattered
alpha pixels remain. It is rejected: it does not establish original character
identity or alpha-edge acceptance. Do not promote it to an asset or visual target.
The existing v001 source and `G_Spirit.uasset` remain unchanged.

Generated source:
`C:/Users/HP/.codex/generated_images/01a0c93a-4fed-71e2-8bb4-3faa449a0984/exec-546bb52f-549d-4165-807c-794793a260a1.png`.
Ignored local copy:
`Artifacts/QA/UI01/BadgeMaterial/G-Spirit-Rejected-20261004.png`.
SHA-256 `962f5349c3fa659c512071d87a60cff33dfcf247ff8b926237932f81de854000`.
Read-only Pillow 12.1.0 inspection: 1471x1069 RGBA, alpha extrema 0..255,
nonzero-alpha bounding box [0, 8, 1376, 1056), zero corner alpha.
Neither generated output is committed. No new layered art source is claimed.

This is the third rejected reconstruction after the two recorded on 2026-10-02.
Further full regeneration is deferred until a more reliable art handoff can
preserve the reference's actual identity; UI01 and UI02 acceptance remain open.

## Concrete art handoff

Reconstruct the original upper-left spirit in its x82/y276, 207x185 region;
the original gameplay PNG above remains the sole identity authority, with no
new character design. Match the face/eye spacing and tiny smile, thin circlet,
small gold lantern and left-flowing wisp contours at native reference size.
Do not treat any generated candidate as the identity reference.

Deliver a genuine editable layered art file under `ArtSource/Companions/G`
(body/wisps, circlet and lantern separately editable), plus a versioned RGBA
export retaining the full pose and transparent margins. Supply export dimensions,
content bounds and source/export hashes; never overwrite v001. Inspect edges on
light/dark backdrops and the G scene, with no checkerboard, opaque fringe or
unrelated specks. No educational text or scene background belongs in the cutout.

After identity/edge inspection, use genuine Unreal import for a new owned texture,
retain the current texture fallback, contain rather than stretch its aspect in
the reference region, and capture a frozen 884x1780 native comparison plus overlay.
Review exact face/circlet/lantern/wisp differences before accepting the static art.
Layer delivery supports later motion but does not pass UI02 or physical-device gates.
