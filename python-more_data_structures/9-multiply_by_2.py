#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for my_list in a_dictionary:
        new_dictionary[my_list] = a_dictionary[my_list] * 2
    return (new_dictionary)
