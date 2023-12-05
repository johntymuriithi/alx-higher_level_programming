#!/usr/bin/python3
"""
    this method writes to file
    """


def append_write(filename="", text=""):
    """
    this method writes to file at the end
    """
    with open(filename, 'a', encoding="utf-8") as myfile:
        num = myfile.write(text)
        return num
