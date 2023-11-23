#!/usr/bin/python3
"""
simple function that adds to integers
lets look at it
"""


def add_integer(a, b=98):
    """
    method that adds two numbers
    returns sum
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        a = int(b)
    return int(a) + int(b)
