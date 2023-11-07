#!/usr/bin/python3
"""Log parsing module"""


from sys import stdin


status_code = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
        }
total_size = k = 0


def printer():
    """print status"""
    print(f"File size: {total_size}")
    for key, value in sorted(status_code.items()):
        if value > 0:
            print('{:s}: {:d}'.format(key, value))


try:
    for line in stdin:
        split_line = line.split()
        if len(split_line) >= 2:
            status = split_line[-2]
            total_size += int(split_line[-1])
            if status in status_code:
                status_code[status] += 1
        k += 1
        if k % 10 == 0:
            printer()
    printer()
except KeyboardInterrupt as err:
    printer()
