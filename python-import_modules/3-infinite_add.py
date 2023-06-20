#!/usr/bin/python3
import sys
if __name__ == "__main__":
    result = 0
    argvv = sys.argv[1:]
    for args in argvv:
        result += int(args)
print(result)
