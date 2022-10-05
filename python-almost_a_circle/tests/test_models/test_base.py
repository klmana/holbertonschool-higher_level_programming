#!/usr/bin/python3
'''
Unit test for Base class
'''

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    '''
    Unit tests suite for Base class
    '''

    def test_constantId(self):
        '''
        Test of Base for correctly initializing an id
        '''
        b = Base(5)
        self.assertEqual(b.id, 5)

    def test_autoId(self):
        '''
        Test of Base for automatically assigning and incrementing an id
        '''
        b = Base()
        self.assertEqual(b.id, 1)


if __name__ == "__main__":
    unittest.main()
