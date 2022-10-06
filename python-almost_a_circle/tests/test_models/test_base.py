#!/usr/bin/python3
"""
  Unit test for Base class
"""

import json
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
      Unit tests suite for Base class
    """
    def setUp(self):
        Base.__nb_objects = 0

    def test_constantId(self):
        """
          Test of Base for correctly initializing an id
        """
        __nb_objects = 0
        b = Base(5)
        self.assertEqual(b.id, 5)

    def test_autoId(self):
        """
          Test of Base for automatically assigning and incrementing an id
        """
        b = Base()
        self.assertEqual(b.id, 1)

    def test_to_json_string(self):
        """
          Test to_json_string(None)
        """
        diction = {'id': 1, 'x': 2, 'y': 3, 'width': 4, 'height': 5}
        json_dic = Base.to_json_string([diction])
        self.assertTrue(isinstance(diction, dict))
        self.assertTrue(isinstance(json_dic, str))
        self.assertCountEqual(
            json_dic, '[{"id": 1, "x": 2, "y": 3, "width": 4, "height": 5}]')
        json_d_1 = Base.to_json_string(None)
        self.assertEqual(json_d_1, '[]')
        ero = ('to_json_string() missing 1 required positional argument: ' +
               "'list_dictionaries'")
        with self.assertRaises(TypeError) as index:
            Base.to_json_string()
        self.assertEqual(ero, str(index.exception))
        ero = 'to_json_string() takes 1 positional argument but 2 were given'
        with self.assertRaises(TypeError) as index:
            Base.to_json_string([{1, 2}], [{3, 4}])
        self.assertEqual(ero, str(index.exception))

    def test_from_json_string(self):
        """
          Test from_json_string
          That json string return to list
        """
        string = '[{"id": 1, "x": 2, "y": 3, "width": 4, "height": 5}]'
        json_str = Base.from_json_string(string)
        self.assertTrue(isinstance(string, str))
        self.assertTrue(isinstance(json_str, list))
        self.assertCountEqual(
            json_str, [{'id': 1, 'x': 2, 'y': 3, 'width': 4, 'height': 5}])
        json_string_1 = Base.from_json_string(None)
        self.assertEqual(json_string_1, [])
        ero = ("from_json_string() missing 1 required positional argument:"
               + "'json_string'")
        with self.assertRaises(TypeError) as index:
            Base.from_json_string()
        self.assertEqual(ero, str(index.exception))
        ero = 'from_json_string() takes 1 positional argument but 2 were given'
        with self.assertRaises(TypeError) as index:
            Base.from_json_string('[1]', '[2]')
        self.assertEqual(ero, str(index.exception))


if __name__ == "__main__":
    unittest.main()
