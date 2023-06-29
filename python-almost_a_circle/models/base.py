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
        """returns json value of object in json

        Args:
            list_dictionaries (list): returns string repr of shapes

        Returns:
            string: repr of object in json
        """
        if list_dictionaries is None or []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """save to file to sace to a file withot dump methos

        Args:
            list_objs (list): cont  ins squares and rectangles
        """
        filename = cls.__name__ + ".json"
        data = cls.to_json_string(list_objs) if list_objs is not None else "[]"
        with open(filename, "r") as file:
            file.write(data)
