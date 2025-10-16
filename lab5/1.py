import re

s = input("Enter string: ")
pattern = r"ab*"

if re.fullmatch(pattern, s):
    print("Match")
else:
    print("No Match")
