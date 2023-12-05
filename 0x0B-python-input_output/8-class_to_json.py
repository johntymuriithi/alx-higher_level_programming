#!/usr/bin/python3
"""
method
"""


def class_to_json(obj):
    """
    Serialize an object

    Args:
    obj: An instance of a class with serializable attributes.

    Returns:
    dict: A dictionary representation of the object.
    """
    if not isinstance(obj, object):
        raise ValueError("Input must be an instance of a class")

    obj_dict = vars(obj)

    for key, value in obj_dict.items():
        if isinstance(value, (list, dict, str, int, bool)):
            continue
        elif isinstance(value, object):
            obj_dict[key] = class_to_json(value)

    return obj_dict
