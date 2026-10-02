"""Rebuild the editable G wordmark candidate; requires fonttools==4.61.1.

Outlines the repository's OFL Cormorant font, then adds authored ornament.
No reference pixels, raster edits, external fonts or Unreal assets are generated.
"""
from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.transformPen import TransformPen


def main():
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
    lettering = ' '.join(paths)
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
    target = root / 'ArtSource/UI/G/Vector/G-Wordmark-v001.svg'
    target.write_text(svg, encoding='utf-8', newline='\n')
    print(target)


if __name__ == '__main__':
    main()
