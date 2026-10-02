# G wordmark bevel candidate

The owner merged the focus integration #17 into `dev` at `f0fd74b` on
2026-10-02. This bounded UI01 increment addresses the wordmark's flat/pale material
relative to the immutable G reference's ivory edge and warm inset gold.

New editable master `ArtSource/UI/G/Vector/G-Wordmark-v002.svg` preserves the
v001 master, licensed Cormorant SemiBold glyph geometry, authored curls/Q swash,
430x140 canvas and native placement. Separate SVG layers add an ivory rim,
warm interior gradient, lower offset bevel and thin upper highlight. The revision
does not identify or accept original lettering. Font/letterform, capital proportions,
ornament shape and lighting still differ. Full UI01 fidelity remains unaccepted.

The builder defaults to v002; `--revision v001` retains the original reconstruction
path. The staging helper now pairs v002 with the existing runtime resource.
Exact source/runtime bytes use LF attributes. Provenance/pinned font hash and
license are recorded beside the SVG. No raster edit, image generation, new font,
binary asset, generated project file, learning fixture, scoring, motion or runtime
C++ change occurs. All instructional text and controls remain live widgets.

Preliminary dirty native captures `20261002-110041-capture-initial` (884x1780)
and `20261002-110059-capture-pausefocus` (260x640, simulated 0.9 inset) exit 0
and pass dimensions/unselected state. Both PNGs were inspected against the original
and v001 native baseline. Warm shading/rim are visible; narrow title remains separate
from focused Pause. Metadata records the dirty worktree and optional desktop
tooltip suppression. These are preliminary, not final packaged evidence.
Warm real editor build check passes (zero actions, exit 0), log
`Artifacts/Logs/Build/WordQuestEditor-20261002-110014.log`.

## Final clean verification

Implementation source: `ce2bba4a0357de4cd0d50585761e7445d1080ad9`, clean worktree.
Both real targets pass: editor warm check (zero actions, 1.19 seconds) and Game
build (five actions, 17.78 seconds). Full Win64 cook/stage/archive passes, UAT
76.97 seconds, exit 0, complete archive evidence:
`Artifacts/Packages/Win64/20261002-110437-143626`. Head/worktree/input invariants
and all 48 recorded payload checks pass. Manifest SHA-256:
`3aedf41f5e2eeff45ed2f4fea54a6c7706bffd407e7a26d6ee2cbdc78b4f546e`.

UnrealPak extraction exits 0; the extracted wordmark, runtime copy and v002 master
match SHA-256 `34eb2dc12e2c1be40db36f862924431ee5b26ce82fe5424ecec4098d6fd9b6b2`.
Exact extraction evidence is in the package's `WordmarkExtract.log` and
`WordmarkExtract.json`. Builder reproduction is byte-identical for v002.
The first raw-byte v001 reproduction check failed because its preserved checkout
has 32 CRLF endings while the builder emits LF. Its original bytes were restored
in a finally block. A read-only in-memory check confirms identical normalized
SVG text: preserved raw hash `080b8abab341089c9bc51dd693ea1ea5a33037d5b4abd8250d557e1e48072f41`,
generated LF hash `e397842f40e69c65cd16ef4bd44185adfc72f89bdc6b6c6765215416f05ffd9d`.
No raw-byte equality is claimed for v001. All seven staged SVG pairs pass. All six original-reference
hashes and all 27 existing Python tests pass. Git LFS is available; no new binary
asset is committed. XML checks confirm identical canvas/group transform and
glyph/ornament path geometry between v001/v002; material layers account for changes.

Each packaged run below verifies archive hashes, exits 0, passes requested state
and dimensions, and records clean source/package identity. All eight PNGs were
directly inspected; programmatic focus and desktop safe-zone simulation do not
establish physical/platform accessibility.

| Run under `Artifacts/QA/UI01` | Inspected result |
| --- | --- |
| `20261002-110711-packaged-capture-initial` | 884x1780; warm lettering and ivory rim, compared with original and v001 baseline. |
| `20261002-110721-packaged-capture-pausefocus` | 260x640, 0.9 inset; title separate from focused minimum-size Pause. |
| `20261002-110730-packaged-capture-large` | 390x844, 0.9 inset; brand retains decorative scale while 200% learning text wraps/scrolls. |
| `20261002-110740-packaged-capture-initial` | 844x390; title/Pause retained, compact hero and reading layout preserved. |
| `20261002-110749-packaged-capture-longselectedfocus` | 844x390, 200%; oversized selected B badge/marker/first line visible; leading-content gate passes. |
| `20261002-110759-packaged-capture-keydisabled` | 390x844, 0.9 inset; native key/state/focus/final Pause visibility contracts pass. |
| `20261002-110808-packaged-capture-correct` | 390x844, 0.9 inset; one correct evaluation, disabled controls and scrollable feedback start retained. |
| `20261002-110818-packaged-capture-hint` | 390x844, 0.9 inset; assisted correct state and Hint-used label retained. |

Comparison captures use optional `--no-tooltips`; `keydisabled` retains ordinary
tooltip behavior. Both existing Unreal context tests pass, zero failures/not run,
exit 0, in `20261002-110827-automation-initial/Report`.

Read-only RGB comparison with `20261002-092603-packaged-capture-initial` finds
16,480 changed pixels, all within the title region. Changed bounds, exclusive
right/bottom: x232..652/y29..157, inside existing x229..659/y23..163. Pixels outside
that region are unchanged. Evidence: `Artifacts/QA/UI01/G-Wordmark-Bevel-Comparison.json`.
This isolates the material change; it is not a similarity/acceptance score against
the original. The existing comparison helper creates
`Artifacts/QA/UI01/g-wordmark-bevel-comparison.html` with unchanged embedded images
and a 50% overlay. Browser/overlay interaction is unverified; earlier local-page
navigation blocks were not bypassed.

Initial dedicated review at clean `40a3801` against actual `origin/dev` (`f0fd74b`)
completed with exit 0 and no actionable findings; raw evidence is
`Artifacts/Reviews/20261002-111700`. That report preceded the corrected v001
line-ending reproduction wording above. Final dedicated read-only review at clean
`8faa3fcaf9d645494a23a7dd9b3d9f73fd1ace36` against actual `origin/dev`,
`f0fd74b24585e7f48688970c589f072cc72f9dec`, completed with exit 0 and no actionable
introduced defects. Head/worktree remained unchanged; raw evidence:
`Artifacts/Reviews/20261002-112020`. The reviewer checked SVG parity, references
and whitespace; it did not independently rerun Unreal builds or physical-device
acceptance. Subsequent records are documentation only; the packaged runtime and
builder bytes remain unchanged. Raw captures/builds remain local and
ignored under `Artifacts`.
[PR #18](https://github.com/rloterh/WordQuest/pull/18) is published as a regular
PR against `dev`; the owner merged it on 2026-10-02, 11:27:16 UTC, at
`c8c0dd382b94019c36fb66f2df788d5f7d817724`. GitHub has no configured
status checks; the local verification above supplies the recorded evidence.
Physical/manual input, screen-reader, art fidelity, editorial fixture review,
phone/offline, performance, UI02 motion and release gates remain open.
