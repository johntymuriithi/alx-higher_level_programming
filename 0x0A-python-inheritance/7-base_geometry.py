#!/usr/bin/python3
"""
This code returns list of all availble attributes and methods of an object

"""


class BaseGeometry:
    """
    this is empty
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if not isinstance(name, str):
            raise TypeError(f"{name} must be a string")
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
