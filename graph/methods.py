from typing import List, Optional, Deque
from collections import deque
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


def topological_sort(adj_matrix: List[List[int]]) -> List[int]:
    """
    Topological Sort
    :param adj_matrix: Adjacent Matrix
    :return: Topological Sort Result List
    """
    n: int = len(adj_matrix)
    indeg: List[int] = [0 for i in range(n)]
    v: List[bool] = [False for i in range(n)]
    res: List[int] = []
    for i in range(n):
        for j in adj_matrix[i]:
            indeg[j] += 1

    for j in range(n):
        if indeg[j] == 0 and not v[j]:
            __bfs(j, adj_matrix, indeg, v, res)

    return res


def __bfs(s: int, adj_matrix: List[List[int]], indeg: List[int], v: List[bool], res: List[int]) -> None:
    """
    Breadth First Search
    :param s:
    :param adj_matrix:
    :param indeg:
    :param v:
    :param res:
    :return:
    """
    queue: Deque[int] = deque()
    queue.append(s)
    v[s] = True
    while len(queue) > 0:
        u: int = queue.popleft()
        res.append(u)
        for i in adj_matrix[u]:
            indeg[i] -= 1
            if indeg[i] == 0 and not v[i]:
                v[i] = True
                queue.append(i)
