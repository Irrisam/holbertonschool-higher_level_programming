#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return None
    result = my_list[0]
    for i in my_list:
        if i > result:
            result = i
    return result


my_list = [-5, -90, -2, -13, -34, -5, -13, -3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
