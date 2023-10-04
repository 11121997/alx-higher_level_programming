#!/usr/bin/python3
def remove_char_at(str, n):
    newstr = ''
    for k, v in enumerate(str):
        if k != n:
            newstr += v
    return newstr
