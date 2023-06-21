#!/usr/bin/python3
"""dunno what it does yet"""


class BaseGeometry:
    """who knows, I do not"""
    def __init__(self):
        pass

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """valdiates value argument

        Args:
            name (string): name of value
            value (int): int value of value

        Raises:
            TypeError: if value is not int 
            ValueError: if value is egual or less than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be an integer".format(name))
