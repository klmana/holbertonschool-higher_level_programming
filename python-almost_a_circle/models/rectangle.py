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

    def validator(self, name, value):
        """
          Verify and validate conditions
        """
        if type(value) is not int:
            raise TypeError('{:s} must be an integer'.format(name))
        elif name in ['width', 'height'] and value <= 0:
            raise ValueError('{:s} must be > 0'.format(name))
        elif name in ['x', 'y'] and value < 0:
            raise ValueError('{:s} must be >= 0'.format(name))

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
        self.validator('width', value)
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
        self.validator('height', value)
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
        self.validator('x', value)
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
        self.validator('y', value)
        self.__y = value

    def area(self):
        """
          Defines area that returns the area
          value of the Rectangle instance.
        """
        return self.__width * self.__height

    def display(self):
        """
          That prints in stdout the Rectangle instance with
          the character (#) - and no need to handle x and y
        """
        for row in range(self.y):
            print()
        for row in range(self.height):
            print('{}{}'.format(' ' * self.x, '#' * self.width))

    def __str__(self):
        """
          print method and return formated string
        """
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
           Update the class Rectangle by updating the public method
           def update(self, *args): by changing the prototype to update
           (self, *args, **kwargs)assigns a key/value argument to attributes:
         """
        if args:
            list_args = ['id', 'width', 'height', 'x', 'y']
            index = 0
            for arg in args:
                setattr(self, list_args[index], arg)
                index += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
          Return the dictionary representation of a Rectangle
        """
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
