#!/usr/bin/python3
"""check for inheritance"""


def inherits_from(obj, a_class):
    """check for inheritance

    Args:
        obj (class): check for inhritance to
        a_class (class): check for inheritance from

    Returns:
        Bool: True is true, else, Flase
    """
    if type(obj) is not a_class:
        return issubclass(type(obj), a_class)
