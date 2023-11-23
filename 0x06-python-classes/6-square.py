#!/usr/bin/python3
"""This is a class

It is not empty

"""


class Square:
    """Class object.

    It is not empty.

    """
    def __init__(self, size=0, position=(0, 0)):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if position[0] == "" or position[1] == "":
            raise TypeError("position must be a tuple of 2 positive integers")

        if not (isinstance(position[0], int) and isinstance(position[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")

        if position[1] < 0:
            raise ValueError("position must contain 2 positive integers")
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        space = " " * self.__position[0]
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(space + "#" * self.__size)
