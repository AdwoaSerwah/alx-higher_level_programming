#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    final_list = []
    temp_list = [tuple_a, tuple_b]
    for i in range(len(temp_list)):
        for j in range(2):
            if len(temp_list[i]) == 0 or (len(temp_list[i]) == 1 and j == 1):
                final_list.append(0)
            elif (len(temp_list[i]) == 1 and j == 0) or len(temp_list[i]) >= 2:
                final_list.append(temp_list[i][j])

    a = final_list[0] + final_list[2]
    b = final_list[1] + final_list[3]
    new_tuple = (a, b)
    return (new_tuple)
