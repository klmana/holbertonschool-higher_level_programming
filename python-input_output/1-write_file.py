#!/usr/bin/python3
"""
 function that writes a string to a text file
 (UTF8) and returns the number of characters written:
"""


def write_file(filename="", text=""):
    """
      Write a string to a text file UTF8.
      filename : The name of the file.
      text (str): The text to write to the file.
      Return: The number of characters written.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
