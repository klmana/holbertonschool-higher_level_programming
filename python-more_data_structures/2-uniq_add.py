#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    for number in set(my_list):
        add += number
    return add
