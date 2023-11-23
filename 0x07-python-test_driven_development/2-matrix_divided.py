#!/usr/bin/python3
"""
simple function that adds to integers
"""


def matrix_divided(matrix, div):
    """
    this method divides elements of a matrix
    It is well done
    """
    if len(matrix) == 0:
        raise ValueError("Empty")
    if len(matrix[0]) == 0:
        raise ValueError("Empty")
    if type(matrix) is not list:
        raise ValueError("Empty")
    if not matrix:
        raise ValueError("Matrix must be there")
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    outer = []
    size = len(matrix[0])

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        inner = []
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(msg)
            inner.append(round(item / div, 2))
        outer.append(inner)
    return outer
