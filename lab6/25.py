my_list = ["Rome", "Beks", "Omar"]
filename = input("Enter the filename: ")

with open(filename, 'w') as file:
    for name in my_list:
        file.write(name + "\n")

print("List has been written to file successfully.")
