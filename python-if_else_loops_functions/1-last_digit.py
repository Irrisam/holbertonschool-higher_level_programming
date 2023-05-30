#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    numberf = - number
else:
    numberf = number

comparer = numberf % 10

negdigit = comparer = - comparer

if comparer == 0:
    print(f"Last digit of {number} is {comparer} and is 0")

elif comparer < 6 and comparer != 0:
    print(f"Last digit of {number} is {negdigit} and is less than 6 and not 0")

else:
    print(f"Last digit of {number} is {comparer} and is greater than 5")
