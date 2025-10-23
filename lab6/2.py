text = input("Введите текст: ")

upper = 0
lower = 0

for i in text:
    if i.isupper():   
        upper += 1
    elif i.islower():   
        lower += 1

print("Lower case:", lower)
print("Upper case:", upper)
