#!/usr/bin/python3

def uppercase(str):
    result = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            intstr = ord(i) - 32
            result += "{:c}".format(intstr)
        else:
            result += i
    print(result)
