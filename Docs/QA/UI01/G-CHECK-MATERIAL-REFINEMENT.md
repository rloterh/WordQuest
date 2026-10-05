# G Check material refinement

PR #44 is owner-merged at `8f51a15` (2026-10-05, 01:17:57 UTC). This bounded UI01
increment returns to the material differences disclosed in the merged PR #43.
The reference has a more sculpted, saturated violet face and stronger gold/bevel
separation than the v001 reconstruction. The proposed v002 uses explicit curved
edge lighting, revised face/rim gradients, smaller glints and less blue-grey wash.
It is hand-authored SVG, with no baked label/star or reference pixel extraction.
No imagegen is required for this existing vector asset.

`ArtSource/UI/G/Vector/G-Check-Surface-v002.svg` renders to its 776x226 export with
the pinned development-only resvg renderer. The helper now accepts explicit
`--revision v002`; default v001 reproduction remains unchanged. A real Unreal
texture commandlet creates `/Game/UI/G/G_CheckReverieV2`, with sRGB UI compression/
group, bilinear filtering, no mips or streaming. V001 source/export/texture and the
earlier generated surface remain intact. Native decoration selects v002, then
v001, then the generated surface, then native fill; all authored revisions use
the existing full UVs/nine-slice slot. Production handlers, text, separate star,
pointer/keyboard behavior, scoring and fixtures are unchanged.

```powershell
python Tools/AssetImport/render_g_check_surface.py --revision v002 --check
python Tools/AssetImport/render_g_check_surface.py --check
```

Git LFS 3.7.1 and its process filter were verified before adding binary artwork.
The real import passes with zero errors/warnings; raw log/report are
`Artifacts/Logs/UI01/check-refinement-import.log` and `check-refinement-import.json`.
The real four-action Editor build passes in 57.20s
(`Artifacts/Logs/Build/WordQuestEditor-20261005-012851.log`). Native dirty preflight
`20261005-013006-capture-initial` passes and its whole screen, Check crop and
original/candidate comparison were inspected. The same eight opaque-face points
used for v001 improve from 9.875 to 7.875 mean absolute channel error. Individual
points do not all improve; this is not a whole-material acceptance metric. The
surface still has simpler bevel/gloss/texture than the reference. Changes are
confined to Check except 964 unchanged Pause/plaque backend pixels at maximum one
color level versus the packaged baseline. The live label/star and other layout
remain intact. Raw diagnostic samples, crops and 50% overlay are under
`Artifacts/QA/UI01/CheckRefinement20261005/`; diagnostics do not become product art.
All 82 Python QA checks, six immutable references, ten staged SVG pairs and both
v001/v002 byte-identical export reproductions pass. Synthetic tests do not replace
native checks. Final clean package and dedicated review are recorded below.

## Missing-art checks

All six dirty-source checks below have native/helper exit zero and complete state/
cue evidence. Held captures also pass the ordered pointer/hover/capture, 200% text,
action-content and cancellation checks. Every PNG was inspected. Owned asset paths
were moved only into a verified ignored holding directory and restored in `finally`;
all three hashes match provenance. No deletion, substitution or fabricated asset
occurred. The negative tests intentionally launch with missing optional art.

| Fallback | Initial 884x1780 | Held Check, 260x640, safe .9, 200% |
|---|---|---|
| v001 (v002 absent) | `20261005-013455-capture-initial` | `20261005-013519-capture-pointerpress` |
| Generated (both authored absent) | `20261005-013542-capture-initial` | `20261005-013604-capture-pointerpress` |
| Native (all three absent) | `20261005-013630-capture-initial` | `20261005-013654-capture-pointerpress` |

V001 and generated initial PNGs are exactly equal in RGB to their prior Editor
captures (`20261004-205213` and `20261004-174307` respectively). The native fill
retains live label/star, held-press feedback and zero submission/evaluation.
Records are `Artifacts/QA/UI01/CheckRefinement20261005/fallback.json` and raw runs.

## Final clean Win64 evidence

Clean runtime source/art is `31e4b5d72cd8c0f36573874c133d5f26755ff164`. The complete
Win64 Development archive is `Artifacts/Packages/Win64/20261005-014044-332374`,
manifest SHA-256
`8bdc092738ee6a0dc9083ae5b3eafc3e1f1399ee23a5a316a8788d2c970990b9`.
BuildCookRun passes in 159.43s, with full cook 521 packages, zero errors/warnings,
all stages exit zero and unchanged clean head/worktree/inputs. All 49 archived
payload sizes/hashes verify before every native launch. Automatic exact archived
executable firewall coverage passes on attempt one at 01:43:48.1168607 UTC,
2026-10-05, Private/Public LocalSubnet. No policy, ACL or task configuration changes.

