"""Import the pinned action serif in an isolated initialized Unreal editor."""
import hashlib
import json
from pathlib import Path
import unreal

root = Path(__file__).resolve().parents[2]
source = root / 'ArtSource/Fonts/LiberationSerif/LiberationSerif-Bold.ttf'
expected = 'd754ba427cfe0bca54ae052384baa8f842da5bd6550ad4da024ac441e7a7d5ce'
if not source.is_file() or hashlib.sha256(source.read_bytes()).hexdigest() != expected:
    raise RuntimeError('Missing or changed pinned action serif')
subsystem = unreal.get_editor_subsystem(unreal.EditorAssetSubsystem)
destination = '/Game/UI/G/G_ActionBold'
if subsystem.does_asset_exist(destination):
    raise RuntimeError('G_ActionBold exists; inspect before reimporting')
task = unreal.AssetImportTask()
task.filename = str(source)
task.destination_path = '/Game/UI/G'
task.destination_name = 'G_ActionBold'
task.automated = True
task.replace_existing = False
task.save = True
factory = unreal.FontFileImportFactory()
factory.set_editor_property('batch_create_font_asset', unreal.BatchCreateFontAsset.YES)
task.factory = factory
unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task])
face = unreal.load_asset(destination)
if not task.imported_object_paths or not isinstance(face, unreal.FontFace):
    raise RuntimeError('Font import did not produce G_ActionBold')
if not subsystem.save_loaded_asset(face):
    raise RuntimeError('Could not save G_ActionBold')
report = root / 'Artifacts/Logs/UI01/action-serif-import.json'
report.parent.mkdir(parents=True, exist_ok=True)
report.write_text(json.dumps(dict(source=str(source.relative_to(root)), source_sha256=expected,
    asset=destination, imported_paths=list(task.imported_object_paths),
    type=face.get_class().get_name(), status='imported_unapproved_action_candidate'), indent=2), encoding='utf-8')
unreal.log('WORDQUEST_ACTION_SERIF_IMPORT_COMPLETE')
unreal.SystemLibrary.quit_editor()
