# Static G companion from original pixels

PR #39 is merged at `51b6241`. The owner explicitly requested a retry and permitted
a better alternative if built-in imagegen was unsuitable. No permission/approval
block prevented generation. The exact-pixel diagnostic crop (72,266)-(300,471)
made the small reference character clearer without replacing the immutable original.

## Retry and corrected assessment

Built-in imagegen background-removal edit used only that inspected 228x205 crop.
It still redrew character details/proportions and left stray alpha pixels; it is
discarded, not imported or adopted as the target. Exact prompt/output provenance
is in `ArtSource/Companions/G/Reconstruction/G-Spirit-Retry-20261004-PROMPTS.md`.
Close-up inspection also shows that the original already contains substantial gold
banding and a tiny pink mouth detail. Earlier "thin circlet/no tongue" constraints
were too restrictive; those features alone are not introduced defects. The original
character, not an idealized description or previous generated output, is authoritative.

## Source-based static alternative

The owner's alternative authorization is used for a deterministic original-pixel
cutout, with a hand-traced editable SVG mask and pinned resvg renderer. No character
RGB paintover, generative reconstruction or resolution enhancement occurs in this
selected candidate. `SourcePixels/G-Spirit-Reference-Detail-v001.png` is a new working
crop under `ArtSource/Companions/G`, pixel-identical to the original region; the supplied
reference is unchanged. The three named mask paths are editable static alpha shapes
(body, top wisp, lantern), with a .35-source-pixel Gaussian edge feather.
They are not three separately reconstructed animation layers: the body region still
contains visible lantern pixels and hidden body art has not been painted. Do not
animate those masks independently or add a second companion over this one.

The 228x205 RGBA export has zero corner alpha, extrema 0..255 and nonzero-alpha
bounding box [9,12,200,200). All 10,821 fully opaque pixels are exactly equal in RGB
to their original x+72/y+266 pixels. This establishes retained source integrity, not
exact alpha recovery or full visual acceptance. Source wisps already contain baked
scene color/translucency; a traced mask cannot recover unknown foreground/background
components. Light/dark QA composites were inspected. Tight contour choices, fringe,
source softness and high-resolution quality still require art review. The source
resolution is unchanged; no new high-resolution detail or layered master is claimed.

Reproduce with `python Tools/AssetImport/render_g_reference_spirit.py --check` using
development-only resvg-py 0.5.0 / resvg 0.48.1 already used by the panel renderer.
Exact source/mask/export/import hashes and limits are recorded in adjacent provenance.
The genuine Unreal Python texture import sets sRGB, UI group, editor-icon compression,
bilinear filtering, no mips and never-stream. New texture: `/Game/UI/G/G_SpiritReference`.
The previous `G_Spirit` and its v001 source remain unchanged; original reference hashes
and all eight raw SVG resources are preserved. Binary art has one writer and LFS.

Native placement draws the full export at x72/y266, 228x205 reference units, including
transparent crop margins; this preserves source coordinate mapping and aspect ratio.
Missing candidate retains the previous framed texture and its exact containment path.
Compact hero/landscape hiding, responsive scale, live controls, scoring and draft
fixtures remain unchanged. This is a single static companion, not UI02 motion.

## Verification in progress

Genuine import exits 0 with zero errors/warnings and completion marker:
`Artifacts/Logs/UI01/reference-spirit-import.log` and adjacent JSON.
Editor compilation succeeds in six actions, 31.15 seconds;
`Artifacts/Logs/Build/WordQuestEditor-20261004-140241.log`.
All 67 Python QA checks, eight staged SVG pairs, six immutable reference hashes and
byte-exact PNG reproduction pass. Read-only source integrity and mask diagnostic
evidence are under `Artifacts/QA/UI01/SpiritRetry20261004`.
Dirty native preflight `20261004-140649-capture-initial` exits 0 at 884x1780,
initial state and option cues pass. The PNG and close-up were inspected against
the immutable original and PR #39's packaged baseline. Its 10,821 fully opaque
mask-corresponding pixels match the original RGB exactly at native coordinates;
mean absolute channel difference is 0.00 versus 42.30 for the earlier generated
companion at those same points. This is an interior correspondence check selected
by the mask, not a global fidelity/edge/alpha score. Comparison changes 20,250 pixels,
bounds [81,277,284,466), zero outside the crop region [72,266,300,471).
The prior larger generated face/lantern is removed; no second companion is added.
Final initial preflight PNG SHA-256:
`367a687da0de98c66ac9d745490d6b82afa80423555ebd553441d45effcacace`.
Raw comparison and reference/baseline/final crops:
`Artifacts/QA/UI01/SpiritRetry20261004/preflight-comparison.json`.
Omission fallback exits 0 with complete native checks in
`20261004-141220-capture-initial` (884x1780) and
`20261004-141239-capture-initial` (390x844, .9 simulated safe area, 200% text).
Both PNGs were inspected: the previous framed companion returns, enlarged reading
reflows/scrolls with live controls. The reference-sized fallback RGB is identical
over the entire screen to PR #39's initial baseline. The new owned texture was
temporarily moved into ignored QA storage and restored in `finally` with exact
SHA-256; source/old texture remained untouched. Raw metadata:
`Artifacts/QA/UI01/SpiritRetry20261004/fallback.json`.
## Clean package and runtime checks

