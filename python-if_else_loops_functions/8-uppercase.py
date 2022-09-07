#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        change = 0
        if ord(letter) > 96 and ord(letter) < 123:
            change = 32
        print("{:s}".format(chr(ord(letter) - change)), end="")
    print()
