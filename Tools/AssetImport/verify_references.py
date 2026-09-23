"""Read-only SHA-256 and PNG-dimension check of six immutable references."""
import hashlib
import json
from pathlib import Path
import struct


def main():
    package = Path(__file__).resolve().parents[2] / 'Planning/WordQuest-UI-Realms-Addendum'
    entries = json.loads((package / 'specs/reference-manifest.json').read_text())
    if len(entries) != 6:
        raise ValueError('Expected six supplied reference images')
    for entry in entries:
        path = (package / entry['file']).resolve()
        if not path.is_relative_to(package.resolve()):
            raise ValueError('Reference path escapes package')
        data = path.read_bytes()
        if data[:8] != b'\x89PNG\r\n\x1a\n' or data[12:16] != b'IHDR':
            raise ValueError(f'Not a PNG with IHDR: {path.name}')
        dimensions = struct.unpack('>II', data[16:24])
        digest = hashlib.sha256(data).hexdigest()
        if dimensions != (entry['width'], entry['height']) or digest != entry['sha256']:
            raise ValueError(f'Reference changed: {path.name}')
        print(f'PASS {entry["file"]}: {dimensions[0]}x{dimensions[1]}, SHA-256 {digest}')


if __name__ == '__main__':
    main()
