#!/usr/bin/python3
"""
  Class Student that defines a student by:
"""


class Student:
    """Student class
    """

    def __init__(self, first_name, last_name, age):
        """initialize method of the student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
          retrieves a dictionary representation of student instance
        """
        return self.__dict__
