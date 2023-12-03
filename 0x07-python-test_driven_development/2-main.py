#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)
print(matrix_divided([[1, -2.5, 3], [4.0, -5, 6.98]], -3))
print(matrix_divided([[1.1, 2.2, 3.3], [4.4, 5.5, 6.6]], 3))
try:
    print(matrix_divided([["Ama", 2, 3]], 2))
except Exception as e:
    print(e)
