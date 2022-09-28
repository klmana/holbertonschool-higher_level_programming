#!/usr/bin/python3
"""
  Class MyInt that inherits from int:
"""


class MyInt(int):
    """
      Class with int object MyInt
      has == and != operators inverted
    """

    def __eq__(self, other):
        """
          eq:equal equal method
          to see if it knows how to compare itself to an int.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
          ne:not equal method
        """
        return super().__eq__(other)
