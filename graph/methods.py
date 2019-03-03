from typing import List, Optional
from .common import INFINITY


def warshall_floyd(distance_matrix: List[List[int]]) -> Optional[List[List[int]]]:
    """
    APSP Solver with Warshall Floyd Algorithm
    :param distance_matrix: Distance Between Nodes Matrix
    :return: distance_matrix
    """
    n: int = len(distance_matrix[0])
    for k in range(n):
        for i in range(n):
            if distance_matrix[i][k] == INFINITY:
                continue
            for j in range(n):
                if distance_matrix[k][j] == INFINITY:
                    continue
                distance_matrix[i][j] = \
                    min(distance_matrix[i][j], distance_matrix[i][k] + distance_matrix[k][j])
    for l in range(n):
        if distance_matrix[i][i] < 0:
            return None
    return distance_matrix

