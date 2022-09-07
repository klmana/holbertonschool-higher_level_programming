#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):
        if number % 5 is 0 and number % 3 is 0:
            word = "FizzBuzz"
        elif number % 5 is 0:
            word = "Buzz"
        elif number % 3 is 0:
            word = "Fizz"
        else:
            word = str(number)
        print("{:s}".format(word), end=" ")
