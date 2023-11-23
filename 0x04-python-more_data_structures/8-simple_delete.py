#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    index = list(a_dictionary.keys())
    if key in index:
        del a_dictionary[key]
    return a_dictionary
