"""Rebuild the editable G wordmark candidate; requires fonttools==4.61.1.

Outlines the repository's OFL Cormorant font, then adds authored ornament.
Revision v003 replaces only W and its curls with reference-guided vector curves.
No reference pixels, raster edits, external fonts or Unreal assets are generated.
"""
import argparse
from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.transformPen import TransformPen


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--revision', choices=['v001', 'v002', 'v003'], default='v003',
                        help='v003 reconstructs the capital W; v001/v002 reproduce preserved candidates')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    font = TTFont(root / 'ArtSource/Fonts/CormorantGaramond/CormorantGaramond-SemiBold.ttf')
    glyphs, cmap = font.getGlyphSet(), font.getBestCmap()
    # Fit one fixed English brand, not educational/localized text. Capitals rise
    # above the lowercase line, with room below for the separate Q flourish.
    cap = BoundsPen(glyphs)
    glyphs[cmap[ord('W')]].draw(cap)
    scale = 76 / (cap.bounds[3] - cap.bounds[1])
    paths, advance = [], 0
    for letter in 'WordQuest':
        glyph = glyphs[cmap[ord(letter)]]
        factor = 1.13 if letter == 'Q' else 1
        pen = SVGPathPen(glyphs, ntos=lambda n: f'{n:.3f}'.rstrip('0').rstrip('.'))
        glyph.draw(TransformPen(pen, (scale, 0, 0, -scale * factor, advance, 91)))
        paths.append(pen.getCommands())
        advance += glyph.width * scale - 1.5
    # A single horizontal fit preserves cap/lowercase proportions. Authored
    # curves remain editable separately from the licensed glyph outlines.
    lettering = ' '.join(paths[1:] if args.revision == 'v003' else paths)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="430" height="140" viewBox="0 0 430 140">
  <title>WordQuest — G wordmark candidate</title>
  <desc>OFL Cormorant outlines with authored gold finish, capital curls, Q swash and star. Not accepted original lettering.</desc>
  <defs>
    <linearGradient id="pearlGold" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0" stop-color="#fff8ef"/><stop offset=".28" stop-color="#fff3e5"/>
      <stop offset=".57" stop-color="#e9c39e"/><stop offset=".74" stop-color="#fff1da"/>
      <stop offset="1" stop-color="#d39868"/>
    </linearGradient>
    <linearGradient id="edgeGold" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0" stop-color="#fff4dd"/><stop offset="1" stop-color="#af755f"/>
    </linearGradient>
  </defs>
  <g transform="translate(10 5) scale({410 / advance:.6f} 1)">
    <path d="{lettering}" transform="translate(1.1 1.4)" fill="#61405f"/>
    <path d="{lettering}" fill="url(#pearlGold)" stroke="url(#edgeGold)" stroke-width=".7"/>
  </g>
  <!-- Tapered capital curls and independent Q tail; closed fills, no font dependency. -->
  <path d="M22 23 C11 9 0 19 5 29 C9 36 18 31 15 25 C13 23 10 24 10 27 C5 22 13 14 22 23Z
           M82 23 C89 0 107 2 104 17 C103 24 97 27 93 22 C90 18 93 13 96 14 C93 20 100 22 101 16 C104 7 91 5 82 23Z"
        fill="url(#pearlGold)" stroke="#e7ba91" stroke-width=".6"/>
  <path d="M219 91 C237 100 257 118 289 118 C327 120 361 113 380 103
           C356 125 314 131 285 125 C254 121 236 102 219 91Z"
        fill="url(#pearlGold)" stroke="#e7ba91" stroke-width=".7"/>
  <path d="M75 134 C113 111 159 105 191 117 L185 122 C154 109 111 119 75 134Z"
        fill="url(#pearlGold)"/>
  <path d="M212 108 Q214 121 226 124 Q214 127 212 138 Q209 127 198 124 Q209 121 212 108Z"
        fill="#edc496" stroke="#fff0da" stroke-width=".7"/>
  <path d="M212 111 L212 124 L201 124 Q210 121 212 111Z" fill="#fff8ed"/>
  <path d="M212 124 L223 124 Q215 128 212 137Z" fill="#bd8c72"/>
  <path d="M235 124 L254 125 L235 127 L232 125Z" fill="#efcca5"/>
