"""Render the authored G pearl SVG to a reproducible Unreal import source."""
import argparse
import hashlib
import json
from pathlib import Path
import struct
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Reproduce and compare without writing')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    sys.path.insert(0, str(root / 'Artifacts/Tools/resvg'))
    import resvg_py
    if resvg_py.__version__ != '0.5.0':
        raise RuntimeError('Use development-only resvg-py==0.5.0; see the vector README')
    source = root / 'ArtSource/UI/G/Vector/G-Answer-Pearl-v001.svg'
    target = root / 'ArtSource/UI/G/Exports/G-Answer-Pearl-v001.png'
    data = resvg_py.svg_to_bytes(svg_path=str(source), width=1380, height=238, skip_system_fonts=True)
    if data[:8] != b'\x89PNG\r\n\x1a\n' or struct.unpack('>II', data[16:24]) != (1380, 238):
        raise RuntimeError('Unexpected rendered PNG dimensions/signature')
    if args.check:
        if not target.is_file() or target.read_bytes() != data:
            raise RuntimeError('Missing/stale pearl PNG export')
    else:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    print(json.dumps(dict(svg_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
        png_sha256=hashlib.sha256(data).hexdigest(), renderer=resvg_py.__version__,
        resvg=resvg_py.__resvg_version__, dimensions=[1380,238], reproduced=args.check), indent=2))


if __name__ == '__main__':
    main()
