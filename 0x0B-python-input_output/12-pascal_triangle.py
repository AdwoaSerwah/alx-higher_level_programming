#!/usr/bin/python3
"""This module defines a function called pascal_triangle"""


def pascal_triangle(n):
    """
    Returns n rows of the pascal triangle

    Args:
        n (int): Number of rows to return

    Return:
        List of lists
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]

    new_list = [[1], [1, 1]]
    n = n - 2
    for i in range(n):
        tmp = [1]
        for j in range(len(new_list[i + 1]) - 1):
            sum = new_list[i + 1][j] + new_list[i + 1][j + 1]
            tmp.append(sum)
        tmp.append(1)
        new_list.append(tmp)
    return new_list
