filename1 = input("Enter source file name: ")
filename2 = input("Enter destination file name: ")

with open(filename1, 'r') as src, open(filename2, 'w') as dst:
    dst.write(src.read())

print(f"Contents copied from {filename1} to {filename2}")
