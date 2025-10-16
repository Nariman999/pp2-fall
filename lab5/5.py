import re

s = input("Enter string: ")
pattern = r"a.*b"

if re.fullmatch(pattern, s):
    print("Match")
else:
    print("No Match")
