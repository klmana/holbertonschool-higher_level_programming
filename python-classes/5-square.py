#!/usr/bin/python3
""" class for Square """


class Square:
    """ Square class represents.
    Private instance attribute: size:
    . property def size(self):to retrieve it
    . property setter def size(self, value)to set it
    .Instantiation with optional size.
    .Public instance method: def area(self).
    .that returns the current square area
    """

    def __init__(self, size=0):
        """Initialize the class square."""
        self.__size = size

    @property
    def size(self):
        """Property getter of  size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter the size to a value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """print to stdout square with the character #"""
        if self.__size is 0:
            print()

        for row in range(self.__size):
            for colum in range(self.__size):
                print('{}'.format('#'), end='')
            print()
