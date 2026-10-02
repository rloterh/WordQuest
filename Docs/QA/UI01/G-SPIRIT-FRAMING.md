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

Native comparison, final clean build/package evidence and review are pending.

## Remaining gates

The existing face, eyes, circlet, lantern proportions and fine wisps still differ
from the original. Framing does not pass identity, alpha-edge or UI01 acceptance.
Material/lettering fidelity, fixture review, manual input/screen reader, offline
isolation, mobile tools/phone, frame-time/memory, UI02 motion and release remain
open. Cold D3D12 pipeline delay remains unresolved; renderer settings are unchanged.
