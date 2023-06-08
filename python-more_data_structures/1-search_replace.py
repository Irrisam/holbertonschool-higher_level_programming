#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None or my_list == 0:
        return None
    counter = 0
    for i in my_list:
        if i == search:
            my_list[counter] = replace
        counter += 1
    return my_list
