#!/usr/bin/python3
"""
Function if the object is an instance of a class that
inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
      Check if the object is an instance of a class that inherited
      obj: object to check
      a_class: class to check for
      returns: True or False otherwise
    """

    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
