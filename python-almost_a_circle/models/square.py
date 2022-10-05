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

    def update(self, *args, **kwargs):
        """
          Update the class Square by adding the public method
          def update(self, *args, **kwargs) that assigns attributes:
          Args  :
          Args  : The pointer to the arguments or we can call
          the list of arguments - no-keyworded arguments
          Kwargs: The double pointer to the key word arguments
        """

        if args:
            index = 0
            list_args = ['id', 'size', 'x', 'y']
            for arg in args:
                setattr(self, list_args[index], arg)
                index += 1
            return
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
          Update the class Square by adding
          the public method def to_dictionary(self):
          That returns the dictionary representation of a Square:
        """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
