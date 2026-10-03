# G reading-font candidate

Unmodified Liberation Sans Regular (weight 400) and Bold (700), version 2.1.5,
are a measured sans-serif candidate for live G learning text. They do not identify
the generated reference's exact typeface and do not establish fidelity acceptance.

Upstream release/tag: [Liberation Fonts 2.1.5](https://github.com/liberationfonts/liberation-fonts/releases/tag/2.1.5),
commit `4b0192046158094654e865245832c66d2104219e`.
The binary archive linked by that release is
[liberation-fonts-ttf-2.1.5.tar.gz](https://github.com/liberationfonts/liberation-fonts/files/7261482/liberation-fonts-ttf-2.1.5.tar.gz).
Downloaded 2026-10-03; archive SHA-256:
`7191c669bf38899f73a2094ed00f7b800553364f90e2637010a69c0e268f25d0`.
Only the two named TTFs and license were copied from regular archive members.
No font bytes, glyphs, names or license text were changed.

| File | Bytes | SHA-256 |
| --- | --- | --- |
| LiberationSans-Regular.ttf | 410712 | 76d04c18ea243f426b7de1f3ad208e927008f961dc5945e5aad352d0dfde8ee8 |
| LiberationSans-Bold.ttf | 414456 | 788abee4c806d660e8aee46689dd8540cd4bb98da03dcc9d171ce3efd99a9173 |
| LICENSE | 4414 | 93fed46019c38bbe566b479d22148e2e8a1e85ada614accb0211c37b2c61c19b |

The adjacent unchanged SIL OFL 1.1 permits bundling/redistribution subject to its
conditions. An identical license copy under `Game/Content/ThirdPartyLicenses` is
staged as NonUFS for the packaged game. TTFs and genuinely imported Unreal FontFaces
use Git LFS. This record concerns these font files, not broader game rights clearance.

fontTools 4.61.1 inspection confirms the weights/version and coverage for ASCII
32–126, curly English quotes, en/em dashes, ellipsis, é/ñ, IPA schwa and primary
stress. The current draft learning strings are covered. The runtime composite
retains the engine's fallback faces/script routing for other glyphs; comprehensive
future editorial/phonetic and platform accessibility qualification remains open.

Only the word, clue, prompt, answer labels and feedback use this candidate family.
Decorative mode lettering, badges/result symbols, progress and Pause controls keep
their existing sans faces; action/brand display assets remain unchanged. Point-size
rounding, the readability floor and the 200% override continue through the existing
live layout. Native comparison, package and device evidence are recorded separately.
