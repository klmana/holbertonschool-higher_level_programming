#!/usr/bin/python3
"""
 function that appends a string at the end of a text file
 (UTF8) and returns the number of characters added:
"""


def append_write(filename="", text=""):
    """
      Append to file with text
      filename: Add to this object
      text: The string to append
      return: The umber of characters added
    """

    with open(filename, mode="a", encoding="utf-8") as f:
        if f.write(text):
            return len(text)
