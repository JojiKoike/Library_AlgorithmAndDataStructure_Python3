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


prenum: List[int] = []
lowest: List[int] = []
parent: List[int] = []
visited: List[bool] = []
timer: int = 0


def articulation_point(g: List[List[int]]) -> List[int]:
    """
    Graph Articulation Point Finder
    :param g: Graph
    :return: Articulation Point index list
    """
    n: int = len(g)
    global prenum, lowest, parent, visited, timer
    prenum = [0 for i in range(n)]
    lowest = [0 for i in range(n)]
    parent = [-1 for i in range(n)]
    visited = [False for i in range(n)]
    timer = 1
    __dfs(0, -1, g)
    ap: List[int] = []
    np: int = 0
    for i in range(1, n):
        p: int = parent[i]
        if p == 0:
            np += 1
        elif prenum[p] <= lowest[i]:
            ap.append(p)
    if np > 1:
        ap.append(0)
    return ap


def __dfs(current: int, prev: int, g: List[List[int]]) -> None:
    """
    Depth First Search For Graph Articulation Finder
    :param current: Current Visit Node Index
    :param prev: Previous Visit Node Index
    :param g: Search Target Graph
    :return:
    """
    global prenum, lowest, parent, visited, timer
    prenum[current] = lowest[current] = timer
    timer += 1
    visited[current] = True

    for next in g[current]:
        if not visited[next]:
            parent[next] = current
            __dfs(next, current, g)
            lowest[current] = min(lowest[current], lowest[next])
        elif next != prev:
            lowest[current] = min(lowest[current], prenum[next])
