#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return None
    for row in matrix:
        sep = ""
        for element in row:
            print("{}{:d}".format(sep, element), end='')
            sep = " "
        print()
