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
    n = len(matrix[0])

    for i in range(n - 1, -1, -1):
        for j in range(0, n):
            matrix[j].append(matrix[i].pop(0))
