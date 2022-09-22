#!/usr/bin/python3

"""
    This function that  prints a text with 2 new lines after each of these
    characters: ., ? and :
    text_indentation
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    """
    delimiter = ".?:"
    index = 0
    if type(text) != str:
        raise TypeError('text must be a string')
    while index < len(text):
        print(text[index], end='')
        if text[index] in delimiter:
            print("\n")
            index += 2
        else:
            index += 1
