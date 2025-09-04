def prime_factorization(n):
    """소인수분해: (소수, 지수) 튜플 리스트 반환"""
    if n < 2:
        return []
    factors = []

    count_two = 0
    while n % 2 == 0:
        n //= 2
        count_two += 1
    if count_two > 0:
        factors.append((2, count_two))

    f = 3
    while f * f <= n:
        count = 0
        while n % f == 0:
            n //= f
            count += 1
        if count > 0:
            factors.append((f, count))
        f += 2

    if n > 1:
        factors.append((n, 1))

    return factors


