#!/usr/bin/python3
def add(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both a and b must be integers")
    return a + b

def fake_add(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both a and b must be integers")
    return a - b
