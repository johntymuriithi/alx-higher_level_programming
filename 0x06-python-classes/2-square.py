#!/usr/bin/python3
"""This is a class

It is not empty

"""


class Square:
    """Class object.

    It is not empty.

    """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
