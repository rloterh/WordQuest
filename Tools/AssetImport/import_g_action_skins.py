"""Import the blank G action-skin candidates with Unreal's Python commandlet."""
import json
from pathlib import Path
import unreal

root = Path(__file__).resolve().parents[2]
exports = [
    ('G-Hint-Skin-v001-Candidate.png', 'G_HintSkin', 1024),
    ('G-Check-Skin-v001-Candidate.png', 'G_CheckSkin', 1024),
    ('G-Pause-Skin-v001-Candidate.png', 'G_PauseSkin', 512),
]
reports = []
for filename, name, maximum in exports:
    source = root / 'ArtSource/UI/G/Reconstruction' / filename
    if not source.is_file():
        raise RuntimeError(f'Missing source: {source}')
    task = unreal.AssetImportTask()
    task.filename = str(source)
    task.destination_path = '/Game/UI/G'
    task.destination_name = name
    task.automated = True
    task.replace_existing = True
    task.save = True
    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task])
    texture = unreal.load_asset(f'/Game/UI/G/{name}')
    if not task.imported_object_paths or not isinstance(texture, unreal.Texture2D):
        raise RuntimeError(f'{name} import produced no texture')
    texture.set_editor_property('srgb', True)
    texture.set_editor_property('compression_settings', unreal.TextureCompressionSettings.TC_EDITOR_ICON)
    texture.set_editor_property('lod_group', unreal.TextureGroup.TEXTUREGROUP_UI)
    texture.set_editor_property('mip_gen_settings', unreal.TextureMipGenSettings.TMGS_NO_MIPMAPS)
    texture.set_editor_property('never_stream', True)
    texture.set_editor_property('filter', unreal.TextureFilter.TF_BILINEAR)
    texture.set_editor_property('max_texture_size', maximum)
    if not unreal.get_editor_subsystem(unreal.EditorAssetSubsystem).save_loaded_asset(texture):
        raise RuntimeError(f'Could not save imported {name}')
    reports.append({'source': str(source.relative_to(root)), 'asset': list(task.imported_object_paths),
        'max_texture_size': maximum, 'status': 'imported_unapproved_candidate'})
report = root / 'Artifacts/Logs/UI01/action-skins-import.json'
report.parent.mkdir(parents=True, exist_ok=True)
report.write_text(json.dumps(reports, indent=2), encoding='utf-8')
unreal.log('WORDQUEST_ACTION_SKINS_IMPORT_COMPLETE')
