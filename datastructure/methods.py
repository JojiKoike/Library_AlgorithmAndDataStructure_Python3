"""
DataStructure Methods Module
"""
from typing import List, Optional
from .structs import Node, Point


def make_kd_tree(l: int, r: int, depth: int, points: List[Point], tree: List[Node], np: int) -> Optional[int]:
    """
    Meke K-dimension Tree
    :param l:
    :param r:
    :param depth:
    :param points:
    :param tree:
    :param np:
    :return:
    """
    if not l < r:
        return None
    mid: int = int((l + r) / 2)
    t: int = np
    np += 1
    if depth % 2 == 0:
        s_points: List[Point] = sorted(points[l:r], key=lambda point: point.x)
        for i, point in enumerate(s_points):
            points[l + i] = point
    else:
        s_points: List[Point] = sorted(points[l:r], key=lambda point: point.y)
        for i, point in enumerate(s_points):
            points[l + i] = point
    tree[t].location = mid
    tree[t].l = make_kd_tree(l, mid, depth + 1, points, tree, np)
    tree[t].r = make_kd_tree(mid + 1, r, depth + 1, points, tree, np)

    return t


def find_range_search(v: int, sx: int, tx: int, sy: int, ty: int, depth: int,
                      points: List[Point], tree: List[Node], ans: List[Point]) -> None:
    """
    Range Search
    :param v: Search Target Tree Root Node id
    :param sx: Search Range min-x
    :param tx: Search Range max-x
    :param sy: Search Range min-y
    :param ty: Search Range max-y
    :param depth: Current Depth in tree
    :param points: Point List
    :param tree: Search Tree
    :param ans: Answer Point List
    :return: None
    """
    x: int = points[tree[v].location].x
    y: int = points[tree[v].location].y

    if sx <= x <= tx and sy <= y <= ty:
        ans.append(points[tree[v].location])

    if depth % 2 == 0:
        if tree[v].l is not None and sx <= x:
            find_range_search(tree[v].l, sx, tx, sy, ty, depth + 1, points, tree, ans)
        if tree[v].r is not None and x <= tx:
            find_range_search(tree[v].r, sx, tx, sy, ty, depth + 1, points, tree, ans)
    else:
        if tree[v].l is not None and sy <= y:
            find_range_search(tree[v].l, sx, tx, sy, ty, depth + 1, points, tree, ans)
        if tree[v].r is not None and y <= ty:
            find_range_search(tree[v].r, sx, tx, sy, ty, depth + 1, points, tree, ans)
