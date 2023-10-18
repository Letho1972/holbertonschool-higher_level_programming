#!/usr/bin/python3
"""Simple module that append a text file and print it to stdout"""


def append_write(filename="", text=""):
    """Function that append a text file"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
