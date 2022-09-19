#!/usr/bin/python3
""" class for Square """


class Square:
    """Square class represents with the
    Private instance attribute: size
    Instantiation with optional size
    """

    def __init__(self, size=0):
        """Initialize the class."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2
