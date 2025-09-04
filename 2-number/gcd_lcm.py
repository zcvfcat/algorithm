def gcd(a, b):
    """최대공약수 (유클리드 호제법)"""
    while b != 0:
        a, b = b, a % b
    return abs(a)


def lcm(a, b):
    """최소공배수"""
    if a == 0 or b == 0:
        return 0
    return abs(a // gcd(a, b) * b)


def gcd_list(numbers):
    """리스트의 최대공약수"""
    if not numbers:
        return 0
    from functools import reduce
    return reduce(gcd, numbers)


def lcm_list(numbers):
    """리스트의 최소공배수"""
    if not numbers:
        return 0
    from functools import reduce
    return reduce(lcm, numbers)


