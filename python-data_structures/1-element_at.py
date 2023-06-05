#!/usr/bin/python3
def element_at(my_list, idx):
    """

    Args:
        my_list (_type_): List of element to print from
        idx (_type_): Index of element to print

    Returns:
        _type_: None on error
    """
    if idx < 0 or idx > len(my_list):
        print("None")
        return (None)
    print("Element at index {:d} is {:d}".format(idx, len(my_list)))
