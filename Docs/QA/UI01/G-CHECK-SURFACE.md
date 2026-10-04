# G editable Check surface

The owner merged PR #42 at `39d757f` on 2026-10-04, 18:30:42 UTC. This bounded
UI01 candidate replaces the generated Check decoration with an editable SVG master
and genuine Unreal texture. Softer violet lighting, a pale-gold rim, filtered
bevel and four static glints contain no baked label or star. It remains a simpler
reconstruction than the reference; full visual acceptance is open.

## Source and native integration

`ArtSource/UI/G/Vector/G-Check-Surface-v001.svg` is a 388x113 canvas rendered to
`ArtSource/UI/G/Exports/G-Check-Surface-v001.png` at 776x226 with pinned development-only
resvg-py 0.5.0 / resvg 0.48.1. `python Tools/AssetImport/render_g_check_surface.py
--check` reproduces the exact PNG without writing. Normal builds use the committed
PNG/Unreal asset and require no renderer install. No imagegen, original-pixel
extraction or reference modification occurred. Adjacent provenance records hashes.

The real Unreal texture-only commandlet imports `G_CheckReverie.uasset`: sRGB,
UI compression/group, bilinear, no mips or streaming. Final import exit 0 and
zero errors/warnings; raw evidence is `Artifacts/Logs/UI01/check-surface-import-rim.log`
and `check-surface-import.json`. It reports the genuine `/Game/UI/G/G_CheckReverie`
object and 776x226 dimensions. Git LFS 3.7.1/process filter were verified before
adding the new PNG and Unreal binary. Earlier generated PNG/asset remain unchanged.

```powershell
& 'C:/Program Files/Epic Games/UE_5.8/Engine/Binaries/Win64/UnrealEditor-Cmd.exe' 'C:/Projects/WordQuest/Game/WordQuest.uproject' -EnablePlugins=PythonScriptPlugin -run=pythonscript '-script=C:/Projects/WordQuest/Tools/AssetImport/import_g_check_surface.py' -Unattended -NullRHI -NoSplash -NoSound
```

The decoration uses its full export UVs and the existing nine-slice margins
(.145 horizontal, .45 vertical) and responsive 388x113 reference slot. Full texture
dimensions drive drawing scale, preserving rounded ends during stacked/large-text
layout. The separate native label/star, tooltip, focus/hover/press, disabled state,
minimum target, selection/scoring and fixture remain unchanged. Missing authored
texture selects the prior generated asset with its original UV crop. Missing
both retains native fill/outline and live label/star. Images remain hit-test invisible.

## Preliminary verification

Real Editor build at `Artifacts/Logs/Build/WordQuestEditor-20261004-201237.log`
passes four actions in 48.01s. All 68 Python QA checks pass. Six immutable supplied
references and byte-identical PNG reproduction pass. The initial native preflight
`20261004-201343-capture-initial` showed a flatter bevel; edge softness and peripheral
glow were revised and genuinely reimported before final preflight
`20261004-201856-capture-initial`. Both captures were inspected. These dirty-source
captures are preliminary evidence. An initial clean package at `ac6c621`
(`Artifacts/Packages/Win64/20261004-203609-989777`) and twelve native checks passed,
but visual inspection still found a flatter rim. Darker edge separation, warmer
gold, faint peripheral texture and a continuous highlight replace the earlier
hard-ended highlight. The final genuine reimport and inspected dirty preflight
`20261004-205213-capture-initial` pass. Earlier verification/batch/fallback records
are retained with `-early` suffixes. The local comparison's integer Y assumption
was corrected to the observed footprint [399,1451,787,1564); cooked asset inspection
uses IoStore rather than assuming textures are in the loose-file PAK. No product
code change was needed for these diagnostic assumptions. Final clean package
evidence for the revised art is recorded below.

Missing-art checks in `Artifacts/QA/UI01/CheckMaterial20261004/fallback.json`
all pass and all four captures were inspected:

| Art available | Proof | Capture |
|---|---|---|
| Earlier generated texture | Initial 884x1780 | `20261004-205512-capture-initial` |
| Earlier generated texture | Focused Check, 200%, 260x640 safe .9 | `20261004-205537-capture-actions` |
| Neither Check texture | Initial 884x1780 | `20261004-205600-capture-initial` |
| Neither Check texture | Focused Check, 200%, 260x640 safe .9 | `20261004-205623-capture-actions` |

Each helper/native exit is 0 with complete state/focus/large-text evidence. The
generated fallback's entire PNG matches prior Editor evidence
`20261004-174307-capture-initial` exactly. Missing both retains readable live
label/star and navy focus on the native fill. Exact owned asset paths were moved
only into a verified local holding directory and restored in `finally`; both
hashes match provenance. Ten existing staged SVG pairs also pass byte parity.

## Final clean Win64 evidence

