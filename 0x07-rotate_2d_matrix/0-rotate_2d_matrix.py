#!/usr/bin/python3
"""
Module for rotating a 2D matrix in place by 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a given n x n 2D matrix by 90 degrees clockwise in place.

    Args:
        matrix (list of lists): A 2D matrix of size n x n.

    Returns:
        None: The matrix is modified in place.
    """
    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()
