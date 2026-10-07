# G Check star facets

PR #52 is owner-merged into `dev` at `ea8fb8e` on 2026-10-06, 23:59:23 UTC.
This bounded UI01 correction returns to the separate Check star. The original G
ornament has white/lilac/gold directional faces and a violet center; the current
v001 reconstruction has a broad continuous pale cross.

## Source and diagnostic limits

`ArtSource/UI/G/Vector/G-Check-Star-v002.svg` keeps the 48x48 canvas. It authors a
taller silhouette at (23,26), four directional gradient faces, a violet center,
pale edge highlights and restrained static halo/four small glints. V001 stays
unchanged. The existing staging helper selects v002; targeted LF attributes keep
master/runtime byte parity stable on future checkouts. No new native code, binary
asset, font, fixture, hit area, label layout or input handler is included. There is
no imagegen, raster editing or original-reference pixel extraction. All glints are
static; this is not UI02 motion work.

Provenance: `ArtSource/UI/G/Vector/G-Check-Star-v002-PROVENANCE.json`.
Master/runtime SHA-256:
`4719f4794d3a2a7b5282cf3e11aaca1e7f5f0e5aa74524258301ab79dd7e5e8e`.
Preserved v001 SHA-256:
`1a682d7450e9ba5ce22920f279d6ab8d27f6710756446359c3731b1dfc65c285`.

Read-only region [465,1480,519,1545). White threshold R/G/B>225; warm threshold
R>190, G>150, R>B+10. Measurements depend on opacity, background and antialiasing;
they are not exact outer geometry, contrast or whole-material acceptance.

| Image | White bounds, half-open | White center / pixels | Warm bounds / pixels |
|---|---|---|---|
| Original | [475,1492,507,1527) | (491,1509.5) / 149 | [490,1496,507,1530) / 125 |
| Prior native | [477,1493,507,1523) | (492,1508) / 229 | [475,1491,509,1525) / 138 |
| Final Editor | [474,1491,508,1527) | (491,1509) / 147 | [490,1496,509,1528) / 153 |

White coverage/center approach the reference. Warm coverage does not improve by
pixel count; its placement becomes directional rather than a surrounding gold
cross. The white bounds are still 34x36 versus original 32x35, and the reference's
softer contours, facet colors, glow and small glints remain imperfect. Shared
action surface/rim and live type differences are outside this correction.

## Native preflight and missing icon

Real UE 5.8.2 Editor target succeeds (up-to-date), 5.11 seconds, exit zero:
`Artifacts/Logs/Build/WordQuestEditor-20261007-000245.log`.
All 96 existing Python QA tests, six immutable references and ten source/runtime
SVG parity pairs pass. Git LFS 3.7.1 verifies; only text assets are added here.

First native trial `20261007-000252-capture-initial` completes with native/helper
exit zero. The image is captured before Unreal finishes draining its derived-data
cache on shutdown. The pale right edge is then refined; its original SVG and
metrics remain ignored as `first-trial.svg` and `first-trial-assessment.json`.
Final dirty preflight `20261007-001133-capture-initial` completes at 884x1780,
100% text with native/helper exit zero and expected initial state/cues. Its full
screen, region crop and enlarged diagnostic/50% overlay are inspected against the
original. There are 1,449 changed star-region pixels versus #52's prior package,
plus only the known 964 one-channel Pause/plaque Editor/package backend differences.
Zero pixels change elsewhere. Source PNGs remain unchanged by QA diagnostics.

Two omission runs move only the owned runtime star SVG into an absolute-path-
verified ignored holding folder, restoring it in `finally`:

| Run under `Artifacts/QA/UI01/` | Observation |
|---|---|
| `20261007-001309-capture-initial` | 884x1780, 100%, centered live Check label without star/gap |
| `20261007-001330-capture-actions` | 260x640, intrinsic 200%, safe-zone 0.9, stacked action labels fit and Check focus is visible |

Both native/helper exits are zero and all applicable state/cue/layout/focus/action-
content checks pass. Both PNGs are inspected. The star is restored to its unchanged
v002 hash and all ten parity pairs pass again. These dirty-source checks do not
establish recovery from a damaged package or physical-device acceptance.

For packaging headroom, native lossless NTFS compression is applied only to six
known successful old staging EXE/PDB pairs. All 12 staged and matching archive hashes
verify before compression; all staged hashes verify afterward. Free bytes rise
from 2,878,476,288 to 5,699,891,200. Archives are unchanged; no file deletion/move or
machine policy change occurs. Raw report: `CheckStar20261007/stage-compression.json`.

