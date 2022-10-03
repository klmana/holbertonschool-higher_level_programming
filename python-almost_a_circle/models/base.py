#!/usr/bin/python3
"""
  Module:
  This class will be the “base” of all other classes in this project.
  The goal of it is to manage id attribute in all your future classes
  and to avoid duplicating the same code (by extension, same bugs)
"""


class Base:
    """
      Base Class
      Attributes:
      _nb_objects: number of objects created
      id: id of object an integer and need to test the type of it
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
          Init base method
          args:
          id: id of the  object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
