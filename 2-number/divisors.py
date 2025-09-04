def _factorization(n):
    if n < 2:
        return []
    factors = []
    cnt = 0
    while n % 2 == 0:
        n //= 2
        cnt += 1
    if cnt > 0:
        factors.append((2, cnt))
    f = 3
    while f * f <= n:
        c = 0
        while n % f == 0:
            n //= f
            c += 1
        if c > 0:
            factors.append((f, c))
        f += 2
    if n > 1:
        factors.append((n, 1))
    return factors


def divisors(n):
    """n의 모든 약수를 정렬된 리스트로 반환"""
    if n == 0:
        return []
    if n < 0:
        n = -n
    factors = _factorization(n)
    divs = [1]
    for p, e in factors:
        current = []
        power = 1
        for _ in range(e):
            power *= p
            for d in divs:
                current.append(d * power)
        divs.extend(current)
    return sorted(divs)


def num_divisors(n):
    """약수의 개수"""
    if n == 0:
        return 0
    if n < 0:
        n = -n
    factors = _factorization(n)
    result = 1
    for _, e in factors:
        result *= (e + 1)
    return result


def sum_of_divisors(n):
    """약수의 합"""
    if n == 0:
        return 0
    sign = -1 if n < 0 else 1
    n = abs(n)
    factors = _factorization(n)
    total = 1
    for p, e in factors:
        total *= (p ** (e + 1) - 1) // (p - 1)
    return sign * total


