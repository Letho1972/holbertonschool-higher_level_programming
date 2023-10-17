#!/usr/bin/python3

""" Module 0-lookup """


def lookup(obj):
    """
    Function that return the list of available attributes
    and methods of an object

    Args:
        obj: object to check

    Returns:
        the list  of an object
    """
    return dir(obj)
