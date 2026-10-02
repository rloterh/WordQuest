# Local cooked Win64 G proof — mobile and art gates open

The owner merged PR #8 at `eae3475` on 2026-10-02. This follow-up verifies the
existing G screen in a real local Win64 Development archive. It adds packaging
and capture tooling; game code, assets, renderer settings and fixture are unchanged.
No deployment, public distribution, release or mobile acceptance is implied.

## Reproduction and evidence contract

From the repository root, with the recorded UE 5.8.2 CL 56702186:

```powershell
python Tools/QA/test_package_helpers.py
python Tools/BuildScripts/package_g_win64.py
```

The packager prints its timestamped directory under `Artifacts/Packages/Win64`.
Pass that directory to `python Tools/QA/run_g_proof.py capture --package-run`.
For example, the completed local evidence run used:

```powershell
python Tools/QA/run_g_proof.py capture --package-run Artifacts/Packages/Win64/20261002-005207-658190
python Tools/QA/run_g_proof.py capture --proof actions --width 390 --height 844 --safe-zone 0.9 --package-run Artifacts/Packages/Win64/20261002-005207-658190
```

Packaging requires a clean commit and SVG parity. It explicitly builds the editor
using the established helper, then UAT builds the game, cooks GPrototype, creates
pak/IoStore containers, stages and archives. `-skipbuildeditor` reuses the editor
just built; it does not skip a required build. UAT's `UbtArgs` applies to the client,
so both routes explicitly request no IDE hot reload, `-NoUBA` and two build actions.
The cooker requests two shader workers on this 16-thread host. UBA still reports
local execution; no engine dependency or security policy was bypassed.

The installed engine archives directly into `Archive`. `run.json` records command,
editor/UAT exits, source commit, clean status, raw input hashes and every archived
file's size/SHA256. A failed process, absent archive/containers, changed commit,
worktree or raw inputs leaves evidence incomplete and returns failure.
Packaged capture verifies all recorded payload files before launching the archived
native game executable. It records the package commit and manifest SHA separately
from current checkout revision. Runtime-created Saved files are not shipped payload.
Automation remains editor-based; the packaged route supports capture/state proofs.

Generated `Game/Build/**/FileOpenOrder/*.log` traces are now narrowly ignored.
`Game/Build` source resources remain eligible for Git. All archives/caches/logs
remain ignored. Five subprocess-mocked tests cover editor failure stopping UAT,
cook error propagation, zero exit with no archive, incomplete manifest rejection
and changed-payload rejection. No fake Unreal assets/executables are created.

## Verified results, 2026-10-02

Final packaged implementation: clean `f695ff860fa6b46725f5d7742309afb3c2de8cdf`.
Run: `Artifacts/Packages/Win64/20261002-005207-658190`, with successful editor build
in `EditorBuild.log` / `Artifacts/Logs/Build/WordQuestEditor-20261002-005207.log`.
`UAT.log` records game build, full cook of 510 packages, stage and archive success;
UAT exit 0, helper exit 0, all provenance invariants true. The archive contains
1,067,293,016 bytes including development/debug files; this is not a mobile size
or memory budget. Manifest SHA256:
`f914255e7d4b2711c9997ea6b00897c807a5fe2afbd909da503304bfea635aa4`.

Installed UnrealPak listing/extraction exited 0 (`PakList.log`, `PakExtract.log`).
`RawResources.json` records exact input-hash matches for the draft JSON and all
five SVGs extracted from the archived pak. Cooked textures/font and raw vectors
are visible in the packaged normal capture; no loose resource substitution was used.

All native runs below used the same verified archive and clean `f695ff8`, exited 0,
and passed expected dimensions/state tuples. Their PNGs were inspected directly.
They ran on this Windows 11 host with D3D12/PCD3D_SM6, not on a phone.

| Run under `Artifacts/QA/UI01` | Observation |
| --- | --- |
| `20261002-005503-packaged-capture-initial` | 884x1780; G textures/font, all SVGs and live text visible; initial unselected/unevaluated state |
| `20261002-005606-packaged-capture-correct` | 390x844; correct A, repeated submit still one evaluation; complete feedback/disabled actions |
| `20261002-005949-packaged-capture-actions` | 390x844, requested simulated 0.9 inset; 200% stacked actions/icons visible with Check focus; no evaluation |
| `20261002-010043-packaged-capture-hint` | 390x844; assisted correct A, one evaluation, assistance feedback and disabled labels visible |
| `20261002-010052-packaged-capture-resumed` | 390x844; B preserved after blocked paused actions and resume, zero evaluations, Pause focus restored |
| `20261002-010102-packaged-capture-wrong` | 390x844; incorrect B, one evaluation, complete feedback |
| `20261002-010111-packaged-capture-empty` | 390x844; choose-before-checking feedback, no selection/evaluation |

Both existing Unreal tests passed, zero failures/skips, in
`20261002-010211-automation-initial/Report`. Five helper tests, original-reference
hashes, SVG parity, LFS integrity and whitespace checks pass. Later edits only add
fresh-checkout test-directory setup and documentation; package/game code is unchanged.

The first attempt (`20261002-002559-627599`) returned UAT exit 6 due to Live Coding;
the explicit editor-build route corrected this. The first full cook
(`20261002-002907-869951`) succeeded in UAT but its provenance check rejected a
mid-run housekeeping commit. The next (`20261002-004737-589864`) passed UAT with
unchanged source but exposed the helper's incorrect Windows-subfolder assumption.
These are retained failed/incomplete helper runs, not final acceptance evidence.

The first two packaged launches waited several minutes at D3D12 pipeline creation
during shutdown before exiting 0. Later warm runs completed substantially sooner.
This is an unresolved performance observation, not a measured startup/shutdown,
frame-time, thermal or memory qualification. Renderer settings were not altered.

Dedicated read-only PR review is pending against actual `origin/dev`.

## Limits and next gates

This closes the bounded local Win64 cooking/archive/raw-resource/runtime gap only.
No network-isolated offline launch, clean-machine installation, manual activation,
screen-reader service, packaged automation suite, Shipping build, signing, mobile
package or physical-phone qualification was performed. Android engine receipt
absence and no adb-connected phone were rechecked on 2026-10-02. Art/brand/spirit/
font matching and fixture editorial approval remain unfinished. UI01 fidelity,
UI02 motion, original P01/V10 mobile acceptance and release gates remain open.
