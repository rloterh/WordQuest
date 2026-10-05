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
native checks. Clean package and dedicated review are pending.

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

Full UI01 art/type/material fidelity, UI02 motion, manual/platform accessibility,
draft-content editorial approval, Android/phone, isolated offline, performance
and original release gates remain open. No later milestone, deployment, release
or implementation-agent merge is performed.
