#!/usr/bin/python3
def multiple_returns(sentence):
    my_list = []
    my_list.append(sentence)
    my_len = len(my_list[0])

    if my_len == 0:
        first_char = None
    else:
        first_char = my_list[0][0]

    return my_len, first_char
