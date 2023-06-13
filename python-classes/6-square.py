#!/usr/bin/python3
"""A module with as simple empty Square class."""


class Square:
    """Class defining a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Define square."""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """give access to hidden data

        Returns:
            Integer: size value
        """
        return self.__size

    @property
    def position(self):
        return self.__position

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

    def position(self, value):
        if self.value[0] < 0 or self.value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """Printing # for the squares"""
        if self.__position[1] > 0:
            print("\n" * self.__position[1])
        for i in range(self.size):
            if self.size != 0:
                if self.__position[0] > 0:
                    for i in range(self.__position[0]):
                        print(" ", end="")
                print("#" * self.size)
            else:
                print()
