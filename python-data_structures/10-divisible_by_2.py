#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    counter = 0
    new_list = {}
    for i in my_list:
        if i % 2 == 0:
            new_list[counter] = True
        else:
            new_list[counter] = False
        counter += 1
    return new_list
