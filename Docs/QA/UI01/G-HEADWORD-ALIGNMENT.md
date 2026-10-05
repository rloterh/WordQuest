# G live headword alignment

PR #45 is owner-merged at `b0d3b24` (2026-10-05, 02:00:45 UTC). This bounded UI01
correction refines only the live word role using the existing genuine licensed
Liberation Sans reading composite. No font file, imported asset, license, fixture,
art or learning/control handler changes. It does not identify the font originally
used in a generated reference image or accept exact letterforms/antialiasing.

With the reading composite available, reference word pixels move from 76 to 77,
the measured/drawn font uses letter spacing -5, horizontal slot offset moves from
107 to 110 reference units and vertical offset is raised by 1.5 units. Measurement
uses the same font information as drawing. Existing readability floor, point-size
rounding, actual 200% enlargement, per-character overflow wrapping, minimum
95-unit block height, measured expansion and downstream flow remain. Missing
either reading FontFace retains the previous 76-pixel/default-family/zero-spacing/
107-offset/unraised fallback. Other text roles use zero spacing as before.

## Preliminary evidence

Fixed-region navy glyph bounds (R<65, G<60, B<125, word region [150,680,730,780))
measure the original at 450x71, center (446,731.5), versus prior packaged native
445x69, center (443.5,731.5). These are diagnostic extents, not font identity or
whole-screen acceptance. Existing clue/prompt/answer/mode differences remain.

The first real Editor build passes in 66.99s
(`Artifacts/Logs/Build/WordQuestEditor-20261005-021830.log`). Initial dirty preflight
`20261005-022052-capture-initial` passes and its full screen and original/baseline/
candidate word crops were inspected. It reaches 450x70 and horizontal center 446,
but vertical center 733 is lower than the target; the 1.5-unit raise addresses this
before final verification. Only word-region pixels change, apart from the known
964 Pause/plaque Editor/package pixels at maximum channel delta one. Diagnostics
and raw comparison are under `Artifacts/QA/UI01/WordType20261005/` and are not
product art.

The final real Editor build passes in 44.49s
(`Artifacts/Logs/Build/WordQuestEditor-20261005-022516.log`). Aligned preflight
`20261005-022601-capture-initial` passes: word bounds [221,697,671,767), 450x70,
center (446,732). The remaining half-pixel vertical-center difference and one-pixel
height difference are disclosed. Other measured text roles remain unchanged.
Only 5,657 word-region pixels change, plus the same 964 one-level Pause/plaque
Editor/package variations. Final full screen and word crop were inspected.

With the Bold reading asset temporarily omitted, native fallback captures
`20261005-022822-capture-initial` and `20261005-022846-capture-large` both pass
(884x1780 default; 390x844 safe-zone 0.9 at actual 200%). Both PNGs were inspected;
the enlarged screen intentionally scrolls. The asset is restored byte-for-byte
at SHA-256 `ddb17ec624e8c6e8d68b607cbbd14e5302111b07e158074cc101e69de0a78715`.
Against historical fallback `20261003-113737-capture-initial`, glyph bounds remain
[243,694,643,755). A strict threshold-mask equality diagnostic failed: 30 edge
pixels cross the navy threshold, with maximum channel difference three at those
pixels. This is not a pixel-identical fallback claim; historical background/art
changes also differ. Native logs confirm default Roboto loading and word size 57,
while the source preserves the previous fallback parameters. Clean archive,
matrix and dedicated review are pending.

Full static type/art/material fidelity, UI02 motion, manual/platform accessibility,
draft fixture editorial approval, Android/phone, isolated offline, performance and
original release gates remain open. No H/I/later milestone, deployment, release
or implementation-agent merge is performed.
