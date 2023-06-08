#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None or my_list == 0:
        return None
    my_set = set(my_list)
    result = sum(my_set)
    return result