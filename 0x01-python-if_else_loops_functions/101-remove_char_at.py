#!/usr/bin/python3
def remove_char_at(str, n):
    newstr = ''
    for k, h in enumerate(str):
        if k != n:
            newstr += h
    return newstr
