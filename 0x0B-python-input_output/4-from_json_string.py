#!/usr/bin/python3
"""
    this method converts / deserilize python objects to json
    """


def from_json_string(my_str):
    """
    this method converts / deserilize python objects to json
    """
    mod = __import__('json')
    lists = mod.loads(my_str)
    return lists
