#!/usr/bin/python3
"""
 function that reads a text file
 (UTF8) and prints it to stdout:
"""


def read_file(filename=""):
    """
      Read from filename  and prints it to stdout:
      filename: file to manipulate of the file
    """

    with open(filename, encoding="utf-8") as f:
        for line in f.read():
            print(line, end="")
