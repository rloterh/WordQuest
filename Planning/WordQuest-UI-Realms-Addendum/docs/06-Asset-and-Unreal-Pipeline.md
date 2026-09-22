# Asset decomposition and Unreal implementation handoff

## Prefer a hybrid 2.5D reconstruction

The strongest starting route for preserving these exact paintings is layered 2D art with real UI and selective 3D/sprite characters/props. Rebuilding every castle in full 3D would add cost and can move the look further from the reference. Use Blender where actual depth/rigging benefits the scene; keep the source art's lighting and composition as authority.

## Layer extraction inventory per realm

Background sky/moon; distant architecture; midground architecture/waterfalls; foreground foliage/columns; cloud/haze layers; water/reflection mask; companion cutout and clean plate; isolated books/crystals/lanterns; ornamental frame pieces; blank panel surfaces; control normal/pressed/selected variants; logo/icon source; glow/emission masks. Not every realm needs every layer. Record which pixels are painted reconstruction because they were hidden by the original UI.

Use image editing with the original as reference to create clean plates and isolated parts, then manually inspect. Inpainting can change architecture or character identity: compare visible retained regions, do not assume fidelity. Keep reference, masks, reconstructed source and export separately. Never animate a cutout over its original baked copy. These editable layers are future work; the supplied originals and home concepts remain flattened PNGs.

## Source preparation

Use a layered art file format supported by the chosen art tool; define canvas, colour profile, alpha convention and export naming. Store clean foreground masks without halos. Extend cloud/edge artwork beyond the viewport for drift. Give panel/control frames nine-slice or component geometry so corners do not stretch. Keep all educational text out of textures. Maintain source resolution adequate for target pixel density, but do not indiscriminately ship maximum-size layers.

A 2048×4096 uncompressed RGBA layer is roughly 32 MiB before mips; a stack of such layers can consume substantial memory. Actual GPU compression, mips, streaming and render targets determine measured cost. Budget layers deliberately and inspect package size, not merely PNG compression size.

## Runtime structure

ThemeDefinition supplies realm ID, palette/type roles, frame materials, scene bundle, effect profile, preferred companion mapping, fallback ID and compatibility version. ThemeResolver selects the active definition; it knows nothing about answer correctness. ThemePresenter applies an immutable presentation snapshot to common screens. MotionDirector applies motion/quality policy. CompanionPresenter renders selected companion independently. AssetProvider loads validated installed bundles.

In Unreal, use supported data assets/configuration and event-driven UMG changes. Prefer shared widgets with skinnable materials/brushes over cloned screens. Confirm APIs in the actual pinned engine before coding. Localized world effects may use Niagara; modest UI glow may be cheaper as a material animation. Built-in Unreal VFX and UI guidance support these tool categories, but exact performance must be measured. [UMG guidance](https://dev.epicgames.com/documentation/en-us/unreal-engine/optimization-guidelines-for-umg-in-unreal-engine) · [Niagara](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-visual-effects-in-niagara-for-unreal-engine)

## Rendering boundaries

Choose either a screen-space layered scene or camera-fixed world planes based on the P01 benchmark. Keep scene and UI z-order explicit. Use no per-frame logic for static labels. Avoid full-screen translucent blur stacks and oversized render targets. Hard-code neither GPU assumptions nor experimental renderer features into the required launch path. Bake complex atmosphere if it preserves the look more efficiently.

## Asset naming and versioning

Examples: Realm_G_Backdrop_v001, Realm_H_WaterMask_v001, Realm_I_CrystalGlint_v001, UI_ReadingPanel_G, UI_AnswerOption, Companion_G_Idle. All exports carry source ID, exporter settings, rights/provenance, import settings and review status. Binary assets have a single writer and version history. Original reference names/hashes remain stable.

## Runtime loading

Ship a complete low-cost base for G/H/I. Optional high-resolution content cannot make the first home screen blank offline. Load the active realm only, preload a requested next realm at a safe point, and release old scene resources after transition. Measure peak memory during swaps, not just steady state. Failed loading retains a valid realm and records a recoverable diagnostic.

## Agent capability boundary

A coding agent can create code, validators and supported editor scripts. It must run those scripts in the installed engine and inspect the resulting assets to claim completion. Writing Python does not mean a UMG widget or Niagara system exists. When editor execution is unavailable, supply exact manual steps and mark the implementation incomplete. Do not fabricate .uasset/.blend binaries.
