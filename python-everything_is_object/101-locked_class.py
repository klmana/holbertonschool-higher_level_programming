#!/usr/bin/python3
class LockedClass:
    """
    Locked class that prevents user dynamically create the instance
    attribute is called 'first_name'
    """
    __slots__ = ["first_name"]
