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


a = 1
if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__))
if is_same_class(a, float):
    print("{} is an instance of the class {}".format(a, float.__name__))
if is_same_class(a, object):
    print("{} is an instance of the class {}".format(a, object.__name__))
