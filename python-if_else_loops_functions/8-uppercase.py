#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        case = 0
    if ord(letter) > 96 and ord(letter) < 123:
        case = 32
        print("{:s}".format(chr(ord(letter) - case)), end="")
    print()
