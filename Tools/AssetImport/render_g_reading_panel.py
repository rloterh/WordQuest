"""Render the editable blank reading panel with the pinned development renderer."""
import argparse
import hashlib
import json
from pathlib import Path
import struct
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Reproduce without writing')
    parser.add_argument('--version', choices=('v001', 'v002'), default='v001')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    sys.path.insert(0, str(root / 'Artifacts/Tools/resvg'))
    import resvg_py
    if (resvg_py.__version__, resvg_py.__resvg_version__) != ('0.5.0', '0.48.1'):
        raise RuntimeError('Use development-only resvg-py 0.5.0 / resvg 0.48.1')
    source = root / f'ArtSource/UI/G/Vector/G-Reading-Panel-{args.version}.svg'
    target = root / f'ArtSource/UI/G/Exports/G-Reading-Panel-{args.version}.png'
    data = resvg_py.svg_to_bytes(svg_path=str(source), width=1185, height=1710, skip_system_fonts=True)
    if data[:8] != b'\x89PNG\r\n\x1a\n' or struct.unpack('>II', data[16:24]) != (1185, 1710):
        raise RuntimeError('Unexpected panel PNG signature/dimensions')
    if args.check:
        if not target.is_file() or target.read_bytes() != data:
            raise RuntimeError('Missing/stale panel PNG')
    else:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    print(json.dumps(dict(source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
        export_sha256=hashlib.sha256(data).hexdigest(), dimensions=[1185,1710],
        resvg_py=resvg_py.__version__, resvg=resvg_py.__resvg_version__, reproduced=args.check), indent=2))


if __name__ == '__main__':
    main()
