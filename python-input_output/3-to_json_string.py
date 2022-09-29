#!/usr/bin/python3
"""
 function that returns the JSON
 representation of an object (string):
"""
import json


def to_json_string(my_obj):
    """
      return Json object as string
      my_obj: object to convert
      Return: The JSON representation of obj(string):
    """

    return json.dumps(my_obj)
