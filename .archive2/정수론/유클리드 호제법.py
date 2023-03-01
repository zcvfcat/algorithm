from math import gcd, lcm


def greatest_common_divisor(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def recur_gcd(a, b):
    if b == 0:
        return a

    return recur_gcd(b, a % b)


def lowest_common_multiple(a, b):
    return a * b / greatest_common_divisor(a, b)


assert greatest_common_divisor(15, 25) == gcd(15, 25)
assert recur_gcd(15, 25) == gcd(15, 25)
assert lowest_common_multiple(15, 25) == lcm(15, 25)
