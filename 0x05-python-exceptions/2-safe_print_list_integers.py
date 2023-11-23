#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        num = 0
        for index, element in enumerate(my_list):
            if type(element) != int:
                continue
            if index == x:
                break
            print("{:d}".format(element), end='')
            num += 1
        print()
        return num
    except Exception:
        print("Error Occurred:")
