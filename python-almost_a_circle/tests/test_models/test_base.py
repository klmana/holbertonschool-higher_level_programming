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

    def setUpClass(cls):
        """
         Test setup of class
        """

        cls.bs1 = Base()
        cls.bs2 = Base(100)
        cls.bs3 = Base()

    def tearDownClass(cls):
        """
          Test clear objects after all test
        """
        del cls.bs1
        del cls.bs2
        del cls.bs3

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
        self.assertEqual(self.bs1.id, 1)
        self.assertEqual(self.bs2.id, 100)
        self.assertEqual(self.bs3.id, 2)

    def test_obj_id_exist(self):
        """
          Test if obj id increments correctly
        """
        self.assertIsNotNone(self.bs1.id)
        self.assertIsNotNone(Base._Base__nb_objects)

    def test_clsVar_match_id(self):
        """
          Test match class var to obj id
        """
        self.assertEqual(Base._Base__nb_objects, self.sq1.id)

    def test_obj_id(self):
        """
          Test if id is assigning correctly
        """
        self.assertEqual(self.bs1.id, 1)

    def test_base_methods(self):
        """
          Test if method exists in base
        """
        self.assertTrue(hasattr(Base, "__init__"))
        self.assertTrue(hasattr(Base, "integer_validator"))
        self.assertTrue(hasattr(Base, "integer_validator2"))
        self.assertTrue(hasattr(Base, "to_json_string"))
        self.assertTrue(hasattr(Base, "from_json_string"))
        self.assertTrue(hasattr(Base, "save_to_file"))
        self.assertTrue(hasattr(Base, "create"))
        self.assertTrue(hasattr(Base, "load_from_file"))

    def test_to_json(self):
        """
          Test save list to json
        """
        list1 = [
            {'id': 100},
            {'height': 88},
            {'width': 1, 'id': 2, 'height': 88},
            {'id': 4, 'height': 144, 'weight': 700},
            {'width': 22, 'height': 11}
        ]
        empty = []

        base_to_json = Base.to_json_string(list1)

        base_to_empty_json = Base.to_json_string(empty)

        self.assertIsInstance(list1, list)
        self.assertIsInstance(base_to_json, str)

        self.assertIsInstance(empty, list)
        self.assertIsInstance(base_to_empty_json, str)

        base_from_json = Base.from_json_string(rect_to_json)

        self.assertIsInstance(base_from_json, list)


if __name__ == "__main__":
    unittest.main()
