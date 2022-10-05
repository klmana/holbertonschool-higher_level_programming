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

    def setUpClass(cls):
        """
         Test setup of class
        """

        b1 = Base()
        b2 = Base(100)
        b3 = Base()

    def tearDownClass(cls):
        """
          Test clear objects after all test
        """
        del b1
        del b2
        del b3

    def test_output(self):
        """
          Test to stdout
        """
        school = 'Coding'
        language = 'Python3'
        testing = 'Unittest'
        expected_output = "{} {} {}".format(school, language, testing)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            print('Coding Python3 Unittest')
            self.assertEqual(fake_out.getvalue().strip(), expected_output)

    def test_base_cls_doc(self):
        """
          Test if docstring for class is present
        """
        self.assertIsNotNone(Base.__doc__)

    def test_base_methods_doc(self):
        """
          Test if docstring exist for all methods
        """
        self.assertTrue(Base.__init__.__doc__)
        self.assertTrue(Base.integer_validator.__doc__)
        self.assertTrue(Base.integer_validator2.__doc__)
        self.assertTrue(Base.to_json_string.__doc__)
        self.assertTrue(Base.from_json_string.__doc__)
        self.assertTrue(Base.save_to_file.__doc__)
        self.assertTrue(Base.create.__doc__)
        self.assertTrue(Base.load_from_file.__doc__)

    def test_class_var_exist(self):
        """
          Test if class variable has a value after instantiation
        """
        self.assertIsNotNone(Base._Base__nb_objects)

    def test_base_init_id(self):
        """
          Test Base initiation
        """
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 100)
        self.assertEqual(self.b3.id, 2)

    def test_obj_id_exist(self):
        """
          Test if obj id increments correctly
        """
        self.assertIsNotNone(self.bs1.id)
        self.assertIsNotNone(Base._Base__nb_objects)


if __name__ == "__main__":
    unittest.main()
