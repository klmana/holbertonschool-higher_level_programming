#!/usr/bin/python3

'''
Unit test for the Rectangle class
'''
import unittest
from unittest import mock
import io
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    '''
    Unit tests for Rectangle class
    '''

    def test_init(self):
        '''
        Test of Rectangle for width/height and default initialization
        '''
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 5)


if __name__ == "__main__":
    unittest.main()
