#!/usr/bin/python3
"""
  function that writes an Object
  to a text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
      write an object to a text file
      my_obj: Object to manipulate for
      filename: Text file to write for
      Return: object
    """

    with open(filename, "w", encoding="utf-8") as f:
        written = json.dump(my_obj, f)
    return written
