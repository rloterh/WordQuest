# 10 — Sources, assumptions and limitations

## Primary implementation references

- [Epic: Optimization Guidelines for UMG](https://dev.epicgames.com/documentation/en-us/unreal-engine/optimization-guidelines-for-umg-in-unreal-engine): supports event-driven UI updates, careful invalidation and animation choices. Consult documentation matching the installed engine before implementation.
- [Epic: Creating Visual Effects in Niagara](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-visual-effects-in-niagara-for-unreal-engine): Niagara is an available Unreal VFX workflow; its existence does not make every effect appropriate for mobile UI.
- [W3C: Understanding Three Flashes or Below Threshold](https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html): flashing assessment involves more than frequency. Prefer eliminating problematic flashing rather than approaching a threshold.
- [W3C: Understanding Contrast (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) and [Resize Text](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html): accessibility targets to inform native UI validation; no certification is asserted.

## What is proposed versus established

The user selected G/H/I's visual direction and requested theme changes, lively environments and planning for characters/teams. The 30-minute fresh-visit threshold, default Surprise mode, shuffle-bag policy, companion names, exact motion timings, preliminary performance targets and staged scope are product recommendations made in this addendum. They are explicit defaults for prototyping, subject to measured results and product decisions.

The generated references are raster concepts, not source-layer files. Exact fonts, clean plates, rigs, masks, nine-slice borders, native widgets, sound and animations do not yet exist in this handoff. Image editing can help reconstruct layers but must be checked for changed architecture, ornament, lighting and character identity. Some manual retouching or drawing may be necessary. Font licensing and asset rights require a production inventory.

The user reports Unreal Engine 5.8.2 and Blender 5 installed. This package has not inspected that machine or verified platform SDKs, engine plugins, build tools, Apple signing or target hardware. P00 must report what is actually installed; do not silently substitute a different version. No new paid plugin is a prerequisite for the proposed visual proof.

The three new home concepts are drafts. The original gameplay images remain the visual anchors. A faithful implementation is an acceptance goal, not a guarantee of identical pixels on every screen: different aspect ratios, safe areas, text sizes and animation times require controlled adaptation.

Executing every prompt does not automatically make a game shippable. Actual builds, reviewed vocabulary, real device evidence, licensing, store requirements and all original blueprint release gates still apply. This addendum replaces the old visual direction where stated; it does not replace the original complete production plan.
