#!/usr/bin/python3
"""
Function if the object is an instance of
a class that inherited from the specified class
"""


def is_kind_of_class(obj, a_class):
    """
      check if object is instance of
      obj: object of the argument
      Return: True or False otherwise
    """

    return isinstance(obj, a_class)
