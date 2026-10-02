"""Copy editable G SVG icons/ornaments to the project's staged runtime directory."""
import argparse
import hashlib
from pathlib import Path
import shutil
import xml.etree.ElementTree as ET


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Check source/runtime parity without writing')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    pairs = [('G-Hint-Bulb-v001.svg', 'G_HintBulb.svg'), ('G-Check-Star-v001.svg', 'G_CheckStar.svg'),
             ('G-Header-Divider-v001.svg', 'G_HeaderDivider.svg'),
             ('G-Reading-Divider-v001.svg', 'G_ReadingDivider.svg'),
             ('G-Pause-Bars-v001.svg', 'G_PauseBars.svg'),
             ('G-Wordmark-v001.svg', 'G_Wordmark.svg'),
             ('G-Answer-Badge-v001.svg', 'G_AnswerBadge.svg')]
    for original, runtime in pairs:
        source = root / 'ArtSource/UI/G/Vector' / original
        target = root / 'Game/Content/UI/G/Vector' / runtime
        svg = ET.parse(source).getroot()
        if svg.tag != '{http://www.w3.org/2000/svg}svg' or not svg.get('viewBox'):
            raise RuntimeError(f'Invalid SVG root/viewBox: {source}')
        data = source.read_bytes()
        if args.check:
            if not target.is_file() or target.read_bytes() != data:
                raise RuntimeError(f'Stale/missing runtime SVG: {target}')
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
        print(f'{runtime}: source/runtime match, SHA-256 {hashlib.sha256(data).hexdigest()}')
    print('SVG parity only; native rendering, packaging and device acceptance are separate checks.')


if __name__ == '__main__':
    main()
