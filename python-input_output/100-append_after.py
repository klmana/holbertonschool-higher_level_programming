#!/usr/bin/python3
"""
  function that inserts a line of text to a file,
  after each line containing a specific string (see example):
"""


def append_after(filename="", search_string="", new_string=""):
    """
      Append The method
    """

    for_string = ""
    with open(filename, encoding="utf-8") as f:
        for line in f:
            for_string += line
            if search_string in line:
                for_string += new_string
    with open(filename, mode="w") as f:
        f.write(for_string)
