"""
Number methods module
"""


def power(x: int, n: int, m: int) -> int:
    """
    Power Solver
    :param x:
    :param n:
    :param m:
    :return:
    """
    res: int = 1
    if n > 0:
        res = power(x, int(n / 2), m)
        if n % 2 == 0:
            res = (res * res) % m
        else:
            res = (((res * res) % m) * x) % m
    return res
