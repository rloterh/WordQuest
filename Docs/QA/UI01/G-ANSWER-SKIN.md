# G pearl answer-skin candidate — acceptance pending

After the owner merged PR #3 (`8748673`), this bounded art increment replaces flat
answer fills with a separate imported pearl/lavender skin. Text, A–D badges,
selection markers, focus outlines and hit regions remain native widgets. The
decorative image is hit-test invisible and follows each answer's disabled state.
Hover/press use translucent overlays; a missing texture asset falls back to the
existing flat fill. Scoring, the fixture, original references and motion are unchanged.

## Asset and import

Built-in imagegen extracted a blank skin from the immutable G reference, then made
one perimeter/shadow correction. v001 was rejected. The unchanged v002 master is
`ArtSource/UI/G/Reconstruction/G-Answer-Skin-v002-Candidate.png`, 2172x724 RGBA,
with zero alpha at all four corners. Exact prompts, hashes, alpha bounds and UVs
are in the adjacent `G-Answer-Skin-PROMPTS.md` and
`G-Answer-Skin-v002-PROVENANCE.json`. No manually edited pixels or layered source
are claimed. These working exports do not replace or modify the original reference.

Unreal generated `Game/Content/UI/G/G_AnswerSkin.uasset`. Import settings are UI/sRGB,
bilinear, no mips/streaming and configured maximum size 1024. Actual GPU memory or
performance is unmeasured. Both binaries use LFS; integrity checks passed. Runtime
UVs frame the core to omit empty margins, faint stray edge pixels and excess shadow.
The source PNG remains intact.

Initial nine-slice captures exposed border-size clamping: Slate calculates texture
box borders from texture pixels rather than `Brush.ImageSize`. A texture-sized
decorative widget and reference drawing scale now retain a center strip and bounded
borders as rows grow. Captures were retaken after the correction.

Texture-only import uses Unreal's Python commandlet:

```powershell
& 'C:/Program Files/Epic Games/UE_5.8/Engine/Binaries/Win64/UnrealEditor-Cmd.exe' 'C:/Projects/WordQuest/Game/WordQuest.uproject' -EnablePlugins=PythonScriptPlugin -run=pythonscript '-script=C:/Projects/WordQuest/Tools/AssetImport/import_g_answer_skin.py' -Unattended -NullRHI -NoSplash -NoSound
```

Check exit status and `WORDQUEST_ANSWER_SKIN_IMPORT_COMPLETE`. Verified log:
`Artifacts/Logs/UI01/AnswerSkinImport-20261001-commandlet.log`, exit 0, zero errors
and warnings. Earlier normal-editor attempts had a JSON serialization error, then
a shutdown crash after an explicit editor quit; neither counts as a pass. The final
script converts Unreal's array to a Python list and uses normal commandlet completion.
This texture-only route does not replace the earlier Slate-dependent font import.

## Native evidence, 2026-10-01

Final implementation `3e9cefa`: both Win64 Development targets passed, exit 0.
Build logs under `Artifacts/Logs/Build`: `WordQuestEditor-20261001-183536.log` and
`WordQuest-20261001-183809.log`. Both existing `WordQuest.Context` tests passed on
the clean commit, zero failures/skips, under
`Artifacts/QA/UI01/20261001-183809-automation-initial/Report`.

Dedicated read-only Codex review completed at clean `adcab28` against actual base
`origin/dev` (`8748673`), exit 0, with no actionable introduced defects. Evidence:
`Artifacts/Reviews/20261001-184424`. The review did not rerun checks or authorize
a merge. Subsequent updates only record review/publishing status in documentation.

All below exited 0 with expected tuples/dimensions; PNGs were inspected directly.
Each `run.json` records the exact revision/worktree and command.

| Run under `Artifacts/QA/UI01` | Observation |
| --- | --- |
| `20261001-183621-capture-initial` | Clean final implementation, 884x1780; pearl skins with live A–D/text, no selection/evaluation; compared with original |
| `20261001-183621-capture-longfocus` | Clean final implementation, 390x844; 200% extended answers, B focused and fully visible; text stays within the row |
| `20261001-182714-capture-selected` | Clean `b4358d9`, before decorative-scale correction; C marker/outline retained, no evaluation |
| `20261001-182714-capture-correct` | Clean `b4358d9`, before decorative-scale correction; checked A, one evaluation, disabled skin/controls and complete feedback |

`Artifacts/QA/UI01/g-answer-skin-comparison.html` embeds the final initial PNG and
immutable original. Browser interaction is unverified; prior local-navigation
policy blocks were not bypassed. Images were compared directly.

## Limits and next work

This adds a bevel and textured surface to the prototype, not accepted fidelity.
Generated gloss, corners and edge treatment differ; UV framing removes much of
the original external shadow. Further art/border tuning is needed. Enlarged rows
are an accessibility adaptation, not a reference-dimension fidelity pass.

Manual input, accessibility services, phone touch, packaging, GPU/memory and offline
cold-launch checks were not run this turn. Brand, plaque, panel, spirit identity,
dividers and actions remain unfinished/candidates; the fixture is draft. Android
engine support and a connected phone remain missing. UI01, UI02, device and release
gates remain open.