Tested source: clean `0d529822b3d913765c81b5aecd78a36639c71e59`.
Full Win64 Development package passes at
`Artifacts/Packages/Win64/20261004-142310-186663`: warm Editor check (zero actions,
1.82 seconds), fresh Game compilation/link/metadata (five actions, 43.87 seconds),
519-package cook with zero errors/warnings, stage/archive and BuildCookRun 120.37
seconds, all exits 0. Head/worktree/input invariants and all 49 archive size/hash
checks pass. Manifest SHA-256:
`58caf6c61e2973557982045aeeca9b6e2c4b56a9c14608f48f5ed67a9ef8d924`.
Existing automatic firewall task covers the exact new packaged executable at
14:25:30.9979590 UTC on its second bounded invocation; no security policy or
privileged installer changes occur here.

Every native run below records clean matching source/package identity, verified
archive hashes, exit 0 and complete requested dimension/state/cue checks. Every
PNG was viewed. The high-resolution viewer resized to 1017x2048 for display;
raw dimensions are verified as 1768x3560. Paths are under `Artifacts/QA/UI01`.
Safe-zone .9 is a desktop simulation, not physical-phone evidence.

| Run | Proof | Window / text / safe zone |
| --- | --- | --- |
| `20261004-142630-packaged-capture-initial` | Reference-sized initial | 884x1780 / 100% / 1 |
| `20261004-142642-packaged-capture-initial` | High-resolution initial | 1768x3560 / 100% / 1 |
| `20261004-142653-packaged-capture-initial` | Phone-sized composition | 390x844 / 100% / .9 |
| `20261004-142703-packaged-capture-initial` | Enlarged reading, scrolling | 390x844 / 200% / .9 |
| `20261004-142714-packaged-capture-initial` | Narrow initial, scrollable actions | 260x640 / 100% / .9 |
| `20261004-142725-packaged-capture-initial` | Compact landscape, companion hidden | 844x390 / 100% / .9 |
| `20261004-142735-packaged-capture-selected` | Selected C with separate cues | 884x1780 / 100% / 1 |
| `20261004-142746-packaged-capture-correct` | Disabled options and feedback | 884x1780 / 100% / 1 |
| `20261004-142756-packaged-capture-longselectedfocus` | Long selected B, leading content visible | 260x640 / intrinsic 200% / .9 |
| `20261004-142807-packaged-capture-keymodal` | Synthetic Pause/text-size routing | 390x844 / ends 200% / .9 |

Both Unreal `WordQuest.Context` tests pass, zero failed/not-run/in-process,
exit 0, clean source, in `20261004-142941-automation-initial/Report`.
The final packaged initial PNG matches preflight exactly, including its recorded
SHA-256. Thus the same 10,821 fully opaque interior correspondence and scoped
region comparison hold; uncertain edges are excluded from that assertion.
Original/baseline/final close-ups and the 50% overlay were inspected. Native normal
and simulated phone-sized composition show the retained original face/lantern;
high-resolution inspection shows the disclosed source softness. No opaque export
rectangle or duplicate character is introduced. Mask boundaries/translucent
contamination and independent animation source remain unaccepted.
All three new LFS pointers match their actual source/export/Unreal hashes and sizes.

Raw batch/verification/fallback/source evidence is under
`Artifacts/QA/UI01/SpiritRetry20261004`.

## Dedicated review

Read-only review completed at `Artifacts/Reviews/20261004-143346`, actual
`origin/dev` base `51b62411a75e8e4a1320ec6ac128d0097eb3363a`, reviewed head
`8a6614f02f86c1874bdc579a5c24dd19d6fd44d7`. Starting worktree was clean,
exit 0, head/worktree unchanged. No actionable introduced defects were found.
All six original-reference checks passed independently. The review's optional
export reproduction could not read ignored
`Artifacts/Tools/resvg/resvg_py/__init__.py` (PermissionError); this is a review
environment limitation, not a successful independent reproduction. No review
permission/sandbox bypass was attempted. Main-session `--check` passed byte-exact
again after that report. Engine builds/runtime/device checks were not independently
rerun by the reviewer. Subsequent evidence/review/publication documentation does
not change tested runtime source `0d52982`. The owner retains merge authority.
Non-draft [PR #40](https://github.com/rloterh/WordQuest/pull/40) is open against
`dev`; publication adds documentation only after the reviewed head.

## Open gates

Static mask edge/matte acceptance, full UI01 art fidelity, high-resolution editable
companion source, independently reconstructed motion layers/UI02, fixture editorial
approval, manual/platform accessibility, Android/physical phone, isolated offline,
performance and original release gates remain open. Original-pixel retention is not
a phone or release qualification.
