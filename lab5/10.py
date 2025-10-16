import re

def camel_to_snake(text):
    return re.sub(r'([A-Z])', r'_\1', text).lower().lstrip('_')

s = input("Enter CamelCase string: ")
print(camel_to_snake(s))
