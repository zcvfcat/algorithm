t = int(input())


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


for i in range(t):
    a, b = map(int, input().split())
    result = int(a * b / gcd(a, b))
    print(result)
