"""
Data Structure Structs Module
"""
from typing import List


class DisjointSet(object):
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
