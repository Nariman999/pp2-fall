import os

path = input("Enter the path: ")

if os.path.exists(path):
    filename = os.path.basename(path)
    directory = os.path.dirname(path)
    print("File name:", filename)
    print("Directory:", directory)
else:
    print("The specified path does not exist.")
