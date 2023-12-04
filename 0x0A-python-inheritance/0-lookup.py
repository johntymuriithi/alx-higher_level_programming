#!/usr/bin/python3
"""
This code returns list of all availble attributes and methods of an object

"""


def lookup(obj):
    """
    a function to list attributes and methods
    its well defined
    """
    listt = dir(obj)
    return listt
