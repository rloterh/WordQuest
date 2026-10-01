"""Run normal editor with -EnablePlugins=PythonScriptPlugin -ExecutePythonScript=...

Font import needs Slate initialization; do not use the Python commandlet.
"""
import json
from pathlib import Path
import shutil
import unreal

ROOT = Path(__file__).resolve().parents[2]
DESTINATION = '/Game/UI/G'
assets = {
    'G_Background': 'ArtSource/Environments/G/Reconstruction/G-Clean-Plate-v001.png',
    'G_Panel': 'ArtSource/UI/G/Reconstruction/G-Panel-v002-Candidate.png',
    'G_Spirit': 'ArtSource/Companions/G/Reconstruction/G-Spirit-v001-Candidate.png',
    'G_Display': 'ArtSource/Fonts/CormorantGaramond/CormorantGaramond-SemiBold.ttf',
}
subsystem = unreal.get_editor_subsystem(unreal.EditorAssetSubsystem)
subsystem.make_directory(DESTINATION)
for name, source in assets.items():
    source_path = ROOT / source
    if not source_path.is_file():
        raise RuntimeError(f'Missing source: {source}')
    task = unreal.AssetImportTask()
    task.filename = str(source_path)
    task.destination_path = DESTINATION
    task.destination_name = name
    task.automated = True
    task.replace_existing = True
    task.save = True
    if source_path.suffix == '.ttf':
        factory = unreal.FontFileImportFactory()
        factory.set_editor_property('batch_create_font_asset', unreal.BatchCreateFontAsset.YES)
        task.factory = factory
    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task])
    if not task.imported_object_paths:
        raise RuntimeError(f'Import produced no asset: {source}')
    for path in task.imported_object_paths:
        asset = unreal.load_asset(path)
        if isinstance(asset, unreal.Texture2D):
            asset.set_editor_property('srgb', True)
            asset.set_editor_property('compression_settings', unreal.TextureCompressionSettings.TC_EDITOR_ICON)
            asset.set_editor_property('lod_group', unreal.TextureGroup.TEXTUREGROUP_UI)
            asset.set_editor_property('mip_gen_settings', unreal.TextureMipGenSettings.TMGS_NO_MIPMAPS)
            asset.set_editor_property('never_stream', True)
            asset.set_editor_property('filter', unreal.TextureFilter.TF_BILINEAR)
        if not subsystem.save_loaded_asset(asset):
            raise RuntimeError(f'Could not save {path}')
        unreal.log(f'WORDQUEST_IMPORTED {path}')

data = ROOT / 'Game/Content/Data'
data.mkdir(parents=True, exist_ok=True)
shutil.copy2(ROOT / 'ContentSource/Challenges/G-Equivocal-Prototype.json', data / 'G-Equivocal-Prototype.json')
map_path = '/Game/Maps/GPrototype'
if not subsystem.does_asset_exist(map_path):
    editor = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)
    if not editor.new_level(map_path, False) or not editor.save_current_level():
        raise RuntimeError('Unreal could not create/save the empty prototype map')
report = ROOT / 'Artifacts/Logs/UI01/asset-import.json'
report.parent.mkdir(parents=True, exist_ok=True)
report.write_text(json.dumps({'sources': assets, 'map': map_path, 'status': 'imported_unapproved_candidates'}, indent=2))
unreal.log('WORDQUEST_IMPORT_COMPLETE')
