# G action font weight candidate

After the owner merged PR #13 at `793a192`, this bounded UI01 increment adds a
genuine Bold display face for live Hint/Check labels and the existing display-font
Pause heading. It does not identify or accept the reference's exact typeface.
The original gameplay reference remains the visual target; UI02/H/I remain gated.

## Typography and provenance

The previous runtime composite contained only a `Regular` entry, backed by the
licensed Cormorant Garamond SemiBold (weight 600). Bold display requests therefore
fell back to that primary face, rather than selecting a distinct Bold face. Local
UE 5.8 font-cache source confirms named-face lookup followed by primary-face
fallback (`FontCacheCompositeFont.cpp`, `GetDefaultFontData`). This was not plain
regular weight or faux-bold rendering.

Unmodified Cormorant Garamond Bold (weight 700) comes from the same pinned upstream
revision and unchanged SIL OFL as SemiBold. Exact download, byte/hash and glyph
coverage evidence is in [font provenance](../../../ArtSource/Fonts/CormorantGaramond/PROVENANCE.md).
All characters in current action/disabled/Pause display strings are present.
The original SemiBold file, OFL, outlined wordmark and Roboto learning font are
unchanged. No manufactured bold, glyph editing or raster editing is used.

The runtime composite retains SemiBold as `Regular` and adds the actual Bold face
as `Bold` when available. Existing measured icon/label layout, actions, hit regions,
accessible names, focus, scoring and text-size override are retained. Missing Bold
continues through the existing SemiBold primary-face fallback; missing display
fonts retain the bundled live-text fallback.

Unreal's normal isolated editor imported the new FontFace via
`Tools/AssetImport/import_g_action_font.py` (font import requires Slate). It touches
only `/Game/UI/G/G_DisplayBold`; repeat execution refuses an existing destination
until inspected. Successful import marker/type/paths are recorded in
`Artifacts/Logs/UI01/G-Action-Font-Import-20261002.log` and
`Artifacts/Logs/UI01/action-font-import.json`. The helper's own editor quit after
success; the user's existing editor was not closed.

Generated asset `Game/Content/UI/G/G_DisplayBold.uasset`: 1,043,722 bytes, SHA-256
`6ba0112f8ba8a9b43189feb1cc9762633af35c63808687611abecdcf2e17a7a8`.
Read-only byte inspection finds the full unchanged source font at offset 1398.
Both new TTF and genuine Unreal asset use the configured Git LFS filter; existing
UI assets and engine-generated project/module/target files remain unchanged.

## Preliminary native comparison

Real editor compilation passed (6 actions, 31.35 seconds, exit 0):
`Artifacts/Logs/Build/WordQuestEditor-20261002-045657.log`.
Baseline packaged `20261002-044908-packaged-capture-initial` and dirty candidate
editor `20261002-045850-capture-initial` both produce 884x1780 PNGs with initial
unselected/unevaluated state and exit 0. Direct native/reference inspection shows
stronger action stems, closer to the reference's heavy serif action labels,
without moving the reading or controls. This is an implementation judgment, not
owner fidelity acceptance; glyph shape/font identity and finish still differ.

Read-only native PNG analysis finds 1,877 changed RGB pixels, all within
x239..723/y1491..1532, confined to the two action labels. Outside that union the
two RGB captures are identical. Core glyph pixel counts in the documented label
regions rise from 309 to 384 for navy Hint and 672 to 807 for white Check. These
counts demonstrate the rendered weight change; they are not contrast or global
fidelity scores. Regions, thresholds and capture hashes are retained in
`Artifacts/QA/UI01/G-Action-Font-Weight-Comparison.json`.
Baseline metadata records the prior merged package and only a
status-document worktree edit; candidate metadata records the new source/assets.

Missing-Bold fallback passed in dirty editor run
`20261002-050053-capture-actionfocus` at 260x640 with simulated 0.9 inset. Only the
new owned `G_DisplayBold.uasset` was temporarily moved within the workspace;
`fallback-context.json` records the omission/restoration. Native inspection shows
both live labels and Check focus intact, with initial unselected/unevaluated state,
correct PNG dimensions and exit 0. The log confirms the missing Bold package and
loaded SemiBold primary face. The asset was restored in `finally`, with its exact
original SHA-256 verified. This is an editor omission test, not packaged corruption
or phone evidence.