`Artifacts/Packages/Win64/20261004-210122-845447` is complete at clean source/art
`905b475a8f2123a5a9fb5e179e755a8799c687e5`. Editor/Game warm builds used zero
actions (3.35/3.46s); the edited C++ compiled in the earlier Editor build (48.01s)
and initial package Game build (three actions, 36.06s). Final full cook handles
520 packages with zero errors/warnings; all build/cook/stage/archive exits are 0.
BuildCookRun took 146.65s. HEAD/worktree/inputs are unchanged and all 49 payload
sizes/hashes verify. Manifest SHA-256:
`cfce0fb3933c56feca7a89b7c3c7a78160c7a00767031542b2b29d7530707409`.
Automatic exact archived-executable firewall coverage passes on the first attempt
at 21:04:12.0340521 UTC, Private/Public LocalSubnet. No task, ACL or security policy
was changed. This success does not establish the cause of earlier intermittent
task failures.

All twelve packaged captures have helper/native exit 0, complete evidence, matching
clean source/package identity, verified archive hashes, expected dimensions and
applicable state/cue/focus/large-text/keyboard checks. Every PNG was inspected:

| Proof | Dimensions / adaptation | Capture |
|---|---|---|
| Initial | 884x1780 | `20261004-210417-packaged-capture-initial` |
| Initial | 1768x3560 | `20261004-210429-packaged-capture-initial` |
| Initial | 390x844, safe .9 | `20261004-210441-packaged-capture-initial` |
| Initial | 390x844, safe .9, 200% | `20261004-210451-packaged-capture-initial` |
| Focused Check | 260x640, safe .9, 200% | `20261004-210501-packaged-capture-actions` |
| Focused Check | 390x844, safe .9 | `20261004-210512-packaged-capture-actionfocus` |
| Initial | 844x390, safe .9, scrollable reading | `20261004-210523-packaged-capture-initial` |
| Correct | 884x1780 | `20261004-210534-packaged-capture-correct` |
| Wrong | 390x844, safe .9 | `20261004-210545-packaged-capture-wrong` |
| Hint / correct | 390x844, safe .9 | `20261004-210556-packaged-capture-hint` |
| Check without choice | 884x1780 | `20261004-210607-packaged-capture-empty` |
| Disabled-key traversal | 390x844, safe .9 | `20261004-210619-packaged-capture-keydisabled` |

At 200%, focused Check remains readable after native scroll/reveal; the reference
layout and accessible adaptation stay separate. Correct/wrong/Hint states retain
markers, feedback and disabled actions. Disabled navigation skips actions and
reaches Pause. Landscape initial view shows the reading header; later reading
content remains scrollable rather than being claimed visible in that PNG.

The IoStore CSV lists the genuine cooked `../../../WordQuest/Content/UI/G/G_CheckReverie.uasset`.
All ten loose SVGs extracted from the archived PAK match staged source bytes and
the archive hashes remain unchanged by inspection. Raw comparison/cook validation
is `Artifacts/QA/UI01/CheckMaterial20261004/verification.json`; package/helper,
IoStore CSV/log, SVG extraction, batch and native logs are retained locally.
Both real Unreal Context tests pass at clean matching `905b475`, exit 0 and no
failed/not-run/in-process tests, under `20261004-210634-automation-initial/Report`.

## Reference comparison and limits

Final reference-size PNG SHA-256:
`4a47e6975cc46badef2f4b612e8699ff2e9f52d1b648c337b556605464f39fcf`.
Compared with PR #42's packaged initial PNG, 41,402 changed RGB pixels are confined
to the observed Check footprint [399,1451,787,1564); zero pixels change elsewhere.
This verifies the bounded runtime change, not matching to the supplied target.
Editor/package variation is 964 pixels in the unchanged Pause/plaque regions,
maximum channel delta 1, bounds [362,38,855,198). Check itself matches across those
captures; no whole-screen byte identity across backends is claimed.

Original, baseline and final Check diagnostic crops and a whole-screen 50% overlay
were inspected under `Artifacts/QA/UI01/CheckMaterial20261004`. Crops are diagnostic
only, not new references or product assets. Eight fixed opaque face samples
(listed in `verification.json`, excluding label/star/rim) have mean absolute
channel error 9.08 before and 9.88 after. That small sample result worsens slightly;
no overall color/fidelity improvement is claimed. The editable surface has quieter,
simpler gloss/texture, with softer peripheral detail and different bevel/gold finish
from the supplied reference. Those tradeoffs remain visible and unaccepted. The
benefit of this increment is editable art ownership and a reproducible import
pipeline with preserved live controls/fallbacks, not completion of UI01.

Subsequent evidence/review/publication records change docs only; tested source/art
remains `905b475`. Dedicated read-only review against actual `origin/dev` is pending.

## Open gates

The candidate has simpler material/glints than the original. Exact contour, bevel,
gold finish, typography/icon and full UI01 fidelity, UI02 motion, draft fixture
editorial approval, manual pointer/keyboard/hover/press, platform accessibility,
Android/physical-phone, isolated offline, performance and original release gates
remain open. Desktop captures and routed synthetic keys do not establish those gates.
No deployment, release or owner merge occurs.
