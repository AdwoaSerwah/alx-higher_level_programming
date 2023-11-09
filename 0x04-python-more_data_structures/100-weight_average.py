#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    t_score = 0
    t_wgt = 0

    for score, weight in my_list:
        t_score += score * weight
        t_wgt += weight

    if t_wgt == 0:
        return 0

    weighted_avg = t_score / t_wgt
    return weighted_avg
