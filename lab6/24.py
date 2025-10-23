filename = input("Enter the filename: ")

with open(filename, 'r') as file:
    lines = file.readlines()
    print("Number of lines in the file:", len(lines))
