def fibonacci(n):
    """
    cache[i] is built up bottom-up to hold fibonacci(i). Building it iteratively (rather than
    recursing) avoids both the exponential re-work of the naive approach and Python's recursion
    depth limit for large n.
    """
    cache = [0] * max(n + 1, 2)
    cache[0], cache[1] = 0, 1
    for i in range(2, n + 1):
        cache[i] = cache[i - 1] + cache[i - 2]
    return cache[n]
