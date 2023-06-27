#!/usr/bin/python3
"""shebangs indeed"""


class Base:
    """Base class of program
        Args: nb_objects: deals with number of instances
    """
    nb_objects = 0

    def __init__(self, id=None, width=0, height=0, x=0, y=0):
        """initialized instances

        Args:
            id (int,optional): tracks id of different shapes. Defaults to None.
        """
        self.__id = id
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        if id is not None:
            self.id = id
        else:
            Base.nb_objects += 1
            self.id = Base.nb_objects

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
