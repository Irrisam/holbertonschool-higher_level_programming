#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None or matrix == 0:
        return None
    new_matrix = []
    for row in matrix:
        new_row = []
        for value in row:
            new_row.append((value ** 2))
        new_matrix.append(new_row)
    return new_matrix
