#!/usr/bin/python3
""" test casesfor Square class """


import unittest
import pep8
import inspect
import io
import json
import os
from contextlib import redirect_stdout
from models import square
from models.base import Base
Square = square.Square


class TestSquareDocs(unittest.TestCase):
    """
      Test the Square class style and documentation
    """
    @classmethod
    def setUpClass(cls):
        """
          Set up for the doc tests
        """
        cls.sq_funcs = inspect.getmembers(Square, inspect.isfunction)
