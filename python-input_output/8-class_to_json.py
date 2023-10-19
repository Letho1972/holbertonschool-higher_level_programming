#!/usr/bin/python3

"""8-class_to_json module"""


def class_to_json(obj):
    """
    Converts a Python object to a JSON serializable dictionary.

    Args:
        obj (object): The Python object to be converted.

    Returns:
        dict: A dictionary that can be serialized to JSON.
    """
    return obj.__dict__
