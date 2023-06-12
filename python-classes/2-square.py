#!/usr/bin/python3
"""A module with as simple empty Square class"""


class Square:
    """Class defining a square."""

    def __init__(self, size=0):
        """Defines square."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
