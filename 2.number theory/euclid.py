# a    b
# 20 % 6   2
#      6 % 2    0
#          2

import math


def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)


def gcd_2(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return (a * b) // math.gcd(a, b)


gcd(12, 18)
gcd(18, 12)  # a=18, b=12로 매개변수를 바꿔서 호출
gcd(12, 6)  # a=12, b=18 % 12=6으로 매개변수를 바꿔서 호출
gcd(6, 0)   # b=0이므로 6을 반환
