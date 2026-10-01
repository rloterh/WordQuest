"""Import only the G answer-skin candidate using Unreal's Python commandlet.

Texture-only import; no font factory or Slate-dependent operations.
"""
import json
from pathlib import Path
import unreal

root = Path(__file__).resolve().parents[2]
source = root / 'ArtSource/UI/G/Reconstruction/G-Answer-Skin-v002-Candidate.png'
if not source.is_file():
    raise RuntimeError(f'Missing source: {source}')
task = unreal.AssetImportTask()
task.filename = str(source)
task.destination_path = '/Game/UI/G'
task.destination_name = 'G_AnswerSkin'
task.automated = True
task.replace_existing = True
task.save = True
unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task])
texture = unreal.load_asset('/Game/UI/G/G_AnswerSkin')
if not task.imported_object_paths or not isinstance(texture, unreal.Texture2D):
    raise RuntimeError('Answer skin import produced no texture')
texture.set_editor_property('srgb', True)
texture.set_editor_property('compression_settings', unreal.TextureCompressionSettings.TC_EDITOR_ICON)
texture.set_editor_property('lod_group', unreal.TextureGroup.TEXTUREGROUP_UI)
texture.set_editor_property('mip_gen_settings', unreal.TextureMipGenSettings.TMGS_NO_MIPMAPS)
texture.set_editor_property('never_stream', True)
texture.set_editor_property('filter', unreal.TextureFilter.TF_BILINEAR)
texture.set_editor_property('max_texture_size', 1024)
if not unreal.get_editor_subsystem(unreal.EditorAssetSubsystem).save_loaded_asset(texture):
    raise RuntimeError('Could not save imported answer skin')
report = root / 'Artifacts/Logs/UI01/answer-skin-import.json'
report.parent.mkdir(parents=True, exist_ok=True)
report.write_text(json.dumps({'source': str(source.relative_to(root)), 'asset': list(task.imported_object_paths),
    'max_texture_size': 1024, 'status': 'imported_unapproved_candidate'}, indent=2), encoding='utf-8')
unreal.log('WORDQUEST_ANSWER_SKIN_IMPORT_COMPLETE')
