# Art direction, animation, VFX, and audio bible

## Art direction: luminous scholarly adventure

Stylized dimensional art with polished material response, soft sculpted shapes, and deliberate composition. Visual anchors: amber glass, aged brass, deep ink, jade enamel, ivory paper. One focal object per screen; interface surfaces remain readable and tactically quiet. The emotional tone is curiosity, competence, discovery, and warmth.

Palette starting tokens: ink #14233B, parchment #F6EFDF, amber #E9B85C, jade #347F73, coral #CB7464, sky #94C9D6. These are art tokens, not prevalidated contrast pairs. Test every text/background combination separately. Avoid relying on red/green for correctness.

Use an expressive display face for brief headings and an exceptionally readable text face for definitions. Select commercially usable fonts with complete English punctuation and phonetic support or a deliberate fallback. Record font licenses. Do not rasterize body text into generated imagery.

## Asset inventory at v1.0

3 district environment kits; 12 landmark states before/after; 4 principal character designs plus Pip; approximately 30 modular props; 4 core challenge component families; 30–40 functional icons; 12 journal/collection decorations; 3 district music loops; approximately 25 interaction cues; reviewed pronunciation audio per released lemma/sense need. Exact counts are production estimates and can be reduced through reuse without reducing the learning scope.

Environments are fixed-camera or gently parallaxed compositions. Use Blender to sculpt, model, rig and render; choose live 3D for a small number of interactive hero objects and characters where it adds value. Bake lighting/detail into textures or rendered layers when that gives the better mobile tradeoff. Keep editable source files and deterministic exports.

## Asset contract

For each asset: ID, purpose, owner, source file, export recipe, target engine import settings, pivot/orientation, scale, material slots, texture dimensions, alpha rules, LODs where needed, collision requirement, animation set, license/provenance, performance estimate, and review status. Use a test scene to verify centimetre/metre conversion, axis, normals, skinning, colour management, alpha edges and texture compression. Do not rely on an assumed universal Blender-to-Unreal transform.

Initial scene budgets: 1–2 live hero characters, mostly baked environments, ordinary props using texture atlases, mostly 1K textures with 2K reserved for justified hero surfaces. These are provisional production constraints; measured memory and GPU time determine actual limits. Exclude 4K texture proliferation and physically simulated decoration with no interaction value.

## Character animation

Pip animation set: idle subtle glow; inspect; anticipate answer; delighted response; curious near-miss; point to clue; carry fragment; celebrate landmark; settle; sleep/pause. Characters use idle, listen, think, agree, disagree gently, explain, reveal, and farewell. Facial poses must remain legible at phone size. Start with a simple rig and authored poses rather than expensive cinematic facial technology.

Animation state changes follow game events. Interruptibility is part of the contract: an idle cannot prevent a tap; a celebration can shorten; a hint reaction cannot obscure the clue. No per-character bespoke state graph when a shared state interface fits.

## Motion language

| Event | Starting duration | Motion intent | Reduced-motion variant |
|---|---|---|---|
| Button press | 70–100 ms | Small tactile compression | Colour/outline change |
| Tile placement | 140–180 ms | Fast settle with tiny overshoot | Direct placement + highlight |
| Correct answer | 300–450 ms | Ink alignment and warm accent | Check icon and brief tint |
| Near miss | 180–250 ms | Gentle return, no punitive shake | Outline + explanation |
| Explanation open | 180–240 ms | Clear layer transition | Immediate panel |
| Mission finish | 800–1,200 ms, skippable | Landmark response and short flourish | Static completed landmark |
| District restoration | 2–4 seconds, skippable | Directed reveal and emotional payoff | Before/after dissolve |
| Background ambient | Slow loops | Subtle life away from reading | Static scene |

Use consistent easing families and finite animation lifetimes. Animations never determine reward authority. Input can continue after a short feedback beat; a repeated player should not spend more time watching celebration than solving.

## Niagara and effects

Use Niagara for localized world-space ink motes, fragment trails, and landmark reveals after compatibility/performance checks. Use UMG/material-based feedback for common UI actions when simpler and cheaper. Do not assume a third-party Niagara-in-UMG bridge is necessary. Avoid stacking multiple full-screen translucent layers and blur passes.

An effect record specifies emitter count, particle limit, lifespan, screen coverage, material complexity, culling distance, low-tier version, reduced-motion version, trigger, cancellation, pooling and measured GPU cost. Initial common-feedback budget: at most two short-lived effects simultaneously and no effect over the clue text. Numbers are hypotheses to profile, not guarantees.

Mobile baseline does not depend on Lumen, hardware ray tracing, Nanite, volumetric fog, or desktop render paths. Those may be useful for offline cinematics or future high-end variants, but the game must look intentionally finished without them.

## Audio

Create a distinctive restrained musical motif. Amber Archive: felt piano, plucked strings, soft mechanical textures. Conservatory: airy woodwinds and gentle organic percussion. Astral Court: warm sustained harmony and subtle bell accents. Correct-answer sounds should vary slightly without becoming a slot-machine barrage.

Separate gameplay cues, pronunciation and narrative buses. Duck music during pronunciation; never overlap two pronunciation clips. Audio reacts to foreground/background, headphones and mute. All meaning-bearing speech has text. Avoid continual full voice acting for every challenge; it multiplies cost and patch size. License or commission audio, keeping proof of permitted commercial use.

## AI-assisted asset pipeline

Generate multiple concepts from the same brief, then choose a coherent direction. Produce orthographic turnaround, expression sheet, material sheet, colour key, and UI reference. AI concepts are references unless explicitly prepared and reviewed as final assets. Generated images do not supply reliable geometry, UVs, rigging, alpha, or usable UI text automatically.

Reconstruct hero assets in Blender; batch export via reviewed scripts; import into a benchmark scene; inspect on phone; iterate. Maintain source provenance and prompt/reference history. Do not ask a model to imitate a named living artist; describe visual attributes and original references.

## Acceptance rubric

Score 1–5 on hierarchy, readability, material consistency, silhouette, motion timing, emotional appeal, and mobile performance. Require no dimension below 4 for the hero slice, plus no blocking usability or accessibility failure. This rubric is an internal review tool. It cannot establish market appeal without player observation.

Capture identical gameplay at native phone resolution, slow motion, muted, and reduced motion. Review clipping, safe areas, particle obstruction, repeated animation fatigue, and hitches. Polish the common interaction before expanding to the full art inventory.
