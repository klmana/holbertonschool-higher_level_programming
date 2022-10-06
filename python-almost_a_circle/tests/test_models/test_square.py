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


if __name__ == "__main__":
    unittest.main()
