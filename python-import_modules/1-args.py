#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arguments = sys.argv[1:]

    if len(arguments) == 0:
        print("0 arguments.")
    elif len(arguments) == 1:
        print("1 argument: ")
        for index, arg in arguments:
            print("{}: {}".format(index, arg))
    else:
        for index, arg in arguments:
            print("{} arguments:".format(index))
            print("{}: {}".format(index, arg))