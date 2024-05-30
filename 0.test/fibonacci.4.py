from functools import lru_cache


def fibonacci(n: int) -> int:
    if n == 0:
        return 0

    if n == 1 or n == 2:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


@lru_cache(maxsize=None)
def deco_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    
    return fibonacci(n - 1) + fibonacci(n - 2)

def memo_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    
    fib = [0] * (n + 1) 
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    
    return fib[n]
    