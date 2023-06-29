#!/usr/bin/python3
"""A module with a Rectangle Class"""

from models.base import Base


class Rectangle(Base):
    """A Rectangle class that inherits from Base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """A constructor method for the Rectangle class

        Args:
            width (int): the width of the Rectangle
            height (int): the height of the Rectangle
            x (int): the x position of the Recangle
            y (int): the y position of the Rectangle

        Raise:
            TypeError: if one of the is not an integer
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets or sets the width of the Rectangle.

        Raise:
            TypeError: if the width is not an integer.
            ValueError: if the width is <= 0
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets or sets the height of the Rectangle.

        Raise:
            TypeError: if the height is not an integer.
            ValueError: if the height is <= 0
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets or sets the x of the Rectangle.

        Raise:
            TypeError: if x is not an integer.
            ValueError: if x is <= 0
        """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets or sets the y of the Rectangle.

        Raise:
            TypeError: if y is not an integer.
            ValueError: if y is <= 0
        """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns area

        Returns:
            int: square area of rectangle
        """
        return self.width * self.height

    def display(self):
        """displays the rectangle"""
        if self.y > 0:
            for k in range(self.y):
                print()
        for i in range(self.height):
            if self.x > 0:
                for g in range(self.x):
                    print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            j = 0
            print()

    def __str__(self):
        """The __str__ method in Python represents the class
        object as a customized string
        Returns: a formatted string"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args):
        """updates values of rectangle
        """
        if len(args) >= 1 and args[0] is not None:
            self.id = args[0]
        if len(args) >= 2 and args[1] is not None:
            self.width = args[1]
        if len(args) >= 3 and args[2] is not None:
            self.height = args[2]
        if len(args) >= 4 and args[3] is not None:
            self.x = args[3]
        if len(args) >= 5 and args[4] is not None:
            self.y = args[4]
