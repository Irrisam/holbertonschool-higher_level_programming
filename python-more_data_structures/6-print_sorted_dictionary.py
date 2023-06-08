#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None or a_dictionary == 0:
        return None
    dictio = sorted(a_dictionary)
    for i in dictio:
        print("{}: ".format(i), end="")
        print("{}".format(a_dictionary[i]))
