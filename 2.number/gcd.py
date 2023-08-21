def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a


def gcd_recur(a, b):
    if gcd_recur == b:
        return a

    return gcd(b, a % b)
