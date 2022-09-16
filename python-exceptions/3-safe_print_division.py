#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        the_result = a / b
    except ZeroDivisionError:
        the_result = None
    finally:
        print("Inside result: {}".format(the_result))
    return the_result