## Clean packaged verification

Clean source/art head `4f20509567a360d798e4859b850ddf22e16d9158` produces real
Win64 Development archive `Artifacts/Packages/Win64/20261007-001643-063157`.
BuildCookRun succeeds in 83.50 seconds, 522 cooked packages, zero errors/warnings;
native/helper exits zero. Complete manifest records unchanged head/worktree/inputs.
All 49 payload size/hash pairs verify before every packaged launch and again at
completion. Manifest SHA-256:
`1116b6bc9ff1810fed637c73bc31fd6aee9c08cf14d2324f19997cbd7817022d`.
Existing owner-scoped firewall refresh succeeds on attempt two at
00:18:39.0278353 UTC, Private/Public LocalSubnet; policy/task permissions are unchanged.

All nine packaged captures have native/helper exit zero, matching clean source/
package provenance, requested dimensions and all applicable state/cue/layout,
actual text size, action-content, pointer, keyboard and scroll predicates true.
No native Error/Fatal lines occur. All full PNGs are inspected; the 1768x3560
whole-screen view is viewer-resized to 1017x2048.

| Run under `Artifacts/QA/UI01/` | Case | Dimensions / text |
|---|---|---|
| `20261007-001844-packaged-capture-initial` | Frozen comparison | 884x1780 / 100% |
| `20261007-001859-packaged-capture-initial` | Double-size | 1768x3560 / 100% |
| `20261007-001911-packaged-capture-initial` | Phone-shaped initial | 390x844 / 100% |
| `20261007-001922-packaged-capture-actions` | Enlarged stacked controls | 390x844 / intrinsic 200% |
| `20261007-001933-packaged-capture-actions` | Narrow stacked controls | 260x640 / intrinsic 200% |
| `20261007-001945-packaged-capture-pointerpress` | Held virtual Check | 260x640 / 200% |
| `20261007-001956-packaged-capture-pointerclick` | Routed wrong submission/disabled barriers | 390x844 / 200% |
| `20261007-002012-packaged-capture-keysubmit` | Routed keyboard correct submission | 884x1780 / 100% |
| `20261007-002023-packaged-capture-scrollfeedback` | Feedback reading end | 844x390 / intrinsic 200% |

Safe-zone is 1 for reference/double-size/keyboard and 0.9 otherwise; tooltips are
disabled. Stacked action frames expose both full controls. Held Check has native
press/focus feedback without evaluating. Routed pointer/keyboard submit produces
one evaluation and disabled controls; pointer barriers prevent repeated evaluation.
Some reading/held frames leave controls or part of the feedback offscreen; they
do not establish simultaneous visibility of all content. These are Windows
offscreen/synthetic checks, not manual input, platform accessibility or phone evidence.

Both Unreal Context tests succeed with complete clean-source evidence in
`20261007-002035-automation-initial`, zero failed/not-run/in-progress.
The installed UnrealPak's separate `-Extract <directory>` arguments extract only
`G_CheckStar.svg`. Its bytes/hash equal the v002 master and runtime copy, and the
pak manifest hash remains unchanged afterward.

The final reference-size comparison against #52's package changes exactly 1,449
pixels inside the star region and zero elsewhere, bounds [470,1487,513,1532).
Live labels, Hint bulb, both control surfaces, reading layout, wordmark, companion
and background are pixel-identical in this comparison. Initial PNG SHA-256:
`731e01cdaba8178994d441bef3d5c37a1d5052a0820d35cff3d8e55d3dfd1bf7`.
Editor/package differs only at the known 964 Pause/plaque pixels in
[362,38,855,198), maximum channel delta one. Star metrics equal the Editor trial.

Raw scripts/logs/crops/overlays/metrics remain ignored under
`Artifacts/QA/UI01/CheckStar20261007/`: `assessment.json`, `fallback.json`,
`verification.json`, `final-comparison.json`, helper logs and extracted SVG.
Source/art remains the clean tested `4f20509` tree; later commits update documentation.

## Review and remaining gates

Dedicated read-only review against actual `dev` follows before publication.
Full UI01 art/type/material fidelity, UI02 motion, manual/platform accessibility,
draft-fixture editorial approval, Android/physical-phone, isolated offline,
performance and original release gates remain open. The owner retains merge
decisions; no deployment, release or later milestone work is included.
