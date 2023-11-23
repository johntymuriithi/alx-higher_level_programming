#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    index = list(a_dictionary.keys())
    if key in index:
        a_dictionary[key] = value
    elif key not in index:
        a_dictionary[key] = value
    return a_dictionary
