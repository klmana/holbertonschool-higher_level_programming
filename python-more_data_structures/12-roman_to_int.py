#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    nums = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    sum = 0
    for number in range(len(roman_string)):
        value = nums[roman_string[number]]
        if number + 1 < len(roman_string)and nums[roman_string[number + 1]
        ] > value:
            sum -= value
        else:
            sum += value
    return sum
