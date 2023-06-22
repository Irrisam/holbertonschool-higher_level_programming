#!/usr/bin/python3
"""opens a file"""


def read_file(filename=""):
    with open(filename, 'r') as file:
        text = file.readlines()
        print("{}".format(text))


read_file("my_file_0.txt")
