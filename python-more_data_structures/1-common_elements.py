#!/usr/bin/python3
def common_elements(set_1, set_2):
    result = set()
    for item in set_1:
        if item in set_2:
            result.add(item)
    return result
