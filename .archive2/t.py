a, b = map(int, input().split())


def gcd(a, b):
    while a != 0:
        a, b = b % a, a

    return b


def gcm(a, b):
    return a * b // gcd(a, b)


print(gcd(a, b))
print(gcm(a, b))
