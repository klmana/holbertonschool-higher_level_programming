#!/usr/bin/python3
"""
  Module:
  This class will be the “base” of all other classes in this project.
  The goal of it is to manage id attribute in all your future classes
  and to avoid duplicating the same code (by extension, same bugs)
"""

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
          That returns the JSON string representation of list_dictionaries:
          Args:
          List_dictionaries: The list of the dictionaries
          Return: The JSON string representation of list_dictionaries:
        """
        return json.dumps(list_dictionaries or [])
