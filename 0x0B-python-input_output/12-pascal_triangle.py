#!/usr/bin/python3
""" Module that defines a function that returns a list of lists of integers"""


def pascal_triangle(n):
    """ Function that returns a list of lists of integers representing the
    Pascal's triangle of n
    """
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        triangle = [[1], [1, 1]]
        for i in range(2, n):
            row = [1]
            for j in range(1, i):
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            row.append(1)
            triangle.append(row)
        return triangle
