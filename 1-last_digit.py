#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_n = abs(number) % 10
if (number < 0):
    last_n = -last_n
if last_n > 5:
    print(f"Last digit of {number} is {last_n} and is greater than 5")
elif last_n == 0:
    print(f"Last digit of {number} is {last_n} and is 0")
else:
    print(f"Last digit of {number} is {last_n} and is less than 6 and not 0")
