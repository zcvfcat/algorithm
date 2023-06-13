from functools import lru_cache


def fibonacci(n):
    """
    기본 꼬리재귀
    상향식
    """
    if n == 0 or n == 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci2(n):
    """
    하향식
    """
    if n == 0 or n == 1:
        return n

    memo = [0, 1]

    for n in range(2, n + 1):
        memo += [memo[n - 1] + memo[n - 2]]
        
    return memo[n]


@lru_cache(maxsize=None)
def fibonacci_memo(n):
    if n == 0 or n == 1:
        return n

    return fibonacci_memo(n - 1) + fibonacci_memo(n - 2)


n = 10
print(fibonacci(n))
print(fibonacci2(n))
print(fibonacci_memo(n))
