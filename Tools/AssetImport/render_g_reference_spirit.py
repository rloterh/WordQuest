"""Render the editable static mask over original G companion pixels."""
import argparse
import hashlib
import json
from pathlib import Path
import struct
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Reproduce without writing')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    base = root / 'ArtSource/Companions/G'
    detail = base / 'SourcePixels/G-Spirit-Reference-Detail-v001.png'
    if hashlib.sha256(detail.read_bytes()).hexdigest() != '881c06f6b4dc6e885fca63827474f567d3e08a17a7e8af3be04e7ed87da6358f':
        raise RuntimeError('Original-pixel detail changed; inspect provenance before updating')
    sys.path.insert(0, str(root / 'Artifacts/Tools/resvg'))
    import resvg_py
    if (resvg_py.__version__, resvg_py.__resvg_version__) != ('0.5.0', '0.48.1'):
        raise RuntimeError('Use development-only resvg-py 0.5.0 / resvg 0.48.1')
    source = base / 'Masks/G-Spirit-Reference-v001.svg'
    target = base / 'Exports/G-Spirit-Reference-v001.png'
    data = resvg_py.svg_to_bytes(svg_path=str(source), resources_dir=str(source.parent),
        width=228, height=205, skip_system_fonts=True)
    if data[:8] != b'\x89PNG\r\n\x1a\n' or struct.unpack('>II', data[16:24]) != (228, 205):
        raise RuntimeError('Unexpected spirit PNG signature/dimensions')
    if args.check:
        if not target.is_file() or target.read_bytes() != data:
            raise RuntimeError('Missing/stale spirit export')
    else:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    print(json.dumps(dict(mask_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
        export_sha256=hashlib.sha256(data).hexdigest(), dimensions=[228, 205],
        resvg_py=resvg_py.__version__, resvg=resvg_py.__resvg_version__, reproduced=args.check), indent=2))


if __name__ == '__main__':
    main()
