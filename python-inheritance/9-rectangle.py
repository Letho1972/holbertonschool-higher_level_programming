#!/usr/bin/python3


""" module 8-rectangle """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle.

    This class inherits from the BaseGeometry class
    and extends it to specifically handle rectangles.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.

    Methods:
        __init__(width, height): Initializes a new Rectangle
        instance with the specified width and height.

    """
    def __init__(self, width, height):
        """
        Initialize a new Rectangle.

        Parameters:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If either width or height is not an integer.
            ValueError: If either width or height is less than or equal to 0.
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
    Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle, which is the product of
            its width and height.

        Example:
            >>> rect = Rectangle(5, 7)
            >>> rect.area()
        35
        """
        return self.__height * self.__width

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
            str: A string in the format "[Rectangle] <width>/<height>".

        Example:
            >>> rect = Rectangle(5, 7)
            >>> str(rect)
            '[Rectangle] 5/7'
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
