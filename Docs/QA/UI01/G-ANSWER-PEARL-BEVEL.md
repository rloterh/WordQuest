# G answer pearl bevel candidate

The owner merged PR #37 into `dev` at `3c04337` on 2026-10-03, 14:16:49 UTC.
This bounded UI01 correction addresses the comparatively flat answer tile face
and weak lower bevel/shadow. The original remains immutable. Prior native baseline:
`Artifacts/QA/UI01/20261003-131118-packaged-capture-initial/native.png`, SHA-256
`ceb59328f455efad8fd1dfb0d536920f10827ebb0fd4a73164437d3edd855636`.

## Editable art and integration

`ArtSource/UI/G/Vector/G-Answer-Pearl-v002.svg` adds a softer inner edge highlight,
brighter lower rim, cooler face gradient and tighter violet contact shadow.
The face geometry and 690x119 canvas remain unchanged; rim thickness increases
from 1.5 to 2.2 reference units. No labels, badges or outcome cues are baked in.
The previous master/export/Unreal texture remain unchanged. This is hand-authored
simplified material, not extracted original pixels or accepted exact fidelity.

`render_g_answer_pearl.py --version v002 --check` reproduces the new 1380x238 RGBA
export with pinned development-only resvg-py 0.5.0 / resvg 0.48.1. Default v001
reproduction remains intact; builds use checked-in Unreal assets.
The actual texture commandlet uses explicit `-WordQuestAnswerBevel` to import
separate `G_AnswerPearlBevel`, verifying the export pin and Texture2D/save.
It configures sRGB/UI compression/group, bilinear filtering, no mips or streaming.
Native loading prefers this asset, then existing `G_AnswerPearl`; neither available
retains the existing opaque fill/outline behavior. The fallback is not loaded when
the candidate loads successfully. Existing always-cook includes both textures.
Each full-size BGRA8 surface is about 1.25 MiB before engine bookkeeping; this is
a source-size calculation, not measured GPU memory or phone performance.

Native drawing retains the 666x95 core, two-times export scale, margins
[112,96,112,136] texture pixels, row placement and 44-unit corners. Only the
middle surface stretches as accessible/long content grows. Live text, badge,
selection/focus/pressed outlines, disabled reading and learning/input are unchanged.

## Current verification

Actual import exited 0 with the completion marker and 0 errors/warnings:
`Artifacts/Logs/UI01/answer-bevel-import.log` / `.json`.
The saved texture is 51,017 bytes, SHA-256
`4f45be0325d11dbfb01b6da0a629d7563ca60499dbec7a2d594faa981e33fd5b`.
Source/export hashes and settings are recorded in adjacent v002 provenance.
Both new binaries use configured Git LFS. RGBA alpha is 0–255, nonzero bounds
[3,0,1377,231), four transparent corners, no internal row holes at alpha >=128.
These are scoped alpha checks; the soft upper shadow can reach the canvas edge.
Both versions reproduce exactly. Actual Editor compilation passed four actions
in 44.46s, exit 0: `Artifacts/Logs/Build/WordQuestEditor-20261003-142747.log`.
All 66 Python checks, eight SVG pairs and six original reference hashes pass.

Dirty native preflight `20261003-143438-capture-initial` exited 0 with complete
dimension/state/cue checks. The full PNG, first-tile original/baseline/final crops
and diagnostic half-opacity overlay were inspected. Rim/face shading is closer;
painterly detail, exact softness and shadow remain unfinished.
At x700, six fixed 5x3 median face samples (offsets 6/15/30/55/80/89) and four
shadow samples (95/99/103/108) use documented row-top alignment: original y990,
unchanged native y987. Face mean absolute RGB channel error improves from 5.44
to 1.56; shadow from 11.00 to 8.42. This first unselected tile profile is scoped,
not a global fidelity score. Minimum sampled face contrast against opaque native
ink RGB(24,20,83) is 11.30:1; this does not qualify all states, antialiasing or
manual/platform accessibility. Initial comparison changes 272,668 RGB pixels
within [98,983,786,1435), with zero changes outside four tile/gutter regions
[97,983,789,1102), [97,1095,789,1214), [97,1207,789,1326), [97,1319,789,1438).
`Artifacts/QA/UI01/AnswerBevel/comparison.json` records input hashes and samples;
the original and merged baseline remain unchanged.

Missing-candidate runs `20261003-145401-capture-initial` (884x1780) and
`20261003-145444-capture-actions` (390x844, simulated .9 inset, 200%) exited 0
with complete applicable native checks. Both PNGs were inspected; initial is
RGB-identical to the merged PR #37 baseline. The owned texture was restored
with its exact hash in `AnswerBevel/fallback.json`. Missing-package warnings
are expected for this editor omission test; it does not corrupt/qualify a package.
Both Unreal Context tests pass at clean `caa9dd3f2bcc6fb1b3ce347cfd19525fa4112e18`
in `20261003-145726-automation-initial`: 2 succeeded, none failed/not run/in process.

## Package refresh race and bounded fix

First clean package `Artifacts/Packages/Win64/20261003-145924-242871` passed
Editor/Game checks (three Editor relink/metadata actions, 7.72s; three Game actions,
48.97s), full BuildCookRun (132.63s, 518 cooked packages, 0 errors/warnings).
Its helper nevertheless exited 1 and correctly marked evidence incomplete:
the successful protected-task receipt did not include the new executable.
It is retained as failed helper evidence, not the final qualified archive.
A later protected `last-run.json` includes that exact archived executable.
The minute-triggered task can already be running while archiving completes,
having enumerated executable paths earlier; this is the inferred timing scenario.

`local_firewall.py` now retries the same owner-installed protected task up to
three times only when a successful receipt omits the exact requested executable.
It never changes firewall policy, passes arbitrary arguments, requests elevation
or runs project code as SYSTEM. Task/timeout/JSON failures still propagate; three
uncovered receipts still fail packaging. Per-invocation timeout remains 135s,
with at most three invocations; no unlimited retry is introduced.
The added regression checks stale-success then exact coverage through identical
task invocations; existing checks now verify bounded rejection and immediate
task failure. All 67 Python checks pass. Native code/art are unchanged by this fix.
Fresh complete packaging, final responsive checks and dedicated review are pending.

## Remaining gates

Painterly surface/rim softness, brand/companion identity and full UI01 art acceptance,
draft-fixture editorial approval, UI02 motion, manual/platform accessibility,
Android/physical phone, isolated offline play, performance and original release
gates remain open. Windows offscreen/synthetic checks do not pass manual/device gates.
