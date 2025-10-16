import re

s = input("Enter text: ")
result = re.sub(r"[ ,.]", ":", s)
print(result)
