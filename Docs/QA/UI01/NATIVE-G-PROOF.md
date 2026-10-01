# Native G static engineering proof — acceptance pending

Implemented after the owner merged foundation PR #1 (`6a840e0`) on 2026-09-23.
The prototype is a native Unreal UMG screen with separate imported backdrop,
panel and spirit, live educational text, four answers, hint, check and pause.
The backdrop still includes foreground clouds; separated motion layers are unfinished.

The owner merged PR #2 on 2026-10-01. The later
[answer-control follow-up](G-ANSWER-CONTROLS.md) adds native A–D badges and revises
answer spacing/wrapping. The screenshots and discrepancy table below describe the
original PR #2 proof; its unfinished art and acceptance limits still apply.

The subsequent [pearl answer-skin candidate](G-ANSWER-SKIN.md) replaces the flat
answer fills and records native scaling/state evidence. Its art remains unapproved.

The later [progress-plaque candidate](G-PROGRESS-PLAQUE.md) adds separate decoration
behind centered live prototype progress, with native portrait/safe-area/landscape
captures. It does not establish campaign persistence or art acceptance.

## Behavior and scope

`FContextQuestion` validates the local JSON fixture. `FContextAttempt` owns selection,
assistance, pause and exactly-once evaluation independently of art or theme. Initial
selection is empty; selection alone does not evaluate; hints mark the attempt assisted;
pause blocks answer actions. Completed answers disable selection and submission.
Pause offers resume, reading text at 100/200%, and resetting this isolated question.
Keyboard: 1–4 select, H hints, P/Escape pauses, Enter checks when the screen has focus;
Tab/Space/Enter also activate native focused buttons. No campaign reward is granted.
The displayed 3/7 is a reference fixture, not persistent campaign progression.

The exact EQUIVOCAL fixture remains `awaiting_owner_prototype_review`, release false.
Engineering semantic check: “neither confirmed ... nor denied” supports A (ambiguous
or noncommittal), not hostility, detail or certainty. This does not substitute for
owner/editorial approval. No remote AI or service keys are used in question logic.

## Reproduction

Use recorded UE 5.8.2 CL 56702186. LFS must fetch genuine Unreal assets. Editor and
standalone Win64 Development builds have passed with the new implementation.

```powershell
python Tools/BuildScripts/build_wordquest.py
python Tools/BuildScripts/build_wordquest.py --target Game
python Tools/QA/run_g_proof.py automation
python Tools/QA/run_g_proof.py capture
python Tools/QA/run_g_proof.py capture --proof correct
python Tools/QA/run_g_proof.py capture --proof long --width 390 --height 844
python Tools/QA/run_g_proof.py capture --proof large --width 844 --height 390
python Tools/QA/run_g_proof.py capture --width 390 --height 844 --safe-zone 0.9
```

The helper runs the actual editor/game process, retains command, base HEAD, dirty
worktree status, logs, report and PNG under `Artifacts/QA/UI01`. Capture completion
requires exit 0, expected state tuple and exact requested PNG dimensions; it does
not assert visual acceptance. The C++ tests cover all four outcomes, changed selection,
no initial/invalid selection, pause, idempotent hint/submission and fixture load/failure.
Two tests passed, zero failed/skipped. Raw report:
`Artifacts/QA/UI01/20260923-121756-automation-initial/Report/index.json`.

Final editor build: `Artifacts/Logs/Build/WordQuestEditor-20260923-124005.log`, exit 0.
Game build: `Artifacts/Logs/Build/WordQuest-20260923-124214.log`, exit 0.
Native initial 884x1780 PNG:
`Artifacts/QA/UI01/20260923-124125-capture-initial/native.png`.
It contains real rendered controls; no flattened reference sits behind invisible buttons.

To recreate the comparison document without modifying either PNG:

```powershell
python Tools/QA/compare_g.py Artifacts/QA/UI01/20260923-124125-capture-initial/native.png
```

`Artifacts/QA/UI01/comparison.html` embeds original/native images side by side and
at identical dimensions with a 50% opacity slider. Browser automation could not
inspect that local page: the in-app connection was unavailable and Chrome's tool
URL policy blocked file navigation. No workaround was attempted. Native and original
PNGs were inspected directly; interactive overlay behavior remains unverified.

## Visible differences and remedies

