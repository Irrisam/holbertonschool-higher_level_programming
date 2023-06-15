#!/usr/bin/python3

def print_square(size):
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        if size != 0:
            print("#" * size)
        else:
            print()


print_square()
