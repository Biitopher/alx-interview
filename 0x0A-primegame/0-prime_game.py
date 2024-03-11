#!/usr/bin/python3
"""Function outlining prime game"""


def isWinner(x, nums):
    """Defines the winner in the prime game"""
    def is_prime(num):
        """Returns if the number is a prime number or not"""
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_primes(num):
        """Collects the prime numbers"""
        primes = []
        for i in range(2, num + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def optimal_move(nums):
        """Indicates the optimal prime number for the win"""
        if not nums:
            return []
        primes = get_primes(max(nums))
        if primes:
            for p in primes:
                if p in nums:
                    nums = [i for i in nums if i % p != 0]
            return nums
        return []

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        current_player = "Maria"
        while True:
            nums = optimal_move(nums)
            if not nums:
                if current_player == "Maria":
                    ben_wins += 1
                else:
                    maria_wins += 1
                break
            current_player = "Ben" if current_player == "Maria" else "Maria"

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
