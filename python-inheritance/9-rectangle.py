#!/usr/bin/python3
"""
 Class Rectangle that inherits from
 BaseGeometry (7-base_geometry.py).
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
      Rectangle subclass
      width and height that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
          initialization method
          width of rectangle and height of rectangle
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """
          calculate area of width rectangle
          and height rectangle that inherits from BaseGeometry

        """
        return self.__width * self.__height

    def __str__(self):
        """
          print method and return formated string
        """
        return "[{}] {}/{}".format(__class__.__name__,
                                   self.__width, self.__height)
