# G wordmark Q-swash candidate

The owner merged PRs #27 and #28 into `dev` on 2026-10-02, 21:50:42 and
21:50:59 UTC. This bounded UI01 change uses a v004 editable master to reconstruct
the reference's Q loop and two tapered ribbons. The older outlined Q descender
and flat tail did not reproduce that silhouette. The font file and earlier
masters are preserved; this is a derivative graphic, not a modified font or
accepted original lettering.

A baseline editor capture at clean `77d4fde` (`20261002-215625-capture-initial`)
and two dirty native preflights (`215840` and `220121`, same date, capture-initial)
pass their state/dimension/cue checks. Both revised preflights were inspected.
The first revision's loop was too broad and ribbon branch too thin; the second
revision narrows the loop and gives the upturned branch a fuller taper. A parity
check after rebuilding intentionally caught the stale runtime copy, which was
then restaged and passes. Clean packaging and final native verification follow;
no acceptance is established by these preliminary checks.

Reproduction preserves v001 after CRLF/LF normalization; v002/v003/v004 reproduce
byte-identically. Original bytes are restored after every reproduction check.
Seven non-Q licensed glyph paths, authored W, fit transform, gradient definitions
and under-title ornament match the prior master. An initial XML comparison included
inter-element tail whitespace and rejected an extra blank line; the corrected
comparison excludes that tail while retaining all W attributes/children. Evidence:
`Artifacts/QA/UI01/wordmark-swash-integrity.py` and `.json`. All 63 existing Python
QA tests pass. Master/runtime/provenance are documented in the vector README.

The Android engine receipt remains absent and adb lists no device. The supported
Computer Use inventory still fails with a missing native-pipe connection, so no
manual desktop/Launcher control is claimed. Art, editorial, manual/platform
accessibility, phone/offline/performance, UI02 motion and release gates remain open.

The first clean package at `5a55ed4` (`20261002-220533-074642`) passed both
real targets, cook/stage/archive, nine inspected native contracts and both Unreal
tests. However, reference-size pixel analysis found 6,220 changed pixels outside
the lower-Q region: removing its descender shortened the shared glyph gradient's
object bounds, unintentionally changing shading on other lettering. This package
is preliminary, not the final art evidence. Raw batch/analysis files are retained
with the `wordmark-swash-unpinned-gradient-` prefix; the archive is unchanged.

The correction gives the shared glyph path separate gradients mapped explicitly
to its original vertical bounds. Original local gradients remain for W/ornament.
Dirty native preflight `20261002-221346-capture-initial` reduces changes outside
the lower-Q region to three pixels, each differing by one RGB byte level. Final
clean packaging and captures verify this corrected material mapping.
