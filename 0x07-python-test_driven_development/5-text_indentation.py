#!/usr/bin/python3
"""
this is tdd
no playin
"""
def text_indentation(text):
    """
    this method divides elements of a matrix
    It is well done
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    for item in text:

        i += 1
        if item == '.' or item == '?' or item == ':':
            print(item, end="")
            print()
            print()
            continue
        print(item, end="")
        if i == len(text):
            print()
