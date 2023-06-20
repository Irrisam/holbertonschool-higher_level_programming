#!/usr/bin/python3
"""checks if an object inherits from kind of the same class"""


def is_kind_of_class(obj, a_class):
    """checks if an object inherits from kind of the same class

    Args:
        obj (object): object to check
        a_class (class): class to check from

    Returns:
        Bool: True if true, False if not
    """
    if isinstance(obj, a_class):
        return True
    return False
