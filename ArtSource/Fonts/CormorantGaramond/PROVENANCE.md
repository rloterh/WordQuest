# Candidate display font

Cormorant Garamond SemiBold, unmodified upstream TTF. Downloaded 2026-09-23 from
the Cormorant project's pinned revision `9719e26aa8e26d7a30e736667427b9e05b5db059`:

- https://github.com/CatharsisFonts/Cormorant/blob/9719e26aa8e26d7a30e736667427b9e05b5db059/fonts/ttf/CormorantGaramond-SemiBold.ttf
- https://github.com/CatharsisFonts/Cormorant/blob/9719e26aa8e26d7a30e736667427b9e05b5db059/OFL.txt

The adjacent `OFL.txt` permits redistribution under SIL OFL 1.1. Font SHA256:
`dc4bc094dc3c55cf79ff2f6f0ba1e501b712fc3cf3742296cd8fdcc6e995127d`.
License SHA256: `60700d351cac4650c51f3f9db318d2a420f8b45052dba2715eb5fec41f0f6956`.

This is a licensed candidate, not an identification of the reference's brand or
button lettering. It lacks the reference's custom flourishes, bevel and lighting.
The native prototype uses Unreal's bundled Roboto for educational text. Its license
is copied unchanged to `ArtSource/Licenses/ROBOTO_License.txt`; it is also a candidate
whose metrics differ from the reference. Phone glyph and fallback checks remain open.

## Genuine Bold action face candidate (2026-10-02)

Unmodified `CormorantGaramond-Bold.ttf` was downloaded from the same pinned
upstream revision, under the unchanged adjacent OFL:
https://github.com/CatharsisFonts/Cormorant/blob/9719e26aa8e26d7a30e736667427b9e05b5db059/fonts/ttf/CormorantGaramond-Bold.ttf

SHA-256: `cc23bd9f374e7497b822b53a74e0c732ee3c926624840a03e5663e5eef688be4`;
size 1,042,268 bytes. Its Git blob SHA-1
`39e067fb0d22e528a173ce89a78d69c255a4b1e9` matches the pinned GitHub contents API.
Local fontTools inspection reports OS/2 weight 700 (existing SemiBold is 600) and
coverage for current Hint/Check/disabled/Pause display strings. No font bytes,
glyphs or license text were modified; no faux bold or original-font identification
is claimed. Unreal import is `/Game/UI/G/G_DisplayBold`, used as the actual `Bold`
entry beside the preserved SemiBold `Regular` entry. The outlined brand asset and
Roboto learning text remain unchanged. Art/phone/font acceptance remains open.
