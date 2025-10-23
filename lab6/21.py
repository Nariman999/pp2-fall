import os
path = input("Enter the path: ")

print("Directories:")
for item in os.listdir(path):
    if os.path.isdir(os.path.join(path, item)):
        print(item)

print("\nFiles:")
for item in os.listdir(path):
    if os.path.isfile(os.path.join(path, item)):
        print(item)

print("\nAll directories and files:")
for item in os.listdir(path):
    print(item)
