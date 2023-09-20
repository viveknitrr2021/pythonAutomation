from pathlib import Path

root_dir = Path('D:/pythonAutomation/files')
# file_paths = list(root_dir.iterdir())
# print(file_paths)

file_path = root_dir.glob("**/*")

for path in file_path:
    if path.is_file():
        new_file = path.parts[-2] + "-" + path.name
        new_path = path.with_name(path.name)
        print(path)
        print(new_path)
        path.rename(new_path)

# for path in file_paths:
#     new_file = "new-" + path.stem + path.suffix
#     print(path)
#     print(new_file)
#     new_path = path.with_name(new_file)
#     print(new_path)
#     path.rename(new_path)

# for path in file_paths:
#     print(path)
#     for filepath in path.iterdir():
#         print(filepath)




