#!/usr/bin/python3
from add_0 import add

if __name__ == "__main__":
    a = 1
    b = d
    try:
        print("{} + {} = {}".format(a, b, add(a, b)))
    except TypeError as e:
        print(e)