All fourteen captures below have native/helper exit zero, complete evidence,
matching clean source/package identity, verified manifest/payload hashes and
expected dimensions. Every applicable state, cue, feedback, keyboard/focus,
pointer/held-capture/cleanup, text-size and action-content check passes. No native
Error/Fatal lines were found. Every PNG was inspected; the 1768x3560 full-screen
preview was displayed at reduced resolution, while the recorded PNG dimensions
and hash retain the original capture. Runs below live under `Artifacts/QA/UI01/`
and end in `-packaged-capture-<mode>`, with `native.png`, raw log and `run.json`.

| Run prefix | Mode | Viewport / adaptation |
|---|---|---|
| `20261005-014353` | initial | 884x1780, safe 1 |
| `20261005-014406` | initial | 1768x3560, safe 1 |
| `20261005-014418` | initial | 390x844, safe .9 |
| `20261005-014429` | initial | 390x844, safe .9, 200% |
| `20261005-014439` | pointerpress | 260x640, safe .9, 200% |
| `20261005-014450` | pointerhover | 390x844, safe .9 |
| `20261005-014503` | initial | 844x390, safe .9 |
| `20261005-014514` | correct | 884x1780, safe 1 |
| `20261005-014526` | wrong | 390x844, safe .9 |
| `20261005-014537` | hint / assisted correct | 390x844, safe .9 |
| `20261005-014548` | empty Check | 884x1780, safe 1 |
| `20261005-014600` | keydisabled | 390x844, safe .9 |
| `20261005-014611` | pointerclick | 390x844, safe .9 |
| `20261005-014627` | pointerresumed | 260x640, safe .9, 200% |

Held Check retains its live label/star and navy press outline without submission;
hover retains the gold outline. Wrong/assisted-correct feedback keeps non-color
markers and disabled controls, and native routed release evaluates once. Pause
blocks underlying pointer input and Resume preserves the unsubmitted choice.
At enlarged/narrow/landscape sizes, reading still requires scrolling and some
words wrap; no claim is made that every control/text is visible in initial PNGs.
These are synthetic desktop checks, not manual/touch/platform accessibility.

IoStore lists the genuine cooked `/Game/UI/G/G_CheckReverieV2.uasset`. All ten
SVGs extracted from the loose-file PAK match staged bytes; the PAK/UTOC hashes
remain unchanged by inspection. Both real Unreal Context tests pass at matching
clean source in `20261005-014647-automation-initial`, exit zero, no failed/not-run/
in-process tests. Python evidence is `Artifacts/Logs/UI01/check-refinement-python-checks.log`.
The batch, package, native logs, IoStore CSV, extraction, comparison and validation
records are under `Artifacts/QA/UI01/CheckRefinement20261005/`.

Against PR #44's clean packaged baseline, 39,116 changed RGB pixels are confined
to Check [399,1451,787,1564); zero change elsewhere. The reference-sized final
matches the Editor Check exactly; 964 unchanged Pause/plaque backend pixels vary
at most one channel level, so full Editor/package PNG identity is not claimed.
The fixed eight-point face error remains 9.875 before and 7.875 after in the actual
package. Original/baseline/final diagnostic crops and 50% overlay were inspected.
This supports a local color improvement and bounded change, not full bevel/gold/
texture/type fidelity or acceptance of existing differences. V001 SVG/PNG/asset
and generated fallback hashes remain intact. No supplied reference changed.

Evidence/review/publication updates are documentation only; tested runtime remains
`31e4b5d`.

## Internal review

Dedicated read-only Codex review in `Artifacts/Reviews/20261005-015202` completes
with exit zero against actual `origin/dev` base
`8f51a158a86f136999223d4340591ba21a3e8133`, clean reviewed head
`b6234d0f6d63f2a5b683d203f40afd091874156d`. Head/worktree remain unchanged during
review. No actionable introduced defects were found. The reviewer confirms the
fallback/cooking support, provenance hashes, LFS attributes, reference integrity
and diff whitespace; Unreal builds, runtime/device checks were not independently
rerun. Review does not accept material differences or authorize an owner merge.
Subsequent review/publication commits are docs only.
[PR #45](https://github.com/rloterh/WordQuest/pull/45) was owner-merged into `dev`
on 2026-10-05 at 02:00:45 UTC (`b0d3b24`). The implementation/review helper did not
merge it; merging does not pass the recorded open gates.

Full UI01 art/type/material fidelity, UI02 motion, manual/platform accessibility,
draft-content editorial approval, Android/phone, isolated offline, performance
and original release gates remain open. No later milestone, deployment, release
or implementation-agent merge is performed.
