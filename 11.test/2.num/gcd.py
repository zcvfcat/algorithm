def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)


def gcd_2(a, b):
    while b != 0:
        a, b = b, a % b

    return a


def lcm(a, b):
    return (a * b) // gcd(a, b)
