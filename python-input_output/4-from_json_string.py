#!/usr/bin/python3

""" 4-from_json_string module"""
import json


def from_json_string(my_str):
    """
    Select a JSON formatted string into a Python object.

    Args:
        my_str (str): A JSON formatted string.

    Returns:
        obj: The Python object selected from the input string.

    Raises:
        JSON codeError: If the input string is not valid JSON.

    Example:
        >>> from_json_string('{"key": "value"}')
        {'key': 'value'}
    """
    return json.loads(my_str)
