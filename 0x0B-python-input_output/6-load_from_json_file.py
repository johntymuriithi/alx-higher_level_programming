#!/usr/bin/python3
"""
    this method writes to file
    """


def load_from_json_file(filename):
    """
    this method writes to file
    """
    mod = __import__('json')
    with open(filename, 'r', encoding="utf-8") as filee:
        num = mod.load(filee)
        return num
