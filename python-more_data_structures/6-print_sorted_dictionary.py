#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for key, key_dictionary in sorted(a_dictionary.items()):
        print("{}: {}".format(key, key_dictionary))
