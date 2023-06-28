#!/usr/bin/python3
"""shebangs indeed"""

from base import Base


class Rectangle(Base):
    """rectangle class

    Args:
        Base (class): parent class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes instances of rectangles

        Args:
            width (int): rectangle width
            height (int): rectangle height
            x (int, optional): x axis. Defaults to 0.
            y (int, optional): y axis. Defaults to 0.
            id (int, optional): shape's id. Defaults to None.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """width getter"""
        return self.width

    @width.setter
    def width(self, value):
        """width setter"""
        self.width = value

    @property
    def height(self):
        """height getter"""
        return self.height

    @height.setter
    def height(self, value):
        """height setter"""
        self.height = value

    @property
    def x(self):
        """x getter"""
        return self.x

    @x.setter
    def x(self, value):
        """x setter"""
        self.x = value

    @property
    def y(self):
        """y getter"""
        return self.y

    @y.setter
    def y(self, value):
        """y setter"""
        self.y = value
