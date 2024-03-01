#!/usr/bin/python3
"""function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    if (len(list_of_integers) == 0):
        return None
    else:
        peak = list_of_integers[0]
        for k in range(len(list_of_integers)):
            if (list_of_integers[k] > peak):
                peak = list_of_integers[k]
        return peak
