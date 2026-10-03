# G authored pearl answer surface

The owner merged PR #30 into `dev` at `00e044e` on 2026-10-03, 04:05:55 UTC.
The original reference has a soft pearl answer face and thin rim; the previous
generated skin has extra rolled highlights and a busier perimeter. This bounded
UI01 candidate authors a separate editable surface while retaining live learning
text, badges, result markers and input/reading behavior.

## Source and genuine Unreal import

Master: `ArtSource/UI/G/Vector/G-Answer-Pearl-v001.svg`. Its broad ivory/lilac
gradients, 44px outer corners, thin rim and soft shadow contain no text or badge.
No original pixels were extracted/edited and no image generation was used.
The 1380x238 RGBA export `ArtSource/UI/G/Exports/G-Answer-Pearl-v001.png` is rendered
directly by pinned development-only resvg-py 0.5.0 / resvg 0.48.1. Normal builds
use checked-in art and need no renderer dependency. The adjacent provenance
records reference/source/export hashes and limitations; `render_g_answer_pearl.py
--check` reproduces the PNG byte-identically without writing.

Unreal's actual texture-only Python commandlet imported and saved
`Game/Content/UI/G/G_AnswerPearl.uasset`, with sRGB, UI compression/group, bilinear
filtering, no mips and no streaming. Commandlet exit 0, zero errors/warnings;
completion marker and source hash are recorded under
`Artifacts/Logs/UI01/answer-pearl-import.log` / `.json`. Earlier generated PNG
and `G_AnswerSkin.uasset` remain unchanged. Git LFS 3.7.1 and its process filter
were verified before adding the new binary export and Unreal asset.

Import from repository root:

```powershell
& 'C:/Program Files/Epic Games/UE_5.8/Engine/Binaries/Win64/UnrealEditor-Cmd.exe' 'C:/Projects/WordQuest/Game/WordQuest.uproject' -EnablePlugins=PythonScriptPlugin -run=pythonscript '-script=C:/Projects/WordQuest/Tools/AssetImport/import_g_answer_pearl.py' -Unattended -NullRHI -NoSplash -NoSound
```

## Native integration

The logical canvas is 690x119, exported at 2x for the thin rim. Its 666x95 face
starts at (12,4) in reference units. The decorative image is placed 12px left
and 4px above its unchanged answer button, scaled with the composition. Insets
(56,48,56,68 reference units, doubled in texture pixels) preserve rounded corners
and shadow while a 3px logical middle strip
stretches with row growth. The full export is used, without UV cropping. Images
remain hit-test invisible. Normal/disabled unselected skins use their own thin
rim; native hovered/pressed/selected/focused outlines remain, with a matching
44px scaled radius. Missing texture still uses the ordinary opaque fill/outline.
Static answer content retains the submitted-reading contrast wrapper; disabled
buttons remain disabled and skipped by navigation. No scoring or fixture changes.

## Final art verification

The real Editor target compiled the edited C++ successfully (71.81s).
Two dirty-source 1x preflights on `00e044e` passed and were inspected:
`Artifacts/QA/UI01/20261003-042125-capture-initial` (884x1780) and
`20261003-042250-capture-longselectedfocus` (260x640, safe .9, 200% long text).
These show the softer surface and retained selected/focus/letter/marker content.
They are preliminary, not final 2x evidence. The final export increased to
1380x238, with matching native drawing scale; its reimport also completed with
exit 0 and zero commandlet errors/warnings. Earlier import log/metadata use
the `answer-pearl-import-1x` prefix under `Artifacts/Logs/UI01`.
These preflights are retained as intermediate evidence, not acceptance.

At clean implementation `0e17385e237cdec792adac4469e3ae12296ec360`, the first
2x candidate passed actual Editor/Game compilation (12.07s/46.22s), full Win64
packaging (155.56s), all 14 inspected packaged captures and both Unreal tests
(`20261003-043521-automation-initial`, failed/notRun/inProcess 0). All 63 Python
tests, six reference hashes, seven SVG parity checks and byte-exact PNG reproduction
passed. The native source change is preserved by the final art adjustment below.
Archive `Artifacts/Packages/Win64/20261003-042733-699999` remains preliminary art
evidence: source export SHA was `94ad1b8f825bcb9182e2dae961409a7360d701958123176f2760cabe2e158d5e`.
Its inspected reference-row comparison found the lower rim too muted. Only the
editable rim gradient's last stop changed from darker lilac to pale ivory/lilac;
geometry, body shading, shadow and native code remain unchanged. The revised
2x export was genuinely reimported with zero commandlet errors/warnings. Preserved batch/analysis
scripts and results use `answer-pearl-muted-rim-` under `Artifacts/QA/UI01`;
their earlier import metadata/log use the same suffix under `Artifacts/Logs/UI01`.

Final art source is clean `def5c5f459371213a4c853a8f5376a1d27babc58`.
The real Editor/Game checks passed in 1.76s/1.72s, both up to date (zero compile
actions); the native code is identical to the compiled/tested `0e17385` revision.
Fresh full Win64 BuildCookRun passed in 67.08s, including BGRA8 1380x238 texture
cooking. Archive `Artifacts/Packages/Win64/20261003-043958-979684` has 48 verified
payload hashes, unchanged head/worktree/inputs and complete evidence. Manifest
SHA-256: `c599a41124f2cb03476de3d8ca01211b602bbbd7f15fe5f06993f8a1d23bf512`.

