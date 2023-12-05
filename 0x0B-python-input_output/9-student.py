#!/usr/bin/python3
"""
    class to json
    """


class Student:
    """
    class to json
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        class to json
        """
        obj_dict = vars(self)

        for key, value in obj_dict.items():
            if isinstance(value, (list, dict, str, int, bool)):
                continue
            elif isinstance(value, object):
                obj_dict[key] = to_json(value)

        return obj_dict
