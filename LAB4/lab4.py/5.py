n= int(input("enter n: "))
def down(n):
    for i in range (n, -1, -1):
        yield i

for s in down(n):
    print (s)