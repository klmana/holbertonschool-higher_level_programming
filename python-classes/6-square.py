#!/usr/bin/python3
""" class for Square """


class Square:
    """ Square class represents.
    Private instance attribute: size:
    . property def size(self):to retrieve it
    . property setter def size(self, value)to set it
    Private instance attribute: position:
    .property def position(self): to retrieve it
    .property setter def position(self, value): to set it:
    .Instantiation with optional size.
    .Public instance method: def area(self).
    .Public instance method: def my_print(self)
    .if size is equal to 0, print an empty line """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the class square."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """To retrieve the position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position to a value."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """That returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """That prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
            return

        for indent_Top in range(0, self.__position[1]):
            print()
        for row in range(self.__size):
            for indent_Left in range(0, self.__position[0]):
                print(' ', end='')

            for colum in range(self.__size):
                print('#', end='')
            print()
