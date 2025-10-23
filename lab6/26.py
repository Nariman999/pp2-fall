import string

for letter in string.ascii_uppercase:
    filename = f"{letter}.txt"
    with open(filename, 'w') as file:
        file.write(f"This is file {filename}\n")

print("Files A.txt to Z.txt have been created.")
