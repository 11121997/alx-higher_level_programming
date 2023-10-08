#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    list2 = []
    for k in my_list:
        if (k % 2) == 0:
            list2.append(True)
        else:
            list2.append(False)
    return list2
        
