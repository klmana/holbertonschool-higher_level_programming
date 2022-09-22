#!/usr/bin/python3

"""
    This function prints a square with the character #.
    size is the size length of the square
"""


def print_square(size):
    """
    Prints a square with the character where size is #.
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        for row in range(size):
            for colum in range(size):
                print("#", end="")
            print()
