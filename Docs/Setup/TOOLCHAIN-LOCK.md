# Provisional toolchain lock

Recorded 2026-09-22. This is an inventory pin, not a passed P01 production decision.

- Unreal 5.8.2 / CL 56702186 / compatible CL 55116800.
- Engine path: `C:\Program Files\Epic Games\UE_5.8`.
- Blender 5.1.0 / adfe2921d5f3.
- VS Build Tools 2022 17.14.26; MSVC executable 19.44.35222.
- Windows SDK 10.0.26100.0; engine-bundled .NET SDK 10.0.203.
- .NET Framework 4.8 SDK and targeting pack added with VS Installer on 2026-09-23.
- Git 2.53.0.windows.1 and LFS 3.7.1.
- Android SDK root `%LOCALAPPDATA%\Android\Sdk`; installed NDK r27d
  (27.3.13750724), API 36 and build-tools 36.0.0 available.
- Android JDK selection unresolved: installed PATH Java 17 and Studio JBR 25.

The missing NetFxSDK dependency was resolved; the real Win64 Development editor
target compiled and linked successfully on 2026-09-23 (7 actions, exit 0).
Android platform binaries and required target receipts are absent from the engine installation.
Win64 Turnkey SDK verification passed; Android was not recognized as a checked platform.
Standalone Win64 Development game-target compilation/link passed with the recorded
MSVC/Windows SDK. No mobile platform runtime is qualified.

The owner authorized resolving build prerequisites on 2026-09-23. Only the missing
.NET Framework SDK/targeting pack were added; no engine upgrade or paid plugin was
introduced. Record packaging outputs before promoting mobile compatibility claims.
