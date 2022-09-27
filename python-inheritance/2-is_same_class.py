#!/usr/bin/python3
"""
 Function to check class if the object is
 exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """
     Check for class if same type of the object
     obj: object import
     Return: True or False otherwise
    """

    if type(obj) is a_class:
        return True
    else:
        return False
