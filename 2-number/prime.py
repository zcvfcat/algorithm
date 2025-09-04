import math


def is_prime(n):
    """기초 소수 판별 (sqrt(n))"""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    if n % 3 == 0:
        return n == 3
    limit = int(math.isqrt(n))
    f = 5
    while f <= limit:
        if n % f == 0 or n % (f + 2) == 0:
            return False
        f += 6
    return True


def sieve(limit):
    """에라토스테네스의 체: 2..limit 범위 소수 리스트 반환"""
    if limit < 2:
        return []
    is_composite = [False] * (limit + 1)
    is_composite[0] = True
    is_composite[1] = True
    for p in range(2, int(math.isqrt(limit)) + 1):
        if not is_composite[p]:
            start = p * p
            step = p
            is_composite[start : limit + 1 : step] = [True] * (((limit - start) // step) + 1)
    return [i for i in range(2, limit + 1) if not is_composite[i]]


