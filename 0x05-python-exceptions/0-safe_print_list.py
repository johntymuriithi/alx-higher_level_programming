#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        num = 0
        for index, element in enumerate(my_list):
            if index == x:
                break
            print(element, end='')
            num += 1
        print()
        return num
    except IndexError as err:
        print(f"Error Occurred: {err}")
