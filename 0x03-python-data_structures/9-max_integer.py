#!/usr/bin/python3

def max_integer(my_list=[]):
    my_len = len(my_list)
    temp = sorted(my_list)

    if my_len == 0:
        my_max = None
    else:
        my_max = temp[-1]
    return (my_max)
