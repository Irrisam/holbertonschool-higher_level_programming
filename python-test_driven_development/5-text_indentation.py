#!/usr/bin/python3
def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in text:
        print("{}".format(i), end="")
        if i == "." or i == "?" or i == ":":
            print("\n\n", end="")
