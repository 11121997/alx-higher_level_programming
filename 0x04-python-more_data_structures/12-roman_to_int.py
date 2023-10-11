#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    total = 0
    n = 0
    rm_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for k in reversed(roman_string):
        n = rm_num[k]
        total += n if total < n * 5 else -n
    return total
