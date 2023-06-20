#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        tuple_a = (0, 0)
    if len(tuple_b) == 0:
        tuple_b = (0, 0)
    if len(tuple_a) == 1:
        tuple_a = (tuple_a[0], 0)
    if len(tuple_b) == 1:
        tuple_b = (tuple_b[0], 0)
    a0 = tuple_a[0] + 0
    b0 = tuple_b[0] + 0
    a1 = tuple_a[1] + 0
    b1 = tuple_b[1] + 0
    resa = a0 + b0
    resb = a1 + b1
    return (resa, resb)
