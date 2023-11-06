#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new = []
    [new.append(my_list[i]) for i in range(len(my_list))]
    if (idx < 0 or idx > len(new) - 1):
        return (new)
    new[idx] = element
    return (new)
