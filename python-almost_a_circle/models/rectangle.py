#!/usr/bin/python3
"""shebangs indeed"""

from models.base import Base


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
