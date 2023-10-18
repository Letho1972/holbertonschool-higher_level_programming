#!/usr/bin/python3

""" 3-to_json_string module """
import json


def to_json_string(my_obj):
    """
    Function that returns the JSON representation of an object string.

    Args:
        my_obj (obj): Python object.

    Returns:
        str: JSON string representation of the object.
    """
    return json.dumps(my_obj)
