"""Import the authored Hint surface with Unreal, preserving the old texture."""
import hashlib
import json
from pathlib import Path
import unreal

root = Path(__file__).resolve().parents[2]
source = root / 'ArtSource/UI/G/Exports/G-Hint-Surface-v001.png'
expected = '78eaa7094eb2e832a0d8cdff5b19106ce140689870d9f2f6d50640a4b37e8107'
if not source.is_file() or hashlib.sha256(source.read_bytes()).hexdigest() != expected:
    raise RuntimeError('Missing/changed Hint export; inspect before updating its pin')
task = unreal.AssetImportTask()
task.filename = str(source)
task.destination_path = '/Game/UI/G'
task.destination_name = 'G_HintReverie'
task.automated = True
task.replace_existing = True
task.save = True
unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task])
texture = unreal.load_asset('/Game/UI/G/G_HintReverie')
if not task.imported_object_paths or not isinstance(texture, unreal.Texture2D):
    raise RuntimeError('Hint import produced no texture')
texture.set_editor_property('srgb', True)
texture.set_editor_property('compression_settings', unreal.TextureCompressionSettings.TC_EDITOR_ICON)
texture.set_editor_property('lod_group', unreal.TextureGroup.TEXTUREGROUP_UI)
texture.set_editor_property('mip_gen_settings', unreal.TextureMipGenSettings.TMGS_NO_MIPMAPS)
texture.set_editor_property('never_stream', True)
texture.set_editor_property('filter', unreal.TextureFilter.TF_BILINEAR)
if not unreal.get_editor_subsystem(unreal.EditorAssetSubsystem).save_loaded_asset(texture):
    raise RuntimeError('Could not save imported Hint texture')
report = root / 'Artifacts/Logs/UI01/hint-surface-import.json'
report.parent.mkdir(parents=True, exist_ok=True)
report.write_text(json.dumps(dict(source=str(source.relative_to(root)),
    source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
    asset=list(task.imported_object_paths), dimensions=[texture.blueprint_get_size_x(), texture.blueprint_get_size_y()],
    status='imported_unapproved_authored_surface'), indent=2), encoding='utf-8')
unreal.log('WORDQUEST_HINT_SURFACE_IMPORT_COMPLETE')
