#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argvv = sys.argv[1:]
    if len(argvv) == 0:
        print("0 arguments.")
    elif len(argvv) == 1:
        i = 1
        print("1 argument:")
        print("{:d}: {:s}".format(i, argvv[0]))
    else:
        i = 1
        print("{:d} arguments:".format(len(argvv),))
        for args in argvv:
            print("{:d}: {:s}".format(i, args))
            i += 1
