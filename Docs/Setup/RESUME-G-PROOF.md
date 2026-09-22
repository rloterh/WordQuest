# Resume the bounded G proof

## Immediate manual prerequisite

Open Visual Studio Installer, modify **Build Tools 2022**, choose **Individual
components**, and add **.NET Framework 4.8 SDK** and its targeting pack. The initial
editor build failed with `Could not find NetFxSDK install dir` in SwarmInterface.
Do not confuse this with the already present .NET 10 SDK. Do not edit Unreal's
SwarmInterface or bypass its dependency check. Handle any Windows security dialog
directly; the agent has not granted inbound network access.

From repository root:

```powershell
python Tools/AssetImport/verify_references.py
python Tools/BuildScripts/build_wordquest.py
```

The build helper checks UE 5.8.2 CL 56702186, invokes the generated editor target,
limits concurrency to two, requests `-NoUBA`, propagates failure and
saves the full output under `Artifacts/Logs/Build`. It does not install tools.
The game build still reports a UBA **local** executor in this installed engine;
do not infer that the flag removes all UBA internals or changes firewall policy.
Open `Game/WordQuest.uproject` in the verified engine after a successful build.
If engine association is not registered on another checkout, select the installed
5.8.2 engine through UnrealVersionSelector. Do not create a second project.

Inspect generated renderer settings before the first scene: the New Project UI
recorded Mobile/Scalable but the template still contains ray-tracing/Lumen settings.
Apply and verify the mobile rendering choices in the actual editor; this template
configuration is not a performance qualification.

## UI01 then UI02

1. Resolve art handoff and font licenses. Confirm prototype fixture review; its JSON
   explicitly remains non-release content. Create genuine imported assets with Unreal.
2. Implement one shared native screen with live word/clue/options/hint/submit/pause.
   Theme data carries G/H/I IDs; correctness code never reads realm or motion state.
3. Validate no initial choice, submit-without-choice, each answer, selection changes,
   deterministic feedback, assisted hint state, repeat submit and keyboard focus.
4. Capture actual native 884x1780 frozen t=0 view. Compare alongside original and with
   50% overlay; record panel, companion, type, palette and anchor differences. Fix
   material deviations. Save capture metadata and images under `Artifacts`.
5. Check narrow/tall/landscape windows, safe areas, long clue/options and 200% text.
   Reading/controls reflow or scroll, maintain accessible targets, and never depend
   on a flattened screenshot. Verify in the running application.
6. Only after UI01, add separated cloud/glow and full/reduced/battery/freeze controls.
   Test t=0/5/15/30, inactive cancellation, no ghost layers and 60-second recording.

## Android handoff, explicitly unverified

The SDK exists but this engine installation lacks
`Engine/Binaries/Android/UnrealGame.target`. Use the original engine installation
manager to add Android platform support for **the same UE 5.8.2 installation**. If
managed by Epic Launcher, use the installed engine's Options; its launcher inventory
was empty during P00, so do not assume that route currently manages this installation.
No engine replacement or upgrade is required by this report.

Then run the engine's non-installing check:

```powershell
& 'C:\Program Files\Epic Games\UE_5.8\Engine\Build\BatchFiles\RunUAT.bat' Turnkey -command=VerifySdk -platform=Android -unattended
& "$env:LOCALAPPDATA\Android\Sdk\platform-tools\adb.exe" devices -l
```

Read platform results, not just exit code: the initial Android check returned 0
without recognizing a platform. Reconcile engine SDK requirements (local API 36,
build-tools 36, preferred NDK r27c) and Java compatibility using actual packaging.
Public docs differ; no tested Android toolchain is yet pinned.

Connect and authorize a physical Android phone for adb. Record model/OS/resolution,
APK build commit/content hash, cold launch, offline launch, all answers, motion-off,
background/resume, safe areas, 200% text and a 60-second recording. Measure sustained
frame time and memory on named hardware. No APK currently exists, so no guessed
package ID/install command is presented as executable evidence.

Mac/Xcode/iPhone and store-signing readiness remain later dependencies. Desktop,
packaged desktop, Android package and physical-device gates must be reported separately.
