#!/usr/bin/python3
"""
  function that adds a new attribute
  to an object if it’s possible:
"""


def add_attribute(obj, objname, value):
    """
       obj: class object to add attribute
       objname: object name
       value: value of attribute to add
    """
    if not hasattr(obj, "__dict__") and not hasattr(an_obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, objname, value)
