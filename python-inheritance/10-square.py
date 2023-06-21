#!/usr/bin/python3
"""A module with a BaseGeometry class"""


class BaseGeometry():
    """A base geometry class"""

    def area(self):
        """A public instance method that raises an Exception

        Args: nothing

        Returns: nothing

        Raises: Exception
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A public instance method that valides value argument.

        Args:
            name (str): Name attached to the values
            value (int): Value, must be a positive integer

        Returns: nothing

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less or equal to 0
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """subclass defining a rectangle

    Args:
        BaseGeometry (class): base geometries lol
    """

    def __init__(self, width, height):
        """initiates rectangles

        Args:
            width (int): width
            height (int): width
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """The __str__ method in Python represents the class
        object as a customized string

        Returns: a formatted string
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """returns mul of height by width

        Returns:
            int: square area
        """
        return self.__width * self.__height


class Square(Rectangle):

    def __init__(self, size):
        """init for a square

        Args:
            size (int): size of square
        """
        super().integer_validator(self, size)
        self.__size = size

    def __str__(self):
        """The __str__ method in Python represents the class
        object as a customized string

        Returns: a formatted string
        """
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
    
    def area(self):
        """A public instance method that coputes
        the rectangle area

        Returns: the rectangle area
        """
        return self.__size ** 2
