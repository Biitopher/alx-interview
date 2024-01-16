#!/usr/bin/python3
"""minimum operations"""


def minOperations(n):
    """defines minimum operations"""
    if n < 2:
        return 0
    factor_list = []
    x = 1
    while n != 1:
        x += 1
        if n % x == 0:
            while n % x == 0:
                n /= x
                factor_list.append(x)
    return sum(factor_list)