All 14 final packaged captures below exited 0, passed applicable native state,
layout/reading/focus/result checks, verified package hashes and have complete
evidence. All PNGs were inspected; raw logs contain no `Error:`/`Fatal:` lines.
Paths are under `Artifacts/QA/UI01/20261003-`:

| Run suffix | Viewport | Reading/proof |
| --- | --- | --- |
| 044231-packaged-capture-initial | 884x1780 | initial |
| 044302-packaged-capture-selected | 884x1780 | selected |
| 044331-packaged-capture-correct | 884x1780 | correct |
| 044356-packaged-capture-wrong | 884x1780 | wrong |
| 044420-packaged-capture-initial | 1768x3560 | 2x viewport |
| 044443-packaged-capture-initial | 260x640 | safe .9 |
| 044508-packaged-capture-focus | 844x390 | landscape, safe .9 |
| 044534-packaged-capture-large | 390x844 | 200%, safe .9 |
| 044558-packaged-capture-longfocus | 390x844 | long answers, 200%, safe .9 |
| 044623-packaged-capture-longselectedfocus | 260x640 | long selected B, 200%, safe .9 |
| 044647-packaged-capture-correct | 390x844 | 200%, safe .9 |
| 044713-packaged-capture-wrong | 390x844 | 200%, safe .9 |
| 044739-packaged-capture-keydisabled | 390x844 | routed disabled navigation, safe .9 |
| 044804-packaged-capture-keyretry | 390x844 | routed retry/200% focus, safe .9 |

`answer-pearl-analysis.py`/`.json` preserve read-only comparisons and nine static
opaque-core/adjacent-backing contrast samples. Minimum sample ratio is 9.76:1,
including submitted letters, answer text and the correct marker; this is not
whole-screen or platform accessibility certification. Initial/correct comparisons
against the PR #30 native baseline change 279,000/275,069 pixels, with zero changes
outside the four answer/shadow regions (2px diagnostic margins). Baseline runtime
source/content/art under `ArtSource/UI` match merged `dev`; only handoff prose
differs. Original/reference/native input hashes remain unchanged. Inspected row
crops and the 50% reference overlay use the `answer-pearl-` diagnostic prefix.
The double rolled highlights are removed and the thin lower rim is closer to
the reference. Painterly grain, precise surface tone/rim softness and existing
panel/character/wordmark/action/type differences remain unaccepted.

`verify-answer-pearl.py` and `answer-pearl-verification.json` locally record
archive/capture hashes and unchanged old
art. Final SVG/PNG/Unreal texture hashes are respectively:

- `26f749f73ce702bfee4f927067a776788ca109076428a5b4db455676382978d4`
- `613ba83c8f251936929cc5a6877d6c267237c17eb34d8ac702e9020084f09424`
- `0192b1783ed8c267d36949b853e2fa21311762fb94f12e4b0d5a209326c975f7`

Binary export/texture LFS pointer OIDs match the actual files. Six supplied
references, seven SVG pairs and final byte-exact PNG reproduction pass. Both
Unreal tests passed at unchanged native implementation `0e17385`. After the
owner's firewall request, all 66 Python QA tests passed (including three optional
firewall-helper failure/coverage checks).

The owner's automatic firewall request was additionally verified on clean
`a8745af6eaed9ac8d94424b9dadc71a699dbe871`. Archive
`Artifacts/Packages/Win64/20261003-050358-635571` passed Editor/Game up-to-date
checks (2.74s/2.10s) and full BuildCookRun (145.79s). All 48 payload hashes and
source invariants pass; manifest SHA-256 is
`774bfe8d9052497e1f2a24b5818112a412874a2bbaee5b655cdd5d9e8324e355`.
The package helper automatically refreshed the protected local task and confirmed
this new archive's executable at 05:06:45 UTC. ActiveStore has an enabled Allow rule
for that exact binary, Private/Public and LocalSubnet. No additional UAC was needed.
Native launch `20261003-050715-packaged-capture-initial` exited 0 with complete,
hash-verified evidence and passed state/option-cue checks. Its inspected 884x1780
PNG is byte-identical to final-art initial capture `044231`; no new visual change
was introduced by this build-tool integration. Local metadata is in
`answer-pearl-firewall-verification.json`. These are native/policy checks; the
unavailable desktop connection does not establish a visual security-dialog test.
Dedicated read-only review of clean `f32f1586a856103d4718799e5b5861ed769fb8a3`
against actual `origin/dev` (`00e044e`) completed with exit 0 and no actionable
introduced defects. Head/worktree remained unchanged; raw report and metadata are
under `Artifacts/Reviews/20261003-050853`. The reviewer did not independently rerun
builds, runtime checks or device tests. Owner retains the merge decision.

[PR #31](https://github.com/rloterh/WordQuest/pull/31) publishes the answer-surface
candidate and optional package refresh against `dev` as a regular PR. The local
firewall configuration is already applied on the owner's machine; merging code
does not install that privileged task on another computer.

This is simplified candidate art. Draft learning/progress fixtures, editorial,
manual/platform accessibility, UI02 motion, phone/offline/performance and release
gates remain open. Android engine payload is still absent and adb reports no phone.
