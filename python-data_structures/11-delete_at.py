#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    counter = 0
    if idx < 0 or idx is None:
        return my_list
    del my_list[idx]
    return my_list
