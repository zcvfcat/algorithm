def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def gcd_recur(a, b):
    if b == 0:
        return a
    return gcd_recur(b, a % b)
