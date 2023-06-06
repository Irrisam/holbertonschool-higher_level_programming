#!/usr/bin/python3
def element_at(my_list, idx):
    """
    Print index.

    Args:
        my_list (list): List of element to print from
        idx (index): Index of element to print

    Returns:
       None on error
    """
    if __name__ == "__main__":
        if idx < 0 or idx >= len(my_list):
            return None
        print("Element at index {:d} is {:d}".format(idx, len(my_list)))
        return
