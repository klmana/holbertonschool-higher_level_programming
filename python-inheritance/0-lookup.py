#!/usr/bin/python3
""" Defines an object attributes and
    methods lookup function.
"""


def lookup(obj):
    """ Return a list of an object available
        attributes and methods of an object:
    """
    return (dir(obj))