| Area | Current difference | Required remedy before UI01 acceptance |
| --- | --- | --- |
| Brand | Plain Cormorant candidate, different width/letterforms; no bevel, Q flourish or underline ornament | Match licensed lettering and supply layered ornament/lighting |
| Progress/pause | Plain 3/7 and pearl pause disk; reference has purple plaques and gold edges | Faithful separate plaque/icon skins |
| Spirit | Different face, silhouette and lantern; smaller visible extent | Faithful original identity extraction and clean alpha; do not approve current candidate |
| Panel | Flatter top and jewel, altered shoulders, stronger orange/gold edge and rounded bottom | Match original contour, ornament positions, edge softness and slice proportions |
| Background | Reconstructed hidden clouds, no separate foreground; one-pixel source-height difference; cover crop changes in other aspect ratios | Reconstruct independent cloud layer and compare architecture/lighting at frozen placement |
| Typography | Roboto differs in word/clue metrics and weight; candidate action serif is thinner | Identify/licence closest fonts, tune measured glyphs and baselines |
| Dividers | Simple live glyphs lack beveled diamond and tapered rules | Separate ornamental assets without baked text |
| Answers | Flat pearl, no raised bevel/shadow or round A–D badges; text starts farther left | Faithful scalable skins with separate live badges, consistent state cues |
| Hint/check | Flat fills; missing bulb/star, bevel, glow and fine texture | Licensed/exported ornaments and faithful pressed/focus/disabled states |
| Position | Answer rows ~2px below target after layout correction; panel apex/edge still differs | Re-measure after final art/font replacements |

No visible motion exists in this static proof. The screen remains static throughout
capture; no time/seed-dependent art is used. UI02 and H/I expansion remain gated.

## Import and ownership

Unreal generated `GPrototype.umap` and the four real imported `.uasset` files.
To regenerate, launch a normal editor with `-EnablePlugins=PythonScriptPlugin`
and `-ExecutePythonScript=<absolute Tools/AssetImport/import_g_prototype.py>`.
The Python commandlet cannot import the font because it lacks Slate initialization;
the normal editor script completed successfully. Python is not a runtime dependency.
The import script copies editorial source JSON into the staged `Content/Data` location;
edit the source and rerun it, rather than editing the staged copy independently.
Font and texture imports remain candidates. Font licensing/provenance is in
`ArtSource/Fonts/CormorantGaramond/PROVENANCE.md`. Original references are unchanged.

## Remaining gates

No cooked package or physical-phone evidence yet. Android Studio is installed,
but UE Android binaries/receipt are missing and no adb device is connected. This
requires the engine's original installation source and a phone; see the existing
Android handoff. Desktop sizing/safe-area simulation cannot certify phone touch
targets, notches, accessibility services, GPU/memory performance or offline cold launch.
The text setting covers question/answer reading and actions; modal/brand scaling,
screen-reader announcements and persistent user preferences remain unfinished.
Do not describe this PR as accepted UI01/UI02 or a release-ready learning game.

Responsive QA exposed stretched panel ornaments and a pause shade drawn underneath
some content. The panel now uses fixed-height top/bottom UV regions with a stretchable
middle; explicit root canvas ordering places the modal above the whole reading tree.
Retest evidence is recorded after those corrections, rather than calling the earlier
screenshots passes on appearance alone.

After the corrections, these native runs exited 0, produced the requested dimensions
and matched their expected state tuples:

| Run under `Artifacts/QA/UI01` | Evidence |
| --- | --- |
| `20260923-124125-capture-initial` | 884x1780, no selection/evaluation |
| `20260923-124152-capture-paused` | 884x1780, B retained, paused, attempted actions rejected |
| `20260923-124221-capture-long` | 390x844, 200% reading text with extended clue/options |
| `20260923-124406-capture-large` | 844x390, 200% reading text; content extends into scrolling |
| `20260923-124447-capture-initial` | 390x844, simulated safe-area ratio 0.9 |

Earlier state captures also verified C selection without evaluation, incorrect B,
assisted A, empty submission, focus B and duplicate correct submission. Each raw
`run.json` records the exact command and expected state result. The layout-only
corrections did not change question/evaluation logic.

In the actual 390x844 game window, manual scrolling reached the whole extended clue,
all four wrapped answers and the stacked Hint/Check controls. Clicking A displayed
the selection marker; clicking Check displayed “Correct” and disabled the answers.
Raw native log: `Artifacts/Logs/UI01/Manual-Long-Fixed.log`. This manual interaction
was observed on desktop; no phone or accessibility-service pass is inferred.
The long-text proof adds artificial stress strings only in non-shipping proof code;
those strings are not additional editorial content.

On 2026-10-01 the clean implementation commit `4b3ed79` was rebuilt successfully,
and both Unreal tests passed again with zero failures/skips. A fresh 390x844 native
correct-answer capture also passed its expected tuple (selected A, submitted,
correct, unassisted, unpaused, exactly one evaluation) and was visually inspected.
Its complete feedback is visible below the disabled controls:
`Artifacts/QA/UI01/20261001-154529-capture-correct/native.png`.
The editor log is `Artifacts/Logs/Build/WordQuestEditor-20261001-154427.log`; the
new automation report is under `20261001-154439-automation-initial/Report`.
The [internal review](INTERNAL-REVIEW.md) completed without actionable findings.
