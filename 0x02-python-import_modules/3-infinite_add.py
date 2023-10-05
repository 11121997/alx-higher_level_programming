#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    for k in range(len(sys.av) - 1):
        sum += int(sys.av[k+1])
    print(sum)
