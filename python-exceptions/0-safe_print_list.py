#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if my_list is None or my_list == 0:
        return None
    cnt = 0
    for _ in my_list:
        cnt += 1
    try:
        print("{}".format(my_list))
    except TypeError:
        pass
    return cnt
