#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    list_element = 0
    try:
        while list_element < x:
            print('{:d}'.format(my_list[list_element]), end='')
            list_element += 1
    except:
        pass
    print()
    return list_element
