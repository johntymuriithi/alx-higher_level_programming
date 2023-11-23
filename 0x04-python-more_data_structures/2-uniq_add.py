#!/usr/bin/python3
def uniq_add(my_list=[]):
    summ = 0
    lists = list(set(my_list))
    for item in lists:
        summ += item
    return summ
