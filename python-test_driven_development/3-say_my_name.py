#!/usr/bin/python3
"""
    This function that prints 'My name is <first name> <last name>' using
    by following the methods:
    say_my_name.
"""

def say_my_name(first_name, last_name=''):
    """
    prints a (string)My name is
    <first name> <last name>
    """
    if type(first_name) != str:
        raise TypeError('first_name must be a string')
    elif type(last_name) != str:
        raise TypeError('last_name must be a string')
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))
