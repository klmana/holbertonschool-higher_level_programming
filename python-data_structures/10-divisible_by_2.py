#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    mynew_list = []
    if my_list:
        for letter in my_list:
            if letter % 2 == 0:
                mynew_list.append(True)
            else:
                mynew_list.append(False)
        return mynew_list
