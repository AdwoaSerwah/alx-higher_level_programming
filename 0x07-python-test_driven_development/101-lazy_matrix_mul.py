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
    np_a = np.array(m_a)
    np_b = np.array(m_b)

    new = np_a @ np_b

    new = new.tolist()

    result_str = np.array(new)
    return result_str
