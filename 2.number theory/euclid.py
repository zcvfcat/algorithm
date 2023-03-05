# a    b
# 20 % 6   2
#      6 % 2    0
#          2

import math

def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)

def gcd_2(a,b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // math.gcd(a,b)
