# G Hint integration into dev

## Reason and actual diff

GitHub confirms owner merge of [PR #49](https://github.com/rloterh/WordQuest/pull/49)
into `dev` at 2026-10-06 22:58:22 UTC, merge
`25eb382151a16f4de8236c9e0363e174828ef3f5`. The owner then merged
[PR #50](https://github.com/rloterh/WordQuest/pull/50) at 22:58:40 UTC, merge
`269d6aa2221ad083da02e4788e74a142cb27fc04`, into its stacked base
`feature/g-answer-cue-proof`. That branch merge occurred after #49 closed and
is not part of `dev`.

`integration/g-hint-pearl-dev` starts at actual `origin/dev` (`25eb382`) and
merges the already owner-merged dependency branch at `269d6aa`, producing clean
integration commit `3c7b20fa92e9cf8b117e75bbc74883365e285834`. This is a local
integration branch, not an implementation-agent PR merge. Against `dev`, the
runtime/art diff is precisely the Hint preferred texture and preserved fallbacks
from #50, with its editable SVG, reproducible export, provenance and genuine
Unreal asset. The answer-cue fix from #49 is already in `dev`.

`git diff --name-only a877a5c 3c7b20f` lists only two documentation files. All
runtime, config, assets, tooling and references are identical to the clean source
used for #50's package. Subsequent integration commits update documentation only.
The material improvement and original unfinished-art limits remain those recorded
in [Hint pearl surface evidence](G-HINT-PEARL-SURFACE.md).

## Fresh integration verification

Checks at clean head `3c7b20f`:

- Real UE 5.8.2 Editor build succeeds, 69.61 seconds, exit zero:
  `Artifacts/Logs/Build/WordQuestEditor-20261006-232051.log`.
- All 96 Python QA tests pass; six supplied references verify unchanged.
- Pinned Hint renderer reproduces the export byte-for-byte; its four provenance
  hashes verify. Git LFS 3.7.1 and both binary filters verify. Ten staged SVGs
  match editable masters byte-for-byte. No new binary asset is authored here.
- Three native captures and both Unreal Context tests complete with native/helper
  exit zero, clean source provenance and all applicable predicates true. All three
  PNGs are visually inspected at their native dimensions.

| Run under `Artifacts/QA/UI01/` | Check |
|---|---|
| `20261006-232218-capture-initial` | 884x1780, actual 100%, safe-zone 1, frozen initial screen |
| `20261006-232351-capture-pointerhintpress` | 260x640, actual 200%, safe-zone 0.9, held virtual Hint press and cleanup |
| `20261006-232414-capture-cuecorrect` | 260x640, actual 200%, safe-zone 0.9, submitted correct answer cue geometry |
| `20261006-232436-automation-initial` | Both Unreal Context tests succeed, zero failed/not-run/in-progress |

Tooltips are disabled. The held-press frame reveals Hint and its native press/focus
feedback without consuming a hint or evaluating. Other content is partly offscreen;
it does not establish simultaneous visibility of every control. The correct-cue
frame reveals the chosen answer and first label line, not the feedback reading end.
These are Windows offscreen/synthetic checks, not manual input or phone evidence.

Initial PNG SHA-256 is
`faa72e1ba463d261405bb3c3dc4ccc542a931fbad2d529f6265078f8e8f93b62`.
It is RGB-identical to #50's final Editor trial. Against the retained #50 packaged
initial screen, only the known 964 Pause/plaque pixels differ, maximum channel delta
one, bounds [362,38,855,198). No new visual change is introduced by integration.

The retained clean #50 archive `20261006-222520-298494` is freshly verified:
all 49 payload size/hash pairs, all 11 recorded inputs against this checkout, and
manifest SHA-256
`252e524a9942bde70f441e20944c1bceb067575b55a0ca1d834b702eaf7d68db` match.
This is evidence reuse from source `a877a5c`, not a new cook/package of the integration
commit. #50's fourteen packaged captures and four missing-art checks remain recorded
in its QA document; they are not repeated or relabeled as new runs.

Raw integration scripts, helper logs and reports remain ignored under
`Artifacts/QA/UI01/HintIntegration20261006/` (`verification.json`,
`asset-verification.json`, `image-comparison.json`).

## Remaining gates

The integration PR targets `dev` directly. Dedicated read-only review against that
actual base must complete before publication; the owner retains the merge decision.
Full UI01 material/type/art fidelity, UI02 motion, manual/platform accessibility,
editorial approval of draft fixtures, Android/physical-phone, isolated offline,
performance and original release gates remain open. No deployment, release or
later milestone work is included.
