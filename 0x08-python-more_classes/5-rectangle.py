#!/usr/bin/python3

"""
Create class Rectangle that defines a rectangle by
private instance attribute: width:, and
private instance attribute: height:
Methods getter and Setter properties for the width and height
And raising errors if certain conditionas are not met.
"""


class Rectangle:
    """
    Instantiating variables of width and height

    Args:
        width (int)
        height (int)
    Dazzit, Dazzall.
    """
    def __init__(self, width=0, height=0):
        # initialize private attributes
        self.height = height
        self.width = width

    @property
    def width(self):
        # property to retrive width
        return self.__width

    @width.setter  # setter method for width
    def width(self, value):
        # verify that value is an integer
        if type(value) is not int or isinstance(value, (float, bool)):
            raise TypeError("width must be an integer")

        # check that value is >= 0
        if value < 0:
            raise ValueError("width must be >= 0")

        # update private instance attribute
        self.__width = value

    @property
    def height(self):
        # property to retrive height
        return self.__height

    @height.setter  # setter method for height
    def height(self, value):
        # verify that value is an integer
        if type(value) is not int or isinstance(value, (float, bool)):
            raise TypeError("height must be an integer")

        # check that value is >= 0
        if value < 0:
            raise ValueError("height must be >= 0")

        # update private instance attribute
        self.__height = value

    def area(self):
        return self.__height * self.width

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""

        result = ""
        for _ in range(self.__height):
            result += "#" * self.__width + "\n"

        return result.rstrip("\n")

    def __repr__(self):
        """Return a string representation of the rectangle for eval()."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
