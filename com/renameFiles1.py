from pathlib import Path
from datetime import datetime

root_dir = Path('D:/pythonAutomation/files')
file_path = root_dir.glob("**/*")

for path in file_path:
    if path.is_file():
        seconds_created = path.stat().st_ctime
        date_created = datetime.fromtimestamp(seconds_created).strftime("%Y-%m-%d_%H:%M:%S")
        new_file = date_created + '_' + path.name
        new_path = path.with_name(new_file)
        print(path)
        print(new_path)
        path.rename(new_path)
