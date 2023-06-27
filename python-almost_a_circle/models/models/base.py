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
        if id is not None:
            self.id = id
        else:
            Base.nb_objects += 1
            self.id = Base.nb_objects
