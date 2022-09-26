#!/usr/bin/python3
class LockedClass:
    """
    Locked class that prevents user dynamically create the instance
    attribute is called 'first_name'
    """

    def __init__(self, first_name=""):
        self.first_name = first_name

    __slots__ = ["first_name"]
