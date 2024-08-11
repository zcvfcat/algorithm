from functools import lru_cache


def fibonacci(n: int):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def memo_fibonacci(n: int):
    if n <= 1:
        return n

    memo = [0, 1]

    for i in range(2, n + 1):
        memo.append(memo[i - 1] + memo[i - 2])

    return memo[n]


def fibonacci_iterative(n: int):
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b


@lru_cache(maxsize=None, )
def deco_fibonacci(n: int):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
