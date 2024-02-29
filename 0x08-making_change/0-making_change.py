#!/usr/bin/python3
"""Change comes from within"""


def makeChange(coins, total):
    """Sort thethe fewest number of coins needed to meet certain amount"""
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    num_coins = 0
    current_total = total

    for coin in coins:
        num_of_coins = current_total // coin

        current_total -= num_of_coins * coin
        num_coins += num_of_coins

        if current_total == 0:
            break

    if current_total != 0:
        return -1

    return num_coins
