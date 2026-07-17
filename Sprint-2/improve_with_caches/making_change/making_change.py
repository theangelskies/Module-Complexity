from typing import List


def ways_to_make_change(total: int) -> int:
    """
    Given access to coins with the values 1, 2, 5, 10, 20, 50, 100, 200, returns a count of all of the ways to make the passed total value.

    For instance, there are two ways to make a value of 3: with 3x 1 coins, or with 1x 1 coin and 1x 2 coin.

    cache[amount] is built up bottom-up to hold the number of ways to make `amount` using the coins
    considered so far. Building it iteratively (rather than recursing per coin used) avoids both the
    redundant re-work of the original approach and Python's recursion depth limit for large totals.
    """
    if total == 0:
        return 0

    coins: List[int] = [1, 2, 5, 10, 20, 50, 100, 200]
    cache = [0] * (total + 1)
    cache[0] = 1
    for coin in coins:
        for amount in range(coin, total + 1):
            cache[amount] += cache[amount - coin]

    return cache[total]
