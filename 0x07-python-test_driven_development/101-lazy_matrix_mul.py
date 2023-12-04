#!/usr/bin/python3
"""This module defines a function called lazy_matrix_mul"""

import numpy as np


def lazy_matrix_mul(m_a=[[1]], m_b=[[1]]):
    """
    Computes the multiplication of two matrices

    Args:
        m_a (list of lists): First matrix
        m_b (list of lists): Second matrix

    Returns:
        list of lists: New matrix
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0 or any((len(row) == 0) for row in m_a):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or any((len(row) == 0) for row in m_b):
        raise ValueError("m_b can't be empty")
    if not all(isinstance(m, (float, int)) for row in m_a for m in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(m, (float, int)) for row in m_b for m in row):
        raise TypeError("m_b should contain only integers or floats")
    col_len_a = len(m_a[0])
    col_len_b = len(m_b[0])
    if any((len(row) != col_len_a) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if any((len(row) != col_len_b) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if col_len_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    for i in range(len(m_a)):
        for j in range(len(m_a[i])):
            if m_a[i][j] != m_a[i][j] or m_a[i][j] == float('inf') \
                    or m_a[i][j] == float('-inf'):
                m_a[i][j] = 10

    for i in range(len(m_b)):
        for j in range(len(m_b[i])):
            if m_b[i][j] != m_b[i][j] or m_b[i][j] == float('inf') \
                    or m_b[i][j] == float('-inf'):
                m_b[i][j] = 10

    np_a = np.array(m_a)
    np_b = np.array(m_b)

    new = np_a @ np_b

    new = new.tolist()

    return new
