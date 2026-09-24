import os

current_directory = os.getcwd()

print(current_directory)

files = os.listdir()

print(files)

print(os.path.exists("main.py"))
print(os.path.exists("missing.py"))
print(os.path.exists("__pycache__"))

print(os.path.isfile("main.py"))
print(os.path.isdir("main.py"))

print(os.path.isfile("__pycache__"))
print(os.path.isdir("__pycache__"))

if not os.path.exists("test_folder"):
    os.mkdir("test_folder")
    print("Directory created")
else:
    print("Directory already exists")

if os.path.exists("test_folder") and not os.path.exists("renamed_folder"):
    os.rename("test_folder", "renamed_folder")
    print("Directory renamed")
else:
    print("Rename not needed")

if os.path.exists("test_folder"):
    os.rmdir("test_folder")
    print("Directory removed")
else:
    print("Directory not found")