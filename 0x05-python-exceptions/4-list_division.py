#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div_list = []

    for k in range(list_length):
        try:
            div_list.append(my_list_1[k] / my_list_2[k])
        except TypeError:
            div_list.append(0)
            print("wrong type")
            continue
        except ZeroDivisionError:
            div_list.append(0)
            print("division by 0")
            continue
        except IndexError:
            div_list.append(0)
            print("out of range")
            continue
        finally:
            pass
    return div_list
