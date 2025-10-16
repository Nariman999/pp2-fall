import re

s = input("Enter camelCase string: ")
result = re.sub(r'([A-Z])', r' \1', s).strip()
print(result)
