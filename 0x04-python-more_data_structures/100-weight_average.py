#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    mul = 0
    num1 = 0
    for item in my_list:
        summ = 0
        a, b = item
        summ = a * b
        num1 += summ
    for item in my_list:
        mul += item[1]
    return num1 / mul
