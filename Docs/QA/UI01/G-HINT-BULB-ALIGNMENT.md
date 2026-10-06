# G Hint bulb alignment

PR #51 is owner-merged into `dev` at `10110a1` on 2026-10-06, 23:31:36 UTC.
This bounded UI01 correction measures the separate Hint bulb against the original
G gameplay image. The initial diagnostic considered the action row; measured live
label centers are within one pixel while the bulb is 5.5px high and 2px wide.
The change therefore refines only that icon's authored geometry.

## Source and diagnostic limits

`ArtSource/UI/G/Vector/G-Hint-Bulb-v002.svg` preserves the 40x56 canvas and navy
rounded outline with two base bars. It lowers the silhouette five source units,
narrows/shifts the head left and increases stroke width from 2.8 to 3.4. V001
stays unchanged. The existing staging helper selects v002; targeted LF attributes
keep master/runtime bytes identical across checkouts. No new native code, binary
asset, font, fixture, hit area or input handler is included. Missing optional SVG
continues to collapse its decoration and gap while retaining the live Hint label.

Provenance: `ArtSource/UI/G/Vector/G-Hint-Bulb-v002-PROVENANCE.json`.
Master and staged SHA-256:
`88a9b612b8389587b5dc1b9350483720193c3f1d543a290db62b09c70cfe4a57`.
Preserved v001 SHA-256:
`4d191fffb3384d3ade4a9471667a9a8d176a89ecdcd0c8c270560f4f617e86da`.
There is no imagegen, raster editing or original-reference pixel extraction.

Read-only diagnostic region [176,1475,222,1545), threshold R<65/G<60/B<125:

| Image | Opaque ink bounds, half-open | Size | Center | Threshold pixels |
|---|---|---|---|---|
| Original | [182,1487,214,1536) | 32x49 | (198,1511.5) | 366 |
| Prior native | [182,1482,216,1530) | 34x48 | (199,1506) | 288 |
| Candidate Editor | [182,1487,214,1535) | 32x48 | (198,1511) | 382 |

These threshold-dependent antialiased bounds do not identify an exact silhouette,
prove no clipping, measure contrast or accept global fidelity. A half-pixel center
and one-pixel height difference remain. The original's contour/shading, shared
surface/rim placement, live type shape and Check star remain imperfect. Hint/Check
label and star diagnostic bounds remain unchanged. The full Editor pixel diff
against the prior final Editor capture lies in [181,1481,217,1536), wholly within
the bulb region. Captures/crops/overlay are diagnostics, not product artwork.

## Initial checks

Real UE 5.8.2 Editor target succeeds (up-to-date), 2.45 seconds, exit zero:
`Artifacts/Logs/Build/WordQuestEditor-20261006-233504.log`.
All 96 existing Python QA tests, six immutable references and ten staged SVG
parity pairs pass. Git LFS 3.7.1 is verified; this change adds only text assets.

Dirty native preflight `20261006-233515-capture-initial` completes at 884x1780,
100% text with native/helper exit zero and expected unselected state/cues.
The full screen and matched action crops are inspected against the original.

Two missing-SVG checks deliberately move only the owned runtime icon into an
absolute-path-verified ignored holding folder and restore it in `finally`:

| Run under `Artifacts/QA/UI01/` | Observation |
|---|---|
| `20261006-233735-capture-initial` | 884x1780, 100%, live centered Hint label, no bulb/gap |
| `20261006-233818-capture-actions` | 260x640, intrinsic 200%, safe-zone 0.9, both stacked labels fit and Check focus remains visible |

Both native/helper exits are zero, applicable state/cue/layout/focus/action-content
checks pass and both PNGs are inspected. The SVG is restored to its unchanged
v002 hash and all ten parity pairs pass again. These are dirty-source omission
checks, not tests of a damaged package or a phone.

To leave headroom above the existing Zen low-disk threshold before packaging,
native lossless NTFS compression is applied only to EXE/PDB staging copies from
the two known successful #49/#50 runs. All four logical hashes and matching archive
hashes verify before compression; all four staged hashes verify afterward.
Free space rises from 4,129,988,608 to 5,071,265,792 bytes. Archives are unchanged;
no files are deleted or moved, and no machine policy changes. Raw report is
`Artifacts/QA/UI01/ActionAlignment20261006/stage-compression.json`.

## Final verification and gates

Clean package/runtime evidence and dedicated review against actual `dev` follow
before publication. Raw scripts/logs/metrics remain ignored under
`Artifacts/QA/UI01/ActionAlignment20261006/`.
Full UI01 fidelity, UI02 motion, manual/platform accessibility, draft-fixture
editorial approval, Android/physical-phone, isolated offline, performance and
original release gates remain open. The owner retains merge decisions; there is
no deployment, release or later milestone work.
