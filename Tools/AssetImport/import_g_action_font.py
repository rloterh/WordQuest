"""Import only the pinned G Bold face in a normal, isolated Unreal editor.

Use -EnablePlugins=PythonScriptPlugin -ExecutePythonScript=...; font import needs
Slate initialization. This never recreates the project, map or other assets.
"""
import hashlib
import json
from pathlib import Path
import unreal

root = Path(__file__).resolve().parents[2]
source = root / 'ArtSource/Fonts/CormorantGaramond/CormorantGaramond-Bold.ttf'
expected = 'cc23bd9f374e7497b822b53a74e0c732ee3c926624840a03e5663e5eef688be4'
if not source.is_file() or hashlib.sha256(source.read_bytes()).hexdigest() != expected:
    raise RuntimeError('Missing or changed pinned Bold font source')
subsystem = unreal.get_editor_subsystem(unreal.EditorAssetSubsystem)
destination = '/Game/UI/G/G_DisplayBold'
if subsystem.does_asset_exist(destination):
    raise RuntimeError('G_DisplayBold already exists; inspect before reimporting')
task = unreal.AssetImportTask()
task.filename = str(source)
task.destination_path = '/Game/UI/G'
task.destination_name = 'G_DisplayBold'
task.automated = True
task.replace_existing = False
task.save = True
factory = unreal.FontFileImportFactory()
factory.set_editor_property('batch_create_font_asset', unreal.BatchCreateFontAsset.YES)
task.factory = factory
unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task])
face = unreal.load_asset(destination)
if not task.imported_object_paths or not isinstance(face, unreal.FontFace):
    raise RuntimeError('Font import did not produce the expected FontFace')
if not subsystem.save_loaded_asset(face):
    raise RuntimeError('Could not save imported Bold FontFace')
report = root / 'Artifacts/Logs/UI01/action-font-import.json'
report.parent.mkdir(parents=True, exist_ok=True)
report.write_text(json.dumps({'source': str(source.relative_to(root)), 'sha256': expected,
    'asset': destination, 'type': face.get_class().get_name(),
    'imported_paths': list(task.imported_object_paths),
    'status': 'imported_unapproved_font_candidate'}, indent=2), encoding='utf-8')
unreal.log('WORDQUEST_ACTION_FONT_IMPORT_COMPLETE')
unreal.SystemLibrary.quit_editor()
