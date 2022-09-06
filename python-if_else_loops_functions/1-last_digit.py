#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
greater_than = "and is greater than 5"
less_than = "and is less than 6 and not 0"
equal = "and is 0"

if number > 0:
    last = number % 10
else:
    last = ((number * -1) % 10) * -1

if last > 5:
    final = greater_than
elif last == 0:
    final = equal
elif last < 6 and not 0:
    final = less_than
print("Last digit of", number, "is", last, final)
