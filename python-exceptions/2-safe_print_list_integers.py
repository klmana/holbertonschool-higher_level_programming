#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    list_element = 0
    for number in range(x):
        try:
            print("{:d}".format(my_list[number]), end='')
            list_element += 1
        except (TypeError, ValueError):
            pass
    print()
    return list_element
