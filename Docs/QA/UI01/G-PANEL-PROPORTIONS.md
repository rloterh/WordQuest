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

## Remaining verification and gates

Final clean packaging, responsive native captures, Unreal automation and dedicated
read-only review are pending. The panel remains unapproved art; companion identity,
typography, answer/action materials and full UI01 fidelity remain unresolved.
No editorial, UI02 motion, manual accessibility, OS-interruption, network-isolated
offline or physical-phone acceptance follows from this source change.
