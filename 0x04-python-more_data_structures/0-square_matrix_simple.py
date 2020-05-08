#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    if len(matrix) > 0:
        n = []
        for i in matrix:
            n.append([j**2 for j in i])
        return n
