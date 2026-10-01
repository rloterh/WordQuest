"""Create a side-by-side and adjustable overlay of unchanged native/reference PNGs."""
import argparse
import base64
import html
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('capture', type=Path)
parser.add_argument('--output', type=Path, default=Path('Artifacts/QA/UI01/comparison.html'))
args = parser.parse_args()
root = Path(__file__).resolve().parents[2]
reference = root / 'Planning/WordQuest-UI-Realms-Addendum/references/G-Celestial-Reverie-Gameplay.png'
def data(path):
    return 'data:image/png;base64,' + base64.b64encode(path.read_bytes()).decode('ascii')
ref, native = data(reference), data(args.capture)
page = '''<!doctype html><meta charset="utf-8"><title>G static comparison</title>
<style>body{background:#171329;color:#fff;font:16px system-ui;margin:24px}main{display:flex;gap:20px;align-items:start}figure{margin:0;width:min(30vw,442px)}img{width:100%;display:block}.overlay{position:relative}.overlay img+img{position:absolute;inset:0;opacity:.5}label{display:block;margin:16px 0}figcaption{padding:8px 0}input{width:260px}</style>
<h1>G static comparison — acceptance pending</h1><p>Original reference and actual Unreal capture, each shown at the same scale. Overlay starts at 50%. No image pixels are altered.</p>
<label>Native overlay opacity <input id="opacity" type="range" min="0" max="100" value="50"> <output id="value">50%</output></label>
<main><figure><figcaption>Original</figcaption><img src="REF" alt="Original G reference"></figure>
<figure><figcaption>Native capture</figcaption><img src="NATIVE" alt="Unreal native G screen"></figure>
<figure><figcaption>Aligned overlay</figcaption><div class="overlay"><img src="REF" alt="Reference underlay"><img id="blend" src="NATIVE" alt="Native overlay"></div></figure></main>
<p>Capture: CAPTURE</p><script>document.getElementById('opacity').oninput=e=>{document.getElementById('blend').style.opacity=e.target.value/100;document.getElementById('value').value=e.target.value+'%';};</script>'''
page = page.replace('REF', ref).replace('NATIVE', native).replace('CAPTURE', html.escape(str(args.capture)))
args.output.parent.mkdir(parents=True, exist_ok=True)
args.output.write_text(page, encoding='utf-8')
print(args.output.resolve())
