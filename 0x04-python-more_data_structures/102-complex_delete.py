#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key = list(a_dictionary.values())
    if value not in key:
        return a_dictionary

    new = []

    for item, index in a_dictionary.items():
        if index == value:
            new.append(item)
    for num in new:
        del a_dictionary[num]
    return a_dictionary
