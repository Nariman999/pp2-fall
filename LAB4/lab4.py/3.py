n = int(input("Enter n: "))
def en(n):
    for i in range (n +1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

print(",".join(str(i) for i in en(n) ))