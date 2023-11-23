#!/usr/bin/python3
"""
simple function that adds to integers
"""


def print_square(size):
    """
    this method divides elements of a matrix
    It is well done
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    else:
        for _ in range(size):
            print("#" * size)
