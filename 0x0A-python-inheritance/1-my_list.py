#!/usr/bin/python3
"""
This code returns list of all availble attributes and methods of an object

"""


class MyList(list):
    """
    a function to list attributes and methods
    its well defined
    """

    def print_sorted(self):
        for item in self:
            if not isinstance(item, int):
                raise TypeError("Must be an integer")
        sort = sorted(self)
        print(sort)
