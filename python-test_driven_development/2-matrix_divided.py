#!/usr/bin/python3
""" This function that divides all elements of a matrix.
 Divides each element of a matrix_divided(matrix, div).
 of numbers by a number
"""


def matrix_divided(matrix, div):
    """
    Returns a new matrix with the result
    by dividing all elements of a matrix.
    """
    resulta = 0
    new_matrix = []
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"
    matrix_len = len(matrix[0])
    for row in matrix:
        new_list = []
        if matrix_len != len(row):
            raise TypeError('Each row of the matrix must have the same size')
        for element in row:
            if type(element) != int and type(element) != float:
                raise TypeError(error_msg)
            if type(div) != int and type(div) != float:
                raise TypeError('div must be a number')
            if div == 0:
                raise ZeroDivisionError('division by zero')
            resulta = round(element / div, 2)
            new_list.append(resulta)
        new_matrix.append(new_list)
    return new_matrix
