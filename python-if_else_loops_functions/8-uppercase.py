#!/usr/bin/python3

def uppercase(str):

    for i in str:
        ordv = ord(str[i:i+1])
        if ord(str[i]) > 123 and ord(str[i]) < 97:
            print(str)
            i += 1
        else:
            print(chr(str[i] + 22))
