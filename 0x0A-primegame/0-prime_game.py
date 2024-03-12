#!/usr/bin/python3
"""Function outlining prime game"""


def isWinner(x, nums):
    """Defines the winner in the prime game"""
    if not nums or x < 1:
        return None
    n = max(nums)
    sieve = [True for _ in range(max(n + 1, 2))]
    for i in range(2, int(pow(n, 0.5)) + 1):
        if not sieve[i]:
            continue
        for j in range(i*i, n + 1, i):
            sieve[j] = False

    sieve[0] = sieve[1] = False
    a = 0
    for i in range(len(sieve)):
        if sieve[i]:
            a += 1
        sieve[i] = a

    current_player = 0
    for n in nums:
        current_player += sieve[n] % 2 == 1
    if current_player * 2 == len(nums):
        return None
    if current_player * 2 > len(nums):
        return "Maria"
    return "Ben"
