#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    return (sum([number_0 * number_1 for number_0, number_1 in my_list]) / sum(number_1 for number_0, number_1 in my_list))
