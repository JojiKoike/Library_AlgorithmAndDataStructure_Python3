"""
Data Structure Structs Module
"""
from typing import List


class DisjointSet:
    """
    DisjointSet Data Structure
    """

    def __init__(self, size: int) -> None:
        self.rank: List[int] = [i for i in range(size)]
        self.p: List[int] = [i for i in range(size)]
        for i in range(size):
            self.__make_set(i)

    def __make_set(self, x: int) -> None:
        """
        Create New Set includes x only
        :param x:
        :return:
        """
        self.p[x] = x
        self.rank[x] = 0

    def __find_set(self, x: int) -> int:
        """
        Return Root Element of tree x included in
        :param x: element
        :return: Root Element
        """
        if x != self.p[x]:
            self.p[x] = self.__find_set(self.p[x])
        return self.p[x]

    def __link(self, x: int, y: int) -> None:
        if self.rank[x] > self.rank[y]:
            self.p[y] = x
        else:
            self.p[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def unite(self, x: int, y: int) -> None:
        """
        Unite two tree
        :param x: One Tree Element
        :param y: The Other Tree Element
        :return:
        """
        self.__link(self.__find_set(x), self.__find_set(y))

    def same(self, x: int, y: int) -> bool:
        """
        Calculate x and y belong to same tree
        :param x:
        :param y:
        :return:
        """
        return self.__find_set(x) == self.__find_set(y)


class Node:
    """
    Node of x-y plane Data Structure
    """
    def __init__(self, location: int, p: int, l: int, r: int) -> None:
        """
        Constructor
        :param location: Location Index
        :param p: Parent Node Index
        :param l: Left Side Tree Root Index
        :param r: Right Side Tree Root Index
        """
        self.location = location
        self.p = p
        self.l = l
        self.r = r


class Point:
    """
    Point of x-y plane Data Structure
    """
    def __init__(self, point_id: int, x: int, y: int) -> None:
        self.point_id = point_id
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.point_id < other.point_id

    def __str__(self):
        print(self.point_id)
