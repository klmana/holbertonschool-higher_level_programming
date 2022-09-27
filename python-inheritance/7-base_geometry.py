#!/usr/bin/python3
"""
Create a class BaseGeometry
"""


class BaseGeometry:
    """
     Public instance method BaseGeometry class
    """

    def area(self):
        """
          Raises an Exception with the message
          area() is not implemented
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
          check and validates value:if value is an integer
        """
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
