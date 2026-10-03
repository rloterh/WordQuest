# G reading-panel proportions

The owner merged PR #29 into `dev` at `4ed600b` on 2026-10-03,
03:18:03 UTC. This bounded UI01 correction changes the native placement of
the existing unapproved panel candidate. Its former 160px top slice visibly
flattened the arch, raised the shoulders and compressed the purple star.
The 100px bottom slice also flattened the lower corners.

At reference width, fixed top/bottom slice heights now use 220/130px. UV cuts
remain 0–22%, 22–88% and 88–100%; only the middle surface stretches with reading
content. Lower padding increases from 62 to 80px to compensate for the larger
bottom slice's transparent gutter. Text, controls, scroll behavior and panel
width/top origin are unchanged. The preserved RGBA master and Unreal texture
are not edited or reimported. This improves placement; it does not accept the
candidate's generated contour, rim, material or edge fringe.

## Preliminary checks

The first native preflight (`Artifacts/QA/UI01/20261003-032714-capture-initial`)
uses the edited source on dirty `4ed600b`, initially with 74px lower padding.
Native exit, state, cue and dimension checks pass. The actual 884x1780 capture
was inspected alongside the immutable reference and earlier packaged baseline
`20261002-221808-packaged-capture-initial`. Diagnostic top/bottom crops reveal
the taller arch and less compressed corners. The lower rim was still roughly
6px high, so final lower padding is 80px. That adjustment requires fresh builds
and final packaged comparison; this preliminary capture is not final evidence.

The preliminary real Editor/Game builds compiled `ContextScreen.cpp` and exited
zero (45.91s and 110.95s). All 63 existing Python QA tests, six supplied-reference
hashes and seven runtime SVG parity checks pass. Git LFS 3.7.1 and its process
filter are configured. No binary assets are changed.

## Final clean verification

At clean source `5e915a4fb106b9df3c061dbf215ed220b1061c5e`, the final Editor
and Game targets compiled `ContextScreen.cpp` and passed (50.68s and 60.28s).
Full Win64 BuildCookRun passed in 272.11s. Archive:
`Artifacts/Packages/Win64/20261003-033154-733323`. Its manifest records exit 0,
complete evidence, empty starting worktree and unchanged head/worktree/inputs.
All 48 archived file hashes were verified before every packaged capture.
Manifest SHA-256:
`728d1a8d5e7cca9cf16442191ecff8df109328d96fa590f49b5c03cb57afec11`.

All nine final captures below passed helper/native exit, dimension, state and
applicable cue/focus/text checks. Each actual PNG was directly inspected; their
logs contain no Error/Fatal lines. All runs live under `Artifacts/QA/UI01` on
2026-10-03. The responsive cases simulate a 0.9 safe-area ratio.

| Run suffix | Native view | Observed behavior |
|---|---|---|
| `033801-packaged-capture-initial` | 884x1780 | Taller arch, shoulders and lower rim; live initial controls |
| `033825-packaged-capture-correct` | 884x1780 | Feedback extends the middle panel; bottom corners remain separate |
| `033840-packaged-capture-initial` | 260x640 | Narrow text reflows; lower actions remain in the scrollable content |
| `033853-packaged-capture-initial` | 844x390 | Compact hero; reading panel continues below the viewport |
| `033908-packaged-capture-large` | 390x844 | 200% reading wraps and scrolls |
| `033922-packaged-capture-longfocus` | 390x844 | 200% long answer and focused B remain readable in scrolling content |
| `033935-packaged-capture-longselectedfocus` | 260x640 | Narrow long selected B retains letter, marker and focus |
| `033949-packaged-capture-keyretry` | 390x844 | Synthetic native retry/text-size/focus route passes |
| `034002-packaged-capture-modalcycle` | 260x200 | Tiny Pause modal reveals focused retry through its own scroll box |

These are synthetic native checks, not manual keyboard, touch, OS lifecycle or
platform accessibility acceptance. Batch commands/results:
`panel-proportions-batch.py` / `.json`; integrity summary:
`panel-proportions-verification.json`. Both Unreal Context automation tests passed
at the same clean source in `20261003-034123-automation-initial` (failed/notRun/
inProcess 0, native exit 0, evidence complete). All 63 Python QA tests, six
reference hashes and seven SVG parity checks also pass; raw logs use the
`panel-proportions-` prefix under the same QA directory.

Preserved source PNG SHA-256:
`5e39bbce0ef071997628880668e245cc53087a195d74a6c745c385a760360742`.
Preserved Unreal panel asset SHA-256:
`514fa3c92941d5378ed26615c82ecde5bb51d1eec27197b1465911921cb3b5f8`.
Both match `origin/dev` LFS object IDs. The earlier packaged baseline's
`389455c8` source/art/content trees match merged `4ed600b`; this comparison reuses
its recorded captures rather than claiming a fresh baseline run.

## Native reference comparison

`panel-proportions-analysis.py` / `.json` compare actual initial/correct PNGs
against the prior packaged captures. Initial: 470,299 changed pixels, bounding
box `[47,510,836,1648)`, none outside panel region `[47,509,837,1650)`.
Correct: 790,927 changed pixels, bounding box `[47,510,836,1768)`, none outside
the feedback-extended panel region `[47,509,837,1780)`. The first diagnostic
incorrectly applied the initial view's 1650px limit to feedback; it rejected
64,687 expected lower-panel pixels. The corrected state-specific region passes.
This is a diagnostic correction, not a failed native check or a source fix.

Final initial PNG SHA-256:
`94298c76e06b6eb716c44f8b23faa439be817b79b3fd9a3bffb80287613708c8`.
Final correct PNG SHA-256:
`b3b53705a261fceca491eaf1afcea7872c0d5e1221e8b81d0b129c405b259068`.

Original/native top and bottom diagnostic crops and the full 50% comparison
`panel-proportions-half-opacity-diagnostic.png` were directly inspected. Input
bytes remain unchanged. The apex and lower rim are closer to the original;
shoulders remain slightly high, the star wider, and the generated gold rim
brighter/thicker with different fringe. Letter widths, companion identity and
control skins still diverge. No pixel count establishes visual acceptance.

## Remaining verification and gates

Dedicated read-only review is pending. The panel remains unapproved art; companion identity,
typography, answer/action materials and full UI01 fidelity remain unresolved.
No editorial, UI02 motion, manual accessibility, OS-interruption, network-isolated
offline or physical-phone acceptance follows from this source change.
The Android engine receipt remains absent and adb lists no device on 2026-10-03.
