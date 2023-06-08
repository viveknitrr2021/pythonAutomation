from pathlib import Path

p1 = Path('/vks/abc.txt')

with open(p1, 'r') as file:
    print(file.read())

p2 = Path('/vks/ghi.txt')

if not p2.exists():
    with open(p2, 'w') as file:
        file.write('Content 3')

print(p2.name)
print(p2.stem)
print(p2.suffix)

p3 = Path('/vks')
for files in p3.iterdir():
    print(files)

print(list(p3.iterdir()))
