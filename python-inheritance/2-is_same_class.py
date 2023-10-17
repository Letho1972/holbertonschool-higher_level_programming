#!/usr/bin/python3

""" module 2-is_same_class """


def is_same_class(obj, a_class):
    """
    Check if the given object is an instance of the specified class.

    Args:
        obj (object): The object to be checked.
        a_class (type): The class type to compare against.

    Returns:
        that returns True if the object is exactly an instance of
        the specified class ; otherwise False.
    """
    return type(obj) is a_class
