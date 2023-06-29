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

    def update(self, *args, **kwargs):
        """updates values of rectangle
        """
        if len(args) >= 1 and args[0] is not None:
            self.id = args[0]
        if len(args) >= 2 and args[1] is not None:
            self.size = args[1]
        if len(args) >= 3 and args[2] is not None:
            self.x = args[2]
        if len(args) >= 4 and args[3] is not None:
            self.y = args[3]
        if kwargs:
            if "id" in kwargs and kwargs["id"] is not None:
                self.id = kwargs["id"]
            if "size" in kwargs and kwargs["size"] is not None:
                self.size = kwargs["size"]
            if "x" in kwargs and kwargs["x"] is not None:
                self.x = kwargs["x"]
            if "y" in kwargs and kwargs["y"] is not None:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """returns dict representation

        Returns:
            dict: dict of attributes in rectangle
        """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
            }