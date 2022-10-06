#!/usr/bin/python3
""" test casesfor Square class """


import unittest
import os
import json
from unittest import mock
import io
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Testing Square
    """

    def test_instance(self):
        """
        test input size correct standard
        """

        s = Square(6)
        self.assertEqual(s.width, 6)
        self.assertEqual(s.height, 6)

        with self.assertRaises(TypeError):
            Square(5, "1")

        with self.assertRaises(TypeError):
            Square()

        with self.assertRaises(TypeError):
            Square("1")

        with self.assertRaises(ValueError):
            Square(2, -1, 0, 50)

        with self.assertRaises(ValueError):
            Square(-5, 3, 4)

        with self.assertRaises(TypeError):
            Square(1, 2, "3")

        with self.assertRaises(ValueError):
            Square(1, -2)

        with self.assertRaises(ValueError):
            Square(-1, 2)

        with self.assertRaises(ValueError):
            Square(0, 2)

        with self.assertRaises(ValueError):
            Square(1, 2, -3)

        with self.assertRaises(ValueError):
            Square(0)

        s1 = Square(1, 2, 3)
        self.assertEqual(s1.width, 1)
        self.assertEqual(s1.height, 1)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)

        s2 = Square(1, 2)
        self.assertEqual(s2.width, 1)
        self.assertEqual(s2.height, 1)
        self.assertEqual(s2.x, 2)

        s3 = Square(1, 2, 3, 4)
        self.assertEqual(s3.width, 1)
        self.assertEqual(s3.height, 1)
        self.assertEqual(s3.x, 2)
        self.assertEqual(s3.y, 3)
        self.assertEqual(s3.id, 4)

    def test_str_for_square(self):
        """
          Test __str__
        """
        s3 = Square(1, 2, 3, 4)
        self.assertEqual(str(s3), "[Square] (4) 2/3 - 1")

    def test_to_dictionary(self):
        """
            Test method to_dictionary
        """
        s1 = Square(1, 2, 3)
        s1_dictionary = s1.to_dictionary()
        s_dictionary = {'x': 2, 'y': 3, 'id': 3, 'size': 1}
        self.assertEqual(len(s1_dictionary), len(s_dictionary))
        self.assertEqual(type(s1_dictionary), dict)
        s4 = Square(1, 1)
        s4.update(**s1_dictionary)
        s4_dictionary = s4.to_dictionary()
        self.assertEqual(len(s1_dictionary), len(s4_dictionary))
        self.assertEqual(type(s4_dictionary), dict)
        self.assertFalse(s1 == s4)

    def test_created(self):
        """
          Test of Square.create(**{ 'id': 89 }) in Square exists
        """
        s1 = Square.create(**{'id': 89})
        self.assertEqual(s1.id, 89)

        s1 = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)

        s1 = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)

        s1 = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)

    def test_save_to_file(self):
        """
          Test normal load from file
        """
        s1 = Square(7, 3)
        s2 = Square(8)
        squares_input = [s1, s2]
        Square.save_to_file(squares_input)
        squares_output = Square.load_from_file()
        for x in zip(squares_input, squares_output):
            self.assertEqual(str(x[0]), str(x[1]))

    def test_load_from_file(self):
        """
          Test normal load from file
        """
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        squares_output = Square.load_from_file()
        self.assertEqual(squares_output, [])

    def test_save_to_file_none(self):
        """
          Test that `save_to_file() works
        """
        s1 = Square(7, 8, 1)
        s2 = Square(2)
        Square.save_to_file(None)
        self.assertIs(os.path.exists("Square.json"), True)
        with open("Square.json", 'r') as file:
            self.assertEqual(json.loads(file.read()), json.loads('[]'))
        os.remove("Square.json")

    def test_squ_save_to_file(self):
        """
          Test save to file method for Square
        """
        s1 = Square(5)
        filename = 'Square.json'
        Square.save_to_file(None)
        with open(filename, 'r', encoding='utf-8') as f:
            result = f.read()
            self.assertEqual(result, '[]')
        if os.path.exists(filename):
            os.remove(filename)
            Square.save_to_file([])
        with open(filename, 'r', encoding='utf-8') as f:
            result = f.read()
            self.assertEqual(result, '[]')
        if os.path.exists(filename):
            os.remove(filename)
        Square.save_to_file([s1])
        self.assertTrue(os.path.exists(filename))
        with open(filename, 'r', encoding='utf-8') as f:
            result = f.read()
            result = json.loads(result)
            self.assertEqual(result, [s1.to_dictionary()])
        if os.path.exists(filename):
            os.remove(filename)


if __name__ == "__main__":
    unittest.main()
