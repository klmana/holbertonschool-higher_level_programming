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
    if type(text) != str:
        raise TypeError('text must be a string')

    delimiter = '.?:'
    index = 0
    while index < len(text) and text[index] == ' ':
        index += 1
    while index < len(text):
        print(text[index], end='')
        if text[index] == '\n' or text[index] in delimiter:
            print('\n')
        index += 1
        while index < len(text) and text[index] == ' ':
            index += 1
        continue
    index += 1
