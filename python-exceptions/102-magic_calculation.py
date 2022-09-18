#!/usr/bin/python3
def magic_calculation(a, b):
    the_result = 0
    for my_function in range(1, 3):
        try:
            if my_function > a:
                raise Exception('Too far')
            else:
                the_result += (a ** b) / my_function
        except:
            the_result = b + a
            break
    return the_result
