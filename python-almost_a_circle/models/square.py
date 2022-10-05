#!/usr/bin/python3
"""
  Class Square that inherits from Rectangle:
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
      Sqare Class methods
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
          initialize the method
          args:
          Size: The square of the size
          x: x of the position
          y: y of the position
          id: object of the id
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
          print method
          Return: [Square] (<id>) <x>/<y> - <size>
          - in our case, width or height
        """
        return ("[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                              self.id, self.x,
                                              self.y, self.width))

    @property
    def size(self):
        """
          The Width Getter method
          Return: Of the size of the  width and the height
        """
        return self.width

    @size.setter
    def size(self, value):
        """
          width and height setter method
          Arg:
          Value: The size of the value
        """
        self.width = value
        self.height = value
