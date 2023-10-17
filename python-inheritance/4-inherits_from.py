#!/usr/bin/python3

""" module 4-inherits_from """


def inherits_from(obj, a_class):
    """
    Check if an object inherits from a specified class.

    Parameters:
        obj (object): The object to be checked.
        a_class (class): The class to check for inheritance.

    Returns:
        bool: True if the object inherits from the
        specified class, False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
