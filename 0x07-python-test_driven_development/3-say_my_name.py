#!/usr/bin/python3
"""
simple function that adds to integers
"""


def say_my_name(first_name, last_name=""):
    """
    this method divides elements of a matrix
    It is well done
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print(f"My name is {first_name} {last_name}")
