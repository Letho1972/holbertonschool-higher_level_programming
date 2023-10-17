#!/usr/bin/python3

""" module 11-square """

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square.

    This class inherits from the Rectangle class
    and extends it to specifically handle squares.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(size): Initializes a new Square
        instance with the specified size.

    """
    def __init__(self, size):
        """
        Initialize a new Square.

        Parameters:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square, which is the square of its size.

        Example:
            >>> square = Square(5)
            >>> square.area()
            25
        """
        return self.__size ** 2

    def __str__(self):
        """
        Generate a string representation of the Square.

        Returns:
            str: A formatted string indicating that this is a Square object
            along with its width and height.

        Example:
            >>> square = Square(5)
            >>> print(square)
            [Square] 5/5
    """
        return "[Square] {}/{}".format(self.__size, self.__size)
