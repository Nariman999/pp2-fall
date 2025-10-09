
def generate_squares(N):
    for i in range(N + 1):
        yield i ** 2

for num in generate_squares(5):
    print(num, end=" ")
