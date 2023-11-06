#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    [print("{:d}".format(item)) for item in my_list]
