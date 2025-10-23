import os

path = input("Enter the path to delete: ")

if os.path.exists(path):
    print("File exists.")
    if os.access(path, os.W_OK):
        os.remove(path)
        print("File deleted successfully.")
    else:
        print("You don't have permission to delete this file.")
else:
    print("The specified path does not exist.")
