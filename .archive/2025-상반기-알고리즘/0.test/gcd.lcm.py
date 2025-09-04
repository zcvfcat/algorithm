def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a


def lcm(a, b):
    return (a * b)//gcd(a, b)

print(gcd(12,14))
print(lcm(12,14))