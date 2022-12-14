#!/usr/bin/python3
"""
  Module:
  This class will be the “base” of all other classes in this project.
  The goal of it is to manage id attribute in all your future classes
  and to avoid duplicating the same code (by extension, same bugs)
"""

import os
import csv
import json


class Base:
    """
      Base Class
      Attributes:
      _nb_objects: number of objects created
      id: id of object an integer and need to test the type of it
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
          Init base method
          args:
          id: id of the  object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
          That returns the JSON string representation of list_dictionaries:
          Args:
          List_dictionaries: The list of the dictionaries
          Return: The JSON string representation of list_dictionaries:
        """
        return json.dumps(list_dictionaries or [])

    @classmethod
    def save_to_file(cls, list_objs):
        """
          That writes the JSON string representation of list_objs to a file:
          Args:
          List_objs: List of instances who inherits of Base - example:
          list of Rectangle or list of Square instances
        """
        if list_objs:
            js_string = cls.to_json_string([obj.to_dictionary()
                                            for obj in list_objs])
        else:
            js_string = '[]'
        with open(cls.__name__ + '.json', 'w') as f:
            f.write(js_string)

    @staticmethod
    def from_json_string(json_string):
        """
          That returns the list of the JSON string representation json_string:
          Args:
          Json_string: String representing a list of dictionaries
          Return: The list represented by json_string
        """
        if json_string:
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        """
          That returns an instance with all attributes already set:
          Args:
          Dictionary: Of as a double pointer to a dictionary
          Return: instance with create a “dummy”
        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        if cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''
          That returns a list of instances:
          Return: List of instances - the type of these instances depends
          on cls (current class using this method)
        '''
        try:
            filename = cls.__name__ + '.json'
            with open(filename, mode='r') as f:
                for_list = cls.from_json_string(f.read())
            return [cls.create(**for_item) for for_item in for_list]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
          Save to a csv file
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w") as f:
            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            elif cls.__name__ == "Square":
                fieldnames = ["id", "size", "x", "y"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        '''
          Deserializes CSV format from a file.
        '''
        filename = cls.__name__ + ".csv"
        for_list = []
        with open(filename) as f:
            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            elif cls.__name__ == "Square":
                fieldnames = ["id", "size", "x", "y"]
            reader = csv.DictReader(f, fieldnames=fieldnames)
            for_list_d = {}
            for_list_d2 = []
            for d in reader:
                for k, v in dict(d).items():
                    for_list_d[k] = int(v)
                for_list_d2.append(cls.create(**for_list_d))
            return for_list_d2
