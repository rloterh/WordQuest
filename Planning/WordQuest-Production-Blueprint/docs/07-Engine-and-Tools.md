# Engine, tools, and environment plan

## Provisional engine decision

Use Unreal as the first candidate because the owner already has it installed and the art direction benefits from dimensional scenes, native effects, and a unified content editor. The game remains primarily a text-heavy mobile interaction product, so Unreal's packaging, startup, UI accessibility and memory costs must be proven early.

Run one bounded Unreal benchmark before committing to full production: a packaged Android build containing a representative background, one rigged character, 12 letter tiles, large text, audio, a small effect, save/resume, and native keyboard input. Capture sustained frame time, memory, startup and download size. Probe iOS build feasibility at the same stage. An editor viewport on a powerful PC does not pass this gate.

If it fails after one focused optimization pass, document the cause. Compare a lean prototype in a suitable current stable Unity or Godot release using the same art and interactions. This comparison is a contingency, not permission to build two full games. Select the engine based on demonstrated performance, accessibility, development throughput and deployment reliability. Engine changes require a recorded owner decision because they affect cost and the prompt sequence.

## Recommended tool stack

| Tool/system | Role | Decision |
|---|---|---|
| Unreal 5.8.2, user-reported | Game runtime/editor | Verify installed build, pin after P00/P01 |
| C++ | Domain logic, validation boundaries, persistence | Core logic reviewable and testable |
| Blueprints + UMG | Scene assembly and UI presentation | Small graphs; event-driven updates |
| CommonUI | Shared input/navigation where useful | Enable only after packaged compatibility test |
| Niagara | Localized world effects | Built-in candidate; profile mobile behavior |
| Sequencer | Short restoration scenes | Skip/resume support; not every button tween |
| Control Rig / animation tools | Author expressive poses | Use only where they simplify production |
| MetaSounds / engine audio | Interactive sound and mixing | Default audio route; no mandatory middleware |
| Unreal Insights / platform profilers | CPU/GPU/memory diagnostics | Required for performance evidence |
| Blender 5.x | Models, rigs, renders, textures and export scripts | Exact version pinned, exports verified |
| Git + Git LFS | Code and binary asset history | Lock binary assets; exclude generated build data |
| VS Code + supported C++ toolchain | AI-assisted engineering | Discover exact engine compiler requirements |
| Android Studio / SDK / NDK / JDK | Android packaging and device tools | Install versions required by chosen engine |
| Mac + compatible Xcode + iPhone | iOS packaging and signing | Provision before claiming iOS-ready |
| Python | Content validation and asset automation | Pin project environment and dependencies |
| TypeScript + PostgreSQL | Small managed backend, if selected | Resolve provider/SDK at implementation gate |

Optional additions: Figma for collaborative UI source files; a commercial texturing tool if Blender's workflow becomes a bottleneck; a DAW for bespoke audio; a crash-reporting service; an asset inspection plugin proven against the pinned engine. These are candidate purchases, not required installations. Current compatibility, licensing, telemetry behavior, and cost must be checked before use.

Do not install web animation packages such as GSAP, Framer Motion, or Lottie merely because they are popular. They are not automatically native Unreal UI solutions. Rive/Spine-style runtimes or audio middleware merit adoption only after an actual integration need and shipping-build test. Engine-native tools are the initial baseline.

## Version and capability verification

P00 records: engine installation path, exact build/changelist, project association, compiler, SDK/NDK/JDK, Blender build, GPU driver, available disks, device models/OS, Mac/Xcode access, signing account status, AI tool/model labels and editor access. Keep credentials out of reports.

The official Epic mobile pages accessed for this plan are labelled Unreal 5.8. They do not verify the exact installed patch 5.8.2. Blender 5 is user-reported; the exact local patch was not inspected. Some official Blender and Apple-platform requirement pages did not return usable content during research; verify from the local tools and official version-specific requirements during P00.

## Build setup sequence

1. Record environment; create a separate prototype workspace and Git repository when implementation is authorized.
2. Pin engine association and compiler requirements. Build an empty C++ project locally.
3. Configure Android through the supported engine toolchain workflow. Package and install on a physical phone.
4. Establish iOS compilation/signing path with compatible Mac/Xcode and a real iPhone. Record any missing resource explicitly.
5. Add only baseline modules, UMG and required platform components. Disable unused plugins with care.
6. Import one Blender export and verify transform, materials and animation.
7. Establish source/LFS rules and a clean-clone build recipe before large assets accumulate.

## Rendering strategy

Start with a baked-lighting composition and mobile forward rendering; profile against the actual representative scene. Epic recommends forward for precomputed-lighting projects, while deferred has different advantages for dynamic-lighting workloads. Do not assume one path wins universally. [Epic mobile rendering guidance](https://dev.epicgames.com/documentation/en-us/unreal-engine/mobile-rendering-and-shading-modes-for-unreal-engine)

Use event-driven UI changes and avoid unnecessary per-frame bindings or nested layout complexity. [Epic UMG optimization](https://dev.epicgames.com/documentation/en-us/unreal-engine/optimization-guidelines-for-umg-in-unreal-engine)

## Plugin adoption checklist

Need; alternatives; exact version; engine/platform support; source availability; commercial rights; maintenance history; binary packaging; size/memory impact; failure behavior; uninstall path; owner-approved spend if any. Verify in a shipping configuration, not just editor play. Never auto-upgrade all dependencies mid-milestone.
