#!/usr/bin/python3
"""This module define the function matrix_mul"""


def matrix_mul(m_a=[[1]], m_b=[[1]]):
    """
    Multiplies two matrices

    Args:
        m_a (list of lists): First matrix
        m_b (list of lists): Second matrix

    Raises:
        TypeError:  if either is not a list of lists or
                    if either rows has an item that is not an
                    int or float or
                    if the rows of both matrices are of
                    different sizes

        ValueError: if m_a and m_b can't be multiplied or
                    if either is empty

        Returns:
            matrix: A new matrix
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
    sum = 0
    new = []
    for i in range(len(m_a)):
        sum = 0
        tmp = []
        for j in range(col_len_b):
            for k in range(len(m_b)):
                if m_a[i][k] != m_a[i][k] or m_a[i][k] == float('inf') or \
                        m_a[i][k] == float('-inf'):
                    m_a[i][k] = 10

                if m_b[k][j] != m_b[k][j] or m_b[k][j] == float('inf') or \
                        m_b[k][j] == float('-inf'):
                    m_b[k][j] = 10

                product = m_a[i][k] * m_b[k][j]
                sum = sum + product
            tmp.append(sum)
            sum = 0
        new.append(tmp)
    return new
