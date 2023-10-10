#!/usr/bin/python3
"""This module print a square"""


class Square:
    """This is the Square class it attribute is __size of the square
    that prints in stdout the square with the character #"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        for x in range(self.__size):
            print("#" * self.__size)