## Clean cooked verification

Clean runtime/source commit `c15ddfddf1b55f591d338f7212afb2c685a349f7` passes
the real editor target and Win64 Development game build, full cook, stage and
archive. Package evidence is
`Artifacts/Packages/Win64/20261002-050446-409607`; editor and UAT exits are 0,
and head, worktree and recorded inputs remain unchanged. The game build performed
five actions in 25.92 seconds; UAT completed in 86.00 seconds. Manifest SHA-256:
`21f9c153b8b567e83a7bc68abea1e04344e93a0ac79fbf36c6bf2fec399ed1e9`.

UnrealPak successfully extracts `G_DisplayBold.ufont` from the archive (exit 0).
The cooked file is 1,042,276 bytes with SHA-256
`421cf02a61822a29d3500dae3f2df3dedf2319e7b1cda777dc04afb86dd7e6d2`.
Its full 1,042,268-byte source TTF payload matches exactly at offset 4. UE's
`UFontFace::CookAdditionalFilesOverride` / `FFontFaceData::Serialize` write the
font-data array and preprocessed-geometry array: the additional bytes are a
four-byte payload count and trailing zero array count, not a changed TTF.
`CookedBoldFont.json` and `FontExtractCorrected.log` retain this evidence.
An initial `-Extract=dir` attempt exited 1 and refused the existing pak; corrected
`-Extract dir` exited 0. The pak still matches its original manifest hash.
Packaged native logs confirm loading `Content/UI/G/G_DisplayBold.ufont`, rather
than an external ArtSource font. Existing `/Game/UI/G` cook inclusion suffices.

All seven final packaged captures use that clean commit/package and verified
payload hashes. Each exits 0, passes state/dimension checks and was directly
inspected; raw runs live under `Artifacts/QA/UI01/`:

| Run | Window | Inspected state |
| --- | --- | --- |
| `20261002-050724-packaged-capture-initial` | 884x1780 | Normal, unselected live action labels |
| `20261002-050734-packaged-capture-actions` | 390x844 | 200% reading, focused Check |
| `20261002-050743-packaged-capture-hint` | 390x844 | Assisted correct A; disabled Hint/Check labels |
| `20261002-050753-packaged-capture-keymodal` | 390x844 | Pause heading, 200% TextSize focus |
| `20261002-050802-packaged-capture-keytab` | 390x844 | Enabled-control cycle, final Hint focus |
| `20261002-050812-packaged-capture-actionfocus` | 260x640 | Narrow stacked live actions, focused Check |
| `20261002-050821-packaged-capture-actions` | 844x390 | 200% reading, landscape focused Check |

The 390x844/260x640 runs use a simulated 0.9 safe-area inset; this is not phone
safe-area evidence. Native keymodal/keytab traces also pass per-key state, focus,
settings and final focused-control visibility checks. They dispatch synthetic
Slate events and do not establish physical keyboard or screen-reader acceptance.
Native labels remain live and readable within their action groups in these
captures; scrolling and unfinished art remain as documented in earlier proofs.

Both existing Unreal tests pass (2 succeeded, 0 failed/not-run/in-process,
exit 0) at the same clean source commit:
`20261002-050830-automation-initial`. All 22 existing Python tests, six reference
hashes, six SVG source/runtime pairs and LFS/diff checks pass. Raw artifacts
remain local and ignored; no physical-device or art gate is passed.

## Internal review

Dedicated Codex read-only review completed against actual `origin/dev` base
`793a1924d6b31a85fae4c74148aa6ab4b3c32ad8`, reviewing clean head
`6267858c759faeb4816355db89482ad13e19748d`. Exit 0, unchanged head/worktree and
no actionable introduced defects. Raw report and metadata are retained in
`Artifacts/Reviews/20261002-051631`. The review checked the fallback, cook
inclusion, provenance and scope disclosures; it did not rerun builds/runtime
tests. Later commits record review/publication only, with no runtime changes.

## Remaining gates

Exact type/font identification, art identity/fringe/finish, fixture approval,
manual/platform input and screen-reader, Android tooling/phone, offline isolation,
performance, UI02 motion and release acceptance remain open. The prototype is still
one draft EQUIVOCAL question; the displayed `3 / 7` is a fixture, not campaign data.
