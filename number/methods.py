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


def is_prime(n: int) -> bool:
    """
    Prime number judge method
    :param n: judge target number
    :return: Judge Results
    """
    if n <= 1:
        # 0, 1 is not prime number
        return False
    if n % 2 == 0:
        # even number is not prime number
        return False
    i: int = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True
