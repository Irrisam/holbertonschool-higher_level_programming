#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if my_list is None or my_list == 0:
        return None
    cnt = 0
    try:
        for j in range(x): 
            print("{}".format(my_list[j]), end="")
    except IndexError:
        x = j
    print()
    return x
