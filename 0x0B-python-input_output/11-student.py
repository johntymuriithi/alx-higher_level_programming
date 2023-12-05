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

    def to_json(self, attrs=None):
        """our method"""
        ob = vars(self)
        if attrs is None:
            return ob
        else:
            return {
             key: value for key, value in ob.items() if key in attrs
            }

    def reload_from_json(self, json):
        if isinstance(json, dict):
            for key, value in json.items():
                if hasattr(self, key):
                    setattr(self, key, value)
