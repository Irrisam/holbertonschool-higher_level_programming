#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    if my_list is None or len(my_list) == 0:
        return None
    result = list(map(lambda x: x * number, my_list))
    return result
