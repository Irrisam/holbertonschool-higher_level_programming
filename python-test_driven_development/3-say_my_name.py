#!/usr/bin/python3
"""Module that prints name and surname
    Args:
        first_name (str): first name
        last_name (str) : last name
"""


def say_my_name(first_name, last_name=""):
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("{} {}".format(first_name, last_name))
