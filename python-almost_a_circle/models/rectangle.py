#!/usr/bin/python3
"""
  Class Module Create Rectangle
  that inherits from Base:
"""
from models.base import Base


class Rectangle(Base):
    """
      Rectangle subclass inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
          Instance initialization method
          Args:
          Width: Width of the Rectangle
          Height: Height of the Rectangle
          x : The Init of the variable
          y : The Init of the variable
          Id : Id of the  object
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
     def width(self):
         """
           Width getter
         """
         return self.__width

     @width.setter
     def width(self, value):
         """
           Width setter
         """
         self.integer_validator('width', value)
         self.__width = value

     @property
     def height(self):
         """
           Height getter
         """
         return self.__height

     @height.setter
     def height(self, value):
         """
           Height setter
         """
         self.integer_validator('height', value)
         self.__height = value

     @property
     def x(self):
         """
           x : getter
         """
         return self.__x

     @x.setter
     def x(self, value):
         """
           x : setter
         """
         self.integer_validator2('x', value)
         self.__x = value

     @property
     def y(self):
         """
           y : getter
         """
         return self.__y

     @y.setter
     def y(self, value):
         """
           y : setter
         """
         self.integer_validator2('y', value)
         self.__y = value
