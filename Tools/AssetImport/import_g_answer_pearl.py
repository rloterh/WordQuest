"""Import the authored pearl export with Unreal's texture-only Python commandlet."""
import hashlib
import json
from pathlib import Path
import unreal

root = Path(__file__).resolve().parents[2]
source = root / 'ArtSource/UI/G/Exports/G-Answer-Pearl-v001.png'
if not source.is_file():
    raise RuntimeError(f'Missing source: {source}')
task = unreal.AssetImportTask()
task.filename = str(source)
task.destination_path = '/Game/UI/G'
task.destination_name = 'G_AnswerPearl'
task.automated = True
task.replace_existing = True
task.save = True
unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task])
texture = unreal.load_asset('/Game/UI/G/G_AnswerPearl')
if not task.imported_object_paths or not isinstance(texture, unreal.Texture2D):
    raise RuntimeError('Pearl import produced no texture')
texture.set_editor_property('srgb', True)
texture.set_editor_property('compression_settings', unreal.TextureCompressionSettings.TC_EDITOR_ICON)
texture.set_editor_property('lod_group', unreal.TextureGroup.TEXTUREGROUP_UI)
texture.set_editor_property('mip_gen_settings', unreal.TextureMipGenSettings.TMGS_NO_MIPMAPS)
texture.set_editor_property('never_stream', True)
texture.set_editor_property('filter', unreal.TextureFilter.TF_BILINEAR)
if not unreal.get_editor_subsystem(unreal.EditorAssetSubsystem).save_loaded_asset(texture):
    raise RuntimeError('Could not save imported pearl texture')
report = root / 'Artifacts/Logs/UI01/answer-pearl-import.json'
report.parent.mkdir(parents=True, exist_ok=True)
report.write_text(json.dumps(dict(source=str(source.relative_to(root)),
    source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
    asset=list(task.imported_object_paths), status='imported_unapproved_authored_candidate'), indent=2), encoding='utf-8')
unreal.log('WORDQUEST_ANSWER_PEARL_IMPORT_COMPLETE')
