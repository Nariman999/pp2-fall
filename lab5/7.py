def snake_to_camel(text):
    return ''.join(word.title() if i != 0 else word for i, word in enumerate(text.split('_')))

s = input("Enter snake_case string: ")
print(snake_to_camel(s))
