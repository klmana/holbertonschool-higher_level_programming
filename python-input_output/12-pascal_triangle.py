#!/usr/bin/python3
"""
  Create a function def pascal_triangle(n):
  that returns a list of lists of integers
  representing the Pascal’s triangle of n:
"""


def pascal_triangle(n):
    """
      Returns list of lists of integers representing
      the Pascal’s triangle of n:
      n: size of the triangle (row)
      Returns: pascal list of list of integers
    """

    if n <= 0:
        return []

    plist = [[0 for x in range(col + 1)] for col in range(n)]
    plist[0] = [1]

    for col in range(1, n):
        plist[col][0] = 1
        for row in range(1, col + 1):
            if row < len(plist[col - 1]):
                plist[col][row] = plist[col - 1][row - 1] + plist[col - 1][row]
            else:
                plist[col][row] = plist[col - 1][0]
    return plist
