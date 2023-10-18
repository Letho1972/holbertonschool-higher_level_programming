#!/usr/bin/python3

""" 0-read_file module """


def read_file(filename=""):
    """
    Reads and prints the contents of a text file.

    Args:
        filename (str): The name of the file to be read.
        Defaults to an empty string.

    Returns:
        None

    Raises:
        FileNotFoundError: If the specified file is not found.

        UnicodeDecodeError: If an error occurs while decoding
        the file with utf-8 encoding.

    Usage:
        >>> read_file('example.txt')
        This is an example text file.
        It contains multiple lines.
        Each line is separated by a newline character.
    """
    with open(filename, 'r', encoding="utf-8") as file:
        read_data = file.read()
    print(read_data, end='')
