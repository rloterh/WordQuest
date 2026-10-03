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

## Verification in progress

The real Editor target compiled the edited C++ successfully (71.81s).
Two dirty-source 1x preflights on `00e044e` passed and were inspected:
`Artifacts/QA/UI01/20261003-042125-capture-initial` (884x1780) and
`20261003-042250-capture-longselectedfocus` (260x640, safe .9, 200% long text).
These show the softer surface and retained selected/focus/letter/marker content.
They are preliminary, not final 2x evidence. The final export increased to
1380x238, with matching native drawing scale; its reimport also completed with
exit 0 and zero commandlet errors/warnings. Earlier import log/metadata use
the `answer-pearl-import-1x` prefix under `Artifacts/Logs/UI01`.
Native preflight, clean package, responsive/result/contrast checks, Unreal/Python
tests and dedicated read-only review are pending. This is simplified authored
art, not original painterly texture or accepted fidelity. Draft learning/progress
fixtures, editorial, manual/platform accessibility, UI02 motion, phone/offline/
performance and release gates remain open.

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
2x export was genuinely reimported with zero commandlet errors/warnings. Fresh
final art packaging/captures and review are pending. Preserved batch/analysis
scripts and results use `answer-pearl-muted-rim-` under `Artifacts/QA/UI01`;
their earlier import metadata/log use the same suffix under `Artifacts/Logs/UI01`.
