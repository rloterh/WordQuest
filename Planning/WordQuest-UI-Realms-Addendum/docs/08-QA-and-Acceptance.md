# 08 — QA and acceptance

## Evidence required

A screenshot proves composition; a recording proves motion; a packaged build on a named physical device proves runtime behavior. Collect all three. Record build commit, operating system, device, resolution, UI scale, quality tier, theme, companion, motion setting and deterministic capture time. Never describe generated concepts as implemented screens.

| ID | Requirement | Acceptance evidence |
|---|---|---|
| V01 | Original G/H/I identities preserved | Reference-sized frozen captures and overlays; art lead checks composition, panel, type, lighting, companion and contrast |
| V02 | Live responsive UI | Long real sentences, dynamic text scaling and safe-area captures; all text selectable by assistive navigation where supported |
| V03 | Realm modes | Cold launch, short resume, long resume, mission recovery, fixed mode and companion mode test matrix |
| V04 | Stable session | Screen navigation and duplicate foreground events never reroll the active realm |
| V05 | Fair surprise rotation | Each available realm used once per persisted shuffle bag; no boundary repeat where alternatives exist; corrupt state recovers |
| V06 | Living backgrounds | 60-second recordings for each realm, with visible subtle motion and no seam, ghost companion or effects over reading masks |
| V07 | User controls | Reduced motion, battery saver and sparkles-off persist and take effect without restart |
| V08 | Independent companion | Each of three companions works in each realm; explicit link option determines realm only when chosen |
| V09 | Educational integrity | Changing theme, companion or motion never changes an answer, score, review schedule, purchase or saved mission |
| V10 | Reliable packaging | All three base realms function offline in packaged Android and iOS builds; missing assets recover without blank controls |
| V11 | Input and accessibility | Large targets, readable contrast, focus order, non-color feedback, platform back navigation and screen-reader proof on supported platforms |
| V12 | Performance | Named-device frame-time, memory, loading and thermal measurements; quality degradation preserves text and input |

## Performance qualification

Use the baseline blueprint's device/support requirements. Before final asset production, name actual minimum and representative phones and record their OS versions. Proposed initial targets, subject to this benchmark: stable 60 fps on representative devices, stable 30 fps on minimum devices using the battery/low tier. That means nominal frame budgets of 16.7 ms and 33.3 ms, not permission to ignore long frames. Record median, 95th and 99th percentile frame times and count frames above twice the target budget during five minutes of navigation/practice and a 20-minute sustained session. Test a realm swap's peak memory as well as steady state.

Measure cold launch to usable home and input response in release-like builds. Establish loading and memory budgets from the P01 feasibility benchmark; do not invent a universal memory ceiling. Save results in a device table, including ambient conditions, thermal state and whether plugged in. Reduce particles, parallax and texture cost before reducing text quality. Do not repeatedly reload full environments while answering questions.

## Accessibility acceptance

Use at least 44 pt / 48 dp platform-appropriate touch targets and verify actual physical UI scale. Target WCAG-style contrast of 4.5:1 for normal text and 3:1 for large text and essential control boundaries; measure final composites over their brightest and darkest motion states. These are engineering targets, not an automatic certification claim. Test text enlargement to 200% with reflow, scrolling and no clipped answer or action. Adopt the OS reduced-motion preference at first run, while allowing an explicit in-app override. Never rely solely on glow, color, sound or motion to convey correctness.

Avoid high-contrast repeated flashing by design. A frequency-only check does not establish safety: area, luminance and saturated red matter too. Test combined effects, transitions and rewards, including overlapping events. The reduced-motion mode removes parallax, bobbing, drifting, shimmer and decorative particles while retaining static depth and all learning feedback.

## Stateful cases

- App terminated during a question: restore its realm, answer state and content without rerolling or granting extra rewards.
- Explicit realm selection during a mission: queue until a safe home boundary, explain briefly and allow cancellation.
- Companion changed while linked: apply its preferred realm at the next safe boundary; fixed mode stays fixed.
- Corrupt settings, removed theme or interrupted asset load: use a verified fallback; keep learning data intact.
- Foreground event received twice: one visit resolution, one asset transition.
- Background for 29 minutes versus 31 minutes: no fresh visit versus fresh visit, except pinned mission recovery. Use elapsed-time handling resilient to wall-clock changes.
- Several changes made during loading: newest requested selection wins; cancel obsolete loads without dangling callbacks.
- Modal or screen exits while an animation runs: no input lock, retained hidden emitter or late UI callback.

## Release stop conditions

Stop release for unreadable content, inaccessible required controls, crashes, lost learning progress, incorrect scoring, duplicated rewards, uncontrolled flashes, missing offline themes or material departure from accepted references. A failed visual check creates a specific defect with side-by-side evidence, not a request to regenerate every screen. Fix and retest the affected path.

Owner review is reserved for accepting new compositions or material visual departures. Routine implementation, corrections and verification proceed within the selected direction. Maintain a brief decision log: requirement, evidence, owner if needed, disposition and remaining risk.
