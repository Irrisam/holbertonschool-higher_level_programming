#!/usr/bin/python3
"""shebangs indeed"""

from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
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
