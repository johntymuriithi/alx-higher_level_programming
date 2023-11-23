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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        i = 1
        if self.__size == 0:
            print()
        size = self.__size ** 2
        for x in range(size):
            print("#", end="")
            if i == self.__size:
                print()
                i = 0
            i += 1
