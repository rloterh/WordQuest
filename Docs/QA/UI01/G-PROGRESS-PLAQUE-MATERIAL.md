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

## Clean Win64 package and native evidence

All runtime/source checks use clean `30e09f883260964727f2b556530a3c4c338275e5`.
First package `20261004-161941-356049` compiled the Editor (three actions, 5.57s)
and Game (five actions, 44.42s), cooked/staged/archived successfully (BuildCookRun
115.85s, zero cook errors/warnings), but the helper failed on a nonzero protected
firewall-task invocation. Its manifest remains incomplete, exit 1, with the original
error preserved. No failed receipt is treated as successful package evidence.
The same non-elevated refresh helper subsequently confirmed that executable's
exact coverage at 16:26:04.8610303 UTC, first attempt; no policy/task/ACL change.

Fresh final package `Artifacts/Packages/Win64/20261004-162743-349975` passes all
helper stages, exit 0. Both already-compiled targets pass with zero actions (Editor
1.56s, Game 1.62s); full cook processes 519 packages, zero errors/warnings;
stage/archive and BuildCookRun complete in 61.13s. All 49 payload sizes/hashes,
clean source identity and unchanged head/worktree/input checks pass. Manifest SHA-256:
`c7e3efa75e345a402bac4c2aa2d818d848e4c4542c3ec77f84684b44789f66e4`.
Automatic exact executable coverage succeeds on the first attempt at
16:28:59.9406125 UTC, Private/Public LocalSubnet, without a new owner prompt.

All ten final packaged runs below exit 0 and record clean matching source/package
identity, verified archive hashes and complete requested state/dimension/cue
checks. Every native PNG was viewed. The 1768x3560 PNG was displayed by the viewer
at 1017x2048; raw dimensions are independently recorded. Paths are under
`Artifacts/QA/UI01`; .9 is a simulated desktop safe zone, not physical-phone proof.

| Run | Proof | Window / text / safe zone |
| --- | --- | --- |
| `20261004-162904-packaged-capture-initial` | Reference-sized initial | 884x1780 / 100% / 1 |
| `20261004-162917-packaged-capture-initial` | High-resolution initial | 1768x3560 / 100% / 1 |
| `20261004-162928-packaged-capture-initial` | Phone-sized composition | 390x844 / 100% / .9 |
| `20261004-162939-packaged-capture-initial` | Enlarged reading, scrolling | 390x844 / 200% / .9 |
| `20261004-162949-packaged-capture-initial` | Narrow initial, scrollable actions | 260x640 / 100% / .9 |
| `20261004-162959-packaged-capture-initial` | Compact landscape, plaque/progress hidden | 844x390 / 100% / .9 |
| `20261004-163009-packaged-capture-selected` | Selected C with separate cues | 884x1780 / 100% / 1 |
| `20261004-163020-packaged-capture-correct` | Disabled options and feedback | 884x1780 / 100% / 1 |
| `20261004-163031-packaged-capture-longselectedfocus` | Long selected B, leading content visible | 260x640 / intrinsic 200% / .9 |
| `20261004-163042-packaged-capture-keymodal` | Synthetic Pause/text-size routing | 390x844 / ends 200% / .9 |

Both genuine Unreal `WordQuest.Context` tests pass, zero failed/not-run/in-process,
exit 0, clean source, in `20261004-163507-automation-initial/Report`.
All nine cooked SVGs extracted with UnrealPak's documented separate `-Extract`
directory arguments match the staged sources byte-for-byte; pak hash unchanged.
The original reference/baseline/new runtime comparisons remain scoped to the
plaque: 8,800 changed pixels, identical bounds and sample means above. The packaged
PNG SHA-256 is
`bc46bd8226877fdc0ca805a764440be0b9dfed603ed846956b76933ff7260fcc`.
It differs from Editor preflight by 298 RGB pixels within [362,190,523,198), at
most one channel level; no exact Editor/package PNG equivalence is claimed.
The initial QA assertion expecting identical PNG hashes is retained as failed
diagnostic evidence; the corrected comparison explicitly records this small
bounded difference rather than ignoring it. The final package comparison crops
and overlay were generated and viewed, alongside the inspected native images and
earlier overlay. Exact contours, gold/inner bevel and type metrics remain candidate.

Raw source/fallback/package/batch/cooked/comparison evidence is retained under
`Artifacts/QA/UI01/PlaqueMaterial20261004`. Subsequent evidence/review/publication
documentation does not change the tested runtime/source/art revision.

## Dedicated review

Dedicated read-only review completed at `Artifacts/Reviews/20261004-163750`,
actual `origin/dev` base `d7311aeb53d9b87407ec4635577364729af739b9`, reviewed head
`929806be5f82b91dc55431e7709eacab06477a0c`. Starting worktree was clean, exit 0,
head/worktree unchanged. No actionable introduced defects were found. SVG parity,
original-reference integrity and whitespace checks passed independently. Unreal
builds, runtime captures and device gates were not independently rerun. Subsequent
review/publication records change documentation only; the tested runtime/source/art
remains `30e09f8`. The owner retains merge authority.
The owner merged non-draft [PR #41](https://github.com/rloterh/WordQuest/pull/41)
into `dev` on 2026-10-04 at 16:59:11 UTC (`a248b2c`). Publication added documentation
only after the reviewed head.

## Open gates

This is a reconstruction candidate. Exact contour, bevel, texture softness and
progress typography, full UI01 static fidelity, UI02 motion, fixture editorial
approval, manual/platform accessibility, Android/physical-phone, isolated offline,
performance and original release gates remain open. Desktop safe-zone simulations
are not phone evidence. No deployment/release or owner merge is performed here.
