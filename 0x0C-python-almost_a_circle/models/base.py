#!/usr/bin/python3
"""
Almost a circle project
"""


class Base:
    """This is a base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
My rectangle class
"""

        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            mod = __import__('json')
            return mod.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
My rectangle class
"""

        if list_objs is None:
            list_objs = []

        objs = [obj.to_dictionary() for obj in list_objs]

        jsonn = cls.to_json_string(objs)

        filename = f"{cls.__name__}.json"
        with open(filename, 'w') as file:
            file.write(jsonn)

    @staticmethod
    def from_json_string(json_string):
        """return string to json"""
        if json_string is None or not json_string:
            return []
        else:
            mod = __import__('json')
            return mod.loads(json_string)
