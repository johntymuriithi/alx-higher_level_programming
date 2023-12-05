#!/usr/bin/python3
"""
    this method writes to file
    """


def write_file(filename="", text=""):
    """
    this method writes to file
    """
    with open(filename, 'w', encoding="utf-8") as myfile:
        num = myfile.write(text)
        return num
