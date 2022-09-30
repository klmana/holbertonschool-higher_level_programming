#!/usr/bin/python3
"""
  function that returns the dictionary description with
  simple data structure (list, dictionary, string, integer and boolean)
  for JSON serialization of an object:
"""


def class_to_json(obj):
    """
      returns dict description data structure
      obj: Object for JSON serialization of
      Return: The dictionary description with simple data structure
    """
    return obj.__dict__
