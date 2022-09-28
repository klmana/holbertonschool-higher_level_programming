#!/usr/bin/python3
"""
 Class Square that inherits from
 Rectangle (9-rectangle.py).
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
       Class Square that inherits from Rectangle
    """

    def __init__(self, size):
        """
          initialization square method
        """
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """
          The area of a Square instance.
          the area() method from Rectangle.
        """

        return self.__size ** 2
