from pathlib import Path
import zipfile

# have files *.txt in D:/pythonAutomation/files/aks to zip
root_dir = Path('D:/pythonAutomation/files/aks')
archive_path = root_dir / Path('archive.zip')

with zipfile.ZipFile(archive_path, 'w') as zf:
    for path in root_dir.rglob("*.txt"):
        print(path)
        if path.is_file():
            zf.write(path)
        # path.unlink()

# root_dir = Path('D:/pythonAutomation/files/aks')
# dest_path = Path('D:/pythonAutomation/files/aksextracted')
#
# for path in root_dir.glob("*.zip"):
#     with zipfile.ZipFile(path, 'r') as zf:
#         zf.extractall(path=dest_path)
