#!/usr/bin/python3
'''
Unit test for Base class
'''

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest
import sys
import json
import os
from unittest.mock import patch
from io import StringIO


class TestBase(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_base_docs(self):
        """
          To check docstring for all methods
        """
        module_docs = "models.base".__doc__
        self.assertTrue(len(module_docs) > 1)

        class_docs = Base.__doc__
        self.assertTrue(len(class_docs) > 1)

    def test_obj_id(self):
        """
         To check if id is assigning correctly on it
        """
        my_obj = Base()
        my_obj_2 = Base(24)
        my_obj_3 = Base()
        self.assertEqual(self.my_obj.id, 1)
        self.assertEqual(self.my_obj_2.id, 24)
        self.assertEqual(self.my_obj_3.id, 2)
