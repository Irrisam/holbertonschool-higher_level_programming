#!/usr/bin/python3
"""shebangs indeed"""

import json

class Base:
    """Base class of program
        Args: nb_objects: deals with number of instances
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """initialized instances

        Args:
            id (int,optional): tracks id of different shapes. Defaults to None.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        if list_dictionaries is None or []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
