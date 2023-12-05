#!/usr/bin/python3
"""
    this method prints out the contents of a file and it opens it
    """


def read_file(filename=""):
    """
    this method prints out the contents of a file and it opens it
    """
    with open(filename, 'r', encoding="utf-8") as myfile:
        filee = myfile.read()
        print(filee, end='')
