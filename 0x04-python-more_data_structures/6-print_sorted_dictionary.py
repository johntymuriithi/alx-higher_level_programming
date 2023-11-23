#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new = list(a_dictionary.keys())
    new.sort()
    for i, item in enumerate(new):
        print(f"{item}: {a_dictionary[item]}")
