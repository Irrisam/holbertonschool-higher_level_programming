#!/usr/bin/python3
"""A module with as simple empty Square class"""


class Square:
    """Class defining a square."""

    def __init__(self, size=0):
        """Defines square."""
        self.__size = 0
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Method returning square area

        Returns:
            Integer: Return value of square area of square
        """
        return self.__size ** 2
