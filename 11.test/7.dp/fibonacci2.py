from functools import lru_cache

def fibonacci(n):
    if n == 0:
        return 0
    
    elif n == 1 or n == 2:
        return 1
    
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
@lru_cache(maxsize=None)
def fibonacci_memo(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci_memo(n - 1) + fibonacci_memo(n - 2)


