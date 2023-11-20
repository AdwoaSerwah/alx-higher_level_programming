#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    len = 0
    try:
        for i in range(x):
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end="")
                len += 1
        print()
        return len
    except IndexError:
        raise
