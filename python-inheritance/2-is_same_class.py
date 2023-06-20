#!/usr/bin/python3
"""checks if obj is an instance  of given class"""


def is_same_class(obj, a_class):
    """checks for instance

    Args:
        obj obj: obj to be checked
        a_class class: class to be checked from

    Returns:
        _type_: True if same, False if not
    """
    if isinstance(obj, a_class) and type(obj) == a_class:
        return True
    return False
