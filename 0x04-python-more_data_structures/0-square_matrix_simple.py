#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = []
    for i in range(len(matrix)):
        square.append([])
        for j in range(len(matrix[i])):
            square[i].append(matrix[i][j] * matrix[i][j])
    return square
