"""
Graph Structs Module
"""


class Edge(object):
    """
    Edge Data Structure Class
    """
    def __init__(self, destination: int, weight: int) -> None:
        self.destination = destination
        self.weight = weight
