"""
Common module for geometry
"""
import math

# EPS is acceptable error
EPS: float = 1e-10


def equals(x_0: float, x_1: float) -> bool:
    """
    Equality Calculation considering float precision
    :param x_0: One Coordinate Value
    :param x_1: Other Coordinate Value
    :return: Equality Calculation Result
    """
    return math.fabs(x_0 - x_1) < EPS
