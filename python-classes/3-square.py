#!/usr/bin/python3
""" class for square. """


class Square:
    """Square class represents with the
    Private instance attribute: size
    Instantiation with optional size"""
    def __init__(self, size=0):
        """initialize the class"""
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

        def area(self):
            """Returns the current square area"""
        return (self.__size**2)
