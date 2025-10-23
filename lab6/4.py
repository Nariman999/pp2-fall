import time
import math

num = int(input("Enter number: "))
miliseconds = int(input("Enter milliseconds: "))

time.sleep(miliseconds / 1000)
result = math.sqrt(num)

print(f"Square root of {num} after {miliseconds} miliseconds is {result}")
