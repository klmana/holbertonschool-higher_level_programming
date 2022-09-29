#!/usr/bin/python3
"""
  function that returns an object
  (Python data structure) represented by a JSON string:
"""
import json


def from_json_string(my_str):
    """
      convert str to object
      my_str: string to convert
      Return: object (Python data structure)represented by JSON string:
    """

    return json.loads(my_str)
