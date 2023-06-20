#!/usr/bin/python3
"""Create a method to return attr and methods of an object"""


def lookup(obj):
    """function that returns methods and attr of an object

    Args:
        obj class: object to be inspected
    """
    return dir(obj)
