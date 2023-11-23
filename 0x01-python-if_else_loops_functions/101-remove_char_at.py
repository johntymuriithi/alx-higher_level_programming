#!/usr/bin/python3
def remove_char_at(str, n):
    cpy = ""
    for i, st in enumerate(str):
        if i != n:
            cpy += st
    return (cpy)
