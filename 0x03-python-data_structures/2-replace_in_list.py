#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    new_list = []
    list_len = len(my_list) - 1
    if idx < 0:
        return my_list
    if idx > list_len:
        return my_list
    for i, item in enumerate(my_list):
        if i == idx:
            my_list[i] = element
            item = element
        new_list.append(item)
    return new_list
