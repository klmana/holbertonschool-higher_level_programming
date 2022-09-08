#!/usr/bin/python3
for alphabet in range(122, 96, -1):
    if alphabet % 2 == 0:
        num = alphabet
    else:
        num = alphabet - 32
    print("{:s}".format(chr(num)), end="")
