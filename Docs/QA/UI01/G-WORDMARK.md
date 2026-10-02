# G vector wordmark candidate — acceptance pending

Following the owner's PR #9 merge (`c3eece4`, 2026-10-02), this bounded UI01
increment adds a separate editable brand candidate. It replaces the plain visible
Cormorant title with outlined lettering, capital curls, pale-gold shading, a
separate Q swash and the under-title star/flourish. It is not accepted original
lettering or a visual-gate pass.

## Source and runtime behavior

The 430x140 editable master is `ArtSource/UI/G/Vector/G-Wordmark-v001.svg`;
`stage_g_action_icons.py` copies it exactly to
`Game/Content/UI/G/Vector/G_Wordmark.svg`. The existing raw-resource UFS staging
directory includes it. The previous five SVGs, supplied references, raster
masters, learning fixture and scoring are unchanged. No new binary asset or
fabricated Unreal asset is introduced.

`build_g_wordmark.py` outlines the repository's unmodified OFL Cormorant Garamond
SemiBold font and adds authored closed curves. Font provenance/redistribution
license remain adjacent to the original TTF; this is a derivative graphic, not
a new font or identification of the reference typeface. The vector README records
the optional pinned fontTools 4.61.1 reproduction command. Builds use the committed
SVG and do not require fontTools. No image generation/raster editing was used.

Native `FSlateVectorImageBrush` renders the mark at reference coordinates
x229/y23, 430x140, proportional to the existing composition width. It follows
the existing centered responsive hero in portrait/landscape and scrolls with the
screen; learning/control text retains its live 200% sizing path. The mark has a
custom `WordQuest` accessibility name and no pointer hit target. The original
live `Brand` text object is collapsed only when the SVG exists, preserving its
fallback when absent. No screen-reader service pass is claimed.

## Verification

The initial dirty editor capture `20261002-021319-capture-initial` exposed flat
amber shading from unit-valued gradient coordinates. That version is rejected
as final visual evidence; coordinates were changed to explicit SVG percentages.
Build, final native/package checks and review are pending.

## Remaining gates

Letter contours, W curls, Q connection/taper, precise bevel/light and spacing
still differ from the original; owner art acceptance is open. Existing spirit
identity, panel/surface finish and exact typography remain candidates. The fixture
remains editorially unapproved. No UI02 motion, H/I expansion, phone, offline
isolation, Shipping/release or performance qualification is established here.
