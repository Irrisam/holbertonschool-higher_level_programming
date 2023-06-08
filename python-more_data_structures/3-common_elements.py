#!/usr/bin/python3
def common_elements(set_1, set_2):
    if set_1 is None or set_2 is None or set_1 == 0 or set_2 == 0:
        return None
    return set(set_1) & set(set_2)
