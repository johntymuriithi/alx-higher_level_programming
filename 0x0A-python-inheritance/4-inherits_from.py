#!/usr/bin/python3
"""
This code returns list of all availble attributes and methods of an object

"""


def inherits_from(obj, a_class):
    """
    a function to list attributes and methods
    its well defined
    """
    return issubclass(type(obj), a_class)
