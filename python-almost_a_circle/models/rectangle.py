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
