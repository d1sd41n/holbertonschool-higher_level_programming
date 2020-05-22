#!/usr/bin/python3
"""div each num of  alist
"""


def matrix_divided(matrix, div):
    """[summary]

    Arguments:
        matrix {list} -- [list ot div]
        div {int} -- [divident]

    Returns:
        [list] -- [description]
    """
    typeErr = "matrix must be a matrix (list of lists) of integers/floats"
    sizeErr = "Each row of the matrix must have the same size"
    numErr = "div must be a number"
    zeroErr = "division by zero"
    div_matrix = []

    if div == 0:
        raise ZeroDivisionError(zeroErr)
    elif not isinstance(div, (int, float)):
        raise TypeError(numErr)
    elif (not isinstance(matrix, list) or
          len(matrix) == 0 or
          not isinstance(matrix[0], list)):
        raise TypeError(typeErr)
    elif len(matrix[0]) == 0:
        raise TypeError(typeErr)

    size = len(matrix[0])
    for i, l in enumerate(matrix):
        if not isinstance(matrix[i], list):
            raise TypeError(sizeErr)
        if len(matrix[i]) != size:
            raise TypeError(sizeErr)
        div_matrix.append([])
        for j, m in enumerate(matrix[i]):
            if not isinstance(m, (int, float)):
                raise TypeError(typeErr)
            div_matrix[i].append(round(m / div, 2))
    return div_matrix
