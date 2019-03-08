"""
Graph Structs Module
"""
from typing import Optional


class Edge(object):
    """
    Edge Data Structure Class
    """
    def __init__(self, source: Optional[int], destination: int, weight: int) -> None:
        self.source = source
        self.destination = destination
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight
