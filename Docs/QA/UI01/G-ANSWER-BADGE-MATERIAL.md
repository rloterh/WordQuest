# G answer badge material candidate

After the owner merged PR #14 at `3312e95`, this bounded UI01 increment adds
an editable shaded disc behind the existing live A–D letters. The original G
reference has a softer blue-lilac fill and pale lower rim than the previous solid
native badges. The original reference remains the visual target; this is a
reconstruction candidate, not accepted final art or a new visual direction.

## Source and native integration

`ArtSource/UI/G/Vector/G-Answer-Badge-v001.svg` is a hand-authored 70x70 vector
disc with explicit percentage-based gradient coordinates. It contains no letter
or learning content. Unchanged runtime copy:
`Game/Content/UI/G/Vector/G_AnswerBadge.svg`; both SHA-256:
`bb6b04596b5dfbdf725c9890fba888880e6e9423a8697efabc6b6ebdc062c8a8`.
The existing staging/parity helper now handles seven resources. Existing masters,
raster sources, Unreal binary assets and all supplied references are unchanged.
No raster editing, original-pixel extraction or image generation was used.

Each existing answer badge size box now contains an overlay: a noninteractive
Slate vector image and the existing native border/live letter. The selected navy
border, `>` selection marker and answer-button outline remain separate state
cues. No correctness cue appears before submission. Missing SVG collapses only
the decoration and restores the original solid fill/edge; selection still works.
The ornament is excluded from hit testing/accessibility; the answer button retains
its semantic label and interaction region. Native screen-reader service acceptance
is unverified.

Existing badge diameter (70 reference pixels, 32-unit minimum), 200% scaling,
letter font, row measurements, focus routing, scoring, draft fixture and actions
are unchanged. `/Game/UI/G` cook inclusion and `UI/G/Vector` UFS staging already
cover this resource; no packaging setting was changed. No `.uasset` was fabricated
or imported for this SVG path.

## Preliminary native comparison

The real editor build passed: six actions, 12.93 seconds, exit 0.
Log: `Artifacts/Logs/Build/WordQuestEditor-20261002-082005.log`.
Dirty candidate native runs `20261002-082052-capture-initial` and
`20261002-082202-capture-selected` both exited 0 at 884x1780 and passed their
expected state tuples/dimensions. Direct inspection against the immutable original
shows lighter discs and pale rims, with separate live letters; selected C retains
the navy ring, marker and row outline without evaluation. The native and original
font/material edges still differ; this is not UI01 acceptance.

Read-only RGB comparison against prior packaged native
`20261002-050724-packaged-capture-initial` finds 14,845 changed pixels, all inside
the four badge regions (union bounding box x137..206/y1004..1409). Outside those
regions the captures are identical. Twelve documented first-badge interior points
(x148/154/188/196 crossed with y1024/1036/1048) avoid the live letter; their mean
absolute RGB-channel difference from the original decreases from 10.56 to 0.83
on the 0..255 scale. This is a small local color sample, not a global fidelity,
contrast or acceptance score. Exact points/colors, image hashes and exclusion
regions are in `Artifacts/QA/UI01/G-Answer-Badge-Comparison.json`.

Missing-SVG fallback was inspected in dirty editor run
`20261002-082401-capture-focus`, 390x844 with simulated 0.9 inset: original solid
badges/live letters and focused B remain intact, with no selection/evaluation,
correct dimensions and exit 0. Only the new owned runtime SVG was temporarily
moved within the workspace; parity correctly failed (exit 1), and the exact bytes
were restored in `finally`. Context is retained in
`Artifacts/QA/UI01/BadgeFallback/fallback-context.json`. This is an editor omission
test, not packaged corruption or physical-device evidence.

Final clean package/runtime verification is in progress. Raw native
metadata explicitly records dirty preliminary source; it is not clean-commit
package evidence. Dedicated review is pending.

## Remaining gates

Exact badge/answer-skin material and typography acceptance, companion identity,
panel/brand finish, fixture editorial review, manual pointer/keyboard/screen-reader,
phone/offline, performance, UI02 motion and release gates remain open. The screen
still contains one draft EQUIVOCAL question; `3 / 7` is prototype fixture progress.
Raw captures/logs remain local and ignored under `Artifacts`.
