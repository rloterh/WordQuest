# UI00 reconciliation and asset inventory

2026-09-22. Original G, H and I gameplay PNGs were visually inspected, not inferred
from filenames. All six original SHA-256 hashes match the supplied manifest.
Run `python Tools/AssetImport/verify_references.py` for hash/dimension checks.
Home references remain draft proposals; no home design acceptance is implied.

## Precedence

G's lavender cloud palace, curved pearl panel, navy sans reading text, pale gold
ornament and flowing white lantern spirit supersede the earlier amber/jade/Pip
direction. H retains its dark moonlit wisteria panel and round violet spirit. I
retains its celestial bookshelves, sculpted gold frame, plum serif text and capped
winged lantern spirit. Their learning, scoring and semantic controls must be shared.
Realm does not select narrative progress or change an answer key.

## Initial G anchor survey

Reference canvas: 884 x 1780. These pixel bounds are visual estimates from the
original, to refine against the first native capture; they are not a passed match.
Normalized positions are obtained by dividing x by 884 and y by 1780.

| Region | Approximate bounds x, y, width, height | Constraint |
| --- | --- | --- |
| WordQuest mark | 222, 25, 440, 135 | Preserve silhouette; clean typography still needed |
| Pause | 787, 31, 71, 75 | Real labelled control |
| Progress plaque | 352, 168, 178, 61 | Live `3 / 7`, fixture progress only |
| Spirit including lantern | 82, 276, 207, 185 | One separate sprite; no baked duplicate |
| Reading panel | 65, 521, 758, 1097 | Pointed curved top and gold/pearl bevel |
| Mode label | 252, 611, 385, 34 | Letter-spaced navy sans |
| Target word | 216, 691, 442, 65 | Live EQUIVOCAL |
| Clue | 169, 796, 548, 74 | Reference two-line wording |
| Prompt | 186, 926, 515, 35 | Live semantic heading |
| Answers | 109, 990, 666, 431 | Four 95px-high controls, approximately 17px gaps |
| Hint | 99, 1454, 287, 113 | Live assistive action |
| Check answer | 399, 1454, 388, 113 | No selected answer at frozen t=0 |

Reading/interaction mask covers panel interior. Ambient motion must stay in the
upper scene and ornamental edges. At larger text scales the reading area must grow
or scroll; do not merely shrink all text to preserve this reference geometry.

## Layers and remaining production tasks

| Layer | Current state | Next requirement |
| --- | --- | --- |
| G environment clean plate | Generated v001, 884x1779 RGB; visually inspected working candidate | Restore exact 884x1780 canvas, compare retained architecture; lower revealed area is invented reconstruction |
| G spirit + lantern | v001 RGBA candidate; facial/lantern details differ | Faithful traced/masked cutout from original, edge cleanup and identity comparison |
| G panel | v001 rejected for baked checkerboard; v002 alpha repair candidate | Check edge halos, original geometry and nine-slice export |
| Cloud | Not extracted | Isolate a local cloud bank, clean its underlying original and provide overscan; no duplicate ghost bank |
| Lantern emission | Not produced | Local alpha/emission mask, no light spill over reading controls |
| Foreground | Still in background candidate | Separate where scene overlap/resize requires it |
| Answer/hint/check skins | Not produced | Blank scalable surfaces and separate selected/focus/disabled states |
| Logo, progress frame, divider, icons | Not produced | Clean editable ornaments; real control labels |
| H / I layers | Original references only | Produce after G proves shared approach |

All generated outputs are candidates, not approved replacements. No texture has
been imported into Unreal and no animated or layered source document is claimed.
Keep the original reference package unchanged. See `ArtSource/G-ASSET-HANDOFF.md`.

## Font identification and licensing work

- G reading: compare a humanist sans candidate against EQUIVOCAL, clue line lengths
  and the shape of the lowercase `a`; generated image does not establish a font name.
- Brand and action labels: compare serif metrics, swashes and italic-like terminals;
  do not call a generic serif an exact match.
- H/I: maintain distinct serif reading character through the same semantic font roles.
- Identify an exact font or record the measured substitution with captures. Before
  importing, retain its redistribution license and provenance in `ArtSource/Licenses`.
- Check punctuation, bold, 200% text scaling and glyph fallback. No font was downloaded
  or licensed in this inventory. Engine defaults would be provisional, not fidelity proof.

## Dependency-aware board

| Task | State / dependency | Exit evidence |
| --- | --- | --- |
| P00/UI00 inventory | Recorded with missing resources | Version output, hash checks, capability/precedence reports |
| Generated C++ foundation | Generated; editor compile blocked by missing NetFxSDK | Successful `python Tools/BuildScripts/build_wordquest.py` and actual editor launch |
| Fixture review | Owner response pending | Prototype approval recorded; separate release review later |
| UI01 static G | Incomplete; build, font and art gaps | Live controls, frozen 884x1780 capture, overlay, long text/safe-area tests |
| UI02 G motion | Waiting on UI01 | Cloud/glow masks, motion policy, frozen t=0, 60-second native recording |
| Android packaging | Engine Android binaries absent; SDK/JDK compatibility unresolved | Real packaged APK plus offline startup |
| Physical-device acceptance | No adb device; models/OS unknown | Named phone captures, interaction and frame-time/memory measurements |
| H/I expansion | Deferred | G static/motion approach proven first |

No P01 mobile feasibility, UI01, UI02 or production foundation gate is passed by
these documents or generated artwork.
