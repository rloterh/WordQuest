# G progress-plaque vector material — acceptance pending

The owner merged PR #40 into `dev` (`d7311ae`) on 2026-10-04 at 16:07:31 UTC.
This bounded static correction replaces the generated progress decoration with
an editable, blank SVG. The earlier purple rim was brighter, the fill darker and
the shoulders more angular than the immutable G gameplay reference. The new
candidate reconstructs softer purple shading, thin pale-gold bevel and curved
shoulders in the existing 178x61 reference slot at (352,169).

## Source and integration

`ArtSource/UI/G/Vector/G-Progress-Plaque-v001.svg` is hand-authored paths and
gradients, staged byte-for-byte as `Game/Content/UI/G/Vector/G_ProgressPlaque.svg`.
Unreal rasterizes it through the existing native `FSlateVectorImageBrush` path.
There is no imagegen/raster paintover, original-pixel extraction or new binary
Unreal asset. No reference, prior generated plaque master or texture is changed.
The existing staging helper checks nine source/runtime pairs before packaging.

The plaque is decorative, hit-test invisible and excluded from accessibility.
The separate native label remains live `3 / 7`, describing a draft fixture rather
than persisted campaign progress. Its font, centering, shadow, text and semantic
label are unchanged. Compact landscape still collapses plaque and progress.
Missing SVG uses the exact prior texture/UV framing; missing both decorations
still leaves the live progress label. Answer handling, scoring, focus, scrolling,
responsive adaptation and the companion are unchanged.

## Native preflight and fallback

The six-action real Editor build passes, exit 0, 52.15 seconds; all 67 existing
Python QA tests pass. Nine SVG pairs and six immutable references pass.
Build log: `Artifacts/Logs/Build/WordQuestEditor-20261004-161044.log`.
The first dirty native capture (`20261004-161221-capture-initial`) exposed an
unsupported reusable SVG shape (`use`): only the independent highlight appeared.
That candidate is rejected. Explicit paths replace reuse, matching the installed
engine's `SlateSVGRasterizer.cpp`/NanoSVG path. No permission change was needed.

Corrected dirty native `20261004-161454-capture-initial`, 884x1780, exits 0 with
complete state/dimension/cue evidence. Its PNG was inspected alongside the original
and baseline; 50% overlay and diagnostic close-ups were viewed. 8,800 pixels differ
from the prior screen, within [352,169,530,230) only; zero changes occur outside the
bounded plaque comparison region [350,167,532,232). The live label is retained.
Eight fixed opaque face samples at (400,184), (440,181), (487,184), (385,199),
(390,210), (441,219), (497,217), (505,199) have mean absolute channel error versus
the original of 17.04 before and 5.29 after. This is scoped face-color evidence;
it excludes text and uncertain edges and does not establish global fidelity.
Corrected preflight PNG SHA-256:
`1ede7f67bd7409d3f7a9c715f7dfe3d7315f5c69399c3ab9fb6c514326eba1cd`.

Missing-SVG native runs `20261004-161701-capture-initial` (884x1780) and
`20261004-161721-capture-initial` (390x844, .9 simulated safe zone, explicit 200%
text) exit 0, with complete applicable state/cue/large-text/action checks. Both
PNGs were viewed. The reference-sized fallback screen matches the entire prior
screen's RGB exactly, PNG SHA-256
`367a687da0de98c66ac9d745490d6b82afa80423555ebd553441d45effcacace`.
The new runtime SVG was restored byte-for-byte, SHA-256
`4b1f8e673307e376056742827f27eebc60bdb5573951d56ad9207b814db655e3`.
Prior generated source/texture hashes remain unchanged (see source provenance).

Clean Win64 build/cook/archive, packaged captures, genuine Unreal tests and
dedicated review remain in progress. Raw source/fallback/comparison evidence is
retained under `Artifacts/QA/UI01/PlaqueMaterial20261004`.

## Open gates

This is a reconstruction candidate. Exact contour, bevel, texture softness and
progress typography, full UI01 static fidelity, UI02 motion, fixture editorial
approval, manual/platform accessibility, Android/physical-phone, isolated offline,
performance and original release gates remain open. Desktop safe-zone simulations
are not phone evidence. No deployment/release or owner merge is performed here.
