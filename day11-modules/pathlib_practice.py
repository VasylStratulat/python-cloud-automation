from pathlib import Path

current_path = Path.cwd()
print(current_path)

file_path = Path("main.py")

print(file_path.exists())
print(file_path.is_file())
print(file_path.is_dir())

folder = Path.cwd()

new_path = folder / "main.py"

print(new_path)

print(new_path.name)
print(new_path.suffix)
print(new_path.parent)

folder = Path("pathlib_folder")

folder.mkdir(exist_ok=True)

print(folder.exists())
print(folder.is_dir())

folder = Path("pathlib_folder")

if folder.exists():
    folder.rename("renamed_pathlib_folder")
    print("Directory renamed")

folder = Path("renamed_pathlib_folder")

if folder.exists():
    folder.rmdir()
    print("Directory removed")
else:
    print("Directory not found")

file_path = Path("server_info.txt")

file_path.write_text("web-01\nrunning\n443\n")

content = file_path.read_text()

print(content)

print(file_path.exists())
print(file_path.is_file())

size = file_path.stat().st_size

print("File size:", size)

current_folder = Path.cwd()

for file in current_folder.glob("*.py"):
    print(file.name)