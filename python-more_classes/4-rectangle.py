#!/usr/bin/python3
""" Class for Rectangle """


class Rectangle:
    """ class defined by private
        instance attribute width and height
    """

    def __init__(self, width=0, height=0):
        """ Initialization of the rectangle method
        Args:
            width: width of rectangle
            height: height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Set the width of Rectangle object
        Returns:
            Value of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter Method of width
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Set the height of Rectangle object
        Returns:
            Value of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method of height
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """method to return area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """method to return perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """method to print the rectangle with #"""
        if self.__width == 0 or self.__height == 0:
            return ''
        for row in range(self.__height - 1):
            print('#' * self.__width)
        return ('#' * self.__width)

    def __repr__(self):
        """repr method to describe itself"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))
