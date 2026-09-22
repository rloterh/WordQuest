# Visual reference fidelity contract

## Reference authority

The original G/H/I gameplay PNGs are immutable visual targets. Their exact filenames, pixel dimensions and SHA-256 hashes are in `specs/reference-manifest.json`. Do not overwrite them, crop them into new references silently, or replace them with fresh unconstrained image generations. Working exports are separate assets with revision IDs.

The home drafts extend the same identity but are not automatically approved pixel specifications. The common interaction layout is shared while surface geometry, type character and decoration can vary by realm. Original G uses a cleaner sans reading style; H and I use more serif character. Do not homogenize those away without showing the difference to the owner.

## What must remain recognizable

| Realm | Locked visual anchors |
|---|---|
| G | Lavender cloud ocean; floating palace and waterfalls; crescent; warm-white/lilac curved panel; navy reading text; pearl/lavender controls; thin pale gold; flowing white lantern-carrying spirit |
| H | Wisteria arch framing; bridge and glowing stream; moonlit castle; cyan flowers; deep blue-violet panel; ivory text; cool illuminated borders; round violet spirit |
| I | Celestial bookshelves; floating books and crystals; staircase; full moon; ivory-lavender panel; plum serif character; sculpted gold/star trims; lilac tiles; capped winged lantern spirit |

Keep the WordQuest mark's silhouette and placement as a reconstruction target; rebuild a clean brand asset after checking name/font rights. Generated lettering can be imperfect at small size. Do not use a low-resolution logo cutout as a substitute for final typography.

## Static-match pass before motion

1. Capture the target image at its actual dimensions and preserve it.
2. Record normalized anchors for title, progress, hero scene, panel, target word, clue, options, hint and submit using the actual source pixels. Do not assume identical geometry across G/H/I.
3. Reconstruct the reference state with the exact example text, no animation, matched camera, fixed texture import/colour settings and pinned fonts.
4. Compare side by side and using a half-opacity overlay in an image/editor tool. Review layout and material regions separately from text and dynamic masks.
5. Fix composition, scale and material mismatches before adding effects.
6. Capture at realistic phone display size and inspect touch/readability. Record any approved adaptation.

Suggested initial tolerances: key anchor centres within about 1% of viewport dimensions at the matched size, control bounds within about 2%, no unwanted wrapping/truncation, and no material/palette mismatch visible at ordinary phone size. These are project acceptance targets to refine from measured feasibility, not claims of already achieved matching. A global pixel similarity score is insufficient: a flattened screenshot can score perfectly and still be nonfunctional.

## Responsive adaptation

Use a normalized composition with semantic layout regions, not one stretched bitmap. Maintain art focal points with controlled crop and overscan; never stretch a moon or companion. Artwork can extend off-screen while reading surfaces and controls stay within safe areas. Large text can expand/scroll the content region and reduce decorative scene height. Preserve identity, not unreadable fixed line breaks at every font size.

For the reference-size comparison, use reference-like type metrics; for accessible sizes, document the adaptation. A functional accessibility override is not counted as an unexplained visual regression.

## Prohibited shortcuts

No entire screenshot as the clickable UI. No baked definitions or answers. No random substitute castle or mascot. No unrelated asset-pack buttons. No clipping the original companion while animating a second duplicate above it. No adding aggressive bloom to compensate for weak materials. No AI-generated animation of the entire screen that warps letters or hit targets.

## Reference versus production artefacts

Source PNG: visual reference. Decomposed/background-cleaned layers: working art requiring inspection. Engine textures/materials: production candidates after import/device QA. Widget implementation: live text/input/accessibility. Character rig/sprite animation: movement assets. Packaged capture: evidence. Each has a separate ID and status.

## Review states

Concept → reconstruction in progress → static fidelity accepted → motion accepted → device accepted → release qualified. Keep an exception log containing reference, capture, reason, decision and owner when departing materially from the appearance. These gates should reuse existing project reviews, not create a permission request for every routine pixel adjustment.
