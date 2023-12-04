#!/usr/bin/python3
matrix_mul = __import__('100-matrix_mul').matrix_mul

print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
print(matrix_mul([[float('inf')]], [[float('NaN')]]))
print(matrix_mul([[float('inf')]], [[float('inf')]]))
print(matrix_mul([[float('NaN')]], [[float('NaN')]]))
print(matrix_mul([[float('inf')]], [[3]]))
print(matrix_mul([[3]], [[float('NaN')]]))

try:
    print(matrix_mul([[1, -2, 3]], [[3, -4], [5, 6]]))
except Exception as e:
    print(e)

try:
    print(matrix_mul([[1, -2.7]], [[3, 4, -9.9], [5, 6, 7]]))
except Exception as e:
    print(e)

print()
print(matrix_mul([[1, -2]], [[3, -4], [1, 4]]))
print(matrix_mul([[1, -2.7]], [[3, -9.9], [5, 6.5]]))
print(matrix_mul([[1, float('NaN')]], [[3, 4], [float('inf'), 6]]))
print(matrix_mul([[1, 2], [3, 4], [3, 4]], [[5, 6, 1], [7, 8, 2]]))
