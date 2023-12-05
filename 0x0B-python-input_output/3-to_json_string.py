#!/usr/bin/python3
"""
    this method converts / serializea python objects
    """


def to_json_string(my_obj):
    """
    this method converts / serializea python objects
    """
    mod = __import__('json')
    lists = mod.dumps(my_obj)
    return lists
