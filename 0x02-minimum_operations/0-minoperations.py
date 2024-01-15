#!/usr/bin/python3
"""minimum operations"""


def minOperations(n):
    """defines minimum operations"""
    if n <= 1:
        return 0

    def prime_factors(num):
        """defines prime factors"""
        factors = []
        divisor = 2
        while divisor * divisor <= num:
            while (num % divisor) == 0:
                factors.append(divisor)
                num //= divisor
            divisor += 1
        if num > 1:
            factors.append(num)
        return factors

    factors = prime_factors(n)

    if not factors:
        return 0

    dp = [float('inf')] * (n + 1)
    dp[1] = 0

    for i in range(2, n + 1):
        for factor in factors:
            if i % factor == 0:
                dp[i] = min(dp[i], dp[i // factor] + factor)

    return dp[n]
