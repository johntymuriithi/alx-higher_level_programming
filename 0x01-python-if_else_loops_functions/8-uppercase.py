#!/usr/bin/python3
caps = ""


def uppercase(input_str):
    global caps
    for st in input_str:
        if 'a' <= st <= 'z':
            caps += "{}".format(chr(ord(st) - ord('a') + ord('A')))
        else:
            caps += st
    print(caps)
