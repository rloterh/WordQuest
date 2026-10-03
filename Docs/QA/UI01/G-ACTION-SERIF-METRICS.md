# G action serif metrics

The owner merged PR #32 into `dev` at `3d76c9f` on 2026-10-03, 08:20:47 UTC.
This bounded UI01 correction measures live Hint/Check lettering against the
immutable original G gameplay image. The reference-size packaged baseline is
`Artifacts/QA/UI01/20261003-054319-packaged-capture-initial`.

## Candidate integration

The existing Cormorant action face is already genuine weight 700. This change
addresses its thin/high-contrast letterforms with unmodified Liberation Serif
Bold 2.1.5, also weight 700. This is a licensed candidate, not identification of
the reference's exact font. Archive/file/license provenance and glyph coverage
are in `ArtSource/Fonts/LiberationSerif/PROVENANCE.md`.

Unreal's initialized isolated editor imports a separate `G_ActionBold` FontFace
through `Tools/AssetImport/import_g_action_serif.py`. The helper verifies its
pinned TTF hash, refuses an existing destination, checks FontFace type and save,
and exits its own editor after logging success. Source/imported assets use LFS.
The existing staged Liberation Fonts OFL license is identical to the new adjacent
license; the package does not need a second identical copy.

The transient action composite copies the engine composite and replaces only
Bold, preserving fallback faces/script routing. Only Hint/Check and their disabled
labels use it. Missing candidate falls back to the existing display composite
and its former 34px size, 20px gaps and zero optical top padding;
brand/Pause/reading faces remain. Candidate reference pixel size is 31, with the
existing minimum size, point rounding and 200% enlargement. Icon/label groups
use 26/14 reference-unit Hint/Check gaps and 3 units of optical top padding;
the same gaps are included in wrap measurement. Groups continue to be measured,
wrapped and stacked by existing layout. No fixture,
scoring, artwork, hit-region or focus behavior is intentionally changed.

## Verification in progress

Matched label regions use navy R<65/G<60/B<125 for Hint and white R/G/B>225 for
Check. Original bounds are Hint 59x24 and Check 188x24; baseline bounds are 62x22
and 191x25. These fixed-region threshold diagnostics depend on generated
antialiasing; they are not exact font identity, contrast or global fidelity scores.
Real Editor compilation passed, six actions in 84.49 seconds, exit 0:
`Artifacts/Logs/Build/WordQuestEditor-20261003-083201.log`.
All 66 Python QA tests, six original reference hashes and seven SVG pairs pass.
Genuine import exited 0 with the completion marker, saved FontFace and no errors;
one existing NVIDIA TSR driver warning is unrelated to import. Raw evidence is
`Artifacts/Logs/UI01/action-serif-import.log`, `.json`, `-process.json` and
`-verification.json`. The 371,537-byte asset SHA-256 is
`202014e98b769b50a57d600ae182298db7ab7acf4c958dc0c2f573bbca1537dd`;
its unchanged full 370,096-byte TTF occurs at offset 1385.

Dirty native preflights `20261003-083525-capture-initial` and
`20261003-083921-capture-initial` passed and were inspected. The latter exposed
excessive 6-unit baseline compensation; final compensation is 3. Actual recompiles
passed four actions in 27.95s and 26.20s, respectively, in
`Artifacts/Logs/Build/WordQuestEditor-20261003-083738.log` and `-084129.log`.
Clean packaged comparison follows; no final fidelity claim is based on these drafts.

Missing-candidate omission tests `20261003-084005-capture-initial` (884x1780)
and `20261003-084021-capture-actions` (390x844, simulated .9 inset, 200%) both
exited 0 with complete evidence. The reference-size fallback PNG is RGB-identical
to the prior merged packaged baseline; the enlarged fallback was inspected with
both live labels and Check focus visible. Expected missing FontFace warnings are
recorded, and the temporarily moved new owned asset was restored with its exact
SHA-256 in `Artifacts/QA/UI01/action-serif-fallback.json`. The later 6-to-3 padding
adjustment affects only the candidate branch; fallback still uses zero top padding.
This is an editor omission test, not package corruption or physical-device evidence.

## Remaining gates

The panel rim/star, companion identity, wordmark and generated surface materials
remain unfinished. Exact art/font fidelity, editorial fixture approval, manual
input/accessibility, Android support and phone evidence, offline isolation,
performance, UI02 motion and release acceptance remain open. Native offscreen
captures and synthetic input do not establish these gates.
