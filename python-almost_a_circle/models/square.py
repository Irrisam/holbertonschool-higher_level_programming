#!/usr/bin/python3
"""shebangs indeed"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """square, defines a sub class of rectangle class

    Args:
        Rectangle (parent class): parent class used to derive for a square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """initialization of square instances 

        Args:
            size (int): size of square
            x (int, optional): x axis value. Defaults to 0.
            y (int, optional): y axis value. Defaults to 0.
            id (int, optional): id of shape. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """rewrites str to return approriate values

        Returns:
            string: values of square
        """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.width)

    @property
    def size(self):
        """property size eguals to width or height
        Returns:
            int: defines square size
        """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
