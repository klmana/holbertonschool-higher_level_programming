#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mynew_matrix = [[numbers ** 2 for numbers in row] for row in matrix]
    return mynew_matrix
