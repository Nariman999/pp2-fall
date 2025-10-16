import re

s = input("Enter string: ")
pattern = r"[a-z]+_[a-z]+"

if re.fullmatch(pattern, s):
    print("Match")
else:
    print("No Match")
