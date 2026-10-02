# G wordmark capital W candidate

The owner merged [PR #26](https://github.com/rloterh/WordQuest/pull/26) into `dev`
at `e2ef2b0` on 2026-10-02, 20:00:20 UTC. This bounded UI01 increment addresses
the documented capital-letter mismatch against the immutable G gameplay reference.
The prior W has short, narrow lower tips and different curled terminals. New v003
uses authored closed vector curves for splayed stems, deeper tips and curled ends.
It is a reconstruction candidate, not accepted original lettering.

## Ownership and reproduction

New master: `ArtSource/UI/G/Vector/G-Wordmark-v003.svg`; runtime resource:
`Game/Content/UI/G/Vector/G_Wordmark.svg`. Both have SHA-256
`d14ff694d50670c980d064ece5f2cbd561bf2fc72c00813eecd5606b7168efa4`.
LF attributes preserve exact staged bytes. Adjacent v003 provenance records the
reference/font hashes and remaining limitations. Both earlier masters remain
unchanged. The builder now defaults to v003; explicit v001/v002 remain supported.

The other eight Cormorant SemiBold glyph outlines and their advances/transform,
Q swash, under-title ornament, gradient definitions, canvas and native placement
are preserved. The W is a derivative graphic, not a modified font or identification
of the generated reference typeface. The repository font and adjacent OFL license
remain unchanged. No raster editing, image generation, new font, binary asset,
generated project file, runtime C++, learning fixture or scoring change occurs.
All learning/control text remains live, and the existing semantic title/fallback
behavior remains in place. No new screen-reader service pass is claimed.

`python Tools/AssetImport/build_g_wordmark.py --revision v003` uses the existing
optional fontTools 4.61.1 development dependency. Builds render the committed SVG
without that dependency. Reproduction is byte-identical for v002/v003; preserved
v001 reproduces after CRLF/LF normalization. Every original master byte was restored
after that check. Raw integrity metadata:
`Artifacts/QA/UI01/wordmark-capital-integrity.json`. Read-only XML checks verify
the remaining lettering is the exact suffix of the old path, the transform is
unchanged, and Q/ornament attributes and gradient definitions match.

## Clean build and package

Implementation: `db9446dfda2f76f5df058cb9bf7db2a108fbe159`, clean worktree.
Real Editor/Game target checks pass with zero actions because C++ is unchanged.
Editor package preparation: 2.59 seconds,
`Artifacts/Logs/Build/WordQuestEditor-20261002-201516.log`.
Game check: 1.41 seconds, recorded in the package's `UAT.log`.
Full Win64 Development cook/stage/archive passes, UAT exit 0, BuildCookRun
58.47 seconds. Package:
`Artifacts/Packages/Win64/20261002-201516-619491`.
Manifest SHA-256:
`cda2afeadf05e82e0a1b823bca8233e2e0b4d63c0e0535fb583ea6b04711e36d`.
All 48 payload hashes are recorded and verified before every native launch.
Head/worktree/input invariants pass. Outputs remain local and ignored.

UnrealPak extraction passes with exit 0; cooked/runtime/master SVG bytes match.
`WordmarkExtract.json` records the exact command/hash and confirms the pak hash
remains unchanged. The first invocation used `-Extract=<directory>`, which this
installed tool did not recognize as extraction. It rejected creation because the
pak already existed; the corrected `-Extract <directory>` invocation passed.
The rejected log is retained as `WordmarkExtract-Rejected.log`, excluded from final
extraction evidence. The pak hash was checked before and after the successful run.

Dirty editor preflights `20261002-200705-capture-initial` (884x1780) and
`20261002-200839-capture-pausefocus` (260x640, simulated .9 safe area) passed and
were inspected. They are preliminary, separate from the clean package below.
The preceding warm editor check passed in 1.54 seconds, zero actions,
`WordQuestEditor-20261002-200612.log`.

## Native checks

All nine final packaged captures pass native/helper exit, dimensions and applicable
state/cue/focus/reflow contracts. Every PNG was directly inspected, including the
reference-size original beside the new title. Native logs contain no Error/Fatal
lines. Batch/reproduction: `Artifacts/QA/UI01/wordmark-capital-batch.json` and `.py`.
Run prefixes below are 20261002.

| Run | Proof / dimensions | Observed result |
|---|---|---|
| 201710 | initial, 884x1780 | Revised W, unchanged reading layout and empty cues |
| 201722 | correct, same | Revised title independent of readable disabled answers/check and explanation |
| 201732 | pausefocus, 260x640 | Compact title remains readable and separate from focused Pause |
| 201741 | initial, 844x390 | Compact landscape title/Pause retained; reading scrolls |
| 201751 | large, 390x844 | Decorative title retains scale; live 200% reading reflows |
| 201801 | keydisabled, same | Disabled-control traversal and explicit Resume retain result and one evaluation |
| 201811 | keyretry, same | Retry clears result/Hint; selected 200% A leading content visible |
| 201820 | interruptsubmitted, same | Assisted incorrect result survives synthetic interruptions/explicit Resume |
| 201830 | modalcycle, 260x200 | Short safe-area Pause scrolling, Shift/Tab and text toggle contracts pass |

First five runs suppress tooltips for comparison; remaining routes use normal
tooltips. All non-reference runs simulate .9 safe area. Routed input/lifecycle
checks are synthetic native evidence, not manual desktop or physical-phone input.
Both `WordQuest.Context` Unreal tests pass with failed/notRun/inProcess zero and
native exit 0 at clean source: `20261002-202243-automation-initial`.
All 63 Python QA tests, six reference hashes, seven source/runtime SVG pairs, LFS
and whitespace checks pass. No new tests mirroring the vector implementation were
added; reproduction, actual packaged rendering and existing interaction checks
verify this bounded change.

## Read-only comparison

Initial and correct comparisons against PR #26's final captures each find 5,755
changed pixels, all inside the existing title `[229,23,659,163)`. Of those, 5,753
are inside the W region `[229,23,343,136)`. Two other title pixels differ by only
one RGB byte level; their coordinates/values are recorded. An initial assertion of
zero differences outside W was too strict and rejected those two pixels. The
final analysis reports them and requires zero changes outside the whole title;
it does not claim pixel identity for every remaining letter. Glyph paths remain
unchanged. Raw analysis/reproduction: `Artifacts/QA/UI01/wordmark-capital-analysis.json`
and `.py`. Final initial PNG SHA-256:
`83d7915743404944b3db065542e232d627207a668c1ec02cbe2ef68359f6ca40`.
Final correct PNG SHA-256:
`adb5eaf3ab13ab8559b66ff1d8ea215421c78c8e5fa5431585a6a4b3f3d6e052`.

The lower-tip diagnostic finds warm opaque cores using `R>170, G>130, B>120,
R>G+4, R>B+8`. Left/right sample windows are `[265,105,286,137)` and
`[289,105,322,137)` in the original 884x1780 pixel space. Lowest core Y values:

| Tip | Reference | Previous v002 | Revised v003 |
|---|---|---|---|
| Left | 131 | 119 | 130 |
| Right | 129 | 119 | 130 |

This measures two anchors, not complete letterform fidelity. The local
`g-wordmark-capital-comparison.html` embeds unchanged native/reference images with
the existing adjustable overlay; browser/overlay interaction remains unverified.

## Remaining gates

Precise W contours, other letterforms, Q connection/taper, ornament and lighting
remain candidates. Companion identity and panel/control finish also remain open.
The EQUIVOCAL draft and `3 / 7` fixture are unapproved. Static fidelity, editorial,
manual/platform accessibility, full contrast, physical-phone/offline/performance,
UI02 motion and release acceptance are not passed. Android engine support receipt
is absent and adb lists no device on this turn's recheck. The owner retains merge
authority; no agent merge, game deployment or release occurs.

Dedicated read-only Codex review completed at clean
`6d6750232df542f3a14e119751b709a9f98633df` against actual `origin/dev`,
`e2ef2b07bf2f53149d892ea841320120453a5460`, with exit 0 and no actionable
introduced defects. Head/worktree stayed unchanged. The reviewer independently
checked original references, source/runtime SVG parity and diff whitespace;
it did not independently repeat builds, native rendering or device acceptance.
Raw evidence: `Artifacts/Reviews/20261002-203116`. Subsequent review/publication
records change documentation only.
Published as regular [PR #27](https://github.com/rloterh/WordQuest/pull/27)
against `dev`; no agent merge was performed.
