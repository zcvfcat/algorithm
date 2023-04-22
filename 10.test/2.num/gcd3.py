def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)


def gcd3(a, b):
    while b != 0:
        a, b = b, a % b

    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)



print(gcd(12, 18))
print(gcd(18, 12))
print(gcd(12, 6))
print(gcd(6, 0))

print(gcd3(12, 18))
print(gcd3(18, 12))
print(gcd3(12, 6))
print(gcd3(6, 0))