#!/usr/bin/python3
"""
    this method writes to file
    """


def save_to_json_file(my_obj, filename):
    """
    this method writes to file
    """
    mod = __import__('json')
    with open(filename, 'w', encoding="utf-8") as file:
        mod.dump(my_obj, file, ensure_ascii=False, indent=4)
