"""Import only the authored panel export with Unreal's texture commandlet."""
import hashlib
import json
from pathlib import Path
import unreal

root = Path(__file__).resolve().parents[2]
pearl = '-WordQuestPanelPearl' in unreal.SystemLibrary.get_command_line().split()
version = 'v002' if pearl else 'v001'
name = 'G_ReadingPanelPearl' if pearl else 'G_ReadingPanel'
source = root / f'ArtSource/UI/G/Exports/G-Reading-Panel-{version}.png'
expected = ('2fbf91f124eb3ec20e59035f6e8111e53760b925d7a966ca2ed337caf23df794'
    if pearl else 'b179748f71d1977d1df26f0f7985418e867d94e0ac8d8f270fbe2981e8bfa734')
if not source.is_file() or hashlib.sha256(source.read_bytes()).hexdigest() != expected:
    raise RuntimeError('Missing or changed authored panel export; inspect before updating the pin')
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
    raise RuntimeError('Panel import did not produce a Texture2D')
texture.set_editor_property('srgb', True)
texture.set_editor_property('compression_settings', unreal.TextureCompressionSettings.TC_EDITOR_ICON)
texture.set_editor_property('lod_group', unreal.TextureGroup.TEXTUREGROUP_UI)
texture.set_editor_property('mip_gen_settings', unreal.TextureMipGenSettings.TMGS_NO_MIPMAPS)
texture.set_editor_property('never_stream', True)
texture.set_editor_property('filter', unreal.TextureFilter.TF_BILINEAR)
if not unreal.get_editor_subsystem(unreal.EditorAssetSubsystem).save_loaded_asset(texture):
    raise RuntimeError(f'Could not save {name}')
report = root / ('Artifacts/Logs/UI01/reading-panel-v002-import.json' if pearl
    else 'Artifacts/Logs/UI01/reading-panel-import.json')
report.parent.mkdir(parents=True, exist_ok=True)
report.write_text(json.dumps(dict(source=str(source.relative_to(root)), source_sha256=expected,
    assets=list(task.imported_object_paths), version=version,
    status='imported_unapproved_authored_panel'), indent=2), encoding='utf-8')
unreal.log('WORDQUEST_READING_PANEL_IMPORT_COMPLETE')
