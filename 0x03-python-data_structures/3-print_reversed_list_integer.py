#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_len = len(my_list) - 1
    [print("{:d}".format(my_list[i])) for i in range(my_len, -1, -1)]
