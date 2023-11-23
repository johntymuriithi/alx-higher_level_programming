#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = []
    for i, item in enumerate(my_list):
        if item == search:
            item = replace
        new.append(item)
    return new
