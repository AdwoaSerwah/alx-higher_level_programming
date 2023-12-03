#!/usr/bin/python3
"""This modules defines matrix_divided function"""


def matrix_divided(matrix, div):
    """
    Divides a matrix

    Args:
        matrix (list): Matrix
        div (int/float): Number to divide items in matrix

    Returns:
        list: New list
    """
    if not isinstance(matrix, list):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    if (len(matrix) == 0):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(i, list) for i in matrix) or (len(matrix[0]) == 0):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(i, (int, float)) for row in matrix for i in row):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    row_sizes = set(len(row) for row in matrix)
    if len(row_sizes) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new = [[round(element / div, 2) for element in row] for row in matrix]
    return new
