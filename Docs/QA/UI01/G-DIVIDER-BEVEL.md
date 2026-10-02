# G divider bevel candidates

Following owner-merged #18 (`c8c0dd3`), this bounded UI01 increment refines the
two gold dividers' flat line/star finish relative to the immutable original.
New editable v002 masters preserve v001 path coordinates and 214x29/314x29
canvases. Gold gradients, a thin star rim and ivory/darker facets give directional
material shading. Native placement, reading allocations and runtime filenames
are unchanged. Exact line weight/taper, star geometry and lighting remain candidates;
this is not original-pixel extraction or static fidelity acceptance.

The two previous masters remain unchanged. The staging helper uses v002 and
validates exact bytes; four narrow LF attributes protect revised master/runtime
pairs across checkout platforms. Adjacent `G-Divider-v002-PROVENANCE.json` records
paths, hashes, immutable reference and disposition. No new raster/binary/font,
generated Unreal file, C++, learning fixture, scoring or motion change occurs.
Decorative accessibility and missing-resource paths are unchanged; no service or
physical-input acceptance is inferred from that source identity.

Preliminary dirty native `20261002-113334-capture-initial` (884x1780) exits 0
and passes unselected state/dimensions. Direct inspection against original and
the previous packaged baseline shows shaded lines/faceted stars without reading
movement. Metadata records the dirty worktree and optional tooltip suppression.
Real editor warm check passes (zero actions, 1.30 seconds, exit 0), log
`Artifacts/Logs/Build/WordQuestEditor-20261002-113333.log`. All 27 existing Python
tests and six original-reference hashes pass; Git LFS is available.

## Final clean verification

Implementation source: `55ce793a6e43a3e4443480560419fa19823f84b8`, clean worktree.
Both real targets pass their warm checks: editor zero actions, 1.71 seconds;
Game zero actions, 1.18 seconds. Full Win64 cook/stage/archive passes, UAT
56.77 seconds, exit 0. Package:
`Artifacts/Packages/Win64/20261002-113646-719209`. Head/worktree/input invariants
pass; all 48 recorded archive payloads were verified before each launch. Manifest
SHA-256: `6289b6a95de4695d96fa8e8f64882fe2f68d662635cd3730940213832ea5bbb5`.

UnrealPak extraction exits 0; both cooked divider bytes match master/runtime
hashes in the source provenance. Raw extraction:
`DividerExtract.log` / `DividerExtract.json` in the package directory. XML
inspection confirms the six path coordinates and root attributes are identical
between each v001/v002 pair. Previous masters, all other SVGs, C++, generated
project files and supplied references are unchanged. All seven source/runtime
pairs, six original-reference hashes, 27 existing Python tests and whitespace
checks pass. No new binary asset is committed.

All eight packaged runs below exit 0 and pass state/dimension contracts at clean
source/package identity. All eight PNGs were directly inspected. Raw batch evidence:
`Artifacts/QA/UI01/G-Divider-Bevel-Batch.json`.

| Run under `Artifacts/QA/UI01` | Inspected result |
| --- | --- |
| `20261002-113955-packaged-capture-initial` | 884x1780; shaded lines and faceted stars in existing reading positions; original/baseline compared directly. |
| `20261002-114006-packaged-capture-pausefocus` | 260x640, simulated 0.9 inset; divider decoration remains separate from live text and focused Pause. |
| `20261002-114016-packaged-capture-large` | 390x844, 0.9 inset; 200% text wraps/scrolls, dividers follow measured rows. |
| `20261002-114025-packaged-capture-initial` | 844x390; compact hero/header divider preserved, further reading requires scrolling. |
| `20261002-114035-packaged-capture-longfocus` | 844x390, 200%; oversized B badge/first line visible, leading-content gate passes. |
| `20261002-114044-packaged-capture-longselectedfocus` | Same stress size; selected B badge/marker/first line visible, leading-content gate passes. |
| `20261002-114054-packaged-capture-keydisabled` | 390x844, 0.9 inset; native key/state/focus/final Pause visibility contracts pass. |
| `20261002-114103-packaged-capture-hint` | 390x844, 0.9 inset; assisted correct state, disabled controls and scrollable feedback start retained. |

Comparison captures use optional `--no-tooltips`; `keydisabled` retains ordinary
tooltip behavior. These are native/programmatic checks, not OS/manual input or
screen-reader acceptance. Both existing context tests pass with zero failures/not
run, exit 0, in `20261002-114112-automation-initial/Report`.

Read-only RGB comparison with the prior normal packaged capture
`20261002-110711-packaged-capture-initial` finds 1,390 changed pixels, all inside
the two divider regions. Combined changed bounds are x285..599/y647..918
(exclusive right/bottom); zero changed pixels outside the separate header
x335..549/y640..680 and reading x285..599/y880..930 regions. This establishes
change isolation, not original-reference fidelity acceptance. Evidence:
`Artifacts/QA/UI01/G-Divider-Bevel-Comparison.json`. The existing comparison helper
created `g-divider-bevel-comparison.html` with unchanged embedded PNGs and an
adjustable 50% overlay. Browser/overlay interaction is unverified; earlier local-
navigation blocks were not bypassed.

Dedicated read-only Codex review completed at clean
`5185af7a839cbe69fab9910c229c78e6091fa281` against actual `origin/dev`,
`c8c0dd382b94019c36fb66f2df788d5f7d817724`, exit 0 and no actionable introduced
defects. Head/worktree remained unchanged. Raw evidence:
`Artifacts/Reviews/20261002-114527`. It verified SVG parity, original references
and whitespace; it did not rerun engine, packaging or device checks. Subsequent
review/publication records change documentation only; packaged runtime bytes
remain unchanged. Raw evidence stays ignored under `Artifacts`.
[PR #19](https://github.com/rloterh/WordQuest/pull/19) is published as a regular
PR against `dev`, ready for the owner's merge decision. GitHub has no configured
status checks; the local verification above supplies its recorded evidence.
Static art fidelity, manual/platform accessibility, editorial fixture review,
phone/offline, performance, UI02 motion and release gates remain open.
