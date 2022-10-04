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

        length = len(args)
        if length == 0:
            return
        for index in range(length):
            if index == 0:
                if args[index] is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                else:
                    self.id = args[index]
            elif index == 1:
                self.width = args[index]
            elif index == 2:
                self.height = args[index]
            elif index == 3:
                self.x = args[index]
            elif index == 4:
                self.y = args[index]

            elif kwargs and len(kwargs) != 0:
                for key, value in kwargs.items():
                    if key == 'id':
                        if value is None:
                            self.__init__(self.width,
                                          self.height, self.x, self.y)
                        else:
                            self.id = value
                    elif key == 'width':
                        self.width = value
                    elif key == 'height':
                        self.height = value
                    elif key == 'x':
                        self.x = value
                    elif key == 'y':
                        self.y = value
