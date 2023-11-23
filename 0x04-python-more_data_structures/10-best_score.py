#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    value = list(a_dictionary.values())
    maxv = value[0]
    for item in value:
        if item > maxv:
            maxv = item
    for itemm in a_dictionary:
        if a_dictionary[itemm] == maxv:
            return itemm
