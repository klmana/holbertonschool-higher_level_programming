#!/usr/bin/python3
"""
Creates the MyList class inheriting
"""


class MyList(list):
    """
    class MyList that inherits from list
    """
    def __init__(self):
        """
        initialize the object
        """
        super().__init__()

    def print_sorted(self):
        """
        prints the sorted list (ascending sort)
        """
        print(sorted(self))
