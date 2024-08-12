def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return (a * b) // gcd(a, b)


def recur_gcd(a, b):
    if b == 0:
        return a
    return recur_gcd(b, a % b)