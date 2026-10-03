"""Import pinned reading faces in an isolated initialized Unreal editor."""
import hashlib
import json
from pathlib import Path
import unreal

root = Path(__file__).resolve().parents[2]
sources = (
    ('Regular', '76d04c18ea243f426b7de1f3ad208e927008f961dc5945e5aad352d0dfde8ee8'),
    ('Bold', '788abee4c806d660e8aee46689dd8540cd4bb98da03dcc9d171ce3efd99a9173'),
)
subsystem = unreal.get_editor_subsystem(unreal.EditorAssetSubsystem)
# Validate both inputs/destinations before mutating either asset.
for weight, expected in sources:
    source = root / f'ArtSource/Fonts/LiberationSans/LiberationSans-{weight}.ttf'
    if not source.is_file() or hashlib.sha256(source.read_bytes()).hexdigest() != expected:
        raise RuntimeError(f'Missing or changed pinned {weight} font')
    if subsystem.does_asset_exist(f'/Game/UI/G/G_Reading{weight}'):
        raise RuntimeError(f'G_Reading{weight} exists; inspect before reimporting')
rows = []
for weight, expected in sources:
    source = root / f'ArtSource/Fonts/LiberationSans/LiberationSans-{weight}.ttf'
    destination = f'/Game/UI/G/G_Reading{weight}'
    task = unreal.AssetImportTask()
    task.filename = str(source)
    task.destination_path = '/Game/UI/G'
    task.destination_name = f'G_Reading{weight}'
    task.automated = True
    task.replace_existing = False
    task.save = True
    factory = unreal.FontFileImportFactory()
    factory.set_editor_property('batch_create_font_asset', unreal.BatchCreateFontAsset.YES)
    task.factory = factory
    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task])
    face = unreal.load_asset(destination)
    if not task.imported_object_paths or not isinstance(face, unreal.FontFace):
        raise RuntimeError(f'Font import did not produce {destination}')
    if not subsystem.save_loaded_asset(face):
        raise RuntimeError(f'Could not save {destination}')
    rows.append(dict(source=str(source.relative_to(root)), source_sha256=expected,
                     asset=destination, imported_paths=list(task.imported_object_paths),
                     type=face.get_class().get_name()))
report = root / 'Artifacts/Logs/UI01/reading-font-import.json'
report.parent.mkdir(parents=True, exist_ok=True)
report.write_text(json.dumps(dict(status='imported_unapproved_reading_candidates', fonts=rows), indent=2))
unreal.log('WORDQUEST_READING_FONTS_IMPORT_COMPLETE')
unreal.SystemLibrary.quit_editor()
