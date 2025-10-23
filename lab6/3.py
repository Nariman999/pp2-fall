text = input("Введите строку: ")

rev_text = ''.join(reversed(text)) 

if text == rev_text:
    print("Text is palindrome")
else:
    print("Text is not palindrome")
