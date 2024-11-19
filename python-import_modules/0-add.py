#!/usr/bin/python3
from add_0 import fake_add

if __name__ == "__main__":
    a = 1
    b = 2

    try:
        result = fake_add(a, b)
        print(f"FAKE add() => {a} - {b} = {result}")

    except TypeError as e:
        print(f"FAKE add() => {e}")
