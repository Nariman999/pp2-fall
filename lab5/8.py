import re

s = input("Enter camelCase string: ")
result = re.split(r'(?=[A-Z])', s)
print(result)
