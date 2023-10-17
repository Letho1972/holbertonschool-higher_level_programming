#!/usr/bin/python3

""" module 3-is_kind_of_class """


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of a specified class or a subclass of it.

    Args:
        obj (object): The object to be checked.
        a_class (class): The class to check against.

    Returns:
    True if the object is an instance of the specified
    class or a subclass of it, False otherwise.
    """
    return isinstance(obj, a_class)
