#!/usr/bin/python3
for n in range(10):
    for k in range(n, 10):
        if n == 8 and k == 9:
            print("{}".format(89))
        elif n < k:
            print("{}{}".format(n, k), end=", ")