</svg>
'''
    if args.revision in ('v002', 'v003'):
        # Keep licensed glyph and ornament geometry intact. Separate closed-vector
        # layers supply the warm interior, ivory rim and offset lower bevel.
        svg = svg.replace('stop-color="#fff3e5"', 'stop-color="#f5d2ba"')
        svg = svg.replace('stop-color="#e9c39e"', 'stop-color="#ce9b7e"')
        svg = svg.replace('stop-color="#fff1da"', 'stop-color="#fbe4cf"')
        svg = svg.replace('stop-color="#d39868"', 'stop-color="#bf8b72"')
        original_layers = f'''    <path d="{lettering}" transform="translate(1.1 1.4)" fill="#61405f"/>
    <path d="{lettering}" fill="url(#pearlGold)" stroke="url(#edgeGold)" stroke-width=".7"/>'''
        bevel_layers = f'''    <path d="{lettering}" transform="translate(1.2 1.8)" fill="#6a426b" stroke="#6a426b" stroke-width="2.6" stroke-linejoin="round"/>
    <path d="{lettering}" fill="url(#pearlGold)" stroke="#fff8ee" stroke-width="2.8" stroke-linejoin="round"/>
    <path d="{lettering}" fill="url(#pearlGold)" stroke="url(#edgeGold)" stroke-width="1.2" stroke-linejoin="round"/>
    <path d="{lettering}" transform="translate(-.3 -.4)" fill="none" stroke="#fffaf4" stroke-width=".35" stroke-opacity=".65" stroke-linejoin="round"/>'''
        svg = svg.replace(original_layers, bevel_layers)
    if args.revision == 'v003':
        # Authored closed curves reconstruct the reference W's splayed stems,
        # deeper tips and curled terminals in the existing SVG coordinate space.
        # Keep the other eight licensed glyphs, advance/fit, Q and ornaments intact.
        capital = '''M16 22 L37 22 L37 24 C31 24 30 25 32 32
            L48 88 L65 24 L68 22 L86 89 L101 32
            C103 25 101 24 96 24 L96 22 L108 22 L108 24
            C104 24 102 28 100 35 L83 105 Q81 109 79 105
            L63 50 L48 105 Q46 109 44 105 L24 35
            C22 28 20 24 16 24Z
            M31 23 C14 13 1 17 2 33 C3 46 19 48 20 37
            C20 29 13 27 10 32 C10 35 12 37 14 34
            C18 40 8 44 6 35 C4 24 16 19 24 26Z
            M99 26 C109 1 83 4 86 20 C89 29 98 25 97 18
            C95 12 89 15 92 20 C88 19 88 12 93 10
            C104 6 105 18 99 26Z'''
        start = svg.index('  <!-- Tapered capital curls')
        end = svg.index('  <path d="M219 91', start)
        capital_layers = f'''  <!-- Authored reference-guided W; other glyphs retain their licensed outlines. -->
  <g id="capital-W">
    <path d="{capital}" transform="translate(1.2 1.8)" fill="#6a426b" stroke="#6a426b" stroke-width="2.6" stroke-linejoin="round"/>
    <path d="{capital}" fill="url(#pearlGold)" stroke="#fff8ee" stroke-width="2.8" stroke-linejoin="round"/>
    <path d="{capital}" fill="url(#pearlGold)" stroke="url(#edgeGold)" stroke-width="1.2" stroke-linejoin="round"/>
    <path d="{capital}" transform="translate(-.3 -.4)" fill="none" stroke="#fffaf4" stroke-width=".35" stroke-opacity=".65" stroke-linejoin="round"/>
  </g>
'''
        svg = svg[:start] + capital_layers + svg[end:]
        svg = svg.replace('OFL Cormorant outlines with authored gold finish, capital curls, Q swash and star.',
                          'OFL Cormorant ordQuest outlines with a reference-guided authored W, gold finish, Q swash and star.')
    target = root / f'ArtSource/UI/G/Vector/G-Wordmark-{args.revision}.svg'
    target.write_text(svg, encoding='utf-8', newline='\n')
    print(target)


if __name__ == '__main__':
    main()
