#!/usr/bin/python3
""" test casesfor Square class """


import unittest
from unittest import mock
import io
from models.square import Square


class TestSquare(unittest.TestCase):
    '''
    Testing Square
    '''

    def test_instance(self):
        '''
        test input size correct standard
        '''

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
            Square(1, 0)

        with self.assertRaises(ValueError):
            Square(1, 2, -3)

        with self.assertRaises(TypeError):
            Square(1, 2)

        with self.assertRaises(TypeError):
            Square(1, 2, 3)

        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4)

        with self.assertRaises(ValueError):
            Square(0)


if __name__ == "__main__":
    unittest.main()
