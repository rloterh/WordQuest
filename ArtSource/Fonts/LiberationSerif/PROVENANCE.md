# G action serif candidate

Unmodified Liberation Serif Bold, weight 700, version 2.1.5, is a measured
candidate for live Hint/Check labels. It does not identify the generated reference's
exact typeface or establish fidelity acceptance. Other display roles retain their
existing Cormorant faces.

Upstream [Liberation Fonts 2.1.5 release](https://github.com/liberationfonts/liberation-fonts/releases/tag/2.1.5),
tag commit `4b0192046158094654e865245832c66d2104219e`, links
[the binary archive](https://github.com/liberationfonts/liberation-fonts/files/7261482/liberation-fonts-ttf-2.1.5.tar.gz).
The same archive downloaded for PR #32 on 2026-10-03 was reused after verifying
SHA-256 `7191c669bf38899f73a2094ed00f7b800553364f90e2637010a69c0e268f25d0`.
Only the named regular archive members were copied; no font or license bytes changed.

| File | Bytes | SHA-256 |
| --- | --- | --- |
| LiberationSerif-Bold.ttf | 370096 | d754ba427cfe0bca54ae052384baa8f842da5bd6550ad4da024ac441e7a7d5ce |
| LICENSE | 4414 | 93fed46019c38bbe566b479d22148e2e8a1e85ada614accb0211c37b2c61c19b |

The adjacent unchanged SIL OFL 1.1 permits redistribution subject to its conditions.
It is identical to the existing `Game/Content/ThirdPartyLicenses/LiberationSans-LICENSE.txt`
staged NonUFS license, which covers the same Liberation Fonts distribution including
Serif. Its existing package path is retained. Source TTF and genuinely imported
Unreal FontFace use Git LFS.

fontTools 4.61.1 confirms version/weight and every character in the current live
Hint, Check answer, Hint used and Answer checked labels. Runtime copies the engine
composite and replaces only its Bold face, retaining fallback faces/script routing.
Missing action face falls back to the existing display composite. Minimum readable
size, 200% enlargement, live wrapping and measured icon/control layout remain.
Full editorial, platform glyph, accessibility and physical-device acceptance is open.
