#!/usr/bin/python3
"""
  Class Student that defines a student
  by:(based on 9-student.py)
"""


class Student:
    """
      Student class that defines a student
      Public instance attributes:
      : first_name
      : last_name
      : age
    """

    def __init__(self, first_name, last_name, age):
        """
          initialize the method of the student intance
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
          That retrieves a dictionary representation of student instance
          Attrs: list of attributes
          Return: The dictionary representation of
          a Student instance (same as 8-class_to_json.py):
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
