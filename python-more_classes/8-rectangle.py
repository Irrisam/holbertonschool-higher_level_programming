#!/usr/bin/python3
"""
class Rectangle :
Class that define a rectangle

Args:
    width (int, optional): width of the rectangle. Defaults to 0.
    height (int, optional): height of the rectangle. Defaults to 0.
"""


class Rectangle:
    """Defines a rectangle with width and height"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Print the rectangle with a specific character"""
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for column in range(self.__height):
            for row in range(self.__width):
                string += str(self.print_symbol)
            if column is not self.__height - 1:
                string += "\n"
        return string

    def __repr__(self):
        """Return a string representation of the rectangle
        to be able to recreate a new instance
        """
        result = ""
        result = "Rectangle({}, {})".format(self.__width, self.__height)
        return result

    def __del__(self):
        """Print the message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if Rectangle.area(rect_1) == Rectangle.area(rect_2):
            return rect_1
        if Rectangle.area(rect_1) < Rectangle.area(rect_2):
            return rect_2
        else:
            return rect_1
